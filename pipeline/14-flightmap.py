# Video 14 Gate C: flight map, keyframe sheet and first/last frames (from the stills in stills/). Run from the video work folder.
# usage: python3 14-flightmap.py <pipeline dir>   (reads 14-clips.py there for the keyframes of each clip)
from PIL import Image, ImageDraw, ImageFont
import math, importlib.util, sys
S = 'stills/'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n):
    try: return ImageFont.truetype(F, n)
    except Exception: return ImageFont.load_default()
# --- 1. the camera positions on the wide (W0, 768x1360), with the flight order ---
base = Image.open(S + 'W0.png').convert('RGB')
k = 1.25; base = base.resize((int(768 * k), int(1360 * k)))
d = ImageDraw.Draw(base, 'RGBA')
POS = {"TOP": (380, 196), "EDGE": (214, 330), "SHELL": (330, 600), "ROW": (668, 560), "FILL": (470, 766),
       "BASE": (404, 884), "DUCK": (520, 896), "FRONT": (250, 960), "WIDE": (384, 1250)}
LEFT = {"EDGE", "FRONT", "SHELL"}   # labels drawn to the left of the dot
POS = {n: (x * k, y * k) for n, (x, y) in POS.items()}
PATH = [("C2", "FRONT", "SHELL"), ("C3", "SHELL", "BASE"), ("C4", "BASE", "FILL"), ("C6", "FILL", "SHELL"),
        ("C7", "SHELL", "FRONT"), ("C8", "FRONT", "ROW"), ("C9", "ROW", "EDGE"), ("whip", "EDGE", "ROW"),
        ("C11", "EDGE", "FILL"), ("C12", "FILL", "TOP"), ("C13", "TOP", "WIDE"), ("C14", "WIDE", "DUCK"),
        ("C15", "DUCK", "FRONT")]
COL = [(255, 214, 0), (0, 220, 255), (255, 120, 60), (170, 255, 90), (255, 90, 200)]
for i, (c, a, b) in enumerate(PATH):
    (x0, y0), (x1, y1) = POS[a], POS[b]
    off = (i % 3 - 1) * 9; col = (200, 200, 200, 200) if c == "whip" else COL[i % len(COL)] + (230,)
    x0 += off; y0 += off; x1 += off; y1 += off
    d.line([(x0, y0), (x1, y1)], fill=col, width=4 if c == "whip" else 6)
    ang = math.atan2(y1 - y0, x1 - x0); L = 26
    tip = (x1 - 30 * math.cos(ang), y1 - 30 * math.sin(ang))
    d.polygon([tip, (tip[0] - L * math.cos(ang - 0.45), tip[1] - L * math.sin(ang - 0.45)),
               (tip[0] - L * math.cos(ang + 0.45), tip[1] - L * math.sin(ang + 0.45))], fill=col)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    w = 40 if c == "whip" else 30
    d.rounded_rectangle([mx - w, my - 16, mx + w, my + 16], 6, fill=(0, 0, 0, 200)); d.text((mx, my), c, font=font(22), fill=col, anchor='mm')
for n, (x, y) in POS.items():
    d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(255, 255, 255, 235), outline=(0, 0, 0, 255), width=3)
    wlab = 14 * len(n) + 14
    lx = x - 26 - wlab if n in LEFT or x + 26 + wlab >= base.width - 4 else x + 26
    d.rounded_rectangle([lx, y - 18, lx + wlab, y + 18], 6, fill=(0, 0, 0, 210))
    d.text((lx + 7, y), n, font=font(24), fill=(255, 255, 255), anchor='lm')
txt = ["FLIGHT MAP: 9 camera positions, one set",
       "C1  FRONT: the wall drops away (the slice)",
       "C2  FRONT -> SHELL: in through the cut, up",
       "C3  SHELL -> BASE: dives to the surging pipe",
       "C4  BASE -> FILL: rises to the sprays",
       "C5  FILL: films, mist, then a still fog",
       "C6  FILL -> SHELL: rises up the hollow",
       "C7  SHELL -> FRONT: out; mist streams up",
       "C8  FRONT -> ROW: up and round; the gale",
       "C9  ROW -> EDGE: swoops to the thin wall",
       "    whip (edit) EDGE -> ROW: back to 1965",
       "C10 ROW (storm): the three towers fall",
       "    whip (edit) ROW -> EDGE: back",
       "C11 EDGE -> FILL: down to the baffles",
       "C12 FILL -> TOP: up and out into the cloud",
       "C13 TOP -> WIDE: pulls back; the whole set",
       "C14 WIDE -> DUCK: swoops in to the duck",
       "C15 DUCK -> FRONT: out; the tower closes (loop)"]
panel = Image.new('RGB', (1010, base.height), (18, 22, 30)); pd = ImageDraw.Draw(panel)
y = 40
for i, t in enumerate(txt):
    pd.text((30, y), t, font=font(34 if i == 0 else 27), fill=(255, 214, 0) if i == 0 else (235, 235, 235)); y += 70 if i == 0 else 52
out = Image.new('RGB', (base.width + panel.width, base.height)); out.paste(base, (0, 0)); out.paste(panel, (base.width, 0))
out = out.resize((out.width * 2 // 3, out.height * 2 // 3)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
_spec = importlib.util.spec_from_file_location("c14", sys.argv[1] + "/14-clips.py"); _c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c)
CLIPS = [(c, v[0], v[1], v[2], v[3]) for c, v in _c.C.items()]
tw, th = 150, 266; cols = 4; tile_w = 3 * tw + 2 * 22 + 20; tile_h = th + 46
rows = math.ceil(len(CLIPS) / cols)
sheet = Image.new('RGB', (cols * tile_w, rows * tile_h), 'white'); sd = ImageDraw.Draw(sheet)
for i, (c, a, mids, b, secs) in enumerate(CLIPS):
    X = (i % cols) * tile_w + 10; Y = (i // cols) * tile_h + 6
    keys = [a] + mids + ([b] if b else [])
    sd.text((X, Y), f"{c} ({secs} s): {' -> '.join(keys)}" + ("" if b else "  (start only)"), font=font(18), fill='black')
    x = X
    for j, kk in enumerate(keys):
        sheet.paste(Image.open(S + kk + '.png').convert('RGB').resize((tw, th)), (x, Y + 30))
        if j < len(keys) - 1: sd.text((x + tw + 3, Y + 30 + th // 2), '>', font=font(26), fill='black')
        x += tw + 22
sheet.save('gateC_keyframes.jpg', quality=82); print('keyframes', sheet.size)

# --- 3. first and last frames (C15's end still is ST0 itself, so they match part for part) ---
a = Image.open(S + 'ST0.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(a, (560, 40))
fd.text((10, 8), "FIRST FRAME (ST0)", font=font(26), fill='black'); fd.text((570, 8), "LAST FRAME: C15 ends on ST0 itself", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)

# --- 4. all eleven stills, labelled (the set from every angle) ---
names = ["W0", "ST0", "ST1", "SH0", "BA0", "FI0", "ED0", "RO0", "RO1", "TO0", "DU0"]
tw, th = 240, 425; g = Image.new('RGB', (6 * (tw + 8) + 6, 2 * (th + 34) + 10), 'white'); gd = ImageDraw.Draw(g)
for i, n in enumerate(names):
    X = (i % 6) * (tw + 8) + 6; Y = (i // 6) * (th + 34) + 4
    gd.text((X, Y), n, font=font(22), fill='black'); g.paste(Image.open(S + n + '.png').convert('RGB').resize((tw, th)), (X, Y + 28))
g.save('gateC_stills.jpg', quality=82); print('stills', g.size)
