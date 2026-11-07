# Covers for video 02, built only from the video's own frames (no generation credits). Runs in the Higgsfield sandbox (v02/).
# Inputs: stills/*.png, frames pulled from clips (e.g. ffmpeg -ss 0.05 -i clips/B1.mp4 -frames:v 1 thumb/log_b1.png), fonts/HBXLabel.ttf.
# 1080x1920, text kept inside the 3:4 grid crop (y 240-1680) and clear of TikTok's right-side buttons (x>940 below y~950)
# and bottom caption zone (y>1560). 0-4 words, Montserrat ExtraBold, yellow + white with a 16 px black stroke and drop shadow.
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1080, 1920
YEL, BLK, WHT = (255, 208, 28), (10, 10, 12), (255, 255, 255)
FONT = 'fonts/HBXLabel.ttf'   # Montserrat ExtraBold (same face as the video's labels)
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

def concept_A():   # transformation split: log (top) -> storm canoe (bottom)
    top = grade(place('thumb/log_b1.png', W, 1000, fx=0.50, fy=0.60, ty=0.68, zoom=1.0))
    bot = grade(place('stills/PAYOFF.png', W, 1060, fx=0.47, fy=0.50, ty=0.52, zoom=1.10), c=1.14, s=1.10)
    cv = Image.new('RGB', (W, H)); cv.paste(bot, (0, H - 1060))
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon([(0, 0), (W, 0), (W, 900), (0, 1010)], fill=255)
    tp = Image.new('RGB', (W, H)); tp.paste(top, (0, 0)); cv = Image.composite(tp, cv, m)
    cv = vignette(cv, 0.40).convert('RGBA'); d = ImageDraw.Draw(cv)
    d.line([(0, 1010), (W, 900)], fill=BLK, width=30); d.line([(0, 1010), (W, 900)], fill=YEL, width=14)
    word(cv, 290, 375, 'LOG', 190, WHT)
    word(cv, 500, 1150, 'CANOE', 196, YEL)
    arrow(cv, [(430, 470), (610, 590), (680, 780), (630, 1010)])
    return cv
def concept_B():   # curiosity: the twist
    cv = grade(place('stills/CROC.png', W, H, fx=0.48, fy=0.62, ty=0.70, zoom=1.10), c=1.12, s=1.05)
    cv = vignette(cv, 0.50).convert('RGBA')
    word(cv, 540, 330, 'NOT THE', 140, WHT); word(cv, 540, 480, 'CROC', 230, YEL)
    arrow(cv, [(800, 600), (880, 960), (760, 1440)])
    return cv
def concept_C():   # action hero + small log inset (same words as A; tests single hero vs split)
    cv = grade(place('stills/PAYOFF.png', W, H, fx=0.47, fy=0.52, ty=0.60, zoom=1.08), c=1.14, s=1.10)
    cv = vignette(cv, 0.42).convert('RGBA')
    r = 150; cx, cy = 245, 470
    ins = grade(place('thumb/log_b1.png', 2 * r, 2 * r, fx=0.48, fy=0.60, zoom=1.45))
    mk = Image.new('L', (2 * r, 2 * r), 0); ImageDraw.Draw(mk).ellipse((0, 0, 2 * r - 1, 2 * r - 1), fill=255)
    def ring(d, sc, dy):
        d.ellipse((cx - r - 16, cy - r - 16 + dy, cx + r + 16, cy + r + 16 + dy), fill=sc or BLK)
        if sc is None: d.ellipse((cx - r - 9, cy - r - 9, cx + r + 9, cy + r + 9), fill=YEL)
    shadowed(cv, ring); cv.paste(ins, (cx - r, cy - r), mk)
    word(cv, 245, 690, 'LOG', 120, WHT, stroke=13)
    word(cv, 700, 350, 'CANOE', 165, YEL, stroke=15)
    arrow(cv, [(420, 520), (560, 610), (600, 820)])
    return cv
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
