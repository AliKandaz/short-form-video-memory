# Video 04 (H15 seawater to tap water, Hidden By Design look). Runs in the Higgsfield sandbox (v04/).
# Usage: python3 build.py [B1,B2,B3,B4]  (contiguous subset from B1 -> out/preview_<last>.mp4; no argument -> out/final.mp4)
# Inputs: timeline.json, audio/narration_tight.wav, audio/words_tight.json (03-timing.py), clips/<beat>.mp4 (otherwise the
# beat's still with a push-in), stills/*.png. Look: 0.3 s dissolves between beats instead of hard cuts; one-word ALL CAPS captions
# (Montserrat ExtraBold, white, black stroke, drop shadow) at ~73% height (y=1400), below the subjects; white highlight ring on the
# bottle label (B19); white flow chevrons through the pressure exchanger (B15).
import json, os, subprocess, re, sys
from PIL import ImageFont
W, H, FPS, D = 1080, 1920, 24, 0.30
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ALL = [b['beat'] for b in TL['beats']]
SEL = sys.argv[1].split(',') if len(sys.argv) > 1 else ALL
assert SEL == ALL[:len(SEL)], 'preview subsets must start at B1 and be contiguous'
FULL = SEL == ALL; T1 = TL['total'] if FULL else B[SEL[-1]]['end']; tag = 'final' if FULL else 'preview_' + SEL[-1]
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
def run(a): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + a, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
STILL = {'B1':'S0','B2':'TAPSALT','B3':'BOIL','B4':'FUEL','B5':'HALL','B6':'MEMBRANE','B7':'GAUGE2','B8':'HALL','B9':'INTAKE',
         'B10':'CAP','B11':'CAP','B12':'CLOG','B13':'SAND','B14':'POWER','B15':'PX','B16':'CORRODE','B17':'LIME','B18':'PEBBLE',
         'B19':'BOTTLE2','B20':'GLASSES','B21':'PLUME','B22':'DIFFUSER','B23':'DROUGHT3','B24':'RESERVOIR','B25':'PAYOFF','B26':'PERTH',
         'B27':'END'}
ZOOM = 0.06
def seglen(b): return B[b]['len'] + (0 if b == SEL[-1] else D)   # every beat but the last carries the dissolve tail
def seg_still(b, L, out=None):
    n = max(1, round(L * FPS))
    vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
          f"zoompan=z='1.0+{ZOOM}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},trim=duration={L:.3f},setsar=1")
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{STILL[b]}.png','-vf',vf] + ENC + [out or f'seg/{b}.mp4'])
CUT = {}   # beat -> seconds of its clip to keep before dissolving into the beat's still (filled in after review)
def seg_cut(b, L, p, c0, X=0.25):
    run(['-i', p, '-vf', f"trim=duration={c0:.3f},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1"]
        + ENC + [f'seg/{b}_a.mp4'])
    seg_still(b, L - c0 + X, f'seg/{b}_b.mp4')
    run(['-i', f'seg/{b}_a.mp4', '-i', f'seg/{b}_b.mp4', '-filter_complex', f"[0:v][1:v]xfade=transition=fade:duration={X}:offset={c0-X:.3f}[v]",
         '-map', '[v]'] + ENC + [f'seg/{b}.mp4'])
    print(f'  {b}: first {c0:.2f}s of the clip, then the {STILL[b]} still ({L:.2f}s)')
def seg(b):
    L = seglen(b); p = f'clips/{b}.mp4'
    if not os.path.exists(p): print(f'  {b}: still {STILL[b]} ({L:.2f}s)'); return seg_still(b, L)
    if b in CUT: return seg_cut(b, L, p, CUT[b])
    c = dur(p); r = c / L; speed = min(r, 1.25) if r >= 1 else max(r, 0.8); pad = max(0.0, L - c / speed)
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    if pad > 0.02:   # hold the last frame with a slow push-in so it never looks frozen
        n = round(L * FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {b}: clip {c:.2f}s -> {L:.2f}s (speed {speed:.2f}x, hold {pad:.2f}s)')
    run(['-i', p, '-vf', vf] + ENC + [f'seg/{b}.mp4'])
print('Rendering beats', SEL)
for b in SEL: seg(b)
inp = []
for b in SEL: inp += ['-i', f'seg/{b}.mp4']
if len(SEL) == 1: run(inp + ['-c', 'copy', f'out/{tag}_clean.mp4'])
else:
    fc, prev = '', '0:v'
    for k in range(1, len(SEL)):
        fc += f"[{prev}][{k}:v]xfade=transition=fade:duration={D}:offset={B[SEL[k]]['start']:.3f}[v{k}];"; prev = f'v{k}'
    run(inp + ['-filter_complex', fc.rstrip(';'), '-map', f'[{prev}]'] + ENC + [f'out/{tag}_clean.mp4'])
run(['-i','audio/narration_tight.wav','-af',f'apad=whole_dur={TL["total"]:.3f},atrim=0:{T1:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000',
     '-ac','2','-c:a','pcm_s16le',f'out/{tag}_audio.wav'])
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
PF = ImageFont.truetype('/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf', 100); CAPY = 1400; MAXW = 840
words = [w for w in json.load(open('audio/words_tight.json')) if w[0] < T1]
ev = []
for i, (s, e, w) in enumerate(words):
    nxt = words[i+1][0] if i + 1 < len(words) else None
    end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
    end = min(max(end, s + 0.12), T1)
    txt = re.sub(r"[^A-Za-z0-9'\-]", "", w.replace('’', "'")).upper()
    fit = min(100.0, 100.0 * MAXW / max(1.0, PF.getlength(txt)))
    ev.append(f"Dialogue: 2,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAPY})\\fscx{fit*0.9:.0f}\\fscy{fit*0.9:.0f}\\t(0,70,\\fscx{fit:.0f}\\fscy{fit:.0f})}}{txt}")
def ellipse(rx, ry):   # drawn from a top-left origin (0..2rx, 0..2ry): libass places shapes by that corner with \\an7
    k = 0.5523; a, b = rx * k, ry * k
    return (f"m {rx} 0 b {rx+a:.0f} 0 {2*rx} {ry-b:.0f} {2*rx} {ry} b {2*rx} {ry+b:.0f} {rx+a:.0f} {2*ry} {rx} {2*ry} "
            f"b {rx-a:.0f} {2*ry} 0 {ry+b:.0f} 0 {ry} b 0 {ry-b:.0f} {rx-a:.0f} 0 {rx} 0")
def drift(y, beat, frac=1.0):   # where a point at screen y sits after the still's push-in has run for frac of the beat
    z = 1 + ZOOM * (B[beat]['len'] * frac) / (B[beat]['len'] + D); return 960 + (y - 960) * z
def ring(beat, x, y, rx, ry):
    if beat not in SEL: return
    s, e = B[beat]['start'] + 0.15, B[beat]['end'] - 0.05; y2 = drift(y, beat)
    ev.append(f"Dialogue: 1,{ts(s)},{ts(e)},Shape,,0,0,0,,{{\\an7\\move({x-rx},{y-ry},{x-rx},{y2-ry:.0f})\\1a&HFF&\\3c&HFFFFFF&\\bord7\\shad3"
              f"\\fad(150,150)\\p1}}{ellipse(rx, ry)}{{\\p0}}")
OVER = json.load(open('overlays.json')) if os.path.exists('overlays.json') else {}   # positions set after the stills are reviewed
for r in OVER.get('rings', []): ring(r['beat'], r['x'], r['y'], r['rx'], r['ry'])
for c in OVER.get('chevrons', []):   # white chevrons sliding along a path (x0,y0)->(x1,y1), rotated to point along it
    if c['beat'] not in SEL: continue
    t, t_end = B[c['beat']]['start'] + 0.2, B[c['beat']]['end'] - 0.6
    while t < t_end:
        ev.append(f"Dialogue: 1,{ts(t)},{ts(t+0.9)},Shape,,0,0,0,,{{\\an7\\move({c['x0']},{c['y0']},{c['x1']},{c['y1']})\\frz{c.get('rot',0)}"
                  f"\\1c&HFFFFFF&\\3c&H000000&\\bord3\\shad0\\fad(150,250)\\p1}}m 0 34 l 34 0 l 68 34 l 68 48 l 34 14 l 0 48{{\\p0}}"); t += 0.3
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,Montserrat ExtraBold,100,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,7,4,5,40,40,0,1
Style: Shape,Montserrat ExtraBold,20,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H64000000,0,0,0,0,100,100,0,0,1,6,3,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f'out/{tag}.ass', 'w').write(ass)
run(['-i', f'out/{tag}_clean.mp4', '-i', f'out/{tag}_audio.wav', '-vf', f'ass=out/{tag}.ass',
     '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
     '-movflags', '+faststart', '-shortest', f'out/{tag}.mp4'])
print(tag, round(dur(f'out/{tag}.mp4'), 2), 's; target', round(T1, 2))
