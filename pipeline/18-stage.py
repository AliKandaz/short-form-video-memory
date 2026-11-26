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
# ---- loop 2's lever, drawn (the render added a second bar and slimmed the hook) ----
def lever(img):
    """The release lever in the close view: a steel bar with a red handle left of the pile, a rod to the hook's hinge."""
    out = img.copy(); w, h = W, H
    fx, fy = 0.221 * w, 0.652 * h; tx, ty = 0.228 * w, 0.285 * h; hx, hy = 0.2295 * w, 0.205 * h; bw, hw = 15.0, 24.0
    L = (fy - hy) * 0.55
    out = C.shadow(out, [(fx, fy - 4), (fx + L, fy - 4 + L * 0.12), (fx + L, fy + 5 + L * 0.12), (fx, fy + 5)], dark=0.40, blur=2.2)
    lay = out.copy()
    cv2.fillPoly(lay, [np.int32([(fx - bw / 2, fy), (fx + bw / 2, fy), (tx + bw / 2, ty), (tx - bw / 2, ty)])], (84, 92, 98), cv2.LINE_AA)
    cv2.line(lay, (int(fx - bw / 2 + 2), int(fy)), (int(tx - bw / 2 + 2), int(ty)), (176, 186, 190), 3, cv2.LINE_AA)
    cv2.line(lay, (int(fx + bw / 2 - 2), int(fy)), (int(tx + bw / 2 - 2), int(ty)), (48, 54, 60), 3, cv2.LINE_AA)
    cv2.line(lay, (int(tx + 2), int(ty + 24)), (int(0.352 * w), int(0.338 * h)), (52, 58, 64), 7, cv2.LINE_AA)
    cv2.line(lay, (int(tx + 2), int(ty + 22)), (int(0.352 * w), int(0.336 * h)), (140, 150, 156), 2, cv2.LINE_AA)
    cv2.circle(lay, (int(tx + 2), int(ty + 24)), 7, (40, 44, 48), -1, cv2.LINE_AA)
    cv2.line(lay, (int(tx), int(ty)), (int(hx), int(hy)), (34, 30, 176), int(hw), cv2.LINE_AA)
    cv2.line(lay, (int(tx - hw * 0.22), int(ty - 5)), (int(hx - hw * 0.22), int(hy + 5)), (92, 96, 232), 5, cv2.LINE_AA)
    cv2.line(lay, (int(tx + hw * 0.3), int(ty - 3)), (int(hx + hw * 0.3), int(hy + 3)), (22, 18, 120), 4, cv2.LINE_AA)
    diff = (np.abs(lay.astype(np.int32) - out.astype(np.int32)).sum(2) > 0)
    lay = np.clip(lay.astype(np.float32) + np.random.default_rng(4).normal(0, 3.0, out.shape) * diff[..., None], 0, 255)
    m = cv2.GaussianBlur(diff.astype(np.float32), (0, 0), 0.6)[..., None]
    return np.clip(out.astype(np.float32) * (1 - m) + lay * m, 0, 255).astype(np.uint8)
# ---- the trigger in the stage view: what loop 2 added in the close view, brought back at its place ----
def trigger(img, free=False):
    x0, y0, Z = np.load(D + 'work/cv2_view.npy'); a, b = rd('CV2_0'), rd('CV2_3')
    ch = C.changed(b, a, 11).astype(np.uint8); ch = cv2.dilate(cv2.morphologyEx(ch, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)), np.ones((5, 5), np.uint8))
    if free:
        hv = cv2.cvtColor(b, cv2.COLOR_BGR2HSV).astype(int); ch[(hv[..., 0] >= 6) & (hv[..., 0] <= 28) & (hv[..., 1] > 45) & (hv[..., 2] > 55)] = 0
        ch = cv2.morphologyEx(ch, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    sw, sh = int(round(W / Z)), int(round(H / Z))
    small = cv2.resize(b, (sw, sh), interpolation=cv2.INTER_AREA); sm = cv2.resize(ch.astype(np.float32), (sw, sh), interpolation=cv2.INTER_AREA)
    out = img.astype(np.float32); X, Y = int(round(x0)), int(round(y0)); m = np.clip(sm * 1.4, 0, 1)[..., None]
    out[Y:Y + sh, X:X + sw] = out[Y:Y + sh, X:X + sw] * (1 - m) + small.astype(np.float32) * m
    return np.clip(out, 0, 255).astype(np.uint8)
# ---- loop 3: the heaps of chain and their wires ----
HX = (0.085, 0.86)                       # the two heaps' centres, as a share of the width
HW = 0.082                               # a heap's width, as a share of the width
HB = (0.435, 0.483)                      # the bases of the first and the second pair of heaps, as a share of the height
def heap(img, side, y_base, cx=None):
    name = 'LR'[side]; cut = cv2.imread(D + f'work/heap_{name}.png', cv2.IMREAD_UNCHANGED); shm = np.load(D + f'work/heap_{name}_sh.npy')
    ox, oy, ow, oh = np.load(D + 'work/heaps_geom.npy')[side]; sc = HW * W / ow
    c = cv2.resize(cut, None, fx=sc, fy=sc, interpolation=cv2.INTER_AREA); s2 = cv2.resize(shm, (c.shape[1], c.shape[0]), interpolation=cv2.INTER_AREA)
    X = int(round((HX[side] if cx is None else cx) * W - (ox + ow / 2) * sc)); Y = int(round(y_base - (oy + oh) * sc))
    out = img.astype(np.float32); out[Y:Y + c.shape[0], X:X + c.shape[1]] *= s2[..., None]
    return C.paste(np.clip(out, 0, 255).astype(np.uint8), c, X, Y + c.shape[0], 1.0, shadow=0, feather=0.6)[0]
def wire(img, p0, p1):
    out = img.copy(); cv2.line(out, (int(p0[0]), int(p0[1])), (int(p1[0]), int(p1[1])), (58, 62, 66), 2, cv2.LINE_AA)
    cv2.line(out, (int(p0[0]), int(p0[1]) - 1), (int(p1[0]), int(p1[1]) - 1), (168, 176, 180), 1, cv2.LINE_AA); return out
def held(L, base, heaps=0):
    """The boat held by the trigger at the crept position, on `base`; heaps: 0, 1 or 2 pairs of chain heaps wired to it."""
    dy = float(np.load(D + 'work/dy_held.npy')[0]); out = trigger(compose(L, dy, base=base))
    f = C.depth_s(YTOP + dy) / C.depth_s(YTOP); hw_ = (L['hull'].shape[1] * L['hsc'] * f) / 2.0; cx = C.XC + (L['hcx'] - C.XC) * f
    ends = ((cx - hw_ + 14, YTOP + dy - 52), (cx + hw_ - 10, YTOP + dy - 60))                # the stern's and the bow's deck edge
    for k in range(heaps):
        yb = HB[k] * H
        for side in (0, 1):
            out = heap(out, side, yb); out = wire(out, (HX[side] * W + (14 if side == 0 else -14), yb - 0.022 * H), ends[side])
    return out
HF = (0.492, 0.524)                      # where the two pairs of heaps end up after the launch
# ---- the boat afloat ----
YWL = 0.655                              # the waterline's row where the boat floats, as a share of the height
def afloat(L, base, heel=0.0):
    """The hull floating at the foot of the rails on `base`: its bottom fifth under the water. Returns (picture, box)."""
    cut = L['hull']; f = C.depth_s(YWL * H) / C.depth_s(354.0); ch = cut.shape[0]; wl = int(ch * 0.77)      # the cut's row at the waterline
    c = cut.copy(); c[wl:, :, 3] = 0
    c = cv2.resize(c, None, fx=f, fy=f, interpolation=cv2.INTER_LANCZOS4); out = base.astype(np.float32)
    X = int(round(C.XC - c.shape[1] / 2.0)); Y = int(round(YWL * H - wl * f))
    # the hull's dark reflection on the water under it, and a pale line of foam at the waterline
    al = np.zeros((H, W), np.float32); al[Y:Y + c.shape[0], X:X + c.shape[1]] = c[..., 3] / 255.0
    cols = (al.sum(0) > 2); x0, x1 = np.where(cols)[0].min(), np.where(cols)[0].max()
    refl = np.zeros((H, W), np.float32); yw = int(YWL * H); refl[yw:yw + 16, x0 + 6:x1 - 6] = 1.0
    refl = cv2.GaussianBlur(refl, (0, 0), 4.0) * 0.30; refl[:yw] = 0; out *= (1 - refl[..., None])
    before = np.clip(out, 0, 255).astype(np.uint8)
    out = C.paste(before, c, X, Y + c.shape[0], 1.0, shadow=0, feather=0.6)[0]
    g = np.zeros((H, W), np.float32); g[yw - 7:yw + 1] = np.linspace(0.0, 0.55, 8)[:, None]; g *= (al > 0.5)
    out = np.clip(out.astype(np.float32) * (1 - g[..., None]) + before.astype(np.float32) * g[..., None], 0, 255).astype(np.uint8)
    foam = out.copy(); cv2.line(foam, (int(x0 + 6), yw), (int(x1 - 6), yw), (214, 226, 222), 1, cv2.LINE_AA); out = cv2.addWeighted(foam, 0.55, out, 0.45, 0)
    return out, (x0, x1, Y, yw)
def launched(L, base, calm=True):
    """After a launch: the hull afloat, the rails empty; with calm=True the four heaps dragged down to the bank, their wires taut."""
    out = trigger(base.copy(), free=True)
    if calm:
        rut = (62, 98, 140)
        for k in (0, 1):
            y0 = HB[k] * H; y1 = HF[k] * H
            for side in (0, 1):
                xa = HX[side] * W; xb = (HX[side] + (0.03 if side == 0 else -0.03)) * W
                m = np.zeros((H, W), np.float32); cv2.line(m, (int(xa), int(y0 - 8)), (int(xb), int(y1 - 8)), 1.0, int(HW * W * 0.55), cv2.LINE_AA)
                m = cv2.GaussianBlur(m, (0, 0), 2.5)[..., None] * 0.75
                tex = out.astype(np.float32) * 0.45 + np.array(rut, np.float32) * 0.55
                out = np.clip(out.astype(np.float32) * (1 - m) + tex * m, 0, 255).astype(np.uint8)
    out, (x0, x1, Y, yw) = afloat(L, out)
    if calm:
        ends = ((x0 + 16, yw - 30), (x1 - 12, yw - 34))
        for k in (0, 1):
            y1 = HF[k] * H
            for side in (0, 1):
                cx = HX[side] + (0.03 if side == 0 else -0.03); out = heap(out, side, y1, cx=cx)
                out = wire(out, (cx * W + (12 if side == 0 else -12), y1 - 0.02 * H), ends[side])
    return out
if __name__ == '__main__':
    k = sys.argv[1]
    if k == 'S1_1': wr('S1_1P', piles(rd('F1')))
    if k == 'S1_2': wr('S1_2P', rails(rd('S1_1'), rd('S1_1')))
    if k == 'S1_3': wr('S1_3P', cradle(rd('S1_2')))
    if k == 'S1_4': wr('S1_4', compose(layers(), 0.0))
    if k == 'F2':
        L = layers(); x0, x1, y0, y1 = L['cb']
        # how far the cradle creeps: until its wheels' bottom is at 49.2% of the height, over the barbecue
        dy = next(d for d in np.arange(60, 260, 1.0) if (YTOP + d) + (y1 - YTOP) * C.depth_s(YTOP + d) / C.depth_s(YTOP) >= 0.492 * H)
        print('creep dy', dy, 'px =', round(100 * dy / H, 1), '% of the height; grows', round(C.depth_s(YTOP + dy) / C.depth_s(YTOP), 3))
        np.save(D + 'work/dy_held.npy', np.array([dy])); wr('F2', compose(L, dy, base=cv2.imread(D + 'work/plate_crushed.png')))
    if k == 'CV2_3': wr('CV2_3', lever(rd('CV2_2')))
    if k in ('S2_T', 'S3_1', 'S3_2', 'S3_3'):
        L = layers(); base = cv2.imread(D + ('work/plate_crushed.png' if k == 'S2_T' else 'work/plate_wreck.png'))
        wr(k, held(L, base, heaps={'S2_T': 0, 'S3_1': 0, 'S3_2': 1, 'S3_3': 2}[k]))
    if k == 'S3_L': wr('S3_L', launched(layers(), cv2.imread(D + 'work/plate_wreck.png'), calm=True))
    if k == 'F3': wr('F3P', launched(layers(), cv2.imread(D + 'work/plate_wreck.png'), calm=False))
    print('wrote', k + 'P')
