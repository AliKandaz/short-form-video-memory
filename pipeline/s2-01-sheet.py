# usage: python3 s2-01-sheet.py <stills dir> <out.jpg> "O0 O1 O2 O3 O4 O5 O6 P" "I0 I1 I2 I3 I4 I5 I6" "B R CA CB"
# Gate C sheet for style 2: one row per ladder (each still 270x480, labelled), plus the drift of the outside view: the phase
# correlation shift between neighbouring stages over the top 40% of the frame (the house, the fence and the trees, which never
# change), in pixels at 768x1360. Stills are <dir>/<key>.png; a key may name a try (O0.B).
import sys, os, cv2, numpy as np
d, out, rows = sys.argv[1], sys.argv[2], [r.split() for r in sys.argv[3:]]
W, H, G = 270, 480, 10
cols = max(len(r) for r in rows)
sheet = np.full((G + len(rows) * (H + 40 + G), G + cols * (W + G), 3), 255, np.uint8)
def load(k): return cv2.imread(os.path.join(d, k + ".png"))
for ri, r in enumerate(rows):
    for ci, k in enumerate(r):
        im = cv2.resize(load(k), (W, H)); x = G + ci * (W + G); y = G + ri * (H + 40 + G)
        sheet[y + 40:y + 40 + H, x:x + W] = im
        cv2.putText(sheet, k, (x + 4, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (30, 30, 30), 2)
cv2.imwrite(out, sheet, [cv2.IMWRITE_JPEG_QUALITY, 88])
def top(k):
    g = cv2.cvtColor(load(k), cv2.COLOR_BGR2GRAY).astype(np.float32); return g[: int(g.shape[0] * 0.4)]
for r in rows:
    if r and r[0].startswith("O"):
        for a, b in zip(r, r[1:]):
            (dx, dy), resp = cv2.phaseCorrelate(top(a), top(b))
            print(f"{a} -> {b}: shift {dx:+.1f}, {dy:+.1f} px (response {resp:.2f})")
