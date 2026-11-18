"""Mascot-free profile pictures (800x800) and YouTube banners (2560x1440) built from the videos' own stills. No credits.

Made on 18 Nov 2026 when the user asked for "a eye catching profile and banner image for my TikTok and YouTube account" without
the mascot. Everything is cut from stills the videos already paid for, so it costs nothing to rebuild.

Usage:
    python3 make_brand_v2.py <stills_dir> <fonts_dir> <out_dir> [--fetch]
        [--eyebrow "3D CUTAWAY EXPLAINERS"] [--line1 "EVERYDAY THINGS,"] [--line2 "CUT OPEN."] [--pill "NEW VIDEO EVERY OTHER DAY"]
        [--yt-name LetZBuildTogether] [--yt-meta "@LetzBuildTogether · 310 subscribers · 10 videos"]
        [--tt-handle overthinkingyearly] [--tt-stats "0,54,679"]

stills_dir  the stills named in SOURCES (768x1360 seedream renders); --fetch downloads any that are missing from the
            Higgsfield CDN (reachable from a session).
fonts_dir   barlow-condensed-latin-900-normal.woff2 and montserrat-latin-700-normal.woff2
            (npm pack @fontsource/barlow-condensed@5.1.0 @fontsource/montserrat@5.1.0, then untar).
out_dir     avatar-blast-800.png (A, recommended), avatar-hydrant-800.png (B), avatar-portal-800.png (C);
            banner-cutopen-ink-2560x1440.jpg, banner-cutopen-yellow-2560x1440.jpg;
            fit-check-banners.jpg and fit-check-avatars.jpg (how they look on YouTube and TikTok).

Banner geometry (YouTube, 2560x1440 upload): TVs show everything; computers show the full-width strip y 508-931; phones show
only the centre box x 507-2053, y 508-931 (1546x423). The headline and the three hero cards sit inside the phone box with a
30 px margin; the four outer cards are for computers only. Rendered with render.js (Playwright Chromium).
Profile pictures: a circle-safe crop with a yellow ring, shown as a circle by both platforms (98 px on a YouTube channel page,
about 48 px beside a TikTok video, 24-32 px in comments), so the subject is one big shape.
"""
import argparse
import shutil
import subprocess
import tempfile
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

HERE = Path(__file__).resolve().parent
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/"
SOURCES = {  # still name -> (video, Higgsfield result file)
    "manhole_ST1": ("12 manhole covers: the blast", "hf_20261118_031842_f344ad43-437c-425b-ba70-4f0def6fec7d.png"),
    "manhole_U1": ("12 manhole covers: the vented lid from below", "hf_20261118_032117_a992e08f-2078-4bfa-ad21-981cc0906459.png"),
    "manhole_W0": ("12 manhole covers: the street, cut open", "hf_20261118_031512_76d89050-be73-4f41-a29a-9de47155443e.png"),
    "hydrant_END": ("03 fire hydrant", "hf_20261108_224425_e84197e8-e6fd-45d6-825b-ab29d0cb0229.png"),
    "seawater_END": ("04 seawater", "hf_20261110_231831_5397da6f-0e96-4f38-8404-55f61db67fdd.png"),
    "lightning_storm": ("09 lightning: storm", "hf_20261115_210214_f4f85d6a-223b-42c3-bd37-dbbedafee994.png"),
    "lightning_W0": ("09 lightning: day", "hf_20261115_210054_bceb6aeb-d56b-4a43-aaae-cfea608a9e39.png"),
    "sewer_S0": ("08 sewer", "hf_20261115_182843_3668f778-edeb-403c-ab68-939aa50e6454.png"),
}
YELLOW = (255, 200, 61)
W, H = 2560, 1440
SAFE = (507, 508, 2053, 931)
STRIP = (508, 931)

# ---------------------------------------------------------------- profile pictures
AVATARS = {  # file stem -> (still, crop centre x, centre y, crop side) in the 768x1360 still
    "blast": ("manhole_ST1", 400, 800, 640),     # A: the lid lifting off on a column of flame (video 12)
    "hydrant": ("hydrant_END", 400, 715, 880),   # B: the hydrant cut open down to the main (video 03, the 196K Short)
    "portal": ("manhole_U1", 397, 480, 760),     # C: the vented lid from below, daylight through the holes (video 12)
}


def square_crop(im, cx, cy, side):
    """Square crop centred on (cx, cy); anything outside the still repeats the edge pixels, softened."""
    w, h = im.size
    x0, y0 = int(round(cx - side / 2)), int(round(cy - side / 2))
    a = np.asarray(im)
    ys = np.clip(np.arange(y0, y0 + side), 0, h - 1)
    xs = np.clip(np.arange(x0, x0 + side), 0, w - 1)
    out = Image.fromarray(a[ys][:, xs])
    inside = Image.new("L", (side, side), 0)
    ImageDraw.Draw(inside).rectangle([max(0, -x0), max(0, -y0), min(side, w - x0) - 1, min(side, h - y0) - 1], fill=255)
    if inside.getextrema()[0] == 0:
        soft = out.filter(ImageFilter.GaussianBlur(10))
        out = Image.composite(out, soft, inside.filter(ImageFilter.GaussianBlur(6)))
    return out


def vignette(im, strength=0.3):
    s = im.size[0]
    y, x = np.mgrid[0:s, 0:s]
    r = np.hypot(x - s / 2, y - s / 2) / (s / 2)
    m = 1 - strength * np.clip((r - 0.55) / 0.45, 0, 1) ** 2
    return Image.fromarray((np.asarray(im).astype(float) * m[..., None]).clip(0, 255).astype("uint8"))


def make_avatar(still, cx, cy, side, size=800, ring=YELLOW, ring_w=0.045):
    sq = square_crop(Image.open(still).convert("RGB"), cx, cy, side).resize((size, size), Image.LANCZOS)
    sq = vignette(ImageEnhance.Contrast(ImageEnhance.Color(sq).enhance(1.15)).enhance(1.08))
    out = Image.new("RGB", (size, size), ring)
    rw = int(size * ring_w)
    inner = sq.resize((size - 2 * rw, size - 2 * rw), Image.LANCZOS)
    m = Image.new("L", (inner.width * 4, inner.height * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, m.width - 1, m.height - 1], fill=255)
    out.paste(inner, (rw, rw), m.resize(inner.size, Image.LANCZOS))
    ImageDraw.Draw(out).ellipse([rw - 2, rw - 2, size - rw + 1, size - rw + 1], outline=(20, 20, 20), width=4)
    return out


# ---------------------------------------------------------------- banners
CARDS = {  # card -> (still, top of a 768x1024 (3:4) crop)
    "blast": ("manhole_ST1", 230), "hydrant": ("hydrant_END", 160), "seawater": ("seawater_END", 250),
    "storm": ("lightning_storm", 40), "street": ("manhole_W0", 150), "sewer": ("sewer_S0", 150), "sun": ("lightning_W0", 40),
}
# card, left, top, width (3:4), rotation, z, brightness (<1 = pushed back), blur
LAYOUT = [
    ("sun", 70, 590, 190, -6, 0, .55, 1.5), ("sewer", 290, 572, 200, 5, 0, .7, 0),          # computers only (left)
    ("storm", 2080, 572, 200, -5, 0, .7, 0), ("street", 2310, 590, 190, 6, 0, .55, 1.5),    # computers only (right)
    ("hydrant", 1420, 566, 232, -7, 1, 1, 0), ("seawater", 1772, 566, 232, 7, 1, 1, 0),     # phone box: the hero three
    ("blast", 1586, 541, 262, -1.5, 2, 1, 0),
]
VARIANTS = {
    "ink": dict(bg="#0b1222", bg2="#13203b", grid="rgba(140,170,255,.07)", glow="rgba(255,128,40,.30)",
                glow2="rgba(70,120,230,.22)", text="#ffffff", slice="#ffc83d", eyebrow="#ffc83d", core="#ff5a1f",
                pill_bg="rgba(255,255,255,.09)", pill_bd="rgba(255,255,255,.18)", pill_fg="#ffffff", dark_far=True),
    "yellow": dict(bg="#ffc83d", bg2="#ffd45e", grid="rgba(0,0,0,.06)", glow="rgba(255,255,255,.35)",
                   glow2="rgba(255,150,40,.25)", text="#111111", slice="#111111", eyebrow="rgba(17,17,17,.72)", core="#ff5a1f",
                   pill_bg="#111111", pill_bd="#111111", pill_fg="#ffc83d", dark_far=False),
}
FONTS_CSS = """@font-face{font-family:"BC";font-weight:900;src:url(barlow-condensed-latin-900-normal.woff2) format("woff2")}
@font-face{font-family:"MS";font-weight:700;src:url(montserrat-latin-700-normal.woff2) format("woff2")}"""


def card_div(name, x, y, w, rot, z, light, blur, dark_far):
    h = round(w * 4 / 3)
    filt = ""
    if light < 1:
        filt = f"filter:brightness({light}) saturate({.6 + .4 * light}) blur({blur}px);" if dark_far else f"filter:blur({blur}px);"
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);'
            f'z-index:{z};{filt}"><img src="card_{name}.jpg" alt=""></div>')


def banner_html(var, eyebrow, line1, line2, pill):
    p = VARIANTS[var]
    cards = "".join(card_div(*c, p["dark_far"]) for c in LAYOUT)
    first_hero_left = 1400  # the hydrant card's rotated left edge; the text stops 40 px short of it
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS_CSS}
html,body{{margin:0;padding:0}}
body{{width:{W}px;height:{H}px;overflow:hidden;position:relative;background:{p['bg']}}}
#bg{{position:absolute;inset:0;background:radial-gradient(560px 420px at 1730px 720px,{p['glow']},transparent 70%),
  radial-gradient(900px 520px at 900px 720px,{p['glow2']},transparent 70%),
  linear-gradient(180deg,{p['bg']} 0%,{p['bg2']} 50%,{p['bg']} 100%)}}
#grid{{position:absolute;inset:0;background-image:linear-gradient({p['grid']} 2px,transparent 2px),
  linear-gradient(90deg,{p['grid']} 2px,transparent 2px);background-size:80px 80px;background-position:-2px 28px}}
.card{{position:absolute;box-sizing:border-box;border-radius:26px;border:6px solid #fff;overflow:hidden;background:#000;
  box-shadow:0 28px 60px rgba(0,0,0,.5),0 6px 16px rgba(0,0,0,.35)}}
.card img{{width:100%;height:100%;object-fit:cover;display:block}}
#text{{position:absolute;left:560px;top:0;height:{H}px;display:flex;flex-direction:column;justify-content:center;z-index:3}}
#inner{{display:flex;flex-direction:column}}
.eyebrow{{font:700 30px/1 "MS",sans-serif;letter-spacing:.24em;color:{p['eyebrow']};margin:0 0 12px 6px;white-space:nowrap}}
.l1{{font:900 124px/.88 "BC",sans-serif;color:{p['text']};letter-spacing:.01em;white-space:nowrap}}
.slice{{position:relative;display:inline-block;align-self:flex-start;font:900 206px/.88 "BC",sans-serif;letter-spacing:.01em;
  white-space:nowrap;margin:4px 0 0 -4px}}
.slice span{{display:block}}
.slice .core{{color:{p['core']};clip-path:polygon(-2% 53%,102% 41%,102% 51%,-2% 63%)}}  /* only inside the gap */
.slice .top,.slice .bot{{position:absolute;left:0;top:0;color:{p['slice']}}}
.slice .top{{clip-path:polygon(-2% -10%,102% -10%,102% 46%,-2% 58%);transform:translateY(-9px)}}
.slice .bot{{clip-path:polygon(-2% 58%,102% 46%,102% 110%,-2% 110%);transform:translateY(9px)}}
.pill{{display:inline-flex;align-items:center;gap:14px;align-self:flex-start;margin:22px 0 0 4px;padding:13px 28px 13px 22px;
  border-radius:999px;background:{p['pill_bg']};border:2px solid {p['pill_bd']};font:700 28px/1 "MS",sans-serif;
  letter-spacing:.06em;color:{p['pill_fg']};white-space:nowrap}}
.pill i{{width:0;height:0;border-left:19px solid #ffc83d;border-top:11px solid transparent;border-bottom:11px solid transparent}}
</style></head><body><div id="bg"></div><div id="grid"></div>{cards}
<div id="text"><div id="inner"><div class="eyebrow">{eyebrow}</div><div class="l1">{line1}</div>
<div class="slice"><span class="core">{line2}</span><span class="top">{line2}</span><span class="bot">{line2}</span></div>
<div class="pill"><i></i>{pill}</div></div></div>
<script>document.fonts.ready.then(()=>{{
  const T=document.getElementById('inner'), l1=T.querySelector('.l1'), sl=T.querySelector('.slice');
  const maxR={first_hero_left - 40}, maxH={SAFE[3] - SAFE[1] - 2 * 30 - 8};
  const s1=parseFloat(getComputedStyle(l1).fontSize), s2=parseFloat(getComputedStyle(sl).fontSize); let k=1;
  for(let i=0;i<80;i++){{
    const r=T.getBoundingClientRect(), right=Math.max(l1.getBoundingClientRect().right, sl.getBoundingClientRect().right+9);
    if(right<=maxR && r.height<=maxH) break;
    k*=0.99; l1.style.fontSize=(s1*k)+'px'; sl.style.fontSize=(s2*k)+'px';
  }}
  const r=T.getBoundingClientRect();
  document.body.dataset.fit=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom),k.toFixed(3)].join(',');
  document.body.dataset.ready='1';
}});</script></body></html>"""


# ---------------------------------------------------------------- fit checks
def banners_fit_html(variants, args):
    sx, sy, ex, ey = SAFE
    k = 640 / W
    rows = []
    for v in variants:
        rows.append(f"""<div class="row">
<div><h2>{v.title()}: YouTube on a computer</h2><div class="desk"><img class="ban" src="strip_{v}.png" alt="">
<div class="who"><img class="av" src="avatar-blast-800.png" width="96" height="96" alt=""><div><div class="name">{args.yt_name}</div>
<div class="meta">{args.yt_meta}</div></div><span class="sub">Subscribe</span></div></div></div>
<div><h2>{v.title()}: YouTube app (dark mode)</h2><div class="phone"><img class="ban" src="safe_{v}.png" alt="">
<div class="who"><img class="av" src="avatar-blast-800.png" width="64" height="64" alt=""><div><div class="name">{args.yt_name}</div>
<div class="meta">{args.yt_meta}</div></div></div><span class="sub w">Subscribe</span></div></div></div>""")
    tv = "".join(f"""<figure><div class="tv"><img src="full_{v}.jpg" alt=""><div class="zone strip"></div><div class="zone safe"></div></div>
<figcaption>{v.title()}: the full upload (TVs). Dashed: computers. Yellow box: phones.</figcaption></figure>""" for v in variants)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#eef1f5;font:16px/1.4 Inter,system-ui,sans-serif;color:#1b1f27}}
.wrap{{width:1500px;padding:36px 40px 44px;box-sizing:border-box;display:flex;flex-direction:column;gap:30px}}
h1{{font:700 32px/1.1 Inter,sans-serif;margin:0}}
h2{{font:600 14px/1 Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#56607a;margin:0 0 10px}}
.row{{display:flex;gap:30px;align-items:flex-start}}
.desk{{width:960px;background:#fff;border-radius:14px;padding:20px;box-sizing:border-box}}
.desk .ban{{width:920px;height:{round(920 * 423 / 2560)}px;border-radius:12px;display:block}}
.who{{display:flex;gap:16px;align-items:center;margin-top:16px}}
.av{{border-radius:50%;display:block}}
.name{{font:700 24px/1.2 Inter,sans-serif}}
.meta{{color:#606060;font-size:14px}}
.sub{{margin-left:auto;background:#0f0f0f;color:#fff;font:600 15px/1 Inter,sans-serif;padding:11px 18px;border-radius:999px}}
.phone{{width:390px;background:#0f0f0f;border-radius:30px;padding:16px;box-sizing:border-box;color:#f1f1f1}}
.phone .ban{{width:358px;height:{round(358 * 423 / 1546)}px;border-radius:10px;display:block}}
.phone .meta{{color:#aaa;font-size:12px}} .phone .name{{font-size:19px}}
.sub.w{{display:block;text-align:center;margin:14px 0 2px;background:#f1f1f1;color:#0f0f0f}}
.tvs{{display:flex;gap:30px}} figure{{margin:0}} figcaption{{font-size:13px;color:#56607a;margin-top:6px}}
.tv{{position:relative;width:640px;height:360px}} .tv img{{width:640px;height:360px;display:block;border-radius:6px}}
.zone{{position:absolute;box-sizing:border-box}}
.strip{{left:0;top:{STRIP[0] * k}px;width:640px;height:{(STRIP[1] - STRIP[0]) * k}px;border:2px dashed #fff}}
.safe{{left:{sx * k}px;top:{sy * k}px;width:{(ex - sx) * k}px;height:{(ey - sy) * k}px;border:2px solid #ffd000}}
</style></head><body><div class="wrap"><h1>YouTube banner, two versions (no mascot)</h1>{''.join(rows)}
<div class="tvs">{tv}</div></div><script>document.body.dataset.ready='1'</script></body></html>"""


def avatars_fit_html(names, args):
    labels = {"blast": "A (recommended): the blast", "hydrant": "B: the hydrant, cut open", "portal": "C: the vented lid from below"}
    rows = []
    for n in names:
        sizes = "".join(f'<figure><img class="av" src="avatar-{n}-800.png" width="{z}" height="{z}" alt=""><figcaption>{z}px</figcaption></figure>'
                        for z in (98, 48, 32, 24))
        rows.append(f"""<div class="opt"><h2>{labels[n]}</h2><div class="line">
<img class="av" src="avatar-{n}-800.png" width="200" height="200" alt="">
<div class="sizes" style="background:#fff">{sizes}</div><div class="sizes" style="background:#0f0f0f;color:#aaa">{sizes}</div></div></div>""")
    following, followers, likes = args.tt_stats.split(",")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#eef1f5;font:16px/1.4 Inter,system-ui,sans-serif;color:#1b1f27}}
.wrap{{width:1040px;padding:36px 40px 44px;box-sizing:border-box;display:flex;flex-direction:column;gap:26px}}
h1{{font:700 32px/1.1 Inter,sans-serif;margin:0}}
h2{{font:600 14px/1 Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#56607a;margin:0 0 10px}}
.av{{border-radius:50%;display:block}}
.line{{display:flex;gap:26px;align-items:center}}
.sizes{{display:flex;gap:22px;align-items:flex-end;padding:16px 20px;border-radius:12px}}
.sizes figure{{margin:0;text-align:center;font-size:12px}}
.tt{{display:flex;gap:30px;align-items:flex-start}}
.prof{{width:390px;background:#fff;border-radius:30px;padding:28px 20px;box-sizing:border-box;text-align:center}}
.prof .av{{margin:0 auto}} .handle{{font:700 19px/1.3 Inter,sans-serif;margin-top:12px}}
.stats{{display:flex;justify-content:center;gap:26px;margin-top:12px}} .stats b{{display:block;font-size:18px}} .stats span{{font-size:13px;color:#777}}
.follow{{display:inline-block;margin-top:16px;background:#fe2c55;color:#fff;font:600 16px/1 Inter,sans-serif;padding:12px 54px;border-radius:6px}}
.feed{{position:relative;width:270px;height:480px;border-radius:18px;overflow:hidden;background:#000}}
.feed img.f{{width:100%;height:100%;object-fit:cover;display:block}}
.rail{{position:absolute;right:10px;top:150px;display:flex;flex-direction:column;align-items:center;gap:16px}}
.rail .av{{border:2px solid #fff}}
.plus{{position:absolute;left:50%;top:40px;transform:translateX(-50%);width:20px;height:20px;border-radius:50%;background:#fe2c55;color:#fff;
  font:700 16px/20px Inter,sans-serif;text-align:center}}
</style></head><body><div class="wrap"><h1>Profile picture, three options (TikTok and YouTube)</h1>{''.join(rows)}
<div><h2>A on TikTok: your profile, and beside a video in the feed</h2><div class="tt">
<div class="prof"><img class="av" src="avatar-blast-800.png" width="96" height="96" alt=""><div class="handle">@{args.tt_handle}</div>
<div class="stats"><div><b>{following}</b><span>Following</span></div><div><b>{followers}</b><span>Followers</span></div><div><b>{likes}</b><span>Likes</span></div></div>
<span class="follow">Follow</span></div>
<div class="feed"><img class="f" src="feed.jpg" alt=""><div class="rail"><div style="position:relative">
<img class="av" src="avatar-blast-800.png" width="48" height="48" alt=""><div class="plus" style="top:38px">+</div></div>
</div></div>
<div class="feed"><img class="f" src="feed2.jpg" alt=""><div class="rail"><div style="position:relative">
<img class="av" src="avatar-blast-800.png" width="48" height="48" alt=""><div class="plus" style="top:38px">+</div></div>
</div></div>
</div></div></div><script>document.body.dataset.ready='1'</script></body></html>"""


def render(html_path, png_path, w, h, full=False):
    cmd = ["node", str(HERE / "render.js"), str(html_path), str(png_path), str(w), str(h)] + (["full"] if full else [])
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stills")
    ap.add_argument("fonts")
    ap.add_argument("out")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--eyebrow", default="3D CUTAWAY EXPLAINERS")
    ap.add_argument("--line1", default="EVERYDAY THINGS,")
    ap.add_argument("--line2", default="CUT OPEN.")
    ap.add_argument("--pill", default="NEW VIDEO EVERY OTHER DAY")
    ap.add_argument("--yt-name", default="LetZBuildTogether")
    ap.add_argument("--yt-meta", default="@LetzBuildTogether · 310 subscribers · 10 videos")
    ap.add_argument("--tt-handle", default="overthinkingyearly")
    ap.add_argument("--tt-stats", default="0,54,679")
    args = ap.parse_args()
    stills, fonts, out = Path(args.stills), Path(args.fonts), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, (_, f) in SOURCES.items():
        if not (stills / f"{name}.png").exists():
            if not args.fetch:
                raise SystemExit(f"missing {stills / name}.png (run with --fetch)")
            stills.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(CDN + f, stills / f"{name}.png")
    work = Path(tempfile.mkdtemp(prefix="brand_v2_"))
    for woff in ("barlow-condensed-latin-900-normal.woff2", "montserrat-latin-700-normal.woff2"):
        shutil.copy(fonts / woff, work / woff)

    for n, (s, cx, cy, side) in AVATARS.items():
        av = make_avatar(stills / f"{s}.png", cx, cy, side)
        av.save(out / f"avatar-{n}-800.png", optimize=True)
        av.save(work / f"avatar-{n}-800.png")
    for c, (s, y0) in CARDS.items():
        im = Image.open(stills / f"{s}.png").convert("RGB").crop((0, y0, 768, y0 + 1024))
        ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.1)).enhance(1.04).save(work / f"card_{c}.jpg", quality=92)

    for v in VARIANTS:
        (work / f"banner_{v}.html").write_text(banner_html(v, args.eyebrow, args.line1, args.line2, args.pill), encoding="utf-8")
        render(work / f"banner_{v}.html", work / f"banner_{v}.png", W, H)
        ban = Image.open(work / f"banner_{v}.png").convert("RGB")
        ban.save(out / f"banner-cutopen-{v}-2560x1440.jpg", quality=93, optimize=True)  # YouTube's limit is 6 MB
        ban.crop((0, STRIP[0], W, STRIP[1])).save(work / f"strip_{v}.png")
        ban.crop(SAFE).save(work / f"safe_{v}.png")
        ban.resize((1280, 720), Image.LANCZOS).save(work / f"full_{v}.jpg", quality=88)
        print(v, (out / f"banner-cutopen-{v}-2560x1440.jpg").stat().st_size // 1024, "KB")

    Image.open(stills / "manhole_ST0.png" if (stills / "manhole_ST0.png").exists() else stills / "manhole_W0.png").convert("RGB").save(work / "feed.jpg")
    Image.open(stills / "hydrant_END.png").convert("RGB").save(work / "feed2.jpg")
    (work / "fit_banners.html").write_text(banners_fit_html(list(VARIANTS), args), encoding="utf-8")
    render(work / "fit_banners.html", work / "fit_banners.png", 1500, 900, full=True)
    Image.open(work / "fit_banners.png").convert("RGB").save(out / "fit-check-banners.jpg", quality=88)
    (work / "fit_avatars.html").write_text(avatars_fit_html(list(AVATARS), args), encoding="utf-8")
    render(work / "fit_avatars.html", work / "fit_avatars.png", 1040, 900, full=True)
    Image.open(work / "fit_avatars.png").convert("RGB").save(out / "fit-check-avatars.jpg", quality=88)
    shutil.rmtree(work)
    print("wrote", sorted(p.name for p in out.iterdir()))


if __name__ == "__main__":
    main()
