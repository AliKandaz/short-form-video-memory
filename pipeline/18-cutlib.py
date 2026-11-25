# Cut-outs and paste-ups for video 18's stage pictures (free, on this machine): a part is cut out of a rendered still and laid
# onto another at an exact place and size; the paste-up is then the reference for one seedream pass that renders it clean.
import cv2, numpy as np
def lawnlike(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(int); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    return (H >= 22) & (H <= 85) & (S >= 60) & (V >= 60)
def changed(img, base, thr=14):
    a = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32); b = cv2.cvtColor(base, cv2.COLOR_BGR2LAB).astype(np.float32)
    d = a - b; d -= np.median(d.reshape(-1, 3), axis=0); return np.sqrt((d ** 2).sum(2)) > thr
def cut(img, base, box, open_k=7, keep_frac=0.004, drop_lawn=True):
    """The changed, not-lawn part of img inside box (x0, x1, y0, y1 as fractions), as a mask 0/255."""
    h, w = img.shape[:2]; x0, x1, y0, y1 = box; reg = np.zeros((h, w), bool); reg[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)] = True
    ll = lawnlike(img) if drop_lawn else np.zeros((h, w), bool)
    m = np.full((h, w), cv2.GC_BGD, np.uint8); m[reg] = cv2.GC_PR_BGD
    fg = reg & changed(img, base) & ~ll
    fg = cv2.morphologyEx(fg.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
    m[fg] = cv2.GC_PR_FGD; m[cv2.erode(fg.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)] = cv2.GC_FGD
    cv2.grabCut(img, m, None, np.zeros((1, 65)), np.zeros((1, 65)), 6, cv2.GC_INIT_WITH_MASK)
    k = (((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD)) & ~ll).astype(np.uint8) * 255
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((open_k, open_k), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8); big = sorted(range(1, n), key=lambda i: -st[i, cv2.CC_STAT_AREA]); o = np.zeros_like(k)
    for i in big:
        if st[i, cv2.CC_STAT_AREA] > keep_frac * st[big[0], cv2.CC_STAT_AREA]: o[lab == i] = 255
    ff = o.copy(); cv2.floodFill(ff, None, (0, 0), 255); return o | cv2.bitwise_not(ff)
def crop_rgba(img, mask):
    ys, xs = np.where(mask > 0); return np.dstack([img, mask])[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
def paste(base, cutout, x_left, y_bottom, scale=1.0, shadow=0.45, feather=0.6):
    """Lay an RGBA cut-out on base with its left edge at x_left and its bottom at y_bottom (pixels). Returns (image, box)."""
    h, w = base.shape[:2]
    c = cv2.resize(cutout, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LANCZOS4)
    ch, cw = c.shape[:2]; X = int(round(x_left)); Y = int(round(y_bottom)) - ch
    out = base.astype(np.float32); al = np.zeros((h, w), np.float32); col = np.zeros((h, w, 3), np.float32)
    y0, y1, x0, x1 = max(Y, 0), min(Y + ch, h), max(X, 0), min(X + cw, w)
    al[y0:y1, x0:x1] = c[y0 - Y:y1 - Y, x0 - X:x1 - X, 3] / 255.0; col[y0:y1, x0:x1] = c[y0 - Y:y1 - Y, x0 - X:x1 - X, :3]
    if shadow:
        sh = np.roll(np.roll(al, int(0.035 * w), axis=1), int(0.012 * h), axis=0); sh = np.clip(cv2.GaussianBlur(sh, (0, 0), 9) * shadow - al, 0, 1)
        out *= (1 - sh[..., None])
    al = cv2.GaussianBlur(al, (0, 0), feather)
    return (out * (1 - al[..., None]) + col * al[..., None]).astype(np.uint8), (X, Y, cw, ch)
def pct(box, w, h):
    X, Y, cw, ch = box; return f"x {100*X/w:.1f}-{100*(X+cw)/w:.1f}%  y {100*Y/h:.1f}-{100*(Y+ch)/h:.1f}%"

# ---- the stage's perspective (measured on K0S, 768x1360): lines that run down the lawn meet far above the frame ----
W0, H0 = 768, 1360
XC, YVP, YREF = 384.0, -2453.0, 734.0          # centre line, vanishing point, the bank's row (54% down)
def depth_x(x_at_bank, y):
    """x (px) at row y of the line down the lawn that crosses the bank's row at x_at_bank (px)."""
    return XC + (x_at_bank - XC) * (y - YVP) / (YREF - YVP)
def depth_s(y):
    """Size of a thing at row y against its size at the bank's row."""
    return (y - YVP) / (YREF - YVP)
def shadow(img, poly, dark=0.42, blur=2.5):
    """Darken img inside a polygon (a cast shadow on the grass)."""
    m = np.zeros(img.shape[:2], np.float32); cv2.fillPoly(m, [np.int32(poly)], 1.0); m = cv2.GaussianBlur(m, (0, 0), blur) * dark
    return (img.astype(np.float32) * (1 - m[..., None])).astype(np.uint8)
def put(img, cut, cx, y_base, scale=1.0, feather=0.5):
    """Lay an RGBA cut-out with its bottom centre at (cx, y_base)."""
    c = cv2.resize(cut, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LANCZOS4)
    out, box = paste(img, c, cx - c.shape[1] / 2.0, y_base, 1.0, shadow=0, feather=feather); return out

def pile(img, cx, y_base, wpx, hpx, water_y=None, rng=None, body=(112, 124, 128), cap=(188, 198, 200)):
    """Draw one round steel pile standing at (cx, y_base): wpx wide, hpx tall, lit from the left, with its shadow to the right.
    With water_y, the pile stands in the lake: the part below row water_y is seen through the water."""
    rng = rng or np.random.default_rng(int(cx * 7 + y_base))
    out = img.copy(); h, w = img.shape[:2]; r = wpx / 2.0; e = r * 0.45          # e: half-height of the cap's ellipse
    top = y_base - hpx
    if water_y is None:                                                            # the shadow on the grass, to the right
        L = hpx * 1.05
        out = shadow(out, [(cx - r * 0.3, y_base - e * 0.9), (cx + L, y_base - e * 0.9 + L * 0.12), (cx + L, y_base + e + L * 0.12), (cx + r * 0.3, y_base + e)], dark=0.50, blur=1.6)
    lay = np.zeros((h, w, 4), np.float32)
    xs = np.arange(int(cx - r - 2), int(cx + r + 3)); ys = np.arange(int(top - e - 2), int(y_base + e + 3))
    for y in ys:
        for x in xs:
            if not (0 <= x < w and 0 <= y < h): continue
            u = (x - cx) / r
            if abs(u) > 1: continue
            k = np.sqrt(1 - u * u); yb = y_base + e * k; yt = top + e * k; ytt = top - e * k
            if ytt <= y < yt:                                                      # the cap, with a darker rim
                rim = 1.0 if (y - ytt) > 1.2 and (yt - y) > 1.2 and abs(u) < 0.86 else 0.80
                c = np.array(cap, np.float32) * rim * (1.0 - 0.05 * u)
            elif yt <= y <= yb:                                                    # the body: lit from the left, a highlight, dark to the right
                sh = 1.18 - 0.30 * (u + 1) + 0.22 * np.exp(-((u + 0.45) / 0.22) ** 2) - 0.10 * max(0.0, (yt + 3 - y)) / 3
                c = np.array(body, np.float32) * sh * (1.0 - 0.10 * (y - top) / max(hpx, 1))
            else: continue
            lay[y, x, :3] = np.clip(c + rng.normal(0, 3.5), 0, 255); lay[y, x, 3] = 1.0
    a = cv2.GaussianBlur(lay[..., 3], (0, 0), 0.6)[..., None]
    res = out.astype(np.float32) * (1 - a) + lay[..., :3] * a
    if water_y is not None:                                                        # below the surface: mostly the water's colour
        wy = int(water_y); src = img.astype(np.float32); mix = np.zeros((h, w, 1), np.float32); mix[wy:] = 0.62
        res = res * (1 - mix * a) + src * (mix * a)
        cv2.ellipse(res, (int(cx), wy), (int(r * 1.5), max(2, int(e * 1.3))), 0, 0, 360, (236, 240, 232), 1, cv2.LINE_AA)
    return np.clip(res, 0, 255).astype(np.uint8)

def rail(img, x_at_bank, y0, y1, lift_at_bank, wpx_at_bank, y_water=None, y_dip=None, side=+1, base=None):
    """Draw one steel rail lying along the line down the lawn through (x_at_bank, the bank's row), from row y0 to row y1,
    held `lift` px above the ground on the pile heads. Below row y_water it slopes down under the surface until row y_dip
    and is seen through the water (base: the picture without the rail, for the water's colour). side=+1: we see its
    right-hand face (a rail left of the centre line), -1 its left-hand face."""
    h, w = img.shape[:2]; out = img.copy().astype(np.float32); base = img if base is None else base
    def geom(y):
        s = depth_s(y); x = depth_x(x_at_bank, y); lift = lift_at_bank * s
        if y_water is not None and y > y_water:
            lift = lift * max(0.0, 1 - (y - y_water) / max(1.0, (y_dip - y_water))) - 10 * s * min(1.0, (y - y_water) / max(1.0, (y_dip - y_water)))
        return x, lift, wpx_at_bank * s
    # the shadow on the grass (only on land)
    ys = np.arange(y0, min(y1, y_water if y_water is not None else y1), 2.0)
    polyL = []; polyR = []
    for y in ys:
        x, lift, wd = geom(y); sx = x + lift * 1.05; sy = y + lift * 0.12
        polyL.append((sx - wd / 2, sy)); polyR.append((sx + wd / 2, sy))
    sh = np.zeros((h, w), np.float32); cv2.fillPoly(sh, [np.int32(polyL + polyR[::-1])], 1.0); sh = cv2.GaussianBlur(sh, (0, 0), 2.0) * 0.45
    out *= (1 - sh[..., None])
    # the rail itself: a side face under a top face
    lay = np.zeros((h, w, 4), np.float32)
    ys = np.arange(y0, y1, 1.0)
    top = []; topr = []; face = []
    for y in ys:
        x, lift, wd = geom(y); yy = y - lift
        top.append((x - wd / 2, yy)); topr.append((x + wd / 2, yy)); face.append((x + side * wd / 2, yy, wd * 0.9))
    fpoly = [(x, y) for x, y, d in face] + [(x, y + d) for x, y, d in face[::-1]]
    web = np.zeros((h, w), np.float32); cv2.fillPoly(web, [np.int32(fpoly)], 1.0)
    # thicken the side face a little toward the centre so it reads as a deep beam
    m_top = np.zeros((h, w), np.float32); cv2.fillPoly(m_top, [np.int32(top + topr[::-1])], 1.0)
    front = np.zeros((h, w), np.float32)                      # the lower end's face
    x, lift, wd = geom(ys[-1]); yy = ys[-1] - lift
    cv2.fillPoly(front, [np.int32([(x - wd / 2, yy), (x + wd / 2, yy), (x + wd / 2, yy + wd * 0.9), (x - wd / 2, yy + wd * 0.9)])], 1.0)
    rng = np.random.default_rng(7)
    noise = rng.normal(0, 3.0, (h, w, 1)).astype(np.float32)
    colour = np.zeros((h, w, 3), np.float32); alpha = np.zeros((h, w), np.float32)
    for m, c in ((web, (58, 66, 70)), (front, (50, 56, 60)), (m_top, (150, 160, 164))):
        colour[m > 0] = c; alpha[m > 0] = 1.0
    # a brighter line along the top's lit edge
    edge = np.zeros((h, w), np.uint8); cv2.polylines(edge, [np.int32(top)], False, 255, 1, cv2.LINE_AA)
    colour[edge > 0] = (196, 206, 208)
    colour += noise * (alpha[..., None] > 0)
    a = cv2.GaussianBlur(alpha, (0, 0), 0.5)[..., None]
    if y_water is not None:                                  # under the surface: mostly the water's colour
        mix = np.zeros((h, w, 1), np.float32)
        for y in np.arange(int(y_water), int(y1) + int(lift_at_bank) + 12):
            if 0 <= y < h: mix[int(y)] = 0.0
        # rows of the rail that are below the surface: the rail's drawn row yy > surface row of its ground point y_water..: tint by depth
        for y in ys:
            if y > y_water:
                x, lift, wd = geom(y); yy = int(y - lift); t = min(1.0, (y - y_water) / max(1.0, (y_dip - y_water)))
                if lift < 4 * depth_s(y):                    # at or under the surface
                    mix[max(0, yy - 1):min(h, yy + int(wd) + 3), max(0, int(x - wd)):min(w, int(x + wd) + 1)] = 0.35 + 0.35 * t
        colour = colour * (1 - mix) + base.astype(np.float32) * mix
    res = out * (1 - a) + colour * a
    return np.clip(res, 0, 255).astype(np.uint8)

def merge(prev, gen, allow, thr=12, grow=9, feather=4.0, use_changed=True):
    """The picture before, with only the step taken from a generated picture: gen's pixels where it differs from prev
    INSIDE the allowed region (a 0/1 mask), tone-matched to prev. Returns (picture, share of the frame taken)."""
    h, w = prev.shape[:2]; P = prev.astype(np.float32); G = gen.astype(np.float32)
    allow = (allow > 0)
    ring = cv2.dilate(allow.astype(np.uint8), np.ones((41, 41), np.uint8)).astype(bool) & ~allow
    same = ring & (np.abs(P - G).sum(2) < 40)
    off = np.median((P - G)[same], axis=0) if same.sum() > 500 else np.zeros(3, np.float32)
    Gm = np.clip(G + off, 0, 255)
    if use_changed:
        a = cv2.cvtColor(prev, cv2.COLOR_BGR2LAB).astype(np.float32); b = cv2.cvtColor(Gm.astype(np.uint8), cv2.COLOR_BGR2LAB).astype(np.float32)
        ch = (np.sqrt(((a - b) ** 2).sum(2)) > thr) & allow
        ch = cv2.morphologyEx(ch.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        m = cv2.dilate(ch, np.ones((grow, grow), np.uint8)).astype(np.float32) * allow
    else:
        m = allow.astype(np.float32)
    m = cv2.GaussianBlur(m, (0, 0), feather)[..., None]
    return np.clip(P * (1 - m) + Gm * m, 0, 255).astype(np.uint8), float((m > 0.5).mean()), off
def boxes(shape, bs):
    """A 0/1 mask from boxes (x0, x1, y0, y1) given as shares of the frame."""
    h, w = shape[:2]; m = np.zeros((h, w), np.uint8)
    for x0, x1, y0, y1 in bs: m[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)] = 1
    return m

def rutlike(img):
    """Bare brown earth (the ruts the truck left): renders tend to turf them over, so the merges keep them from the picture before."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(int); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    return (H <= 21) & (S >= 70) & (V >= 60) & (V <= 215)
def merge_keep(prev, gen, allow, keep, lit_v=150.0, **kw):
    """merge(), but where `keep` is set in prev (ruts) and gen shows only grass there, prev stays, darkened if gen put a shadow on it."""
    out, share, off = merge(prev, gen, allow, **kw)
    G = np.clip(gen.astype(np.float32) + off, 0, 255).astype(np.uint8)
    k = (keep > 0) & lawnlike_any(G) & (allow > 0)
    v = cv2.cvtColor(G, cv2.COLOR_BGR2HSV)[..., 2].astype(np.float32)
    f = np.clip(cv2.GaussianBlur(v, (0, 0), 3) / lit_v, 0.5, 1.0)
    f[f > 0.85] = 1.0
    k = cv2.GaussianBlur(cv2.dilate(k.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), 1.5)[..., None]
    res = out.astype(np.float32) * (1 - k) + prev.astype(np.float32) * f[..., None] * k
    return np.clip(res, 0, 255).astype(np.uint8), share, off
def lawnlike_any(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(int); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    return (H >= 22) & (H <= 95) & (S >= 45)
