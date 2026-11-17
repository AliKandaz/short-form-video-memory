# Video 10 Gate C flight map and keyframe sheet (from 10-jobs stills in stills/). Run locally from the video folder.
# usage: python3 10-flightmap.py <pipeline dir>  (reads 10-clips.py there for the keyframes of each clip)
from PIL import Image, ImageDraw, ImageFont
import math
S = 'stills/'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n):
    try: return ImageFont.truetype(F, n)
    except Exception: return ImageFont.load_default()
# --- 1. map of the camera positions on the wide (W1), with the flight order ---
base = Image.open(S + 'W0.png').convert('RGB')
k = 1.25; base = base.resize((int(768 * k), int(1360 * k)))
d = ImageDraw.Draw(base, 'RGBA')
POS = {"DOOR": (135, 626), "TRAY": (250, 655), "TABLE": (205, 715), "HOIST": (522, 470), "WALL": (392, 705),
       "TOP": (585, 430), "INSIDE": (448, 640), "ROW": (612, 600), "WIDE": (384, 1180)}
POS = {n: (x * k, y * k) for n, (x, y) in POS.items()}
PATH = [("C1", "WIDE", "DOOR"), ("C4", "DOOR", "TRAY"), ("C6", "TRAY", "TABLE"), ("C7", "TABLE", "TRAY"), ("C8", "TRAY", "HOIST"),
        ("C9", "HOIST", "WALL"), ("C11", "WALL", "TOP"), ("C12", "TOP", "INSIDE"), ("C16", "INSIDE", "ROW"), ("C17", "ROW", "TRAY"),
        ("C18", "TRAY", "WIDE")]
COL = [(255, 214, 0), (0, 220, 255), (255, 120, 60), (170, 255, 90), (255, 90, 200)]
for i, (c, a, b) in enumerate(PATH):
    (x0, y0), (x1, y1) = POS[a], POS[b]
    off = (i % 3 - 1) * 9; col = COL[i % len(COL)] + (230,)
    x0 += off; y0 += off; x1 += off; y1 += off
    d.line([(x0, y0), (x1, y1)], fill=col, width=6)
    ang = math.atan2(y1 - y0, x1 - x0); L = 26
    tip = (x1 - 30 * math.cos(ang), y1 - 30 * math.sin(ang))
    d.polygon([tip, (tip[0] - L * math.cos(ang - 0.45), tip[1] - L * math.sin(ang - 0.45)),
               (tip[0] - L * math.cos(ang + 0.45), tip[1] - L * math.sin(ang + 0.45))], fill=col)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    d.rounded_rectangle([mx - 30, my - 16, mx + 30, my + 16], 6, fill=(0, 0, 0, 200)); d.text((mx, my), c, font=font(22), fill=col, anchor='mm')
for n, (x, y) in POS.items():
    d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(255, 255, 255, 235), outline=(0, 0, 0, 255), width=3)
    wlab = 14 * len(n) + 14
    lx = x + 26 if x + 26 + wlab < base.width - 4 else x - 26 - wlab
    d.rounded_rectangle([lx, y - 18, lx + wlab, y + 18], 6, fill=(0, 0, 0, 210))
    d.text((lx + 7, y), n, font=font(24), fill=(255, 255, 255), anchor='lm')
txt = ["FLIGHT MAP: 9 camera positions on one set",
       "C1  WIDE -> DOOR: glides in, the gurney rolls in",
       "C2  DOOR: pushes in, the line goes flat",
       "C3  DOOR: drifts round, ice pours in",
       "C4  DOOR -> TRAY: swoops; the vial freezes",
       "C5  TRAY: slides; the strawberry turns to mush",
       "C6  TRAY -> TABLE: pulls back; antifreeze in",
       "C7  TABLE -> TRAY: pushes in; vial sets to glass",
       "C8  TRAY -> HOIST: flies up; the pod goes in",
       "C9  HOIST -> WALL: swoops to the double wall",
       "C10 WALL: slides to the base; lights out (edit)",
       "C11 WALL -> TOP: rises; topping up, the coffee",
       "C12 TOP -> INSIDE: dives in; the level drops",
       "C13 INSIDE: glides down to the head ends",
       "C14 INSIDE: orbits to the stack of heads",
       "C15 INSIDE: pulls back to the whole tank",
       "C16 INSIDE -> ROW: glides to the oldest tank",
       "C17 ROW -> TRAY: whip (edit); the vial cracks",
       "C18 TRAY -> WIDE: pulls all the way back",
       "C19 WIDE: settles on the first frame (loop)"]
panel = Image.new('RGB', (1010, base.height), (18, 22, 30)); pd = ImageDraw.Draw(panel)
y = 40
for i, t in enumerate(txt):
    pd.text((30, y), t, font=font(34 if i == 0 else 27), fill=(255, 214, 0) if i == 0 else (235, 235, 235)); y += 70 if i == 0 else 52
out = Image.new('RGB', (base.width + panel.width, base.height)); out.paste(base, (0, 0)); out.paste(panel, (base.width, 0))
out = out.resize((out.width * 2 // 3, out.height * 2 // 3)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
import importlib.util, sys
_spec = importlib.util.spec_from_file_location("c10", sys.argv[1] + "/10-clips.py"); _c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c)
CLIPS = [(c, v[0], v[1], v[2]) for c, v in _c.C.items()]
tw, th = 150, 266; cols = 4; tile_w = 3 * tw + 2 * 22 + 20; tile_h = th + 46
sheet = Image.new('RGB', (cols * tile_w, 5 * tile_h), 'white'); sd = ImageDraw.Draw(sheet)
for i, (c, a, mids, b) in enumerate(CLIPS):
    X = (i % cols) * tile_w + 10; Y = (i // cols) * tile_h + 6
    sd.text((X, Y), f"{c}: {a} -> {' -> '.join(mids + [b])}", font=font(18), fill='black')
    x = X
    for j, kk in enumerate([a] + mids + [b]):
        sheet.paste(Image.open(S + kk + '.png').convert('RGB').resize((tw, th)), (x, Y + 30))
        if j < len(mids) + 1: sd.text((x + tw + 3, Y + 30 + th // 2), '>', font=font(26), fill='black')
        x += tw + 22
sheet.save('gateC_keyframes.jpg', quality=82); print('keyframes', sheet.size)

# --- 3. first and last frames ---
a = Image.open(S + 'W0.png').convert('RGB').resize((540, 956)); b = Image.open(S + 'Wb.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(b, (560, 40))
fd.text((10, 8), "FIRST = LAST FRAME (W0)", font=font(26), fill='black'); fd.text((570, 8), "STEP BACK (Wb): C19 flies Wb -> W0", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)
