# Video 16 Gate C: the flight map, every clip's keyframes, the first and last frames, the dog against his key, and all the
# stills. Run from the video work folder, which holds the accepted stills as stills/KEY.png.
# usage: python3 16-flightmap.py     (writes gateC_*.jpg beside stills/)
# Adapted from 15-flightmap.py: a diagram of position thumbnails with the clips as numbered arrows in flight order.
from PIL import Image, ImageDraw, ImageFont
import math
S = 'stills/'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n):
    try: return ImageFont.truetype(F, n)
    except Exception: return ImageFont.load_default()

# --- 1. flight map ---
NODE = {"GUTTER": ("GU", 220, 340), "HIGH": ("HI3", 620, 340), "ROOF": ("RO4", 1020, 340), "STREET": ("ST5", 1420, 340),
        "OUTLET": ("OU1", 220, 870), "FRONT": ("F0", 620, 870), "SIGN": ("SG", 1420, 870)}
TW, TH = 170, 302
W, H = 1640, 1120
m = Image.new('RGB', (W, H), (16, 26, 51)); d = ImageDraw.Draw(m, 'RGBA')
d.text((30, 26), "FLIGHT MAP: 7 camera positions, 13 clips, one set", font=font(34), fill=(255, 214, 46))
PATH = [("C3", "FRONT", "GUTTER"), ("C4", "GUTTER", "OUTLET"), ("C6", "OUTLET", "FRONT"), ("C7", "FRONT", "GUTTER"),
        ("C7", "GUTTER", "HIGH"), ("C8", "HIGH", "ROOF"), ("C10", "ROOF", "STREET"), ("C11", "STREET", "SIGN"),
        ("C12", "SIGN", "FRONT")]
SELF = {"FRONT": "C1 hook / C2 blackout / C13 the show", "GUTTER": "LED bulb, then one pixel", "OUTLET": "C5 the outlet trips",
        "HIGH": "colour runs over the roof", "ROOF": "C9 power injected", "STREET": "the dog howls; cars tune in",
        "SIGN": "the radio sign"}
COL = [(255, 214, 46), (0, 220, 255), (255, 120, 60), (170, 255, 90), (255, 90, 200)]
def centre(n): _, x, y = NODE[n]; return x, y
for i, (c, a, b) in enumerate(PATH):
    (x0, y0), (x1, y1) = centre(a), centre(b)
    off = ((i % 3) - 1) * 16; x0 += off; y0 += off; x1 += off; y1 += off
    ang = math.atan2(y1 - y0, x1 - x0)
    def edge(x, y, sgn):
        dx, dy = math.cos(ang) * sgn, math.sin(ang) * sgn
        t = min((TW / 2 + 12) / abs(dx) if dx else 1e9, (TH / 2 + 12) / abs(dy) if dy else 1e9)
        return x + dx * t, y + dy * t
    sx, sy = edge(x0, y0, 1); ex, ey = edge(x1, y1, -1)
    col = COL[i % len(COL)] + (240,)
    d.line([(sx, sy), (ex, ey)], fill=col, width=7)
    L = 28
    d.polygon([(ex, ey), (ex - L * math.cos(ang - 0.45), ey - L * math.sin(ang - 0.45)),
               (ex - L * math.cos(ang + 0.45), ey - L * math.sin(ang + 0.45))], fill=col)
    mx, my = (sx + ex) / 2, (sy + ey) / 2
    d.rounded_rectangle([mx - 34, my - 18, mx + 34, my + 18], 7, fill=(0, 0, 0, 220))
    d.text((mx, my), c, font=font(24), fill=col, anchor='mm')
for n, (k, x, y) in NODE.items():
    th = Image.open(S + k + '.png').convert('RGB').resize((TW, TH))
    m.paste(th, (int(x - TW / 2), int(y - TH / 2)))
    d.rectangle([x - TW / 2, y - TH / 2, x + TW / 2, y + TH / 2], outline=(255, 255, 255), width=3)
    d.rounded_rectangle([x - TW / 2, y - TH / 2 - 36, x + TW / 2, y - TH / 2 - 4], 6, fill=(0, 0, 0, 230))
    d.text((x, y - TH / 2 - 20), n, font=font(22), fill=(255, 255, 255), anchor='mm')
    d.text((x, y + TH / 2 + 18), SELF[n], font=font(16), fill=(235, 235, 235), anchor='mm')
txt = ["C1  FRONT: the string lights up (hook)", "C2  FRONT: fifty more, then the blackout", "C3  FRONT -> GUTTER: up to the LED bulbs",
       "C4  GUTTER -> OUTLET: down into the rain", "C5  OUTLET: in on the outlet as it trips", "C6  OUTLET -> FRONT: boxes shut; all blink",
       "C7  FRONT -> GUTTER -> HIGH: one pixel, then up", "C8  HIGH -> ROOF: white fades to pink", "C9  ROOF: power fed into the middle",
       "C10 ROOF -> STREET: the music wakes the street", "C11 STREET -> SIGN: cars tune in; the sign",
       "C12 SIGN -> FRONT: tree, arches, snowman", "C13 FRONT: the show plays; the bill"]
panel = Image.new('RGB', (760, H), (10, 16, 32)); pd = ImageDraw.Draw(panel)
y = 70
for t in txt:
    pd.text((26, y), t, font=font(25), fill=(235, 235, 235)); y += 74
out = Image.new('RGB', (W + panel.width, H)); out.paste(m, (0, 0)); out.paste(panel, (W, 0))
out = out.resize((out.width * 3 // 4, out.height * 3 // 4)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
CLIPS = [("C1", ["F0", "F0b"], 4), ("C2", ["F0b", "F1", "F1x"], 5), ("C3", ["F1x", "GU"], 5), ("C4", ["GU", "OU1"], 4),
         ("C5", ["OU1"], 5), ("C6", ["OU1", "OU2", "F1"], 4), ("C7", ["F1", "PX", "HI3"], 6), ("C8", ["HI3", "RO3"], 4),
         ("C9", ["RO3", "RO4"], 4), ("C10", ["RO4", "ST5"], 3), ("C11", ["ST5", "SG"], 8), ("C12", ["SG", "FR6"], 4),
         ("C13", ["FR6"], 5)]
tw, th = 150, 266; cols = 4; tile_w = 3 * tw + 2 * 22 + 20; tile_h = th + 46
rows = math.ceil(len(CLIPS) / cols)
sheet = Image.new('RGB', (cols * tile_w, rows * tile_h), 'white'); sd = ImageDraw.Draw(sheet)
for i, (c, keys, secs) in enumerate(CLIPS):
    X = (i % cols) * tile_w + 10; Y = (i // cols) * tile_h + 6
    sd.text((X, Y), f"{c} ({secs} s): {' -> '.join(keys)}" + ("  (start only)" if len(keys) == 1 else ""), font=font(18), fill='black')
    x = X
    for j, kk in enumerate(keys):
        sheet.paste(Image.open(S + kk + '.png').convert('RGB').resize((tw, th)), (x, Y + 30))
        if j < len(keys) - 1: sd.text((x + tw + 3, Y + 30 + th // 2), '>', font=font(26), fill='black')
        x += tw + 22
sheet.save('gateC_keyframes.jpg', quality=84); print('keyframes', sheet.size)

# --- 3. the first frame, the hook's end state and the last still ---
fl = Image.new('RGB', (3 * 540 + 40, 1010), 'white'); fd = ImageDraw.Draw(fl)
for i, (k, t) in enumerate([("F0", "FRAME 0 (F0): the naive step"), ("F0b", "BY 1 s (F0b): the string is lit"),
                            ("FR6", "LAST STILL (FR6): the finished build")]):
    fl.paste(Image.open(S + k + '.png').convert('RGB').resize((540, 956)), (i * 560, 46))
    fd.text((i * 560 + 8, 10), t, font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=86); print('first/last', fl.size)

# --- 4. the dog: his key, and how he was drawn in the four stills he is in ---
BOX = {"F0": (250, 730, 470, 950), "ST5": (355, 740, 475, 860), "SG": (420, 700, 720, 1120), "FR6": (260, 750, 480, 990)}
dg = Image.new('RGB', (5 * 330 + 10, 400), 'white'); dd = ImageDraw.Draw(dg)
dg.paste(Image.open(S + 'DOG.png').convert('RGB').resize((320, 320)), (5, 50)); dd.text((10, 12), "THE DOG KEY", font=font(24), fill='black')
for i, (k, box) in enumerate(BOX.items()):
    im = Image.open(S + k + '.png').convert('RGB').crop(box)
    s_ = min(320 / im.width, 320 / im.height); im = im.resize((int(im.width * s_), int(im.height * s_)))
    dg.paste(im, (335 + i * 330, 50)); dd.text((340 + i * 330, 12), f"in {k}", font=font(24), fill='black')
dg.save('gateC_dog.jpg', quality=88); print('dog', dg.size)

# --- 5. all fourteen stills, labelled (the set from every angle) ---
names = ["F0", "F0b", "F1", "F1x", "GU", "PX", "OU1", "OU2", "HI3", "RO3", "RO4", "ST5", "SG", "FR6"]
tw, th = 240, 425; g = Image.new('RGB', (7 * (tw + 8) + 6, 2 * (th + 34) + 10), 'white'); gd = ImageDraw.Draw(g)
for i, n in enumerate(names):
    X = (i % 7) * (tw + 8) + 6; Y = (i // 7) * (th + 34) + 4
    gd.text((X, Y), n, font=font(22), fill='black'); g.paste(Image.open(S + n + '.png').convert('RGB').resize((tw, th)), (X, Y + 28))
g.save('gateC_stills.jpg', quality=84); print('stills', g.size)
