# Covers for video 03 (fire hydrant), built only from the video's own frames (no generation credits).
# Runs in the Higgsfield sandbox or locally, from the video folder (v03/):  python3 03-thumbnail.py [A B C D]  (default: all)
# Inputs: stills/*.png and two 2K frames of the B3 clip: thumb/frozen.png (first frame) and thumb/hydrant.png (last frame).
# Font: Montserrat ExtraBold (the video's caption face). Locally, point HBX_FONT at the fontsource .woff; HBX_UI_FONT is only
# used for the platform mock-ups.
# Layout rules (1080x1920): words and subject inside TikTok's 3:4 grid crop (y 240-1680); headline kept above YouTube Shorts'
# bottom title overlay (y < ~1440 on the mobile shelf). 0-4 words, yellow + white with a 16 px black stroke and drop shadow.
# D (final, 9 Nov 2026) is the cover for both platforms; it also writes the two upload sizes and the mock-ups:
#   thumb/cover_D_9x16.jpg   1080x1920  YouTube Shorts custom thumbnail (JPG kept under 2 MB)
#   thumb/cover_D_3x4.jpg    1080x1440  TikTok Studio "Upload cover" (TikTok crops uploads to 3:4)
#   thumb/mock_tiktok_grid.jpg, thumb/mock_youtube_shelf.jpg
import os, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1080, 1920
YEL, BLK, WHT = (255, 208, 28), (10, 10, 12), (255, 255, 255)
FONT = os.environ.get('HBX_FONT', '/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf')   # same face as the captions
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
def concept_D():   # FINAL: the climax set-up (B21 FIRE still): house burning, hydrant barrel still dry -> "IT'S EMPTY"
    im = place('stills/FIRE.png', W, H, fx=0.5, fy=0.5)
    im = neutralise(im, (372, 1236, 446, 1414))   # a cyan glint at the foot of the dry barrel read as water at thumbnail size
    cv = vignette(grade(im, c=1.12, s=1.15), 0.35).convert('RGBA')
    backdrop(cv, (20, 1000, 1060, 1175), 120)     # calms the soil and frost texture behind the headline
    words(cv, 540, 1088, [("IT'S", WHT), ('EMPTY', YEL)], 165)
    arrow(cv, bez((735, 1180), (700, 1318), (484, 1262)))
    return cv
CONCEPTS = {'A': concept_A, 'B': concept_B, 'C': concept_C, 'D': concept_D}

def rounded(im, r):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radius=r, fill=255)
    out = Image.new('RGBA', im.size, (0, 0, 0, 0)); out.paste(im.convert('RGBA'), (0, 0), m); return out
def mock_tiktok_grid(order, path):
    # TikTok profile grid on a 393 pt phone at 3x: 3 columns of 3:4 tiles with 1 pt gutters (the app's own crop of each cover)
    pw, g = 1179, 3; tw = (pw - 2 * g) // 3; th = tw * 4 // 3; rows = (len(order) + 2) // 3
    sheet = Image.new('RGB', (pw, rows * th + (rows - 1) * g + 120), (18, 18, 18)); d = ImageDraw.Draw(sheet)
    d.text((24, 40), 'TikTok profile grid (3:4 crop), phone size', font=ImageFont.truetype(UI, 36), fill=(200, 200, 200))
    for k, n in enumerate(order):
        im = Image.open(f'thumb/cover_{n}.png').convert('RGB').crop((0, GRID[0], W, GRID[1])).resize((tw, th), Image.LANCZOS)
        x, y = (k % 3) * (tw + g), 120 + (k // 3) * (th + g); sheet.paste(im, (x, y))
        dd = ImageDraw.Draw(sheet); dd.polygon([(x + 18, y + th - 46), (x + 18, y + th - 18), (x + 42, y + th - 32)], fill=WHT)
    sheet.save(path, quality=88)
def mock_youtube_shelf(pair, title, path):
    # YouTube app home "Shorts" shelf: two 9:16 cards, title and views overlaid on the bottom of each card, menu dots top-right
    pw = 1179; cw = (pw - 3 * 36) // 2; ch = cw * 16 // 9
    sheet = Image.new('RGB', (pw, ch + 170), (15, 15, 15)); d = ImageDraw.Draw(sheet)
    d.text((36, 40), 'YouTube Shorts shelf, phone size', font=ImageFont.truetype(UI, 36), fill=(200, 200, 200))
    ft, fv = ImageFont.truetype(UI, 40), ImageFont.truetype(UI, 32)
    for k, (n, t) in enumerate(zip(pair, title)):
        card = Image.open(f'thumb/cover_{n}.png').convert('RGBA').resize((cw, ch), Image.LANCZOS)
        grad = Image.new('L', (1, ch), 0)
        for y in range(ch):
            grad.putpixel((0, y), int(max(0, (y - ch * 0.62) / (ch * 0.38)) ** 1.2 * 210))
        card.alpha_composite(Image.composite(Image.new('RGBA', (cw, ch), (0, 0, 0, 255)), Image.new('RGBA', (cw, ch), (0, 0, 0, 0)), grad.resize((cw, ch))))
        dc = ImageDraw.Draw(card); y = ch - 40 - 32 - 14
        lines = t if isinstance(t, list) else [t]
        for i, ln in enumerate(reversed(lines)):
            dc.text((28, y - (i + 1) * 50), ln, font=ft, fill=WHT)
        dc.text((28, y + 6), 'views', font=fv, fill=(220, 220, 220))
        for i in range(3):
            dc.ellipse((cw - 40, 30 + i * 18, cw - 30, 40 + i * 18), fill=WHT)
        sheet.paste(rounded(card, 28), (36 + k * (cw + 36), 120), rounded(card, 28))
    sheet.save(path, quality=88)

if __name__ == '__main__':
    todo = sys.argv[1:] or list(CONCEPTS)
    for name in todo:
        im = CONCEPTS[name]().convert('RGB'); im.save(f'thumb/cover_{name}.png'); im.save(f'thumb/cover_{name}.jpg', quality=90)
        im.resize((360, 640), Image.LANCZOS).save(f'thumb/prev_{name}.jpg', quality=85)
    if 'D' in todo:
        im = Image.open('thumb/cover_D.png').convert('RGB')
        for q in (92, 88, 84):   # YouTube's thumbnail cap was 2 MB for years; stay under it either way
            im.save('thumb/cover_D_9x16.jpg', quality=q, optimize=True, progressive=True)
            if os.path.getsize('thumb/cover_D_9x16.jpg') < 1_900_000: break
        im.crop((0, GRID[0], W, GRID[1])).save('thumb/cover_D_3x4.jpg', quality=92, optimize=True, progressive=True)
        mock_tiktok_grid(['C', 'D', 'A', 'B', 'C', 'A'][:3], 'thumb/mock_tiktok_grid.jpg')
        mock_youtube_shelf(['D', 'C'], [["Why Don't Fire", 'Hydrants Freeze?'], ['(another Short)']], 'thumb/mock_youtube_shelf.jpg')
        print({p: os.path.getsize('thumb/' + p) for p in ('cover_D_9x16.jpg', 'cover_D_3x4.jpg')})
    print('ok')
