# usage: python3 s2-01-check.py <work dir> <out.jpg> CLIP=URL|CLIP ...   (work dir holds stills/<key>.png; clips go to clips/)
# Step 8 check for style 2: downloads each clip (CLIP=URL) to <dir>/clips/<CLIP>.mp4, prints its joins against its start and
# end stills (s2-01-clips.py's table), its motion every half second and its sound level, and writes one sheet with a row per
# clip: the start still, frames every 0.4 s, the last frame and the end still.
import sys, os, subprocess, importlib.util, cv2, numpy as np
d, out = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(os.path.abspath(__file__)), "s2-01-clips.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
os.makedirs(os.path.join(d, "clips"), exist_ok=True)
W, H, G, T = 150, 266, 4, 30
rows = []
for a in sys.argv[3:]:
    name, _, url = a.partition("=")
    clip = name.split(".")[0]; f = os.path.join(d, "clips", name + ".mp4")
    if url: subprocess.run(["curl", "-s", "-o", f, url], check=True)
    start, end = c.C[clip][0], c.C[clip][1]
    cap = cv2.VideoCapture(f); fps = cap.get(cv2.CAP_PROP_FPS); fr = []
    while True:
        ok, im = cap.read()
        if not ok: break
        fr.append(im)
    dur = len(fr) / fps
    def cmp(x, y):
        x = cv2.cvtColor(cv2.resize(x, (384, 680)), cv2.COLOR_BGR2GRAY).astype(np.float32); y = cv2.cvtColor(cv2.resize(y, (384, 680)), cv2.COLOR_BGR2GRAY).astype(np.float32)
        (dx, dy), _ = cv2.phaseCorrelate(x, y); return np.abs(x - y).mean(), dx * 2, dy * 2
    s0 = cv2.imread(os.path.join(d, "stills", start + ".png")); s1 = cv2.imread(os.path.join(d, "stills", end + ".png")) if end else None
    j = "in %.1f (%+.0f,%+.0f px)" % cmp(s0, fr[0])
    if end is not None: j += ", out %.1f (%+.0f,%+.0f px)" % cmp(fr[-1], s1)
    step = max(1, round(fps * 0.1)); mot = [np.abs(cv2.cvtColor(fr[i], cv2.COLOR_BGR2GRAY).astype(np.float32) - cv2.cvtColor(fr[i + step], cv2.COLOR_BGR2GRAY).astype(np.float32)).mean() for i in range(0, len(fr) - step, step)]
    halves = [np.mean(mot[k:k + 5]) for k in range(0, len(mot), 5)]
    vol = subprocess.run(["ffmpeg", "-i", f, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    mv = [l.split(":")[1].strip() for l in vol.splitlines() if "mean_volume" in l]
    print(f"{name}: {dur:.2f} s, join {j}; motion/0.5 s " + " ".join(f"{h:.0f}" for h in halves) + f"; sound mean {mv[0] if mv else 'none'}")
    tiles = [(s0, start)] + [(fr[min(len(fr) - 1, int(round(t * fps)))], f"{t:.1f}") for t in np.arange(0, dur - 0.05, 0.4)] + [(fr[-1], "last")]
    if end is not None: tiles.append((s1, end))
    rows.append((name, tiles))
cols = max(len(t) for _, t in rows)
sheet = np.full((len(rows) * (H + T + G) + G, G + cols * (W + G), 3), 255, np.uint8)
for ri, (name, tiles) in enumerate(rows):
    y = G + ri * (H + T + G); cv2.putText(sheet, name, (G + 2, y + 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 20, 20), 2)
    for ci, (im, lab) in enumerate(tiles):
        im = cv2.resize(im, (W, H)); cv2.putText(im, lab, (4, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 3); cv2.putText(im, lab, (4, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
        x = G + ci * (W + G); sheet[y + T:y + T + H, x:x + W] = im
cv2.imwrite(out, sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])
