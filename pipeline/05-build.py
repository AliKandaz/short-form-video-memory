# Video 05 (idea #1 Aquarius, Classic look). Assemble: beats -> clean master -> audio -> ALL CAPS labels + one-word captions + overlays.
# Runs locally (this session's ffmpeg has libass) or in the Higgsfield sandbox. Work dir layout: timeline.json, audio/narration_tight.wav,
# audio/words_tight.json (05-timing.py), clips/<beat>.mp4 (else the beat's still with its camera move), stills/<KEY>.png,
# fonts/HBXCaption.ttf + fonts/HBXLabel.ttf (Fredoka 700 / Montserrat 800, families renamed), overlays.json (optional, B24 depth line).
# Usage: python3 05-build.py [B1,B2,B3]  (optional contiguous subset from B1 -> out/preview_<last>.mp4; none -> out/final.mp4)
import json, os, subprocess, re, sys
W, H, FPS = 1080, 1920, 24
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
for d in ('seg', 'out'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

STILL = {'B1':'S0','B2':'FLOAT','B3':'S2','B4':'DOOR2','B5':'MOONPOOL2','B6':'CUP2','B7':'MOONPOOL2','B8':'WINDOW2','B9':'S3b',
         'B10':'SPONGE','B11':'BOAT','B12':'FULLSPONGE','B13':'WEEKS','B14':'SHARK','B15':'RUSH','B16':'DECOMP','B16b':'NAP',
         'B17':'PLANE','B18':'NAP','B19':'CAPSULE','B20':'AQUANAUTS','B21':'STORM','B22':'ESCAPE2','B23':'BUOYRIP','B24':'PAYOFF','B25':'END'}
# camera move for beats shown as stills: in = push-in, out = pull-back, up = tilt up, pan = left-to-right, hold = barely moving
MOVE = {'B2':'up','B7':'out','B11':'up','B13':'pan','B15':'up','B17':'pan','B18':'hold'}
WIPE = {'B9': 'S2'}   # build beats with no clip: wipe down from the previous stage into the new still
# use only part of a clip (start s, end s of the source), retimed to fill the beat; e.g. drop a clip's odd ending
CLIPWIN = {'B4': (0.0, 2.0),    # B4: keep the flood coming in, drop the foam pouring out of the cutaway at the end
           'B15': (0.0, 2.9)}   # B15: keep the rush underwater; Kling had him break the surface and fly at the sun after ~3 s

def still_chain(secs, move='in'):
    n = max(1, round(secs * FPS)); base = f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
    if move == 'up':   z, x, y = "1.12", "iw/2-(iw/zoom/2)", f"(ih-ih/zoom)*(1-on/{n})"
    elif move == 'pan': z, x, y = "1.10", f"(iw-iw/zoom)*on/{n}", "ih/2-(ih/zoom/2)"
    elif move == 'out': z, x, y = f"1.08-0.08*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif move == 'hold': z, x, y = f"1.03+0.01*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    else:               z, x, y = f"1.0+0.07*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    return base + f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},trim=duration={secs:.3f},setsar=1"

def seg_still(beat, img, move='in'):
    L = B[beat]['len']
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{img}.png','-vf',still_chain(L, move)] + ENC + [f'seg/{beat}.mp4'])

def seg_wipe(beat, a, b):
    L = B[beat]['len']; t = min(1.0, L * 0.35)
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{a}.png','-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}',
         '-i',f'stills/{b}.png','-filter_complex',
         f"[0:v]{still_chain(L+0.2)}[a];[1:v]{still_chain(L+0.2)}[b];[a][b]xfade=transition=wipedown:duration={t:.2f}:offset=0.25,"
         f"trim=duration={L:.3f},setpts=PTS-STARTPTS[v]",'-map','[v]'] + ENC + [f'seg/{beat}.mp4'])

def seg_clip(beat):
    L = B[beat]['len']; p = f'clips/{beat}.mp4'
    if not os.path.exists(p):
        if beat in WIPE: print(f'  {beat}: no clip -> wipe {WIPE[beat]} -> {STILL[beat]}'); return seg_wipe(beat, WIPE[beat], STILL[beat])
        print(f'  {beat}: still {STILL[beat]} ({MOVE.get(beat, "in")})'); return seg_still(beat, STILL[beat], MOVE.get(beat, 'in'))
    win = CLIPWIN.get(beat); c = (win[1] - win[0]) if win else dur(p); r = c / L
    speed = min(r, 1.25) if r >= 1 else max(r, 0.8)       # retime within 0.8x..1.25x
    played = c / speed; pad = max(0.0, L - played)
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    if pad > 0.02:   # hold the last frame but keep a slow push-in going so it never looks frozen
        n = round(L*FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {beat}: clip {c:.2f}s -> beat {L:.2f}s (speed {speed:.2f}x, hold {pad:.2f}s)')
    pre = ['-ss', f'{win[0]:.3f}', '-t', f'{c:.3f}'] if win else []
    run(pre + ['-i', p, '-vf', vf] + ENC + [f'seg/{beat}.mp4'])

ALL = [b['beat'] for b in TL['beats']]
SEL = sys.argv[1].split(',') if len(sys.argv) > 1 else ALL
assert SEL == ALL[:len(SEL)], 'preview subsets must start at B1 and be contiguous'
T1 = TL['total'] if SEL == ALL else B[SEL[-1]]['end']
tag = 'final' if SEL == ALL else 'preview_' + SEL[-1]
print('Rendering beats', SEL)
for b in SEL: seg_clip(b)
with open('seg/list.txt','w') as f:
    for b in SEL: f.write(f"file '{b}.mp4'\n")
run(['-f','concat','-safe','0','-i','seg/list.txt','-c','copy',f'out/{tag}_clean.mp4'])
run(['-i','audio/narration_tight.wav','-af',f'apad=whole_dur={TL["total"]:.3f},atrim=0:{T1:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000',
     '-ac','2','-c:a','pcm_s16le',f'out/{tag}_audio.wav'])

words = [w for w in json.load(open('audio/words_tight.json')) if w[0] < T1]
def ts(t):
    t = max(0, t); h = int(t//3600); m = int(t%3600//60); s = t%60
    return f"{h}:{m:02d}:{s:05.2f}"
def clean(w):
    w = re.sub(r"[^A-Za-z0-9'’\-]", "", w); return w[:1].upper() + w[1:]
ev = []; prev_end = 0.0
for i, (s, e, w) in enumerate(words):
    s = max(s, prev_end)   # every word shows >= 0.12 s and never overlaps the previous one: a short word pushes the next one back a
    nxt = words[i+1][0] if i+1 < len(words) else None   # little, and the drift resets at the next pause (02-build overlapped: 'Rush'+'Up')
    end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
    end = min(max(end, s + 0.12), T1); prev_end = end
    ev.append(f"Dialogue: 1,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,1000)\\fscx90\\fscy90\\t(0,70,\\fscx100\\fscy100)}}{clean(w)}")
allw = json.load(open('audio/words_tight.json'))
norm = [re.sub(r"[^a-z0-9']", "", w.lower()) for _, _, w in allw]
def find(beat, word, back=0):
    return next(j for j in range(B[beat]['first_word'], len(norm)) if norm[j] == word) - back
# (beat, start word, back, text, end word or None, y)
LABELS = [('B3','hundred',1,'100 TONS OF LEAD',None,1420), ('B7','this',0,'MOON POOL',None,560), ('B9','this',0,'LIFE SUPPORT BUOY',None,560),
          ('B11','about',0,'1 HOUR',None,640), ('B13','this',0,'SATURATION',None,560), ('B15','this',0,'THE BENDS',None,560),
          ('B16b','seventeen',0,'17 HOURS',None,560), ('B17','flight',0,'14-HOUR FLIGHT',None,560), ('B18','this',0,'DECOMPRESSION',None,560),
          ('B20','astronauts',0,'ARTEMIS II CREW',None,560), ('B23','fortyseventon',0,'47 TONS','fourteen',520), ('B23','fourteen',0,'14 MILES',None,520)]
for beat, trig, back, text, endw, y in LABELS:
    if beat not in SEL: continue
    i = find(beat, trig, back); ls = allw[i][0]
    le = (allw[find(beat, endw)][0] - 0.06) if endw else max(B[beat]['end'] - 0.05, ls + 1.6)
    ev.append(f"Dialogue: 0,{ts(ls)},{ts(min(le, T1))},Label,,0,0,0,,{{\\an5\\pos(540,{y})\\fad(60,120)\\fscx70\\fscy70\\t(0,140,\\fscx100\\fscy100)}}{text}")
# B24 depth line: dashed white line from the waterline down to the top of the tank, with "60 FT" beside it (positions in overlays.json)
OV = json.load(open('overlays.json')) if os.path.exists('overlays.json') else {}
if 'depth' in OV and 'B24' in SEL:
    d = OV['depth']; x, y0, y1 = d['x'], d['y0'], d['y1']; s0, s1 = B['B24']['start'], min(B['B24']['end'], T1)
    dash = ''.join(f"m 0 {k} l 6 {k} l 6 {min(k+22, y1-y0)} l 0 {min(k+22, y1-y0)} " for k in range(0, int(y1-y0), 36))
    ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Shape,,0,0,0,,{{\\an7\\pos({x-3},{y0})\\fad(120,120)\\p1}}{dash}{{\\p0}}")
    for yy in (y0, y1):   # end ticks
        ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Shape,,0,0,0,,{{\\an7\\pos({x-22},{yy-3})\\fad(120,120)\\p1}}m 0 0 l 44 0 l 44 6 l 0 6{{\\p0}}")
    ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Label,,0,0,0,,{{\\an6\\pos({d['label_x']},{d['label_y']})\\fad(120,120)}}60 FT")
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,HBX Caption,116,&H00FFFFFF,&H00FFFFFF,&H00000000,&H8C000000,0,0,0,0,100,100,0,0,1,8,5,5,60,60,0,1
Style: Label,HBX Label,104,&H00FFFFFF,&H00FFFFFF,&H50000000,&H78000000,0,0,0,0,100,100,3,0,1,4,6,5,60,60,0,1
Style: Shape,HBX Label,20,&H00FFFFFF,&H00FFFFFF,&H50000000,&H78000000,0,0,0,0,100,100,0,0,1,2,3,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f'out/{tag}.ass','w').write(ass)
run(['-i',f'out/{tag}_clean.mp4','-i',f'out/{tag}_audio.wav','-vf',f'ass=out/{tag}.ass:fontsdir=fonts',
     '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k',
     '-movflags','+faststart','-shortest',f'out/{tag}.mp4'])
print(tag, round(dur(f'out/{tag}.mp4'),2), 's; target', round(T1,2))
