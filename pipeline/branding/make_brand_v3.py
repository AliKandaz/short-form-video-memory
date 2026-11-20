#!/usr/bin/env python3
"""Brand set v3 (20 Nov 2026): a new profile picture and YouTube banner drawn from scratch, with nothing taken from the videos
or the current account (no stills, no mascot, no channel name or numbers). No credits: everything is drawn in code.

The user asked for "a high converting profile and banner picture along with a bio I don't want it to include anything from my
current videos or account. something that makes sense on the type of educational videos I make".

The mark: a white isometric cube with its top front corner cut away, showing what's hidden inside (coloured layers and the cut
ends of a water pipe and a cable): the format of the channel in one shape. Plain outside, interesting inside.

Usage:
    python3 make_brand_v3.py <fonts_dir> <out_dir> [--line1 "YOU'VE SEEN IT."] [--line2 "NOW SEE INSIDE IT."]
        [--highlight INSIDE] [--pill "NEW 3D EXPLAINER EVERY 2 DAYS"]

fonts_dir  anton-latin-400-normal.woff2 and inter-latin-700-normal.woff2, inter-latin-800-normal.woff2
           (npm pack @fontsource/anton@5.2.5 @fontsource/inter@5.2.5, then untar; the files are in package/files/).
out_dir    avatar-v3-1080.png (TikTok), avatar-v3-800.png (YouTube), banner-v3-2560x1440.jpg (YouTube),
           fit-check-v3.jpg (the picture at feed sizes on light and dark, and the banner as TVs, computers and phones crop it).

Banner geometry (YouTube, 2560x1440 upload): TVs show everything; computers show the full-width strip y 508-931; phones show
only the centre box x 507-2053, y 508-931 (1546x423). Everything that matters sits inside the phone box; the outer areas
only carry the background. Profile picture: shown as a circle by both platforms (98 px on a YouTube channel page, about 48 px
beside a TikTok video, 24-32 px in comments), so it is one big shape kept above TikTok's follow badge at the bottom.
Rendered with render.js (Playwright Chromium).
"""
import argparse
import math
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
C30 = math.cos(math.pi / 6)

# Palette: hi-vis yellow and ink, with the inside in orange, teal and navy.
YELLOW, YELLOW_DEEP, INK, INK_2 = "#FFD62E", "#FFBE0B", "#101A33", "#1B2A55"
SKIN_TOP, SKIN_LEFT, SKIN_RIGHT = ("#FFFFFF", "#EEF3FA"), "#DFE6F1", "#BFCADD"   # cool whites read cleaner on yellow
CUT = 0.42                                     # the cut starts 42% of the way in, so the inside shows at small sizes
LAYERS = [(CUT, .70, "#24396F"), (.70, .80, "#14A898"), (.80, .945, "#FF7A2F"), (.945, 1.0, "#FFFFFF")]
FLOOR = "#33508F"
KL, KR = 0.90, 0.76                            # light from the upper left: left faces a little darker, right faces more


def iso(o, s, p):
    x, y, z = p
    return (o[0] + (x - y) * C30 * s, o[1] + (x + y) * 0.5 * s - z * s)


def pts(o, s, ps):
    return " ".join("%.2f,%.2f" % iso(o, s, p) for p in ps)


def mix(c, k):
    c = c.lstrip("#")
    r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = r * k, g * k, b * k
    return "#%02x%02x%02x" % tuple(int(round(max(0, min(255, v)))) for v in (r, g, b))


def faces(c=CUT):
    return dict(
        top=[(0, 0, 1), (1, 0, 1), (1, c, 1), (c, c, 1), (c, 1, 1), (0, 1, 1)],
        right=[(1, 0, 1), (1, 0, 0), (1, 1, 0), (1, 1, c), (1, c, c), (1, c, 1)],
        left=[(0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 1, c), (c, 1, c), (c, 1, 1)],
        floor=[(c, c, c), (1, c, c), (1, 1, c), (c, 1, c)],
        hexagon=[(0, 0, 1), (1, 0, 1), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1)],
        notch=[(c, c, 1), (1, c, 1), (1, c, c), (1, 1, c), (c, 1, c), (c, 1, 1)],
    )


def disc(o, s, plane, centre, r, c=CUT, n=72):
    """A circle on one of the two cut walls (the cut end of a pipe), as an isometric ellipse."""
    ps = []
    for i in range(n):
        t = 2 * math.pi * i / n
        a, b = centre[0] + r * math.cos(t), centre[1] + r * math.sin(t)
        ps.append((c, a, b) if plane == "x" else (a, c, b))
    return pts(o, s, ps)


def cube(o, s, uid, shadow=("#9A5B00", 0.32), c=CUT, ink=INK):
    """The cut cube, centred on o (the cut corner sits exactly on o), s = distance from o to the top point."""
    F, sw = faces(c), s * 0.042
    q = [f'<defs><filter id="bl{uid}" x="-50%" y="-50%" width="200%" height="200%">'
         f'<feGaussianBlur stdDeviation="{s * 0.055:.1f}"/></filter>'
         f'<radialGradient id="ao{uid}" cx="{o[0]}" cy="{o[1]}" r="{s * (1 - c) * 1.05:.1f}" gradientUnits="userSpaceOnUse">'
         f'<stop offset="0" stop-color="#000" stop-opacity="0.38"/><stop offset="0.55" stop-color="#000" stop-opacity="0.10"/>'
         f'<stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
         f'<linearGradient id="tp{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{SKIN_TOP[0]}"/>'
         f'<stop offset="1" stop-color="{SKIN_TOP[1]}"/></linearGradient>'
         f'<clipPath id="nc{uid}"><polygon points="{pts(o, s, F["notch"])}"/></clipPath></defs>']
    if shadow:
        q.append(f'<ellipse cx="{o[0]}" cy="{o[1] + s * 1.03:.1f}" rx="{s * 0.86:.1f}" ry="{s * 0.15:.1f}" '
                 f'fill="{shadow[0]}" opacity="{shadow[1]}" filter="url(#bl{uid})"/>')
    q.append(f'<polygon points="{pts(o, s, F["top"])}" fill="url(#tp{uid})"/>')
    q.append(f'<polygon points="{pts(o, s, F["left"])}" fill="{SKIN_LEFT}"/>')
    q.append(f'<polygon points="{pts(o, s, F["right"])}" fill="{SKIN_RIGHT}"/>')
    for z0, z1, col in LAYERS:   # the layers on the two cut walls
        q.append(f'<polygon points="{pts(o, s, [(c, c, z0), (c, 1, z0), (c, 1, z1), (c, c, z1)])}" fill="{mix(col, KR)}"/>')
        q.append(f'<polygon points="{pts(o, s, [(c, c, z0), (1, c, z0), (1, c, z1), (c, c, z1)])}" fill="{mix(col, KL)}"/>')
    q.append(f'<polygon points="{pts(o, s, F["floor"])}" fill="{FLOOR}"/>')
    # the cut ends of a water pipe (left wall) and a cable (right wall)
    q.append(f'<polygon points="{disc(o, s, "x", (.72, .575), .115, c)}" fill="#EAF6FF"/>')
    q.append(f'<polygon points="{disc(o, s, "x", (.72, .575), .082, c)}" fill="#22C3F3"/>')
    q.append(f'<polygon points="{disc(o, s, "y", (.73, .565), .075, c)}" fill="#FFF0BF"/>')
    q.append(f'<polygon points="{disc(o, s, "y", (.73, .565), .052, c)}" fill="#FFB21E"/>')
    q.append(f'<g clip-path="url(#nc{uid})"><polygon points="{pts(o, s, F["notch"])}" fill="url(#ao{uid})"/>')
    k = iso(o, s, (c, c, c))
    for e in [(c, c, 1), (1, c, c), (c, 1, c)]:
        X, Y = iso(o, s, e)
        q.append(f'<line x1="{k[0]:.1f}" y1="{k[1]:.1f}" x2="{X:.1f}" y2="{Y:.1f}" stroke="#000" stroke-opacity="0.28" '
                 f'stroke-width="{sw * 0.5:.1f}"/>')
    q.append('</g>')
    for a, b in [((0, 1, 1), (c, 1, 1)), ((1, 0, 1), (1, c, 1)), ((1, 1, 0), (1, 1, c))]:
        A, B = iso(o, s, a), iso(o, s, b)
        q.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{B[0]:.1f}" y2="{B[1]:.1f}" stroke="{ink}" '
                 f'stroke-width="{sw * 0.55:.1f}" stroke-linecap="round" opacity="0.5"/>')
    q.append(f'<polygon points="{pts(o, s, F["notch"])}" fill="none" stroke="{ink}" stroke-width="{sw * 0.8:.1f}" '
             f'stroke-linejoin="round"/>')
    q.append(f'<polygon points="{pts(o, s, F["hexagon"])}" fill="none" stroke="{ink}" stroke-width="{sw:.1f}" '
             f'stroke-linejoin="round"/>')
    return "\n".join(q)


def avatar_svg(size=1080, uid="av"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="{size}" height="{size}">'
            f'<defs><radialGradient id="bg{uid}" cx="540" cy="440" r="760" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#FFE45C"/><stop offset="0.55" stop-color="{YELLOW}"/>'
            f'<stop offset="1" stop-color="{YELLOW_DEEP}"/></radialGradient></defs>'
            f'<rect width="1080" height="1080" fill="url(#bg{uid})"/>{cube((540, 500), 382, uid)}</svg>')


def iso_grid(w, h, L, colour, opacity, width):
    """An isometric grid (the cube's own axes) over a w x h canvas."""
    q, t = [], math.tan(math.pi / 6)
    for b in range(-int(w * t) - L, h + int(w * t) + L, L):
        q.append(f'<line x1="0" y1="{b}" x2="{w}" y2="{b + w * t:.1f}"/>')
        q.append(f'<line x1="0" y1="{b}" x2="{w}" y2="{b - w * t:.1f}"/>')
    x, step = 0.0, L * C30                     # the slanted lines cross every L*cos30 across
    while x <= w:
        q.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{h}"/>')
        x += step
    return f'<g stroke="{colour}" stroke-opacity="{opacity}" stroke-width="{width}">' + "".join(q) + '</g>'


FONTS_CSS = """@font-face{font-family:"Anton";src:url(anton-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:700;src:url(inter-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:800;src:url(inter-latin-800-normal.woff2) format("woff2")}"""


def banner_html(line1, line2, highlight, pill):
    W, H = 2560, 1440
    cx, cy, s = 1826, 706, 146                     # the cube, inside the phone box (x 507-2053, y 508-931)
    R = s * 1.33                                   # the yellow disc behind it: the profile picture, at banner size
    glow = (f'<radialGradient id="gl" cx="{cx}" cy="{cy - R * 0.2:.0f}" r="{R * 1.35:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#FFE45C"/><stop offset="0.55" stop-color="{YELLOW}"/>'
            f'<stop offset="1" stop-color="{YELLOW_DEEP}"/></radialGradient>'
            f'<radialGradient id="bgb" cx="1280" cy="720" r="1500" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{INK_2}"/><stop offset="1" stop-color="#0A1124"/></radialGradient>')
    # faint cut cubes for the parts only computers and TVs show
    extras = "".join(f'<g opacity="{op}">{cube((x, y), r, f"x{i}", shadow=None)}</g>'
                     for i, (x, y, r, op) in enumerate([(262, 735, 118, 0.12), (2318, 700, 100, 0.12),
                                                        (520, 250, 78, 0.06), (2060, 1235, 86, 0.06)]))
    l2 = line2.replace(highlight, f'<span class="hl">{highlight}</span>', 1) if highlight else line2
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS_CSS}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0A1124}}
svg{{position:absolute;left:0;top:0}}
#t{{position:absolute;left:577px;top:0}}
h1{{display:inline-block;white-space:nowrap;font-family:"Anton";font-weight:400;color:#FFFFFF;font-size:122px;
line-height:1.02;margin:0;letter-spacing:.012em}}
h1 .hl{{color:{YELLOW}}}
.pill{{display:block;width:max-content;margin-top:28px;background:{YELLOW};color:{INK};font:800 44px/1 "Inter";letter-spacing:.05em;
padding:17px 30px 15px;border-radius:999px;white-space:nowrap}}
</style></head><body>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{glow}</defs>
<rect width="{W}" height="{H}" fill="url(#bgb)"/>{iso_grid(W, H, 120, "#FFFFFF", 0.045, 2)}
{extras}<circle cx="{cx}" cy="{cy + s * 0.08:.0f}" r="{R:.0f}" fill="url(#gl)"/>
{cube((cx, cy), s, "hero")}</svg>
<div id="t"><h1>{line1}<br>{l2}</h1><div class="pill">{pill}</div></div>
<script>
document.fonts.ready.then(() => {{
  const t = document.getElementById('t'), h = t.querySelector('h1'), p = t.querySelector('.pill');
  const maxW = 1020;                          // stop short of the cube
  let fs = 122;
  while (fs > 70 && h.getBoundingClientRect().width > maxW) {{ fs -= 2; h.style.fontSize = fs + 'px'; }}
  let ps = 44;
  while (ps > 30 && p.getBoundingClientRect().width > maxW) {{ ps -= 1; p.style.fontSize = ps + 'px'; }}
  t.style.top = (719.5 - t.getBoundingClientRect().height / 2) + 'px';   // centred in the phone box
  document.body.dataset.ready = '1';
}});
</script></body></html>"""


def avatar_html():
    return ('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#fff}svg{display:block}'
            '</style></head><body data-ready="1">' + avatar_svg() + '</body></html>')


def fit_check_html(banner, avatar):
    def circles(bg):
        return "".join(f'<div class="c" style="width:{z}px;height:{z}px"><img src="{avatar}" width="{z}" height="{z}"></div>'
                       for z in (98, 64, 48, 32, 24))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS_CSS}
body{{margin:0;background:#E8E8E8;font:700 22px "Inter";color:#222;width:1800px}}
.wrap{{padding:28px;display:flex;flex-direction:column;gap:22px}} h2{{margin:0;font:800 26px "Inter"}}
.row{{display:flex;gap:28px;align-items:flex-start}}
.panel{{background:#fff;padding:18px;border-radius:10px}} .dark{{background:#111;color:#eee}}
.c{{border-radius:50%;overflow:hidden;flex:none}} .c img{{display:block}}
.sizes{{display:flex;gap:22px;align-items:center;margin-top:10px}}
.feed{{position:relative;width:300px;height:520px;border-radius:14px;overflow:hidden;
background:linear-gradient(160deg,#3b4a5c,#121820 60%,#0b0f14)}}
.rail{{position:absolute;right:14px;top:180px;display:flex;flex-direction:column;align-items:center}}
.rail .c{{border:3px solid #fff}} .plus{{width:26px;height:26px;border-radius:50%;background:#FE2C55;color:#fff;
font:800 22px/26px "Inter";text-align:center;margin-top:-14px;position:relative}}
.shorts{{position:absolute;left:14px;bottom:18px;display:flex;align-items:center;gap:10px;color:#fff;font:700 18px "Inter"}}
.lbl{{font:700 18px "Inter";color:#666;margin:6px 0 0}} .dark .lbl{{color:#aaa}}
.ban{{position:relative}} .ban img{{display:block}}
.box{{position:absolute;border:3px dashed #FF3B30}}
</style></head><body><div class="wrap">
<h2>Profile picture: the sizes TikTok and YouTube show it at</h2>
<div class="row">
 <div class="panel"><div class="c" style="width:300px;height:300px"><img src="{avatar}" width="300" height="300"></div>
  <div class="lbl">as a circle (both apps)</div></div>
 <div class="panel"><div class="sizes">{circles('#fff')}</div><div class="lbl">98 / 64 / 48 / 32 / 24 px, light mode</div></div>
 <div class="panel dark"><div class="sizes">{circles('#111')}</div><div class="lbl">dark mode</div></div>
</div>
<div class="row">
 <div class="feed"><div class="rail"><div class="c" style="width:52px;height:52px"><img src="{avatar}" width="52" height="52"></div>
  <div class="plus">+</div></div><div class="lbl" style="position:absolute;left:14px;top:14px;color:#ccc">TikTok feed</div></div>
 <div class="feed"><div class="shorts"><div class="c" style="width:36px;height:36px"><img src="{avatar}" width="36" height="36"></div>
  @yourchannel</div><div class="lbl" style="position:absolute;left:14px;top:14px;color:#ccc">YouTube Shorts player</div></div>
 <div class="panel" style="flex:1"><h2>Banner: what each screen shows</h2>
  <div class="ban" style="width:1120px;margin-top:12px"><img src="{banner}" width="1120" height="630">
   <div class="box" style="left:0;top:{508 * 1120 / 2560:.0f}px;width:1114px;height:{423 * 1120 / 2560:.0f}px"></div>
   <div class="box" style="left:{507 * 1120 / 2560:.0f}px;top:{508 * 1120 / 2560:.0f}px;width:{1546 * 1120 / 2560:.0f}px;height:{423 * 1120 / 2560:.0f}px;border-color:#FFD62E"></div></div>
  <div class="lbl">whole image: TVs · red strip: computers · yellow box: phones</div></div>
</div>
<div class="row"><div class="panel"><h2>On a phone (the yellow box, at phone size)</h2>
 <div style="width:390px;height:107px;overflow:hidden;position:relative;margin-top:10px">
 <img src="{banner}" style="position:absolute;width:{2560 * 390 / 1546:.0f}px;left:-{507 * 390 / 1546:.0f}px;top:-{508 * 390 / 1546:.0f}px"></div></div>
 <div class="panel"><h2>On a computer (the red strip)</h2>
 <div style="width:1280px;height:212px;overflow:hidden;position:relative;margin-top:10px">
 <img src="{banner}" style="position:absolute;width:1280px;left:0;top:-254px"></div></div></div>
</div><script>document.fonts.ready.then(()=>document.body.dataset.ready='1')</script></body></html>"""


def render(html, out, w, h, full=False):
    cmd = ["node", str(HERE / "render.js"), str(html), str(out), str(w), str(h)] + (["full"] if full else [])
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fonts_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--line1", default="YOU'VE SEEN IT.")
    ap.add_argument("--line2", default="NOW SEE INSIDE IT.")
    ap.add_argument("--highlight", default="INSIDE")
    ap.add_argument("--pill", default="NEW 3D EXPLAINER EVERY 2 DAYS")
    a = ap.parse_args()
    fonts, out = Path(a.fonts_dir), Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    from PIL import Image
    with tempfile.TemporaryDirectory() as td:
        work = Path(td)
        for f in ("anton-latin-400-normal.woff2", "inter-latin-700-normal.woff2", "inter-latin-800-normal.woff2"):
            shutil.copy(fonts / f, work / f)
        (work / "avatar.html").write_text(avatar_html())
        render(work / "avatar.html", work / "avatar.png", 1080, 1080)
        av = Image.open(work / "avatar.png").convert("RGB")
        av.save(out / "avatar-v3-1080.png", optimize=True)
        av.resize((800, 800), Image.LANCZOS).save(out / "avatar-v3-800.png", optimize=True)
        (work / "banner.html").write_text(banner_html(a.line1, a.line2, a.highlight, a.pill))
        render(work / "banner.html", work / "banner.png", 2560, 1440)
        Image.open(work / "banner.png").convert("RGB").save(out / "banner-v3-2560x1440.jpg", quality=92, optimize=True)
        shutil.copy(out / "banner-v3-2560x1440.jpg", work / "b.jpg")
        shutil.copy(out / "avatar-v3-800.png", work / "a.png")
        (work / "fit.html").write_text(fit_check_html("b.jpg", "a.png"))
        render(work / "fit.html", work / "fit.png", 1800, 1000, full=True)
        Image.open(work / "fit.png").convert("RGB").save(out / "fit-check-v3.jpg", quality=88, optimize=True)
    for f in ("avatar-v3-1080.png", "avatar-v3-800.png", "banner-v3-2560x1440.jpg", "fit-check-v3.jpg"):
        print(f, (out / f).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
