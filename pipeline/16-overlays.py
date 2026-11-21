# Build-format overlays (CLAUDE.md section 5, "Overlays for the build format"), first written for video 16 (21 Nov 2026).
# Everything here is laid over the picture in the edit as ASS events (libass); nothing is ever asked of the image or video
# models. Imported by 16-build.py and 16-gateD.py (importlib, as 16-clips.py imports 16-prompts.py). Run from the work dir
# (fonts/HBXCaption.ttf = Montserrat 800 renamed "HBX Caption", as for the captions).
#   label_events(labels, t0, t1)        a fix's real name, yellow, about a fifth of the way down, for one sentence
#   bill_events(bill, t0, t1)           the price counter: a pill near the top; "+$305" slides in beside it at each "So" and
#                                       the total rolls up; on the closing line the total grows as big as the sky allows
#   STYLES                              the ASS styles these events use (append to the build's [V4+ Styles])
# Sizes follow the caption's convention: libass Fontsize 114 gives the 57 px letters check_video.py measures (15-build.py),
# so Fontsize = 2 x the letter height wanted.
import math
from PIL import ImageFont

W, H, FPS = 1080, 1920, 30
YELLOW, INK, WHITE, BLACK = "&H002ED6FF", "&H00331A10", "&H00FFFFFF", "&H00000000"   # #FFD62E, #101A33 (ASS is BGR)
FONT = 'fonts/HBXCaption.ttf'
LABEL_FS, LABEL_Y, LABEL_MAXW = 140, 384, 940      # ~70 px letters, centred 20% down, fitted to 940 px
LABEL_TOP = 296                                     # no label starts above this (the pill ends at about 266)
BILL_FS, BILL_Y = 88, 222                           # ~44 px digits, centred 11.5% down (the pill's top edge clears 9%)
CHIP_FS = 80
BIG_FS, BIG_Y = 184, 278                            # the final total: ~92 px digits, centred 14.5% down (set per video: it
                                                    # sits in the calm sky above the finished build, never over the build)
ROLL, CHIP_IN, CHIP_HOLD, MERGE, GROW = 0.40, 0.15, 0.50, 0.20, 0.50

STYLES = f"""Style: Label,HBX Caption,{LABEL_FS},{YELLOW},{WHITE},{BLACK},&H8C000000,0,0,0,0,100,100,0,0,1,8,5,5,60,60,0,1
Style: Pill,HBX Caption,20,{INK},{WHITE},{YELLOW},&H78000000,0,0,0,0,100,100,0,0,1,3,4,7,0,0,0,1
Style: Bill,HBX Caption,{BILL_FS},{YELLOW},{WHITE},{BLACK},{BLACK},0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
Style: Chip,HBX Caption,{CHIP_FS},{WHITE},{WHITE},{BLACK},&H8C000000,0,0,0,0,100,100,0,0,1,6,4,4,0,0,0,1
"""

_fonts = {}
def em(fs): return fs * 1000 / 1219                 # libass Fontsize -> em px for Montserrat (ascent 968 + descent 251)
def text_w(txt, fs):
    k = max(1, round(em(fs))); f = _fonts.get(k) or _fonts.setdefault(k, ImageFont.truetype(FONT, k)); return f.getlength(txt)
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def money(v): return f"${v:,.0f}"
def ease(p): p = min(1.0, max(0.0, p)); return 1 - (1 - p) ** 3

def pill_path(w, h):
    r = h / 2; k = 0.5523 * r                       # a stadium shape, drawn from a top-left origin (\an7; 7.4)
    return (f"m {r:.0f} 0 l {w - r:.0f} 0 b {w - r + k:.0f} 0 {w:.0f} {r - k:.0f} {w:.0f} {r:.0f} "
            f"b {w:.0f} {r + k:.0f} {w - r + k:.0f} {h:.0f} {w - r:.0f} {h:.0f} l {r:.0f} {h:.0f} "
            f"b {r - k:.0f} {h:.0f} 0 {r + k:.0f} 0 {r:.0f} b 0 {r - k:.0f} {r - k:.0f} 0 {r:.0f} 0")

def pill_size(txt, fs): return text_w(txt, fs) + 2 * 0.44 * fs, 0.574 * fs + 2 * 0.21 * fs   # digits are 0.574 fs tall

def pill(a, b, cx, cy, txt, fs, alpha=0, wtxt=None):
    """One pill with its number from a to b seconds, centred on (cx, cy). wtxt: size the pill for this text instead."""
    w, h = pill_size(wtxt or txt, fs); al = f"\\alpha&H{int(alpha):02X}&" if alpha else ""
    return [f"Dialogue: 3,{ts(a)},{ts(b)},Pill,,0,0,0,,{{\\an7\\pos({cx - w / 2:.0f},{cy - h / 2:.0f}){al}\\p1}}{pill_path(w, h)}{{\\p0}}",
            f"Dialogue: 4,{ts(a)},{ts(b)},Bill,,0,0,0,,{{\\an5\\pos({cx:.0f},{cy:.0f})\\fs{fs:.0f}{al}}}{txt}"]

def label_events(labels, t0, t1):
    """labels: (TEXT, start, end) in video time; '\\N' splits a long term onto two lines. Pops in, fades out."""
    ev = []
    for txt, a, b in labels:
        if b <= t0 or a >= t1: continue
        lines = txt.split('\\N'); wmax = max(text_w(l, LABEL_FS) for l in lines); sc = min(100, int(100 * LABEL_MAXW / max(wmax, 1)))
        y = max(LABEL_Y, LABEL_TOP + len(lines) * LABEL_FS * sc / 100 / 2)   # a two-line term sits lower, clear of the pill
        ev.append(f"Dialogue: 3,{ts(a - t0)},{ts(min(b, t1) - t0)},Label,,0,0,0,,{{\\an5\\pos({W // 2},{y:.0f})\\fad(0,120)"
                  f"\\fscx{int(sc * .7)}\\fscy{int(sc * .7)}\\t(0,90,\\fscx{int(sc * 1.07)}\\fscy{int(sc * 1.07)})"
                  f"\\t(90,170,\\fscx{sc}\\fscy{sc})}}{txt}")
    return ev

def bill_events(bill, t0, t1):
    """bill: {'start': 3, 'steps': [(t_so, add), ...], 'final': t_bill or None, 'end': t_end}; times in video time.
    The pill shows the running total from frame 0. At each step the price slides in at the pill's right, waits, slides into
    the pill and the total rolls up over ROLL seconds; at 'final' the total grows to BIG_FS at BIG_Y and holds to 'end'."""
    ev = []; cx = W // 2; f = 1 / FPS
    def clip(a, b):                                   # an event's times inside this render's window, or None
        a, b = max(a, t0), min(b, t1); return (a - t0, b - t0) if b - a > 0.001 else None
    v = bill['start']; t = 0.0; end = bill.get('final') or bill['end']
    for t_so, add in bill['steps']:
        roll0 = t_so + CHIP_IN + CHIP_HOLD; new = v + add
        c = clip(t, roll0)
        if c: ev += pill(c[0], c[1], cx, BILL_Y, money(v), BILL_FS)
        # the chip: in from the right, hold, then into the pill
        w_old = pill_size(money(v), BILL_FS)[0]; x1 = cx + w_old / 2 + 26; chip = f"+{money(add)}"
        c = clip(t_so, roll0)
        if c: ev.append(f"Dialogue: 5,{ts(c[0])},{ts(c[1])},Chip,,0,0,0,,{{\\an4\\move({x1 + 46:.0f},{BILL_Y},{x1:.0f},{BILL_Y},0,"
                        f"{int(CHIP_IN * 1000)})\\fad({int(CHIP_IN * 1000)},0)}}{chip}")
        c = clip(roll0, roll0 + MERGE)
        if c: ev.append(f"Dialogue: 5,{ts(c[0])},{ts(c[1])},Chip,,0,0,0,,{{\\an4\\move({x1:.0f},{BILL_Y},{cx - 40:.0f},{BILL_Y})"
                        f"\\fad(0,{int(MERGE * 1000)})\\t(\\fscx60\\fscy60)}}{chip}")
        n = round((ROLL + 0.15) * FPS)               # the roll-up, then a small pop, one event a frame
        for i in range(n):
            a = roll0 + i * f; p = i * f / ROLL
            val = v + (new - v) * ease(p) if p < 1 else new
            pop = 1 + 0.10 * math.sin(math.pi * min(1.0, max(0.0, (i * f - ROLL) / 0.15))) if p >= 1 else 1.0
            c = clip(a, a + f)
            if c: ev += pill(c[0], c[1], cx, BILL_Y, money(round(val)), BILL_FS * pop, wtxt=money(new))
        v = new; t = roll0 + n * f
    c = clip(t, end)
    if c: ev += pill(c[0], c[1], cx, BILL_Y, money(v), BILL_FS)
    if bill.get('final') is not None:                # the total grows in the sky and holds to the end
        tb = bill['final']; n = round(GROW * FPS)
        for i in range(n):
            p = ease((i + 1) / n); a = tb + i * f; c = clip(a, a + f)
            if c: ev += pill(c[0], c[1], cx, BILL_Y + (BIG_Y - BILL_Y) * p, money(v), BILL_FS + (BIG_FS - BILL_FS) * p)
        c = clip(tb + n * f, bill['end'])
        if c: ev += pill(c[0], c[1], cx, BIG_Y, money(v), BIG_FS)
    return ev
