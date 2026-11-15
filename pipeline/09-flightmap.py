# Video 09 Gate C flight map and keyframe sheet (from 09-jobs stills in stills/). Run locally from the video folder.
from PIL import Image, ImageDraw, ImageFont
import math
S = 'stills/'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n):
    try: return ImageFont.truetype(F, n)
    except Exception: return ImageFont.load_default()
# --- 1. map of the camera positions on the wide (W1), with the flight order ---
base = Image.open(S + 'W1.png').convert('RGB')
k = 1.25; base = base.resize((int(768 * k), int(1360 * k)))
d = ImageDraw.Draw(base, 'RGBA')
POS = {"RIDGE": (378, 160), "BATH": (500, 515), "WALL": (690, 430), "GAP": (606, 600), "FOOT": (600, 805),
       "GROUND": (628, 960), "POLE": (65, 300), "PANEL": (232, 680), "WIDE": (384, 1180)}
POS = {n: (x * k, y * k) for n, (x, y) in POS.items()}
PATH = [("C1", "WIDE", "RIDGE"), ("C2", "RIDGE", "BATH"), ("C3", "BATH", "RIDGE"), ("C4", "RIDGE", "WALL"), ("C4", "WALL", "GROUND"),
        ("C5", "GROUND", "WIDE"), ("C6", "WIDE", "GAP"), ("C8", "GAP", "FOOT"), ("C9", "FOOT", "POLE"), ("C10", "POLE", "PANEL"),
        ("C12", "PANEL", "BATH"), ("C15", "BATH", "WIDE"), ("C15", "WIDE", "GROUND"), ("C16", "GROUND", "WIDE")]
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
txt = ["FLIGHT MAP: 10 camera positions on one set",
       "C1  WIDE -> RIDGE: swoops down, the first bolt hits",
       "C2  RIDGE -> BATH: dives after the glow to the shower",
       "C3  BATH -> RIDGE: pulls up and away, the rod rises",
       "C4  RIDGE -> WALL -> GROUND: flies down the cable",
       "C5  GROUND -> WIDE: step back 1, a bolt hits the rod",
       "C6  WIDE -> GAP: swoops in to the side wall",
       "C7  GAP: drifts in, the side flash jumps",
       "C8  GAP -> FOOT: glides down, clamps go on",
       "C9  FOOT -> POLE: whip (far jump)",
       "C10 POLE -> PANEL: bolt hits the pole, rides in",
       "C11 PANEL: drifts in, the surge protector",
       "C12 PANEL -> BATH: flies up through the house",
       "C13 BATH: pushes in on the duck",
       "C14 BATH: the shower stops, eases back",
       "C15 BATH -> WIDE -> GROUND: step back 2, big bolt",
       "C16 GROUND -> WIDE: back to the first frame (loop)"]
panel = Image.new('RGB', (1010, base.height), (18, 22, 30)); pd = ImageDraw.Draw(panel)
y = 40
for i, t in enumerate(txt):
    pd.text((30, y), t, font=font(34 if i == 0 else 27), fill=(255, 214, 0) if i == 0 else (235, 235, 235)); y += 70 if i == 0 else 52
out = Image.new('RGB', (base.width + panel.width, base.height)); out.paste(base, (0, 0)); out.paste(panel, (base.width, 0))
out = out.resize((out.width * 2 // 3, out.height * 2 // 3)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
CLIPS = [("C1", "W", [], "R0B"), ("C2", "R0B", [], "Bg"), ("C3", "Bg", [], "R1"), ("C4", "R1", ["D"], "G"), ("C5", "G", [], "W1B"),
         ("C6", "W1B", [], "S"), ("C7", "S", [], "Sa"), ("C8", "Sa", [], "K"), ("C9", "K", [], "P"), ("C10", "P", ["Pb"], "Es"),
         ("C11", "Es", [], "E1"), ("C12", "E1", [], "B"), ("C13", "B", [], "Bd"), ("C14", "Bd", [], "Bo"), ("C15", "Bo", ["W1B"], "Gg"),
         ("C16", "Gg", [], "W1")]
tw, th = 150, 266; cols = 4; tile_w = 3 * tw + 2 * 22 + 20; tile_h = th + 46
sheet = Image.new('RGB', (cols * tile_w, 4 * tile_h), 'white'); sd = ImageDraw.Draw(sheet)
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
a = Image.open(S + 'W.png').convert('RGB').resize((540, 956)); b = Image.open(S + 'W1.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(b, (560, 40))
fd.text((10, 8), "FIRST FRAME (W)", font=font(26), fill='black'); fd.text((570, 8), "LAST FRAME (W1): + rod, cable, ground rod", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)
