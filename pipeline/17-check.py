# Build-steps test: look at each clip. For every clip named: its size, frame rate and sound track; how far its first and last
# frames sit from the stage stills (shift in px at the still's size); when the change happens (the share of the shed area that
# differs from the first frame, read every frame: the times it passes 10%, 50% and 90% of its final value, and how long the end
# is held); and a sheet of frames for the eye.
#   python3 steps-test-check.py <dir with stills/ and clips/> KEY:START_STILL:END_STILL [...]     e.g. W1:S0B:S1 K1:S0B:S4
import json, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw
D = sys.argv[1]
BOX = (0.0, 0.12, 1.0, 0.85)
def frames(path):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS); out = []
    while True:
        ok, f = cap.read()
        if not ok: break
        out.append(f)
    return fps, out
def shift(a, b):
    h, w = a.shape[:2]; b = cv2.resize(b, (w, h), interpolation=cv2.INTER_AREA)
    best = None
    for (y0, y1) in ((0, int(h * 0.13)), (int(h * 0.72), int(h * 0.84))):       # the house band and the cut face: they never change
        ga = cv2.cvtColor(a[y0:y1], cv2.COLOR_BGR2GRAY).astype(np.float32); gb = cv2.cvtColor(b[y0:y1], cv2.COLOR_BGR2GRAY).astype(np.float32)
        (dx, dy), r = cv2.phaseCorrelate(ga, gb, cv2.createHanningWindow(ga.shape[::-1], cv2.CV_32F))
        best = (dx, dy, r) if best is None or r > best[2] else best
    return best
import os
res = json.load(open(f"{D}/work/check.json")) if os.path.exists(f"{D}/work/check.json") else {}   # add to what is there
for spec in sys.argv[2:]:
    key, s0, s1 = spec.split(":"); path = f"{D}/clips/{key}.mp4"
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-of", "json", path], capture_output=True, text=True).stdout)
    v = [s for s in pr["streams"] if s["codec_type"] == "video"][0]; a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
    fps, F = frames(path); n = len(F); h, w = F[0].shape[:2]
    st0, st1 = cv2.imread(f"{D}/stills/{s0}.png"), cv2.imread(f"{D}/stills/{s1}.png")
    d0, d1 = shift(st0, F[0]), shift(st1, F[-1])
    x0, y0, x1, y1 = int(BOX[0] * w), int(BOX[1] * h), int(BOX[2] * w), int(BOX[3] * h)
    g = [cv2.GaussianBlur(cv2.cvtColor(f[y0:y1, x0:x1], cv2.COLOR_BGR2GRAY), (0, 0), 2).astype(np.float32) for f in F]
    prog = np.array([float((np.abs(x - g[0]) > 18).mean()) for x in g])                 # share of the area changed since frame 0
    step = np.array([0.0] + [float(np.abs(g[i] - g[i - 1]).mean()) for i in range(1, n)])  # motion frame to frame
    fin = prog[-1] if prog[-1] > 0 else 1.0
    def t_at(q):
        i = int(np.argmax(prog >= q * fin)); return i / fps
    quiet = step < max(0.25, 0.08 * step.max()); hold = 0
    for qv in quiet[::-1]:
        if not qv: break
        hold += 1
    res[key] = dict(size=f"{w}x{h}", fps=round(fps, 2), frames=n, seconds=round(n / fps, 2), audio=bool(a),
                    start_shift_px=[round(d0[0], 2), round(d0[1], 2)], end_shift_px=[round(d1[0], 2), round(d1[1], 2)],
                    t10=round(t_at(0.10), 2), t50=round(t_at(0.50), 2), t90=round(t_at(0.90), 2), end_hold_s=round(hold / fps, 2),
                    peak_motion_s=round(int(np.argmax(step)) / fps, 2), prog=[round(float(x), 3) for x in prog], step=[round(float(x), 2) for x in step])
    print(key, {k: v for k, v in res[key].items() if k not in ("prog", "step")})
    # the sheet: 8 frames a second
    idx = [int(round(i * fps / 8)) for i in range(int(n / fps * 8) + 1)]; idx = [i for i in idx if i < n]
    tw, th = 180, 320; cols = 8; rows = (len(idx) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), (16, 26, 51)); dr = ImageDraw.Draw(sheet)
    for j, i in enumerate(idx):
        im = Image.fromarray(cv2.cvtColor(cv2.resize(F[i], (tw, th), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB))
        x, y = (j % cols) * tw, (j // cols) * th; sheet.paste(im, (x, y)); dr.rectangle((x, y, x + 62, y + 18), fill=(0, 0, 0)); dr.text((x + 4, y + 3), f"{i / fps:.2f}s", fill=(255, 255, 255))
    sheet.save(f"{D}/work/sheet_{key}.jpg", quality=88)
json.dump(res, open(f"{D}/work/check.json", "w"), indent=1)
