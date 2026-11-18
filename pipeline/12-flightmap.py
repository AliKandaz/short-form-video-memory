# Video 12 Gate C: flight map, keyframe sheet and first/last frames (from the stills in stills/). Run from the video work folder.
# usage: python3 12-flightmap.py <pipeline dir>   (reads 12-clips.py there for the keyframes of each clip)
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
POS = {"HIGH": (380, 170), "RIM": (470, 390), "STREET": (285, 470), "UNDER-LID": (398, 590), "SENSOR": (480, 680),
       "VAULT": (410, 760), "CABLE": (300, 790), "SIDE": (384, 1240)}
POS = {n: (x * k, y * k) for n, (x, y) in POS.items()}
PATH = [("C1", "STREET", "HIGH"), ("whip", "HIGH", "VAULT"), ("C3", "VAULT", "SIDE"), ("C4", "SIDE", "UNDER-LID"),
        ("C5", "UNDER-LID", "CABLE"), ("C7", "CABLE", "VAULT"), ("whip", "VAULT", "HIGH"), ("C10", "HIGH", "UNDER-LID"),
        ("C11", "UNDER-LID", "RIM"), ("C12", "RIM", "SENSOR"), ("C13", "SENSOR", "RIM"), ("C14", "RIM", "STREET")]
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
    lx = x + 26 if x + 26 + wlab < base.width - 4 else x - 26 - wlab
    d.rounded_rectangle([lx, y - 18, lx + wlab, y + 18], 6, fill=(0, 0, 0, 210))
    d.text((lx + 7, y), n, font=font(24), fill=(255, 255, 255), anchor='lm')
txt = ["FLIGHT MAP: 8 camera positions, one set",
       "C1  STREET -> HIGH: the lid blasts, camera climbs",
       "C2  HIGH: drifts down; the lid tumbles past",
       "    whip (edit) HIGH -> VAULT: back before the blast",
       "C3  VAULT -> SIDE: along the cables, out to the wide",
       "C4  SIDE -> UNDER-LID: swoops in; drips fall",
       "C5  UNDER-LID -> CABLE: drop, push in; salt, crack",
       "C6  CABLE: drifts in; the arc",
       "C7  CABLE -> VAULT: pulls back; smoke fills it",
       "C8  VAULT: tilts up the shaft; the blast",
       "    whip (edit) VAULT -> HIGH",
       "C9  HIGH: rises wider; other lids smoking",
       "C10 HIGH -> UNDER-LID: swoops in; the vented lid",
       "C11 UNDER-LID -> RIM: rises out to the street",
       "C12 RIM -> SENSOR: slush melts in; dives to the box",
       "C13 SENSOR -> RIM: rises; the latched lid lifts",
       "C14 RIM -> STREET: pulls back; the pigeon lands",
       "    (C14 ends on ST9 = frame 0's framing: loop)"]
panel = Image.new('RGB', (1010, base.height), (18, 22, 30)); pd = ImageDraw.Draw(panel)
y = 40
for i, t in enumerate(txt):
    pd.text((30, y), t, font=font(34 if i == 0 else 27), fill=(255, 214, 0) if i == 0 else (235, 235, 235)); y += 70 if i == 0 else 52
out = Image.new('RGB', (base.width + panel.width, base.height)); out.paste(base, (0, 0)); out.paste(panel, (base.width, 0))
out = out.resize((out.width * 2 // 3, out.height * 2 // 3)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
_spec = importlib.util.spec_from_file_location("c12", sys.argv[1] + "/12-clips.py"); _c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c)
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

# --- 3. first and last frames ---
a = Image.open(S + 'ST0.png').convert('RGB').resize((540, 956)); b = Image.open(S + 'ST9.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(b, (560, 40))
fd.text((10, 8), "FIRST FRAME (ST0)", font=font(26), fill='black'); fd.text((570, 8), "LAST FRAME (ST9): C14 ends here", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)
