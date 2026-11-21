# usage: python3 s2-01-pilot.py <clip.mp4> <start.png> <end.png|-> <out.jpg> [times...]
# Gate D check for a style-2 pilot (strategy2.md 6.2 Step 7): a strip of the start still, the clip's frames at the given times
# (default 0 0.5 1 1.5 2 and the last frame) and the end still; then the joins (how far the first frame sits from the start
# still and the last frame from the end still: mean absolute difference 0-255 and the phase-correlation shift in px at
# 768x1360), the motion every half second (mean absolute difference between frames 0.1 s apart) and the sound (mean and peak
# volume, if the clip has a sound track).
import sys, subprocess, json, cv2, numpy as np
clip, s0, s1, out = sys.argv[1:5]
times = [float(t) for t in sys.argv[5:]] or [0, 0.5, 1, 1.5, 2]
cap = cv2.VideoCapture(clip); fps = cap.get(cv2.CAP_PROP_FPS); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); dur = n / fps
frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
n = len(frames); dur = n / fps
print(f"{clip}: {frames[0].shape[1]}x{frames[0].shape[0]}, {fps:.2f} fps, {n} frames, {dur:.2f} s")
def at(t): return frames[min(n - 1, int(round(t * fps)))]
H = 640
def fit(im): return cv2.resize(im, (int(im.shape[1] * H / im.shape[0]), H))
def lab(im, t):
    im = im.copy(); cv2.putText(im, t, (8, 34), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 5); cv2.putText(im, t, (8, 34), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2); return im
tiles = [lab(fit(cv2.imread(s0)), "start still")] + [lab(fit(at(t)), f"{t:.1f} s") for t in times] + [lab(fit(frames[-1]), f"last {dur:.2f} s")]
if s1 != "-": tiles.append(lab(fit(cv2.imread(s1)), "end still"))
gap = np.full((H, 6, 3), 255, np.uint8)
cv2.imwrite(out, np.hstack(sum([[t, gap] for t in tiles], [])[:-1]), [cv2.IMWRITE_JPEG_QUALITY, 88])
def cmp(a, b):
    a = cv2.resize(a, (768, 1360)); b = cv2.resize(b, (768, 1360))
    ga = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY).astype(np.float32); gb = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY).astype(np.float32)
    (dx, dy), r = cv2.phaseCorrelate(ga, gb); return float(np.abs(ga - gb).mean()), dx, dy
m, dx, dy = cmp(cv2.imread(s0), frames[0]); print(f"join in : first frame vs start still: diff {m:.1f}, shift {dx:+.1f},{dy:+.1f} px")
if s1 != "-":
    m, dx, dy = cmp(frames[-1], cv2.imread(s1)); print(f"join out: last frame vs end still: diff {m:.1f}, shift {dx:+.1f},{dy:+.1f} px")
step = max(1, int(round(fps * 0.1))); mot = []
for i in range(0, n - step, step):
    a = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY).astype(np.float32); b = cv2.cvtColor(frames[i + step], cv2.COLOR_BGR2GRAY).astype(np.float32)
    mot.append((i / fps, float(np.abs(a - b).mean())))
print("motion (mean abs diff over 0.1 s), per half second: " + "  ".join(
    f"{t0:.1f}-{t0+0.5:.1f}: {np.mean([m for t, m in mot if t0 <= t < t0 + 0.5]):.1f}" for t0 in np.arange(0, dur - 0.01, 0.5) if any(t0 <= t < t0 + 0.5 for t, m in mot)))
pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-of", "json", clip], capture_output=True, text=True).stdout)
aud = [s for s in pr["streams"] if s["codec_type"] == "audio"]
if aud:
    r = subprocess.run(["ffmpeg", "-i", clip, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    vol = [l.split("] ")[1] for l in r.splitlines() if "mean_volume" in l or "max_volume" in l]
    print(f"sound: {aud[0]['codec_name']} {aud[0].get('sample_rate')} Hz, " + ", ".join(vol))
else:
    print("sound: none")
