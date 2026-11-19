# Video 13 Gate C: flight map, keyframe sheet and first/last frames (from the stills in stills/). Run from the video work folder.
# usage: python3 13-flightmap.py <pipeline dir>   (reads 13-clips.py there for the keyframes of each clip)
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
POS = {"HIGH": (640, 170), "KITCHEN": (228, 318), "TV": (540, 296), "DECK": (300, 436), "RIM": (392, 506),
       "POT": (560, 548), "INSIDE": (466, 604), "BURNER": (520, 690), "WIDE": (384, 1240)}
LEFT = {"RIM", "INSIDE", "KITCHEN"}   # labels drawn to the left of the dot
POS = {n: (x * k, y * k) for n, (x, y) in POS.items()}
PATH = [("C1", "POT", "HIGH"), ("whip", "HIGH", "INSIDE"), ("C4", "INSIDE", "POT"), ("C5", "POT", "BURNER"),
        ("whip", "BURNER", "KITCHEN"), ("C7", "KITCHEN", "RIM"), ("whip", "RIM", "BURNER"), ("C9", "BURNER", "POT"),
        ("C10", "POT", "DECK"), ("C11", "DECK", "HIGH"), ("C12", "HIGH", "WIDE"), ("C13", "WIDE", "TV"), ("C14", "TV", "POT")]
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
       "C1  POT -> HIGH: the bird drops, fire rolls up",
       "    whip (edit) HIGH -> INSIDE: back to the drop",
       "C2  INSIDE: pushes in on the ice",
       "C3  INSIDE: drifts down; drops sink, steam bursts",
       "C4  INSIDE -> POT: rises with the foam",
       "C5  POT -> BURNER: oil onto the flames; fire",
       "    whip (edit) BURNER -> KITCHEN: back in time",
       "C6  KITCHEN: drifts in; the frost melts",
       "C7  KITCHEN -> RIM: out across the lawn",
       "C8  RIM: the bird lifted out; tape at the line",
       "    whip (edit) RIM -> BURNER: oil in, lit",
       "C9  BURNER -> POT: drips; gas off; bird in slowly",
       "C10 POT -> DECK: swoops to the deck",
       "C11 DECK -> HIGH: pulls up; the fryer far out",
       "C12 HIGH -> WIDE: pulls back; the whole yard",
       "C13 WIDE -> TV: flies in; the demo on the news",
       "C14 TV -> POT: back to frame 0 (the loop)"]
panel = Image.new('RGB', (1010, base.height), (18, 22, 30)); pd = ImageDraw.Draw(panel)
y = 40
for i, t in enumerate(txt):
    pd.text((30, y), t, font=font(34 if i == 0 else 27), fill=(255, 214, 0) if i == 0 else (235, 235, 235)); y += 70 if i == 0 else 52
out = Image.new('RGB', (base.width + panel.width, base.height)); out.paste(base, (0, 0)); out.paste(panel, (base.width, 0))
out = out.resize((out.width * 2 // 3, out.height * 2 // 3)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
_spec = importlib.util.spec_from_file_location("c13", sys.argv[1] + "/13-clips.py"); _c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c)
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

# --- 3. first and last frames (C14's end still is ST0 itself, so they match part for part) ---
a = Image.open(S + 'ST0.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(a, (560, 40))
fd.text((10, 8), "FIRST FRAME (ST0)", font=font(26), fill='black'); fd.text((570, 8), "LAST FRAME: C14 ends on ST0 itself", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)

# --- 4. all sixteen stills, labelled (the set from every angle) ---
names = ["W0", "H0", "H1", "D0", "ST0", "ST1", "PT2", "IN0", "IN1", "BU0", "BU1", "R0", "R1", "K0", "K1", "TV0"]
tw, th = 240, 425; g = Image.new('RGB', (8 * tw + 70, 2 * (th + 34) + 10), 'white'); gd = ImageDraw.Draw(g)
for i, n in enumerate(names):
    X = (i % 8) * (tw + 8) + 6; Y = (i // 8) * (th + 34) + 4
    gd.text((X, Y), n, font=font(22), fill='black'); g.paste(Image.open(S + n + '.png').convert('RGB').resize((tw, th)), (X, Y + 28))
g.save('gateC_stills.jpg', quality=82); print('stills', g.size)
