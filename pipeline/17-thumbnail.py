# Covers for video 17 (B12, "How to Keep a T-Rex in Your Back Yard"), built from frames of the video's clean master (no
# generation credits; 16-thumbnail.py's helpers). Runs from the work dir:  python3 17-thumbnail.py [A B C]
# Inputs: frames/step.png (FC1: he steps over the picket fence), frames/ring.png (the hook: the T-rex in his picket ring),
# frames/finished.png (the finished yard), frames/nose.png (the close: nose to nose through the glass), fonts/HBXCaption.ttf.
# Words and subject inside TikTok's 3:4 grid crop (y 240-1680).
#   A  the naive step failing (he steps over the pickets) with the format's hook: "GUESS / THE BILL" and the pill "$???,???"
#   B  before and after with the bill: the picket ring ("$148") above, the finished yard ("$???,???") below
#   C  plain frame with no text: the dog and the T-rex nose to nose through the glass
import os, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1080, 1920
YEL, BLK, WHT = (255, 208, 28), (10, 10, 12), (255, 255, 255)
FONT = os.environ.get('HBX_FONT', 'fonts/HBXCaption.ttf')   # Montserrat ExtraBold
UI = os.environ.get('HBX_UI_FONT', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
GRID = (240, 1680)   # TikTok 3:4 centre crop of a 1080x1920 frame

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
def words(canvas, cx, cy, parts, size, stroke=16):
    # one line in several colours, centred on (cx, cy): parts = [(text, colour), ...]
    f = ImageFont.truetype(FONT, size); sp = f.getlength(' ')
    ws = [f.getlength(t) for t, _ in parts]; x = cx - (sum(ws) + sp * (len(parts) - 1)) / 2
    for (t, col), w in zip(parts, ws):
        def fn(d, sc, dy, t=t, col=col, x=x):
            d.text((x, cy + dy), t, font=f, fill=sc or col, anchor='lm', stroke_width=stroke, stroke_fill=sc or BLK)
        shadowed(canvas, fn); x += w + sp
def arrow(canvas, pts, fill=YEL, w=34):
    # thick polyline with a triangular head at the last point, black outline
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
def bez(p0, p1, p2, n=28):   # quadratic Bezier points, for curved arrows
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
            for t in [i / n for i in range(n + 1)]]
def backdrop(cv, box, alpha=120, blur=45):   # soft dark patch behind a headline on a busy background
    m = Image.new('L', cv.size, 0); ImageDraw.Draw(m).rounded_rectangle(box, radius=60, fill=alpha)
    m = m.filter(ImageFilter.GaussianBlur(blur)); cv.paste(Image.composite(Image.new('RGBA', cv.size, (0, 0, 0, 255)), cv, m), (0, 0))
def neutralise(im, box, sat=0.15, bright=0.80, feather=5):   # grey out a stray colour cast inside box
    x0, y0, x1, y1 = box; patch = im.crop(box)
    patch = ImageEnhance.Brightness(ImageEnhance.Color(patch).enhance(sat)).enhance(bright)
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rectangle((x0 + feather, y0 + feather, x1 - feather, y1 - feather), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(feather)); full = im.copy(); full.paste(patch, (x0, y0))
    return Image.composite(full, im, m)



def pill(cv, cx, cy, txt, size=92):   # the bill counter's pill (ink with a yellow rim), as in the video
    f = ImageFont.truetype(FONT, size); w = f.getlength(txt) + size * 1.1; h = size * 1.55
    d = ImageDraw.Draw(cv); box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    sh = Image.new('RGBA', cv.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + 10, box[2], box[3] + 10), radius=h / 2, fill=(0, 0, 0, 150))
    cv.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(cv); d.rounded_rectangle(box, radius=h / 2, fill=(16, 26, 51), outline=YEL, width=6)
    d.text((cx, cy), txt, font=f, fill=YEL, anchor='mm')

def concept_A():   # the premise failing, with the format's hook
    cv = grade(place('frames/step.png', W, H, fx=0.50, fy=0.40, ty=0.42, zoom=1.12), c=1.08, s=1.10)
    cv = vignette(cv, 0.22).convert('RGBA')
    pill(cv, 540, 345, '$???,???')
    backdrop(cv, (60, 1370, 1020, 1670), 150, blur=40)
    word(cv, 540, 1452, 'GUESS', 136, WHT)
    word(cv, 540, 1592, 'THE BILL', 136, YEL)
    return cv
def concept_B():   # before and after, one above the other, inside the 3:4 crop
    top = grade(place('frames/ring.png', W, 960, fx=0.50, fy=0.30, ty=0.50, zoom=1.15), c=1.06, s=1.08)
    bot = grade(place('frames/finished.png', W, 960, fx=0.50, fy=0.36, ty=0.50, zoom=1.15), c=1.08, s=1.10)
    cv = Image.new('RGB', (W, H), (16, 26, 51)); cv.paste(top, (0, 0)); cv.paste(bot, (0, 960)); cv = cv.convert('RGBA')
    ImageDraw.Draw(cv).rectangle((0, 952, W, 968), fill=YEL)
    pill(cv, 540, 820, '$148', size=96)
    pill(cv, 540, 1062, '$???,???', size=96)       # over the back of the yard, clear of the dog and the window
    return cv
def concept_C():   # plain frame, no text: nose to nose through the glass
    cv = grade(place('frames/nose.png', W, H, fx=0.50, fy=0.50, ty=0.50, zoom=1.0), c=1.05, s=1.06)
    return vignette(cv, 0.12).convert('RGBA')
CONCEPTS = {'A': concept_A, 'B': concept_B, 'C': concept_C}

if __name__ == '__main__':
    import sys
    os.makedirs('thumb', exist_ok=True)
    for n in (sys.argv[1:] or list(CONCEPTS)):
        im = CONCEPTS[n]().convert('RGB')
        im.save(f'thumb/cover_{n}.png'); im.save(f'thumb/cover_{n}_9x16.jpg', quality=92)
        im.crop((0, GRID[0], W, GRID[1])).save(f'thumb/cover_{n}_3x4.jpg', quality=92)
        print('cover', n)
