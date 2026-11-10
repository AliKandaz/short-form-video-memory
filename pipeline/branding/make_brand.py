#!/usr/bin/env python3
"""Make the YouTube profile picture (800x800) and banner (2560x1440) from the channel's existing renders. No credits.

    python3 make_brand.py <src_dir> <fonts_dir> <out_dir> [--eyebrow TEXT] [--line1 TEXT] [--line2 TEXT]

src_dir   mascot_rgba.png (made by cutout.py from the locked mascot, job f97004b9-...) and the finished-build stills
          v1_end.png, v2_end.png, v3_end.png (seedream 768x1360; job ids under END in pipeline/0N-jobs.tsv).
fonts_dir barlow-condensed-latin-800/700-normal.woff2 and barlow-semi-condensed-latin-600-normal.woff2
          (npm pack @fontsource/barlow-condensed@5.1.0 @fontsource/barlow-semi-condensed@5.1.0).
Writes avatar-800.png, banner-2560x1440.png (JPG instead if the PNG is over 6 MB) and fit-check.png (how the banner
crops on TV, desktop and phone, and the avatar at feed sizes). Renders HTML with render.js (Playwright Chromium).

Banner geometry (YouTube, 2560x1440 upload): TV shows everything; desktop shows the full-width strip y 508-931;
phones show the centre box x 507-2053, y 508-931 (1546x423, the scaled-up form of the 1235x338 safe area YouTube
gives for its 2048x1152 minimum). Everything that must be read sits inside that box with a 30 px margin.
"""
import argparse
import html
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent

# brand tokens: blueprint blue from the "how it's built" world, yellow from the mascot's hard hat (hat median #EABD3C)
BLUE = "#1F4E8C"
BLUE_DEEP = "#133463"
GLOW = "#3870B6"
YELLOW = "#FFC83D"
INK = "#081830"
PALE = "#C9DAF0"

W, H = 2560, 1440
STRIP = (508, 931)                 # desktop strip, full width
SAFE = (507, 508, 2053, 931)       # phone box
INNER = (537, 538, 2023, 901)      # safe box minus a 30 px margin
TILE_W, TILE_H, TILE_GAP = 222, 296, 32

# 3:4 crops of the finished builds: (file, x0, y0, width) on the 768x1360 stills
TILES = [
    ("v1_end.png", 100, 330, 560, "MUD", "HOUSE"),
    ("v2_end.png", 40, 300, 680, "LOG", "CANOE"),
    ("v3_end.png", 0, 130, 768, "PIPE", "HYDRANT"),
]


def rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def scale_rgba(im, factor):
    """Resize with premultiplied alpha so edges don't pick up dark fringes."""
    size = (round(im.width * factor), round(im.height * factor))
    return im.convert("RGBa").resize(size, Image.LANCZOS).convert("RGBA")


def clean_feet(mascot):
    """Drop the floor shadow the reference render left around the boots (keeps leather and soles)."""
    a = np.array(mascot).astype(np.float32)
    rgbv = a[..., :3]
    mx, mn = rgbv.max(axis=2), rgbv.min(axis=2)
    sat = (mx - mn) / np.maximum(mx, 1)
    ys = np.arange(a.shape[0])[:, None]
    xs = np.arange(a.shape[1])[None, :]
    region = ys >= 1015
    shadow = region & ((xs < 272) | ((sat < 0.42) & (mx > 95)))
    a[..., 3][shadow] = 0
    return Image.fromarray(a.astype(np.uint8), "RGBA")


def make_avatar(mascot, out_path, size=800):
    s = size
    yy, xx = np.mgrid[0:s, 0:s].astype(np.float32)
    r = np.sqrt((xx - 0.5 * s) ** 2 + (yy - 0.40 * s) ** 2) / (0.70 * s)
    t = (np.clip(r, 0, 1) ** 1.3)[..., None]
    bg = np.array(rgb(GLOW), np.float32) * (1 - t) + np.array(rgb(BLUE_DEEP), np.float32) * t
    img = Image.fromarray(bg.astype(np.uint8)).convert("RGBA")
    grid = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(grid)
    step = s // 8
    for k in range(1, 8):
        d.line([(k * step, 0), (k * step, s)], fill=(255, 255, 255, 14), width=2)
        d.line([(0, k * step), (s, k * step)], fill=(255, 255, 255, 14), width=2)
    img.alpha_composite(grid)

    # head and shoulders: hat top (x 417.5, y 219 on the 832x1248 reference) at 11.5% from the top, centred
    f = 1.95 * size / 800
    m = scale_rgba(mascot, f)
    ox = round(s / 2 - 417.5 * f)
    oy = round(0.115 * s - 219 * f)
    shadow = Image.new("RGBA", m.size, rgb(INK) + (0,))
    shadow.putalpha(m.getchannel("A").filter(ImageFilter.GaussianBlur(14 * size / 800)).point(lambda v: int(v * 0.45)))
    for layer_img, (dx, dy) in ((shadow, (round(10 * f), round(14 * f))), (m, (0, 0))):
        layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
        layer.paste(layer_img, (ox + dx, oy + dy))
        img.alpha_composite(layer)
    img = img.convert("RGB").filter(ImageFilter.UnsharpMask(radius=1.2, percent=55, threshold=2))
    img.save(out_path, optimize=True)
    return out_path


def make_tiles(src, work):
    names = []
    for i, (fname, x0, y0, w, _, _) in enumerate(TILES):
        im = Image.open(src / fname).convert("RGB")
        h = round(w * 4 / 3)
        tile = im.crop((x0, y0, x0 + w, y0 + h)).resize((TILE_W * 2, TILE_H * 2), Image.LANCZOS)
        name = f"tile{i}.png"
        tile.save(work / name)
        names.append(name)
    return names


def arrow_svg():
    return ('<svg class="arrow" viewBox="0 0 40 24" aria-hidden="true"><path d="M2 12h32M24 3l10 9-10 9" fill="none" '
            f'stroke="{YELLOW}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def banner_html(tile_names, mascot_name, mascot_size, eyebrow, line1, line2):
    tiles_left = INNER[2] - (3 * TILE_W + 2 * TILE_GAP)
    tile_top = round((STRIP[0] + STRIP[1]) / 2 - (TILE_H + 12 + 44) / 2)
    figs = []
    for i, (name, t) in enumerate(zip(tile_names, TILES)):
        x = tiles_left + i * (TILE_W + TILE_GAP)
        figs.append(f'<figure class="tile" style="left:{x}px;top:{tile_top}px"><img src="{name}" alt="">'
                    f'<figcaption>{html.escape(t[4])}{arrow_svg()}{html.escape(t[5])}</figcaption></figure>')
    next_x = INNER[2] + 45
    figs.append(f'<figure class="tile next" style="left:{next_x}px;top:{tile_top}px"><div class="plan">?</div>'
                f'<figcaption>NEXT BUILD?</figcaption></figure>')
    mw, mh = mascot_size
    # mascot on the desktop-only left wing: centre x 300, hat top 44 px below the strip's top edge
    m_left = 300 - mw // 2
    m_top = STRIP[0] + 44
    left_max_w = tiles_left - 64 - INNER[0]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Barlow Condensed";font-weight:800;src:url(barlow-condensed-latin-800-normal.woff2) format("woff2")}}
@font-face{{font-family:"Barlow Condensed";font-weight:700;src:url(barlow-condensed-latin-700-normal.woff2) format("woff2")}}
@font-face{{font-family:"Barlow Semi Condensed";font-weight:600;src:url(barlow-semi-condensed-latin-600-normal.woff2) format("woff2")}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:{BLUE}}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  background:
   radial-gradient(ellipse 1400px 620px at 50% 50%, rgba(56,112,182,.62), rgba(56,112,182,0) 72%),
   radial-gradient(ellipse 2200px 1300px at 50% 50%, rgba(19,52,99,0) 55%, rgba(19,52,99,.75) 100%),
   repeating-linear-gradient(0deg, rgba(255,255,255,.11) 0 2px, transparent 2px 160px),
   repeating-linear-gradient(90deg, rgba(255,255,255,.11) 0 2px, transparent 2px 160px),
   repeating-linear-gradient(0deg, rgba(255,255,255,.045) 0 1px, transparent 1px 32px),
   repeating-linear-gradient(90deg, rgba(255,255,255,.045) 0 1px, transparent 1px 32px),
   {BLUE};
  background-position:center,center,0 80px,0 0,0 16px,0 0,0 0}}
.copy{{position:absolute;left:{INNER[0]}px;max-width:{left_max_w}px}}
.eyebrow{{font:600 40px/1 "Barlow Semi Condensed",sans-serif;letter-spacing:.16em;color:{PALE};margin:0 0 18px 4px}}
.headline{{display:inline-block;font:800 160px/.9 "Barlow Condensed",sans-serif;color:#fff;letter-spacing:.005em;
  text-shadow:0 6px 18px rgba(8,24,48,.45)}}
.headline span{{display:block;white-space:nowrap}}
.headline .accent{{color:{YELLOW}}}
.tile{{position:absolute;margin:0;width:{TILE_W}px}}
.tile img{{display:block;width:{TILE_W}px;height:{TILE_H}px;box-sizing:border-box;border:4px solid #fff;border-radius:18px;
  object-fit:cover;box-shadow:0 14px 30px rgba(8,24,48,.5)}}
.tile figcaption{{display:flex;align-items:center;justify-content:center;gap:6px;margin-top:12px;height:44px;
  font:700 36px/1 "Barlow Condensed",sans-serif;color:#fff;letter-spacing:.02em;white-space:nowrap}}
.arrow{{width:28px;height:18px;flex:none}}
.plan{{width:{TILE_W}px;height:{TILE_H}px;box-sizing:border-box;border:4px dashed rgba(255,255,255,.7);border-radius:18px;
  display:grid;place-items:center;font:800 190px/1 "Barlow Condensed",sans-serif;color:{YELLOW};background:rgba(255,255,255,.05)}}
.mascot{{position:absolute;left:{m_left}px;top:{m_top}px;width:{mw}px;height:{mh}px;
  filter:drop-shadow(10px 16px 18px rgba(8,24,48,.45))}}
</style></head><body><div class="canvas">
<img class="mascot" src="{mascot_name}" alt="">
<div class="copy" id="copy"><div class="eyebrow">{html.escape(eyebrow)}</div>
<div class="headline" id="headline"><span>{html.escape(line1)}</span><span class="accent">{html.escape(line2)}</span></div></div>
{''.join(figs)}
</div>
<script>
document.fonts.ready.then(function(){{
  var copy=document.getElementById('copy'), hl=document.getElementById('headline');
  var maxW={left_max_w}, maxH={INNER[3] - INNER[1]}, size=170;
  while(size>60){{ hl.style.fontSize=size+'px';
    if(hl.getBoundingClientRect().width<=maxW && copy.getBoundingClientRect().height<=maxH) break; size-=2; }}
  var h=copy.getBoundingClientRect().height;
  copy.style.top=Math.round({(STRIP[0] + STRIP[1]) / 2}-h/2)+'px';
  document.body.dataset.fontSize=size;
  document.body.dataset.ready='1';
}});
</script></body></html>"""


def fit_check_html(name):
    sx, sy, ex, ey = SAFE
    k = 1280 / W
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#eef1f5;font:16px/1.4 Inter,system-ui,sans-serif;color:#1b1f27}}
.wrap{{width:1440px;margin:0 auto;padding:40px 60px 50px;box-sizing:border-box;display:flex;flex-direction:column;gap:34px}}
h1{{font:700 34px/1.1 Inter,sans-serif;margin:0}}
h2{{font:600 15px/1 Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#56607a;margin:0 0 12px}}
.tv{{position:relative;width:1280px;height:720px}}
.tv img{{width:1280px;height:720px;display:block;border-radius:6px}}
.zone{{position:absolute;box-sizing:border-box}}
.strip{{left:0;top:{STRIP[0] * k}px;width:1280px;height:{(STRIP[1] - STRIP[0]) * k}px;border:3px dashed #ffffff}}
.safe{{left:{sx * k}px;top:{sy * k}px;width:{(ex - sx) * k}px;height:{(ey - sy) * k}px;border:3px solid {YELLOW}}}
.tag{{position:absolute;font:600 15px/1 Inter,sans-serif;padding:6px 9px;border-radius:5px}}
.row{{display:flex;gap:40px;align-items:flex-start}}
.desk{{width:840px;background:#fff;border-radius:14px;padding:22px;box-sizing:border-box}}
.desk .ban{{width:796px;height:{round(796 * 423 / 2560)}px;border-radius:12px;display:block}}
.who{{display:flex;gap:18px;align-items:center;margin-top:18px}}
.who img{{border-radius:50%;display:block}}
.name{{font:700 26px/1.2 Inter,sans-serif}}
.meta{{color:#606060;font-size:15px}}
.phone{{width:390px;background:#0f0f0f;border-radius:34px;padding:16px;box-sizing:border-box;color:#f1f1f1}}
.phone .ban{{width:358px;height:{round(358 * 423 / 1546)}px;border-radius:10px;display:block}}
.phone .meta{{color:#aaa;font-size:12px}}
.phone .name{{font-size:20px}}
.sizes{{display:flex;gap:28px;align-items:flex-end;padding:18px 22px;border-radius:12px}}
.sizes img{{border-radius:50%;display:block}}
.sizes figure{{margin:0;text-align:center;font-size:12px}}
</style></head><body><div class="wrap">
<h1>How it fits</h1>
<div><h2>Full upload (what TVs show)</h2><div class="tv"><img src="{name}" alt="">
<div class="zone strip"></div><div class="zone safe"></div>
<span class="tag" style="left:10px;top:{STRIP[0] * k - 34}px;background:#fff">Desktop shows the dashed strip</span>
<span class="tag" style="left:{sx * k}px;top:{ey * k + 10}px;background:{YELLOW}">Phones show only the yellow box</span></div></div>
<div class="row">
<div><h2>Desktop</h2><div class="desk"><img class="ban" src="strip.png" alt="">
<div class="who"><img src="avatar-800.png" width="120" height="120" alt=""><div><div class="name">overthinkingyearly</div>
<div class="meta">@overthinkingyearly · 13 subscribers · 6 videos</div></div></div></div></div>
<div><h2>Phone</h2><div class="phone"><img class="ban" src="safe.png" alt="">
<div class="who"><img src="avatar-800.png" width="72" height="72" alt=""><div><div class="name">overthinkingyearly</div>
<div class="meta">@overthinkingyearly · 13 subscribers</div></div></div></div></div>
</div>
<div><h2>Profile picture at the sizes YouTube shows it</h2><div class="row">
<div class="sizes" style="background:#fff">{''.join(f'<figure><img src="avatar-800.png" width="{z}" height="{z}" alt=""><figcaption>{z}px</figcaption></figure>' for z in (160, 88, 48, 32, 24))}</div>
<div class="sizes" style="background:#0f0f0f;color:#aaa">{''.join(f'<figure><img src="avatar-800.png" width="{z}" height="{z}" alt=""><figcaption>{z}px</figcaption></figure>' for z in (160, 88, 48, 32, 24))}</div>
</div></div>
</div><script>document.body.dataset.ready='1'</script></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("fonts")
    ap.add_argument("out")
    ap.add_argument("--eyebrow", default="3D BUILD EXPLAINERS")
    ap.add_argument("--line1", default="ONE PROBLEM")
    ap.add_argument("--line2", default="AT A TIME")
    args = ap.parse_args()
    src, fonts, out = Path(args.src), Path(args.fonts), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    work = out / "work"
    work.mkdir(exist_ok=True)

    mascot = Image.open(src / "mascot_rgba.png").convert("RGBA")
    make_avatar(mascot, out / "avatar-800.png")
    shutil.copy(out / "avatar-800.png", work / "avatar-800.png")

    for woff in fonts.glob("*.woff2"):
        shutil.copy(woff, work / woff.name)
    tiles = make_tiles(src, work)
    body = clean_feet(mascot).crop((150, 200, 640, 1090))      # full figure, boots included
    body = scale_rgba(body, 0.9)
    body.save(work / "mascot_banner.png")

    (work / "banner.html").write_text(banner_html(tiles, "mascot_banner.png", body.size,
                                                  args.eyebrow, args.line1, args.line2), encoding="utf-8")
    png = work / "banner.png"
    subprocess.run(["node", str(HERE / "render.js"), str(work / "banner.html"), str(png), str(W), str(H)], check=True)
    banner = Image.open(png).convert("RGB")
    final = out / "banner-2560x1440.png"
    banner.save(final, optimize=True)
    if final.stat().st_size > 6_000_000:
        final.unlink()
        final = out / "banner-2560x1440.jpg"
        banner.save(final, quality=93, subsampling=0)
    print("banner", final, final.stat().st_size, "bytes")

    banner.crop((0, STRIP[0], W, STRIP[1])).save(work / "strip.png")
    banner.crop(SAFE).save(work / "safe.png")
    banner.save(work / "full.jpg", quality=90)
    (work / "fit.html").write_text(fit_check_html("full.jpg"), encoding="utf-8")
    subprocess.run(["node", str(HERE / "render.js"), str(work / "fit.html"), str(out / "fit-check.png"),
                    "1440", "900", "full"], check=True)


if __name__ == "__main__":
    main()
