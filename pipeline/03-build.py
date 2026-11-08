# Video 03 (H1 fire hydrant, Hidden By Design look). Runs in the Higgsfield sandbox (v03/).
# Usage: python3 build.py [B1,B2,B3,B4]  (contiguous subset from B1 -> out/preview_<last>.mp4; no argument -> out/final.mp4)
# Inputs: timeline.json, audio/narration_tight.wav, audio/words_tight.json (03-timing.py), clips/<beat>.mp4 (otherwise the
# beat's still with a push-in), stills/*.png. Look: 0.3 s dissolves between beats instead of hard cuts; one-word ALL CAPS captions
# (Montserrat ExtraBold, white, black stroke, drop shadow) at ~68% height so the valve stays visible; white highlight ring on the
# valve (B4) and the breakaway ring (B14); rising white chevrons in the water column (B10); movie letterbox bars on the geyser (B16).
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
STILL = {'B1':'S0','B2':'S0F','B3':'S1','B4':'S1','B5':'S1W','B6':'S2','B7':'STREET','B8':'TUB','B9':'COLORS','B10':'S3','B11':'HAMMER',
         'B12':'TURNS','B13':'CAR','B14':'RING','B15':'SNAP','B16':'GEYSER','B17':'SNAP','B18':'BURIED','B19':'FLAG','B20':'DOG',
         'B21':'FIRE','B22':'HOOKUP','B23':'ROAR','B24':'END'}
ZOOM = 0.06
def seglen(b): return B[b]['len'] + (0 if b == SEL[-1] else D)   # every beat but the last carries the dissolve tail
def seg_still(b, L):
    n = max(1, round(L * FPS))
    vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
          f"zoompan=z='1.0+{ZOOM}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},trim=duration={L:.3f},setsar=1")
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{STILL[b]}.png','-vf',vf] + ENC + [f'seg/{b}.mp4'])
def seg(b):
    L = seglen(b); p = f'clips/{b}.mp4'
    if not os.path.exists(p): print(f'  {b}: still {STILL[b]} ({L:.2f}s)'); return seg_still(b, L)
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
PF = ImageFont.truetype('/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf', 100); CAPY = 1300; MAXW = 840
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
ring('B4', 540, 1488, 95, 95)      # the valve at the bottom of the dry barrel (S1)
ring('B14', 540, 515, 250, 82)     # the bolted breakaway ring at ground level (RING)
if 'B10' in SEL:                   # chevrons rising up the water column (S3)
    t, t_end = B['B10']['start'] + 0.2, B['B10']['end'] - 0.6
    while t < t_end:
        ev.append(f"Dialogue: 1,{ts(t)},{ts(t+0.9)},Shape,,0,0,0,,{{\\an7\\move(491,1196,491,916)\\1c&HFFFFFF&\\3c&H000000&\\bord3\\shad0"
                  f"\\fad(150,250)\\p1}}m 0 34 l 34 0 l 68 34 l 68 48 l 34 14 l 0 48{{\\p0}}"); t += 0.3
if 'B16' in SEL:                   # movie letterbox while the narrator says "In movies..."
    s, e = B['B16']['start'], B['B16']['end'] + 0.1
    for y in (0, 1710):
        ev.append(f"Dialogue: 0,{ts(s)},{ts(e)},Shape,,0,0,0,,{{\\an7\\pos(0,{y})\\1c&H000000&\\bord0\\shad0\\fad(120,120)\\p1}}m 0 0 l 1080 0 l 1080 210 l 0 210{{\\p0}}")
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
