# Video 18: the stage pictures laid out on this machine (free). Each function draws or pastes ONE step onto the picture
# before it, at an exact place; the paste-up is uploaded and one seedream pass renders it clean (18-prompts.py, PASTE).
#   python3 stage.py S1_1|S1_2|...      (reads and writes <scratch>/v18/stills)
import sys, importlib.util, cv2, numpy as np
_s = importlib.util.spec_from_file_location('cutlib', __file__.replace('18-stage.py', '18-cutlib.py')); C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)
D = '/tmp/claude-0/-home-user-short-form-video-memory/c916d411-dad6-5b75-ab84-87c4db23dfd2/scratchpad/v18/'
W, H = 768, 1360
XL, XR = 0.24, 0.73                     # the two rails, as a share of the width at the bank's row
PW, PH = 18, 46                         # a pile at the bank's row: width and height in px
ROWS = (0.31, 0.36, 0.42, 0.48)         # the piles on the lawn, as a share of the height
def rd(k): return cv2.imread(D + f'stills/{k}.png')
def wr(k, im):
    cv2.imwrite(D + f'stills/{k}.png', im); cv2.imwrite(D + f'sheets/{k}_s.jpg', cv2.resize(im, (540, 956)), [cv2.IMWRITE_JPEG_QUALITY, 88])
    cv2.imwrite(D + f'sheets/{k}_crop.jpg', cv2.resize(im[int(0.12 * H):int(0.70 * H)], (900, int(900 * 0.58 * H / W))), [cv2.IMWRITE_JPEG_QUALITY, 86])
def piles(img):
    out = img.copy()
    for xb in (XL, XR):
        for yr in ROWS:
            y = yr * H; s = C.depth_s(y); out = C.pile(out, C.depth_x(xb * W, y), y, PW * s, PH * s)
        y = 0.555 * H; s = C.depth_s(y); out = C.pile(out, C.depth_x(xb * W, y), y + 18 * s, PW * s, PH * s, water_y=y)
        y = 0.582 * H; s = C.depth_s(y); out = C.pile(out, C.depth_x(xb * W, y), y + 30 * s, PW * s, PH * s * 0.9, water_y=y - 10 * s)
    return out
def rails(img, base):
    out = img.copy()
    for xb, side in ((XL, +1), (XR, -1)):
        out = C.rail(out, xb * W, 0.297 * H, 0.586 * H, PH, 12, y_water=0.548 * H, y_dip=0.586 * H, side=side, base=base)
    return out
YB, YF = 0.300, 0.365                   # the cradle at the top of the rails: its back and front timbers, as a share of the height
CX0, CX1 = 0.215, 0.755                # the cradle's ends, as a share of the width at the bank's row
def box_h(lay, alpha, x0, x1, y, lift, th, top_d, c_top, c_face):
    """A timber lying across the picture: from x0 to x1 at ground row y, lifted `lift`, th thick, top_d deep (in px)."""
    yy = y - lift
    cv2.fillPoly(lay, [np.int32([(x0, yy - top_d), (x1, yy - top_d), (x1, yy), (x0, yy)])], c_top)
    cv2.fillPoly(lay, [np.int32([(x0, yy), (x1, yy), (x1, yy + th), (x0, yy + th)])], c_face)
    cv2.fillPoly(alpha, [np.int32([(x0, yy - top_d), (x1, yy - top_d), (x1, yy + th), (x0, yy + th)])], 1.0)
def cradle(img, dy=0.0):
    """The timber cradle across the rails, its back timber at row (YB + dy) * H."""
    out = img.copy().astype(np.float32); lay = np.zeros((H, W, 3), np.float32); al = np.zeros((H, W), np.float32)
    yb, yf = (YB + dy) * H, (YF + dy) * H; rng = np.random.default_rng(3)
    lift = lambda y: PH * C.depth_s(y) + 9
    TOP, FACE, CTOP, CFACE = (96, 150, 196), (52, 92, 138), (88, 140, 186), (46, 82, 124)
    # cross timbers, from the back timber to the front one, along the lines down the lawn
    for xb in (0.27, 0.38, 0.485, 0.59, 0.70):
        pts = []
        for y in (yb, yf):
            x = C.depth_x(xb * W, y); pts.append((x, y - lift(y)))
        (xa, ya), (xc, yc) = pts; wd = 9
        cv2.fillPoly(lay, [np.int32([(xa - wd / 2, ya), (xa + wd / 2, ya), (xc + wd / 2, yc), (xc - wd / 2, yc)])], CTOP)
        cv2.fillPoly(al, [np.int32([(xa - wd / 2, ya), (xa + wd / 2, ya), (xc + wd / 2, yc), (xc - wd / 2, yc)])], 1.0)
    # the wheels on the rails, under the two long timbers
    for xb in (XL, XR):
        for y in (yb, yf):
            x = C.depth_x(xb * W, y); yy = y - PH * C.depth_s(y) - 3
            cv2.ellipse(lay, (int(x), int(yy)), (6, 7), 0, 0, 360, (44, 48, 52), -1, cv2.LINE_AA); cv2.ellipse(al, (int(x), int(yy)), (6, 7), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
    # the two long timbers
    for y in (yb, yf):
        box_h(lay, al, C.depth_x(CX0 * W, y), C.depth_x(CX1 * W, y), y, lift(y), 10, 8, TOP, FACE)
    lay += rng.normal(0, 4.0, (H, W, 1)).astype(np.float32) * (al[..., None] > 0)
    # the shadow of the whole frame on the grass
    L = lift((yb + yf) / 2); M = np.float32([[1, 0, L * 1.05], [0, 1, L * 0.12 + L]])
    sh = cv2.GaussianBlur(cv2.warpAffine(al, M, (W, H)), (0, 0), 3.0) * 0.42
    out *= (1 - np.clip(sh - al, 0, 1)[..., None])
    a = cv2.GaussianBlur(al, (0, 0), 0.6)[..., None]
    return np.clip(out * (1 - a) + lay * a, 0, 255).astype(np.uint8)
# ---- layers (free): the plate (the yard with rails, ruts, blocks: no boat, no cradle), the cradle, the hull ----
def layers():
    """Cut the cradle (and its shadow) out of S1_3 and load the hull: everything compose() needs, at the top-of-rails position."""
    S2, S3, R = rd('S1_2'), rd('S1_3'), rd('S1_4_R'); plate = cv2.imread(D + 'work/plate_rails.png')
    ch = C.changed(S3, S2, 11); bx = C.boxes(S3.shape, [(0.185, 0.80, 0.285, 0.40)]) > 0
    obj = ch & bx & ~C.lawnlike_any(S3); obj = cv2.morphologyEx(obj.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(obj, 8); keep = np.zeros_like(obj)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 60: keep[lab == i] = 1
    ys, xs = np.where(keep > 0); cb = (xs.min(), xs.max() + 1, ys.min(), ys.max() + 1)
    cradle = np.dstack([S3, keep * 255])[cb[2]:cb[3], cb[0]:cb[1]]
    # the cradle's shadow: how much darker S1_3 is than S1_2 on the grass round it
    l3 = cv2.cvtColor(S3, cv2.COLOR_BGR2LAB)[..., 0].astype(np.float32); l2 = cv2.cvtColor(S2, cv2.COLOR_BGR2LAB)[..., 0].astype(np.float32)
    sb = C.boxes(S3.shape, [(0.185, 0.90, 0.285, 0.475)]) > 0
    ratio = np.ones((H, W), np.float32); m = sb & (keep == 0) & (l3 < l2 - 6) & C.lawnlike_any(S3)
    ratio[m] = np.clip(l3[m] / np.maximum(l2[m], 1), 0.35, 1.0); ratio = cv2.GaussianBlur(ratio, (0, 0), 1.2)
    # the hull's shadow where it sits on the cradle: how much darker the render is than the plate, right of the hull
    off = np.median((plate.astype(np.float32) - R.astype(np.float32))[C.boxes(R.shape, [(0.02, 0.18, 0.30, 0.50)]) > 0], axis=0)
    lr = cv2.cvtColor(np.clip(R.astype(np.float32) + off, 0, 255).astype(np.uint8), cv2.COLOR_BGR2LAB)[..., 0].astype(np.float32)
    lp = cv2.cvtColor(plate, cv2.COLOR_BGR2LAB)[..., 0].astype(np.float32)
    hb = C.boxes(R.shape, [(0.74, 1.0, 0.315, 0.43)]) > 0
    hs = np.ones((H, W), np.float32); m = hb & (lr < lp - 8) & C.lawnlike_any(R)
    hs[m] = np.clip(lr[m] / np.maximum(lp[m], 1), 0.35, 1.0); hs = cv2.GaussianBlur(hs, (0, 0), 1.5)
    hull = cv2.imread(D + 'work/hull_cut.png', cv2.IMREAD_UNCHANGED); sc, cx, y = np.load(D + 'work/hull_scale_S1_4.npy')
    return dict(plate=plate, cradle=cradle, cb=cb, cshadow=ratio, hshadow=hs, hull=hull, hsc=float(sc), hcx=float(cx), hy=float(y))
YTOP = 472.0                             # the row of the hull's keel when the cradle is at the top of the rails
def shift_map(m, dy, f, fill=1.0):
    """A shadow map moved dy down the lawn, grown by f about the centre line."""
    M = np.float32([[f, 0, C.XC * (1 - f)], [0, f, (YTOP + dy) - f * YTOP]])
    return cv2.warpAffine(m, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=fill)
def compose(L, dy=0.0, base=None, hull=True, cradle=True):
    """The plate (or `base`) with the cradle and the hull on it, dy px further down the rails than the top position."""
    out = (L['plate'] if base is None else base).astype(np.float32); f = C.depth_s(YTOP + dy) / C.depth_s(YTOP)
    if cradle:
        out *= shift_map(L['cshadow'], dy, f)[..., None]
    if hull:
        out *= shift_map(L['hshadow'], dy, f)[..., None]
    out = np.clip(out, 0, 255).astype(np.uint8)
    x0, x1, y0, y1 = L['cb']
    def put_cradle(img, rows=None):
        c = L['cradle'] if rows is None else L['cradle'].copy()
        if rows is not None: c[:rows, :, 3] = 0
        c = cv2.resize(c, None, fx=f, fy=f, interpolation=cv2.INTER_LANCZOS4)
        xl = C.XC + (x0 - C.XC) * f; yb = (YTOP + dy) + (y1 - YTOP) * f
        return C.paste(img, c, xl, yb, 1.0, shadow=0, feather=0.6)[0]
    if cradle: out = put_cradle(out)
    if hull:
        hc = cv2.resize(L['hull'], None, fx=L['hsc'] * f, fy=L['hsc'] * f, interpolation=cv2.INTER_LANCZOS4)
        cx = C.XC + (L['hcx'] - C.XC) * f
        out = C.paste(out, hc, cx - hc.shape[1] / 2.0, YTOP + dy, 1.0, shadow=0, feather=0.6)[0]
        if cradle: out = put_cradle(out, rows=int(YTOP - 6 - y0))          # the front timber and wheels, in front of the hull's bottom
    return out
if __name__ == '__main__':
    k = sys.argv[1]
    if k == 'S1_1': wr('S1_1P', piles(rd('F1')))
    if k == 'S1_2': wr('S1_2P', rails(rd('S1_1'), rd('S1_1')))
    if k == 'S1_3': wr('S1_3P', cradle(rd('S1_2')))
    if k == 'S1_4': wr('S1_4', compose(layers(), 0.0))
    print('wrote', k + 'P')
