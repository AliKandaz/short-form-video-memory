# Covers for video 03 (fire hydrant), built only from the video's own frames (no generation credits). Runs in the Higgsfield sandbox (v03/).
# Inputs: stills/*.png and two 2K frames of the B3 clip: thumb/frozen.png (first frame) and thumb/hydrant.png (last frame).
# 1080x1920, text kept inside the 3:4 grid crop (y 240-1680) and clear of TikTok's right-side buttons (x>940 below y~950)
# and bottom caption zone (y>1560). 0-4 words, Montserrat ExtraBold, yellow + white with a 16 px black stroke and drop shadow.
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1080, 1920
YEL, BLK, WHT = (255, 208, 28), (10, 10, 12), (255, 255, 255)
FONT = '/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf'   # same face as the video's captions
def place(src, bw, bh, fx, fy, tx=0.5, ty=0.5, zoom=1.0):
    im = Image.open(src).convert('RGB'); s = max(bw / im.width, bh / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x0 = min(max(0, round(fx * im.width - tx * bw)), im.width - bw); y0 = min(max(0, round(fy * im.height - ty * bh)), im.height - bh)
    return im.crop((x0, y0, x0 + bw, y0 + bh))
def grade(im, c=1.10, s=1.15):
    im = ImageEnhance.Contrast(im).enhance(c); im = ImageEnhance.Color(im).enhance(s)
    return im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=70, threshold=2))
def vignette(im, k=0.45):
    m = Image.new('L', im.size, 0); d = ImageDraw.Draw(m)
    d.ellipse((-im.width * 0.25, -im.height * 0.12, im.width * 1.25, im.height * 1.12), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(160)); dark = Image.new('RGB', im.size, (0, 0, 0))
    return Image.composite(im, Image.blend(im, dark, k), m)
def shadowed(canvas, draw_fn, blur=12, dy=12, alpha=180):
    sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0)); draw_fn(ImageDraw.Draw(sh), (0, 0, 0, alpha), dy)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur))); draw_fn(ImageDraw.Draw(canvas), None, 0)
def word(canvas, cx, cy, s, size, fill, stroke=16):
    f = ImageFont.truetype(FONT, size)
    def fn(d, sc, dy):
        d.text((cx, cy + dy), s, font=f, fill=sc or fill, anchor='mm', stroke_width=stroke, stroke_fill=sc or BLK)
    shadowed(canvas, fn)
    return f.getbbox(s, anchor='mm', stroke_width=stroke)
def arrow(canvas, pts, fill=YEL, w=34):
    # thick polyline with a triangular head at the last point, black outline
    import math
    (x1, y1), (x2, y2) = pts[-2], pts[-1]; a = math.atan2(y2 - y1, x2 - x1); L = 82
    tip = (x2, y2); left = (x2 - L * math.cos(a) + L * 0.75 * math.sin(a), y2 - L * math.sin(a) - L * 0.75 * math.cos(a))
    right = (x2 - L * math.cos(a) - L * 0.75 * math.sin(a), y2 - L * math.sin(a) + L * 0.75 * math.cos(a))
    shaft_end = (x2 - L * 0.7 * math.cos(a), y2 - L * 0.7 * math.sin(a)); line = pts[:-1] + [shaft_end]
    def fn(d, sc, dy):
        P = [(x, y + dy) for x, y in line]; T = [(x, y + dy) for x, y in (tip, left, right)]
        d.line(P, fill=sc or BLK, width=w + 20, joint='curve'); d.polygon(T, fill=sc or BLK)
        if sc is None:
            d.line(P, fill=fill, width=w, joint='curve')
            cx = sum(p[0] for p in T) / 3; cy = sum(p[1] for p in T) / 3
            d.polygon([(cx + (x - cx) * 0.78, cy + (y - cy) * 0.78) for x, y in T], fill=fill)
    shadowed(canvas, fn, blur=10, dy=8)

def concept_A():   # transformation split: frozen burst pipe (top) -> dry barrel hydrant (bottom), arrow to the buried valve
    top = grade(place('thumb/frozen.png', W, 1000, fx=0.50, fy=0.40, ty=0.45, zoom=1.15))
    bot = grade(place('thumb/hydrant.png', W, 1060, fx=0.50, fy=0.76, ty=0.56, zoom=1.0), c=1.12, s=1.10)
    cv = Image.new('RGB', (W, H)); cv.paste(bot, (0, H - 1060))
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon([(0, 0), (W, 0), (W, 900), (0, 1010)], fill=255)
    tp = Image.new('RGB', (W, H)); tp.paste(top, (0, 0)); cv = Image.composite(tp, cv, m)
    cv = vignette(cv, 0.38).convert('RGBA'); d = ImageDraw.Draw(cv)
    d.line([(0, 1010), (W, 900)], fill=BLK, width=30); d.line([(0, 1010), (W, 900)], fill=YEL, width=14)
    word(cv, 470, 330, 'FREEZES', 150, WHT)
    word(cv, 470, 1130, "DOESN'T", 170, YEL)
    arrow(cv, [(290, 1240), (310, 1390), (465, 1452)])
    return cv
def concept_B():   # curiosity: the movie myth, over the snapped top with no water
    cv = grade(place('stills/SNAP.png', W, H, fx=0.50, fy=0.50, ty=0.50, zoom=1.06), c=1.12, s=1.06)
    cv = vignette(cv, 0.48).convert('RGBA')
    word(cv, 470, 300, 'MOVIES', 150, WHT); word(cv, 470, 470, 'LIED', 240, YEL)
    arrow(cv, [(700, 560), (760, 760), (640, 900)])
    return cv
def concept_C():   # plain mid-video cutaway frame, no text (the account's own cover style)
    cv = grade(place('stills/S3.png', W, H, fx=0.50, fy=0.50, ty=0.50, zoom=1.04), c=1.10, s=1.12)
    return vignette(cv, 0.30).convert('RGBA')
for name, fn in [('A', concept_A), ('B', concept_B), ('C', concept_C)]:
    im = fn().convert('RGB'); im.save(f'thumb/cover_{name}.png'); im.save(f'thumb/cover_{name}.jpg', quality=90)
    im.resize((360, 640), Image.LANCZOS).save(f'thumb/prev_{name}.jpg', quality=85)
# grid preview: 3:4 centre crop at phone-grid size + a small feed-size preview
sheet = Image.new('RGB', (3 * 380 + 20, 640 + 300 + 30), (24, 24, 24))
for k, n in enumerate('ABC'):
    im = Image.open(f'thumb/cover_{n}.png'); sheet.paste(im.resize((360, 640), Image.LANCZOS), (10 + k * 380, 10))
    g = im.crop((0, 240, 1080, 1680)).resize((150, 200), Image.LANCZOS); sheet.paste(g, (10 + k * 380, 660))
    sheet.paste(im.resize((84, 150), Image.LANCZOS), (180 + k * 380, 680))
sheet.save('thumb/compare.jpg', quality=85); print('ok')
