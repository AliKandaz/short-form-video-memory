# Checks for a build-steps video (CLAUDE.md 6.2 Steps 5, 7 and 8; written 24 Nov 2026 after the review of video 17).
# 17-check.py's clip check, plus the two things video 17 lacked: when a clip has SETTLED, and what changed between two stills.
#
#   python3 steps-check.py <dir with stills/ clips/ work/> KEY:START_STILL:END_STILL [...]
#       each clip against its two stills: shift in px at its first and last frame; when its step happens (10/50/90%);
#       `settle`: the time from which it stays on its end picture (the next clip must not start before this plus a beat);
#       `busy_s`: how long anything is moving at all; a sheet at 8 frames a second (work/sheet_<KEY>.jpg).
#       Results are added to work/check.json.
#   python3 steps-check.py <dir> --stills A:B [...]
#       what changed from still A to still B, after taking out a shift of the whole view and a drift of the whole tone:
#       the share of the frame that changed, the blobs it is made of, and a sheet (work/stills_<A>_<B>.jpg) with the change
#       painted red. A stage picture is right when the only red is its step: red on the tester, the fences, the house or an
#       earlier build is a change nobody asked for, and the clip between the two pictures will morph it (video 17: the
#       neighbor's fence, the ditch, the picket ring, the size of the night house).
import json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw

D = sys.argv[1]
BOX = (0.0, 0.12, 1.0, 0.85)
SW, SH = 720, 1276

def frames(path):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS); out = []
    while True:
        ok, f = cap.read()
        if not ok: break
        out.append(f)
    return fps, out

def shift(a, b):
    h, w = a.shape[:2]; b = cv2.resize(b, (w, h), interpolation=cv2.INTER_AREA); best = None
    for (y0, y1) in ((0, int(h * 0.13)), (int(h * 0.72), int(h * 0.84))):       # the house band and the cut face
        ga = cv2.cvtColor(a[y0:y1], cv2.COLOR_BGR2GRAY).astype(np.float32); gb = cv2.cvtColor(b[y0:y1], cv2.COLOR_BGR2GRAY).astype(np.float32)
        (dx, dy), r = cv2.phaseCorrelate(ga, gb, cv2.createHanningWindow(ga.shape[::-1], cv2.CV_32F))
        best = (dx, dy, r) if best is None or r > best[2] else best
    return best

def clips(specs):
    path_json = f"{D}/work/check.json"
    res = json.load(open(path_json)) if os.path.exists(path_json) else {}
    for spec in specs:
        key, s0, s1 = spec.split(":"); path = f"{D}/clips/{key}.mp4"
        pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-of", "json", path], capture_output=True, text=True).stdout)
        a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
        fps, F = frames(path); n = len(F); h, w = F[0].shape[:2]
        st0, st1 = cv2.imread(f"{D}/stills/{s0}.png"), cv2.imread(f"{D}/stills/{s1}.png")
        d0, d1 = shift(st0, F[0]), shift(st1, F[-1])
        x0, y0, x1, y1 = int(BOX[0] * w), int(BOX[1] * h), int(BOX[2] * w), int(BOX[3] * h)
        g = [cv2.GaussianBlur(cv2.cvtColor(f[y0:y1, x0:x1], cv2.COLOR_BGR2GRAY), (0, 0), 2).astype(np.float32) for f in F]
        prog = np.array([float((np.abs(x - g[0]) > 18).mean()) for x in g])
        step = np.array([0.0] + [float(np.abs(g[i] - g[i - 1]).mean()) for i in range(1, n)])
        fin = prog[-1] if prog[-1] > 0 else 1.0
        def t_at(q): return int(np.argmax(prog >= q * fin)) / fps
        # settled: from here on every frame is as close to the last frame as the clip's last third of a second is
        dl = np.array([float(np.abs(x - g[-1]).mean()) for x in g]); floor = max(0.8, 1.6 * float(dl[-10:-1].max()))
        late = np.where(dl > floor)[0]; settle = (int(late[-1]) + 1) / fps if len(late) else 0.0
        rest = max(0.35, 2.0 * float(np.median(step[-10:]))); busy = float((step > rest).sum()) / fps
        res[key] = dict(size=f"{w}x{h}", fps=round(fps, 2), frames=n, seconds=round(n / fps, 2), audio=bool(a),
                        start_shift_px=[round(d0[0], 2), round(d0[1], 2)], end_shift_px=[round(d1[0], 2), round(d1[1], 2)],
                        t10=round(t_at(0.10), 2), t50=round(t_at(0.50), 2), t90=round(t_at(0.90), 2),
                        settle=round(settle, 2), busy_s=round(busy, 2), peak_motion_s=round(int(np.argmax(step[2:]) + 2) / fps, 2),
                        prog=[round(float(x), 3) for x in prog], step=[round(float(x), 2) for x in step])
        print(key, {k: v for k, v in res[key].items() if k not in ("prog", "step")})
        idx = [int(round(i * fps / 8)) for i in range(int(n / fps * 8) + 1)]; idx = [i for i in idx if i < n]
        tw, th = 180, 320; cols = 8; rows = (len(idx) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * tw, rows * th), (16, 26, 51)); dr = ImageDraw.Draw(sheet)
        for j, i in enumerate(idx):
            im = Image.fromarray(cv2.cvtColor(cv2.resize(F[i], (tw, th), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB))
            x, y = (j % cols) * tw, (j // cols) * th; sheet.paste(im, (x, y)); dr.rectangle((x, y, x + 62, y + 18), fill=(0, 0, 0)); dr.text((x + 4, y + 3), f"{i / fps:.2f}s", fill=(255, 255, 255))
        sheet.save(f"{D}/work/sheet_{key}.jpg", quality=88)
    json.dump(res, open(path_json, "w"), indent=1)

def stills(pairs):
    for pair in pairs:
        a, b = pair.split(":")
        A = cv2.resize(cv2.imread(f"{D}/stills/{a}.png"), (SW, SH), interpolation=cv2.INTER_AREA)
        B = cv2.resize(cv2.imread(f"{D}/stills/{b}.png"), (SW, SH), interpolation=cv2.INTER_AREA)
        dx, dy, r = shift(A, B)                                                   # the whole view's shift, taken out
        B2 = cv2.warpAffine(B, np.float32([[1, 0, -dx], [0, 1, -dy]]), (SW, SH), borderMode=cv2.BORDER_REPLICATE)
        la = cv2.GaussianBlur(cv2.cvtColor(A, cv2.COLOR_BGR2LAB).astype(np.float32), (0, 0), 3)
        lb = cv2.GaussianBlur(cv2.cvtColor(B2, cv2.COLOR_BGR2LAB).astype(np.float32), (0, 0), 3)
        d = lb - la; drift = np.median(d.reshape(-1, 3), 0); d -= drift           # the whole tone's drift, taken out
        m = ((np.abs(d[..., 0]) > 20) | (np.abs(d[..., 1]) > 11) | (np.abs(d[..., 2]) > 11)).astype(np.uint8)
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        n, lab, stats, cen = cv2.connectedComponentsWithStats(cv2.dilate(m, np.ones((15, 15), np.uint8)), connectivity=8)
        blobs = []
        for i in range(1, n):
            x, y, w, h, area = stats[i]; real = int(m[lab == i].sum())
            if real / m.size >= 0.0015: blobs.append((real / m.size * 100, x / SW, y / SH, (x + w) / SW, (y + h) / SH))
        blobs.sort(reverse=True); tot = float(m.mean() * 100)
        print(f"{a} -> {b}: {tot:.1f}% of the frame changed, in {len(blobs)} blobs; view shift {dx:+.1f},{dy:+.1f} px; "
              f"tone drift L {drift[0]:+.1f} a {drift[1]:+.1f} b {drift[2]:+.1f}")
        for pc, x0, y0, x1, y1 in blobs[:8]:
            print(f"    {pc:5.2f}%  at x {x0 * 100:3.0f}-{x1 * 100:3.0f}%, y {y0 * 100:3.0f}-{y1 * 100:3.0f}%")
        over = B2.copy(); red = np.zeros_like(over); red[..., 2] = 255
        over = np.where(m[..., None] > 0, (0.45 * over + 0.55 * red).astype(np.uint8), over)
        tiles = [cv2.resize(x, (360, 638), interpolation=cv2.INTER_AREA) for x in (A, B, over)]
        for t, txt in zip(tiles, (a, b, f"changed {tot:.1f}%")): cv2.putText(t, txt, (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.imwrite(f"{D}/work/stills_{a}_{b}.jpg", np.hstack(tiles), [cv2.IMWRITE_JPEG_QUALITY, 86])

if __name__ == "__main__":
    if sys.argv[2] == "--stills": stills(sys.argv[3:])
    else: clips(sys.argv[2:])
