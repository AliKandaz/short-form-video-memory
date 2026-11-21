# Video 15 Gate C: flight map, keyframe sheet, first/last frames and all stills (from the accepted stills in stills/, named
# KEY.png). Run from the video work folder. usage: python3 15-flightmap.py <pipeline dir>  (reads 15-clips.py for the keyframes)
# This set has no single wide that shows every position (half the video is inside the bowl, half outside in the lot), so the
# flight map is drawn as a diagram: one thumbnail per camera position, the inside positions on the left, the outside ones on the
# right, and the clips as numbered arrows in flight order (dashed grey = a 0.3 s whip made in the edit).
from PIL import Image, ImageDraw, ImageFont
import math, importlib.util, sys
S = 'stills/'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n):
    try: return ImageFont.truetype(F, n)
    except Exception: return ImageFont.load_default()

# --- 1. flight map ---
NODE = {"SIDE": ("SIDE1", 170, 560), "WHEELS": ("WH0", 470, 940), "ROOF": ("RF0", 470, 250), "LAYERS": ("LA0", 870, 940),
        "FLOOR": ("FL0", 870, 560), "HIGH": ("HI0", 1290, 250), "RAIL": ("RA0", 1290, 940)}
TW, TH = 170, 302
W, H = 1520, 1180
m = Image.new('RGB', (W, H), (18, 22, 30)); d = ImageDraw.Draw(m, 'RGBA')
d.rounded_rectangle([30, 90, 1060, 1150], 24, outline=(90, 110, 140), width=3)
d.text((50, 100), "INSIDE THE STADIUM", font=font(26), fill=(150, 170, 200))
d.rounded_rectangle([1090, 90, 1490, 1150], 24, outline=(170, 140, 90), width=3)
d.text((1110, 100), "OUTSIDE, IN THE LOT", font=font(26), fill=(220, 190, 140))
d.text((30, 30), "FLIGHT MAP: 7 camera positions, 14 clips, one set", font=font(34), fill=(255, 214, 0))
PATH = [("C2", "SIDE", "WHEELS"), ("C2", "WHEELS", "ROOF"), ("whip", "ROOF", "HIGH"), ("C5", "HIGH", "RAIL"),
        ("C7", "RAIL", "HIGH"), ("C8", "HIGH", "LAYERS"), ("whip", "LAYERS", "FLOOR"), ("C11", "FLOOR", "HIGH"),
        ("C13", "HIGH", "RAIL"), ("whip", "RAIL", "SIDE")]
SELF = {"SIDE": "C1 face drops / C14 closes", "ROOF": "C3 roof shuts", "HIGH": "C4 field rolls out / C12 orbit",
        "RAIL": "C6 motor / C13 tortoise", "LAYERS": "C9 water drains", "FLOOR": "C10 court appears", "WHEELS": "C2 wheels turn"}
COL = [(255, 214, 0), (0, 220, 255), (255, 120, 60), (170, 255, 90), (255, 90, 200)]
def centre(n): _, x, y = NODE[n]; return x, y
for i, (c, a, b) in enumerate(PATH):
    (x0, y0), (x1, y1) = centre(a), centre(b)
    off = ((i % 3) - 1) * 14; x0 += off; y0 += off; x1 += off; y1 += off
    ang = math.atan2(y1 - y0, x1 - x0)
    # stop the arrow at the thumbnail's edge
    def edge(x, y, sgn):
        dx, dy = math.cos(ang) * sgn, math.sin(ang) * sgn
        t = min((TW / 2 + 12) / abs(dx) if dx else 1e9, (TH / 2 + 12) / abs(dy) if dy else 1e9)
        return x + dx * t, y + dy * t
    sx, sy = edge(x0, y0, 1); ex, ey = edge(x1, y1, -1)
    col = (190, 190, 190, 220) if c == "whip" else COL[i % len(COL)] + (240,)
    if c == "whip":
        n = int(math.hypot(ex - sx, ey - sy) // 22)
        for k in range(n):
            if k % 2 == 0:
                d.line([(sx + (ex - sx) * k / n, sy + (ey - sy) * k / n), (sx + (ex - sx) * (k + 1) / n, sy + (ey - sy) * (k + 1) / n)], fill=col, width=5)
    else:
        d.line([(sx, sy), (ex, ey)], fill=col, width=7)
    L = 28
    d.polygon([(ex, ey), (ex - L * math.cos(ang - 0.45), ey - L * math.sin(ang - 0.45)),
               (ex - L * math.cos(ang + 0.45), ey - L * math.sin(ang + 0.45))], fill=col)
    mx, my = (sx + ex) / 2, (sy + ey) / 2; w = 44 if c == "whip" else 32
    d.rounded_rectangle([mx - w, my - 18, mx + w, my + 18], 7, fill=(0, 0, 0, 220))
    d.text((mx, my), c, font=font(24), fill=col, anchor='mm')
for n, (k, x, y) in NODE.items():
    th = Image.open(S + k + '.png').convert('RGB').resize((TW, TH))
    m.paste(th, (int(x - TW / 2), int(y - TH / 2)))
    d.rectangle([x - TW / 2, y - TH / 2, x + TW / 2, y + TH / 2], outline=(255, 255, 255), width=3)
    d.rounded_rectangle([x - TW / 2, y - TH / 2 - 36, x + TW / 2, y - TH / 2 - 4], 6, fill=(0, 0, 0, 230))
    d.text((x, y - TH / 2 - 20), n, font=font(22), fill=(255, 255, 255), anchor='mm')
    d.text((x, y + TH / 2 + 18), SELF[n], font=font(17), fill=(235, 235, 235), anchor='mm')
txt = ["C1  SIDE: the solid face drops away: wheels", "C2  SIDE -> WHEELS -> ROOF: down the row, up",
       "C3  ROOF: the roof shuts; down to pale grass", "    whip (edit) ROOF -> HIGH",
       "C4  HIGH: the whole field rolls out", "C5  HIGH -> RAIL: swoops to the wheels",
       "C6  RAIL: in on a wheel's motor", "C7  RAIL -> HIGH: rises; shadows sweep",
       "C8  HIGH -> LAYERS: down to the cut face", "C9  LAYERS: water drains into the pipe",
       "    whip (edit) LAYERS -> FLOOR", "C10 FLOOR: bare floor; the court appears",
       "C11 FLOOR -> HIGH: out the opening, up", "C12 HIGH: slow blimp orbit (ring)",
       "C13 HIGH -> RAIL: down to the tortoise", "    whip (edit) RAIL -> SIDE",
       "C14 SIDE: the face closes = frame 0"]
panel = Image.new('RGB', (760, H), (12, 15, 20)); pd = ImageDraw.Draw(panel)
y = 60
for t in txt:
    pd.text((26, y), t, font=font(25), fill=(150, 150, 150) if t.startswith("    whip") else (235, 235, 235)); y += 58
out = Image.new('RGB', (W + panel.width, H)); out.paste(m, (0, 0)); out.paste(panel, (W, 0))
out = out.resize((out.width * 3 // 4, out.height * 3 // 4)); out.save('gateC_flightmap.jpg', quality=85); print('map', out.size)

# --- 2. every clip's keyframes: start -> (middle) -> end ---
_spec = importlib.util.spec_from_file_location("c15", sys.argv[1] + "/15-clips.py"); _c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c)
CLIPS = [(c, v[0], v[1], v[2], _c.PLAN.get(c, v[3])) for c, v in _c.C.items()]
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

# --- 3. first and last frames (C14's end still is SIDE0 itself, so they match part for part) ---
a = Image.open(S + 'SIDE0.png').convert('RGB').resize((540, 956))
fl = Image.new('RGB', (1100, 1000), 'white'); fd = ImageDraw.Draw(fl)
fl.paste(a, (0, 40)); fl.paste(a, (560, 40))
fd.text((10, 8), "FIRST FRAME (SIDE0)", font=font(26), fill='black'); fd.text((570, 8), "LAST FRAME: C14 ends on SIDE0 itself", font=font(26), fill='black')
fl.save('gateC_first_last.jpg', quality=85); print('first/last', fl.size)

# --- 4. all twelve stills, labelled (the set from every angle) ---
names = ["SIDE0", "SIDE1", "WH0", "RF0", "RF1", "HI1", "HI0", "RA0", "TO0", "LA0", "FL0", "FL1"]
tw, th = 240, 425; g = Image.new('RGB', (6 * (tw + 8) + 6, 2 * (th + 34) + 10), 'white'); gd = ImageDraw.Draw(g)
for i, n in enumerate(names):
    X = (i % 6) * (tw + 8) + 6; Y = (i // 6) * (th + 34) + 4
    gd.text((X, Y), n, font=font(22), fill='black'); g.paste(Image.open(S + n + '.png').convert('RGB').resize((tw, th)), (X, Y + 28))
g.save('gateC_stills.jpg', quality=82); print('stills', g.size)
