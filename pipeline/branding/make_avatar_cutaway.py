#!/usr/bin/env python3
"""Profile pictures without the character (made 18 Nov 2026, no credits), plus a sheet showing how each fits on YouTube.

    python3 make_avatar_cutaway.py <house_still> <short_frame> <out_dir>

house_still  video 09's wide still W0 (seedream 768x1360, job bceb6aeb-d56b-4a43-aaae-cfea608a9e39 in 09-jobs.tsv):
             the storm house sliced open on a block of ground, in daylight. Get its URL with Higgsfield jobs_wait
             (timeout_seconds 0) on the job id; the generation CDN is reachable from a session.
short_frame  any 9:16 frame for the Shorts-player mock-up (the sheet used video 03's END still, job e84197e8-...).
Writes to out_dir:
  avatar-cutaway-house-800.png            A: that house cut out of its sky, pole and road, on the banner's blueprint blue
  avatar-cutaway-icon-yellow-800.png      B: a flat icon of the same idea, roof in the brand yellow #FFC83D
  avatar-cutaway-icon-terracotta-800.png  C: the same icon with the videos' terracotta roof
  fit-check-avatar-cutaway.jpg            all three on the channel page, the Shorts player, a comment and at 48/32/24 px
Needs numpy, Pillow, opencv-python-headless, and the preinstalled Playwright Chromium (via node).
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

GLOW, BLUE_DEEP, INK = (0x38, 0x70, 0xB6), (0x13, 0x34, 0x63), (0x08, 0x18, 0x30)
S = 800


def background(s=S):
    """The old avatar's backdrop: a radial blueprint-blue glow with a faint 8x8 grid (as in make_brand.py)."""
    yy, xx = np.mgrid[0:s, 0:s].astype(np.float32)
    r = np.sqrt((xx - 0.5 * s) ** 2 + (yy - 0.40 * s) ** 2) / (0.70 * s)
    t = (np.clip(r, 0, 1) ** 1.3)[..., None]
    bg = np.array(GLOW, np.float32) * (1 - t) + np.array(BLUE_DEEP, np.float32) * t
    img = Image.fromarray(bg.astype(np.uint8)).convert('RGBA')
    grid = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(grid)
    for k in range(1, 8):
        d.line([(k * s // 8, 0), (k * s // 8, s)], fill=(255, 255, 255, 14), width=2)
        d.line([(0, k * s // 8), (s, k * s // 8)], fill=(255, 255, 255, 14), width=2)
    img.alpha_composite(grid)
    return img


# ---------------------------------------------------------------- A: the real house
def cut_house(src_path):
    """Alpha mask for the W0 still: sky by colour (rows above the eaves, flood-filled from the top edge), then fixed
    rules for what colour can't separate: the pole and its wire (x < 118, and x <= 153 below the eaves), the road
    strips beside the walls (walls at x 154 and 721), and the block trimmed at x 107 so the slice ends at the same
    distance on both sides of the house. Measured on this still only; another still needs its own numbers."""
    src = np.array(Image.open(src_path).convert('RGB'))
    h, w, _ = src.shape
    lab = cv2.cvtColor(src, cv2.COLOR_RGB2LAB).astype(np.float32)
    lab[..., 0] *= 100 / 255.0
    lab[..., 1:] -= 128.0
    roof_zone = 432
    left = cv2.GaussianBlur(np.median(lab[:, 2:26, :], axis=1).reshape(h, 1, 3), (1, 31), 0).reshape(h, 3)
    right = cv2.GaussianBlur(np.median(lab[:, 752:766, :], axis=1).reshape(h, 1, 3), (1, 31), 0).reshape(h, 3)
    t = np.linspace(0, 1, w).reshape(1, w, 1)
    sky = left.reshape(h, 1, 3) * (1 - t) + right.reshape(h, 1, 3) * t
    de = cv2.GaussianBlur(np.sqrt(((lab - sky) ** 2).sum(axis=2)), (3, 3), 0)
    cand = (de < 9.0).astype(np.uint8)
    cand[roof_zone:, :] = 0
    _, lbl = cv2.connectedComponents(cand, connectivity=4)
    bg = np.isin(lbl, list(set(np.unique(lbl[0, :])) - {0}))
    # lawn line per column (first green-ish row below y 760), smoothed
    g = src.astype(np.int32)
    green = (g[..., 1] > g[..., 2] * 1.35) & (g[..., 1] >= g[..., 0] * 0.80)
    lawn = np.array([760 + np.where(green[760:830, x])[0][0] if green[760:830, x].any() else 790 for x in range(w)])
    lawn = np.round(np.convolve(np.pad(lawn, 15, mode='edge'), np.ones(31) / 31, mode='valid')).astype(int)
    yy, xx = np.mgrid[0:h, 0:w]
    above = yy < lawn[None, :]
    bg |= above & ((xx < 118) | ((xx <= 153) & (yy >= roof_zone - 2)) | ((xx >= 722) & (yy >= roof_zone - 2)))
    fg = (~bg).astype(np.uint8)
    n, lbl, stats, _ = cv2.connectedComponentsWithStats(fg, connectivity=4)
    fg = (lbl == 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    inv = 1 - fg
    _, lbl = cv2.connectedComponents(inv, connectivity=4)
    border = set(np.unique(np.r_[lbl[0], lbl[-1], lbl[:, 0], lbl[:, -1]])) - {0}
    fg[(inv == 1) & ~np.isin(lbl, list(border))] = 1
    fg[:, :107] = 0
    alpha = cv2.GaussianBlur(fg.astype(np.float32), (0, 0), 0.7)
    return Image.fromarray(np.dstack([src, (alpha * 255).astype(np.uint8)]), 'RGBA')


def make_house(src_path, out_path, f=0.85, cx_src=437.5, peak_src=176, peak_y=74):
    img = background()
    house = cut_house(src_path)
    house = house.convert('RGBa').resize((round(house.width * f), round(house.height * f)), Image.LANCZOS).convert('RGBA')
    ox, oy = round(S / 2 - cx_src * f), round(peak_y - peak_src * f)
    shadow = Image.new('RGBA', house.size, INK + (0,))
    shadow.putalpha(house.getchannel('A').filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.50)))
    for layer_img, (dx, dy) in ((shadow, (9, 12)), (house, (0, 0))):
        layer = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        layer.paste(layer_img, (ox + dx, oy + dy))
        img.alpha_composite(layer)
    img.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.2, percent=45, threshold=2)).save(out_path, optimize=True)


# ---------------------------------------------------------------- B and C: the flat icon
def icon_svg(roof='yellow'):
    """A near head-on dimetric view (like the videos' camera: slightly above and to the right). One block of ground cut
    toward the viewer, a house flush with the cut and sliced open in the same plane (two floors, a bath upstairs, the
    attic), soil layers, a cyan groundwater band, and a pipe from the bath down through both cuts into the water."""
    AX, AY, BX, BY = 0.94, 0.20, -0.36, 0.40   # screen steps for +x (along the cut) and +y (toward the viewer)
    out = '#0D2546'
    A, BD, HB = 330, 230, 118
    HX0, HX1, HY0, T = 68, 262, 56, 9
    F1, SLAB, HW, HR, OV = 78, 9, 164, 96, 13
    layers = [(0, 11, '#58A83A'), (11, 46, '#7A4A2A'), (46, 76, '#D6A55F'), (76, 96, '#A9683A'), (96, 118, '#39C2E6')]
    rc = {'yellow': ('#FFC83D', '#E9AA2A', '#A9720E'), 'terracotta': ('#E2774A', '#C55E35', '#86361A')}[roof]
    wall_x, cut, back_in, left_in, floor, attic_floor, attic_back = '#E2CDA9', '#FFF8EA', '#FBF1DF', '#E6D3B3', '#D9A766', '#B9824A', '#6E4529'
    pipe_x, pipe_w = 214, 22
    zr, zt = HB + HW, HB + HW + HR
    xm = (HX0 + HX1) / 2
    drop = OV * HR / ((HX1 - HX0) / 2)
    z1, z2, zc = HB + F1, HB + F1 + SLAB, zr - 8

    def shade(c, k):
        r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
        return '#%02X%02X%02X' % tuple(max(0, min(255, round(v * k))) for v in (r, g, b))

    def proj(x, y, z):
        return (x * AX + y * BX, x * AY + y * BY - z)

    pts = [(0, 0, HB), (A, 0, HB), (A, BD, HB), (0, BD, HB), (A, 0, 0), (A, BD, 0), (0, BD, 0), (xm, HY0 - OV, zt),
           (xm, BD, zt), (HX0 - OV, BD, zr - drop), (HX1 + OV, HY0 - OV, zr - drop), (HX0 - OV, HY0 - OV, zr - drop)]
    xs, ys = zip(*(proj(*p) for p in pts))
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    k = 324 / max(math.hypot(px - cx, py - cy) for px, py in zip(xs, ys))
    ox, oy = 400 - cx * k, 416 - cy * k

    def P(x, y, z):
        sx, sy = proj(x, y, z)
        return (ox + sx * k, oy + sy * k)

    def poly(p3, fill, stroke=out, sw=3.0):
        st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ''
        return '<polygon points="%s" fill="%s"%s/>' % (' '.join('%.1f,%.1f' % P(*p) for p in p3), fill, st)

    def ry(y, x0, x1, za, zb, fill, **kw): return poly([(x0, y, za), (x1, y, za), (x1, y, zb), (x0, y, zb)], fill, **kw)
    def rx(x, y0, y1, za, zb, fill, **kw): return poly([(x, y0, za), (x, y1, za), (x, y1, zb), (x, y0, zb)], fill, **kw)
    def rz(z, x0, x1, y0, y1, fill, **kw): return poly([(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)], fill, **kw)

    el = []
    sx, sy = P(A / 2 + 10, BD / 2, 0)
    el.append(f'<ellipse cx="{sx:.1f}" cy="{sy + 30 * k:.1f}" rx="{215 * k:.1f}" ry="{52 * k:.1f}" fill="#081830" opacity="0.42" filter="url(#blur)"/>')
    el.append(rz(HB, 0, A, 0, BD, '#7CCB55'))                                  # lawn
    for top, bot, col in layers:                                                # the cut: right side, then front
        el.append(rx(A, BD, 0, HB - bot, HB - top, shade(col, 0.78), stroke=None))
        el.append(ry(BD, 0, A, HB - bot, HB - top, col, stroke=None))
    zw = HB - 96
    el.append(ry(BD, 0, A, zw - 5, zw, '#A8EEFB', stroke=None))
    el.append(rx(A, BD, 0, zw - 5, zw, '#86D9EA', stroke=None))
    el.append(rx(A, BD, 0, 0, HB, 'none'))
    el.append(ry(BD, 0, A, 0, HB, 'none'))
    for zb, ztop in ((HB, z1), (z2, zc)):                                      # rooms seen through the cut
        el.append(ry(HY0 + T, HX0 + T, HX1 - T, zb, ztop, back_in, sw=2.2))
        el.append(rx(HX0 + T, BD, HY0 + T, zb, ztop, left_in, sw=2.2))
        el.append(rz(zb, HX0 + T, HX1 - T, HY0 + T, BD, floor, sw=2.2))
        if zb == HB:
            el.append(ry(HY0 + T, 104, 150, HB + 26, HB + 58, '#7FB0E6', sw=2.2))
            el.append(rz(z1, HX0 + T, HX1 - T, HY0 + T, BD, floor, sw=2.2))
    bx0, bx1, by0, by1, bh = 160, 244, 150, 218, 26                           # the bath upstairs
    el.append(ry(by1, bx0, bx1, z2, z2 + bh, '#FFFFFF', sw=2.4))
    el.append(rx(bx1, by1, by0, z2, z2 + bh, '#D3DEE6', sw=2.4))
    el.append(rz(z2 + bh, bx0, bx1, by0, by1, '#FFFFFF', sw=2.4))
    el.append(rz(z2 + bh, bx0 + 8, bx1 - 8, by0 + 8, by1 - 8, '#39C2E6', stroke=None))
    el.append(rz(zr, HX0 + T, HX1 - T, HY0 + T, BD, attic_floor, sw=2.2))      # the attic
    el.append(poly([(HX0 + T, HY0 + T, zr), (HX1 - T, HY0 + T, zr), (xm, HY0 + T, zt - T * 1.5)], attic_back, sw=2.2))
    el.append(ry(BD, HX0, HX0 + T, HB, zr, cut))                              # wall, slab and ceiling sections
    el.append(ry(BD, HX1 - T, HX1, HB, zr, cut))
    el.append(ry(BD, HX0, HX1, z1, z2, cut))
    el.append(ry(BD, HX0, HX1, zc, zr, cut))
    el.append(ry(BD, HX0 - 5, HX1 + 5, HB - 7, HB, '#B5AEA2'))                # foundation
    el.append(rx(HX1, BD, HY0, HB, zr, wall_x))                               # outside right wall, two windows
    for zw0 in (HB + 28, z2 + 30):
        el.append(rx(HX1, 160, 110, zw0, zw0 + 36, '#4F80BE', sw=2.4))
    el.append(poly([(xm, HY0 - OV, zt), (xm, BD, zt), (HX1 + OV, BD, zr - drop), (HX1 + OV, HY0 - OV, zr - drop)], rc[0]))
    el.append(poly([(xm, HY0 - OV, zt), (xm, BD, zt), (HX0 - OV, BD, zr - drop), (HX0 - OV, HY0 - OV, zr - drop)], rc[1]))
    th = 12
    el.append(poly([(HX0 - OV, BD, zr - drop), (xm, BD, zt), (HX1 + OV, BD, zr - drop), (HX1 + OV, BD, zr - drop - th),
                    (xm, BD, zt - th * 1.4), (HX0 - OV, BD, zr - drop - th)], rc[2]))
    for z_lo, z_hi, inset in ((zw - 12, HB - 7, 4), (HB - 7, z2 + 3, 0)):     # the pipe, in the cut plane
        el.append(ry(BD, pipe_x - pipe_w / 2, pipe_x + pipe_w / 2, z_lo, z_hi, '#EEF2F5', sw=2.6))
        el.append(ry(BD, pipe_x - pipe_w / 2 + 7, pipe_x + pipe_w / 2 - 7, z_lo + inset, z_hi, '#39C2E6', stroke=None))
    grid = ''.join(f'<line x1="{v}" y1="0" x2="{v}" y2="800" stroke="#fff" stroke-opacity="0.055" stroke-width="2"/>'
                   f'<line x1="0" y1="{v}" x2="800" y2="{v}" stroke="#fff" stroke-opacity="0.055" stroke-width="2"/>'
                   for v in range(100, 800, 100))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800"><defs>'
            '<radialGradient id="bg" cx="0.5" cy="0.40" r="0.70"><stop offset="0" stop-color="#3870B6"/>'
            '<stop offset="1" stop-color="#133463"/></radialGradient><filter id="blur" x="-30%" y="-60%" width="160%"'
            ' height="220%"><feGaussianBlur stdDeviation="16"/></filter></defs><rect width="800" height="800" fill="url(#bg)"/>'
            + grid + ''.join(el) + '</svg>')


SHOT_JS = """
const { chromium } = require('playwright');
(async () => { const [html, out, w, h, full] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 2 });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: full === 'full' }); await b.close(); })();
"""


def shot(html_path, png_path, w, h, work, full=False):
    """Screenshot at 2x with the preinstalled Playwright Chromium (the viewport only, or the whole page)."""
    js = work / 'shot.js'
    js.write_text(SHOT_JS)
    subprocess.run(['node', str(js), str(html_path), str(png_path), str(w), str(h), 'full' if full else 'view'], check=True, cwd=work)


def make_icon(roof, out_path, work):
    html = work / f'icon_{roof}.html'
    html.write_text('<!doctype html><html><head><style>html,body{margin:0}svg{display:block}</style></head><body>' + icon_svg(roof) + '</body></html>')
    shot(html.resolve(), work / f'icon_{roof}@2x.png', 800, 800, work)
    Image.open(work / f'icon_{roof}@2x.png').convert('RGB').resize((S, S), Image.LANCZOS).save(out_path, optimize=True)


# ---------------------------------------------------------------- the fit-check sheet
CSS = """*{box-sizing:border-box} body{margin:0;background:#EEF1F5;font-family:Inter,'DejaVu Sans',sans-serif;color:#0f0f0f;padding:40px 48px 48px;width:1440px}
h1{font-size:30px;margin:0 0 6px;font-weight:800} .sub{color:#555;font-size:16px;margin:0 0 28px}
.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.col{background:#fff;border-radius:18px;padding:22px 22px 24px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.tag{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#1F4E8C;margin-bottom:4px}
.name{font-size:20px;font-weight:800;margin-bottom:16px} .rec{display:inline-block;background:#FFC83D;color:#081830;font-size:12px;font-weight:800;padding:2px 7px;border-radius:6px;margin-left:10px;vertical-align:1px;letter-spacing:.04em}
.hero{display:flex;justify-content:center;margin:4px 0 18px} .hero img{width:200px;height:200px;border-radius:50%}
.lab{font-size:12px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#888;margin:16px 0 8px}
.hdr{display:flex;align-items:center;gap:14px;padding:14px;border-radius:12px} .hdr img{width:72px;height:72px;border-radius:50%}
.hdr .t{font-size:19px;font-weight:700} .hdr .s{font-size:13px;margin-top:3px} .light{background:#fff;border:1px solid #e5e5e5} .light .s{color:#606060}
.dark{background:#0f0f0f;color:#f1f1f1} .dark .s{color:#aaa}
.short{position:relative;width:100%;height:300px;border-radius:12px;overflow:hidden;background:#000}
.short>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 60%}
.short .ov{position:absolute;left:0;right:0;bottom:0;padding:60px 14px 14px;background:linear-gradient(transparent,rgba(0,0,0,.75));color:#fff}
.short .row{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600} .short .row img{width:32px;height:32px;border-radius:50%}
.short .btn{background:#fff;color:#0f0f0f;font-size:13px;font-weight:700;padding:6px 12px;border-radius:18px;margin-left:4px} .short .ti{font-size:14px;margin-top:8px}
.sizes{display:flex;border-radius:12px;overflow:hidden} .sizes div{flex:1;display:flex;align-items:flex-end;justify-content:space-around;padding:14px 8px 10px}
.sizes figure{margin:0;text-align:center;font-size:11px} .sizes img{border-radius:50%;display:block;margin:0 auto 4px}
.sw{background:#fff;border:1px solid #e5e5e5;color:#777} .sd{background:#0f0f0f;color:#999}
.cmt{display:flex;gap:10px;align-items:flex-start;padding:12px 14px;border:1px solid #e5e5e5;border-radius:12px;font-size:13px}
.cmt img{width:24px;height:24px;border-radius:50%;margin-top:1px} .cmt b{font-size:12px} .cmt .c{color:#333;margin-top:2px}"""


def make_fit_check(opts, frame_name, out_path, work):
    cols = []
    for img, tag, name, rec in opts:
        def sizes(cls):
            return f'<div class="{cls}">' + ''.join(f'<figure><img src="{img}" width="{d}" height="{d}"><figcaption>{d}px</figcaption></figure>' for d in (48, 32, 24)) + '</div>'
        cols.append(f'''<div class="col"><div class="tag">{tag}{'<span class="rec">RECOMMENDED</span>' if rec else ''}</div><div class="name">{name}</div>
<div class="hero"><img src="{img}"></div><div class="lab">Channel page</div>
<div class="hdr light"><img src="{img}"><div><div class="t">LetZBuildTogether</div><div class="s">@LetzBuildTogether · 310 subscribers · 10 videos</div></div></div>
<div class="hdr dark" style="margin-top:10px"><img src="{img}"><div><div class="t">LetZBuildTogether</div><div class="s">@LetzBuildTogether · 310 subscribers</div></div></div>
<div class="lab">Shorts player</div><div class="short"><img class="bg" src="{frame_name}"><div class="ov"><div class="row"><img src="{img}">@LetzBuildTogether<span class="btn">Subscribe</span></div><div class="ti">Why Don't Fire Hydrants Freeze? ❄️🚗</div></div></div>
<div class="lab">Comments</div><div class="cmt"><img src="{img}"><div><b>@LetzBuildTogether</b><div class="c">The barrel stays dry until the valve opens. That's the whole trick.</div></div></div>
<div class="lab">Small sizes (light and dark)</div><div class="sizes">{sizes('sw')}{sizes('sd')}</div></div>''')
    html = work / 'fit_check.html'
    html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
                    '<h1>New profile picture: three options, no character</h1><p class="sub">Each one shown where YouTube shows a '
                    'profile picture: the channel page, the Shorts player, comments, and the smallest sizes.</p>'
                    f'<div class="cols">{"".join(cols)}</div></body></html>')
    shot(html.resolve(), work / 'fit_check@2x.png', 1440, 900, work, full=True)
    Image.open(work / 'fit_check@2x.png').convert('RGB').save(out_path, quality=90)


def main():
    house_still, frame, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix='avatar_'))
    names = {'A': 'avatar-cutaway-house-800.png', 'B': 'avatar-cutaway-icon-yellow-800.png', 'C': 'avatar-cutaway-icon-terracotta-800.png'}
    make_house(house_still, out / names['A'])
    make_icon('yellow', out / names['B'], work)
    make_icon('terracotta', out / names['C'], work)
    for n in names.values():
        shutil.copy(out / n, work / n)
    shutil.copy(frame, work / 'short_frame.png')
    make_fit_check([(names['A'], 'Option A', 'The house from your videos', True),
                    (names['B'], 'Option B', 'Flat icon, yellow roof', False),
                    (names['C'], 'Option C', 'Flat icon, terracotta roof', False)],
                   'short_frame.png', out / 'fit-check-avatar-cutaway.jpg', work)
    for n in list(names.values()) + ['fit-check-avatar-cutaway.jpg']:
        print('wrote', out / n, Image.open(out / n).size, f'{(out / n).stat().st_size // 1024} KB')


if __name__ == '__main__':
    main()
