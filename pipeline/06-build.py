# Video 06 (idea #9 Petra, Classic look, one build in one main view). Assemble: beats -> clean master -> audio -> ALL CAPS labels +
# one-word captions + the 39 M height line. Runs locally (ffmpeg with libass). Work dir layout: timeline.json, audio/narration_tight.wav,
# audio/words_tight.json (06-timing.py), clips/C<n>.mp4, stills/<KEY>.png, fonts/HBXCaption.ttf + fonts/HBXLabel.ttf (Fredoka 700 /
# Montserrat 800, families renamed), overlays.json (optional: the height line).
# Usage: python3 06-build.py [B1,B2,B3]  (optional contiguous subset from B1 -> out/preview_<last>.mp4; none -> out/final.mp4)
# New in 06 (shot rule): HOLD beats continue from the previous beat's last frame with a slow push-in, and WIPE beats can start from
# that last frame ('PREV'), so a beat without a clip never jumps to a different-looking still.
import json, os, subprocess, re, sys
W, H, FPS = 1080, 1920, 24
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
for d in ('seg', 'out'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

# beat -> (clip, (source start, source end or None)); C1 covers B1+B2 and is split at the jar tip
CLIPSRC = {'B1': ('C1', (0.0, 2.95)), 'B2': ('C1', (2.95, None)), 'B3': ('C2', None), 'B4': ('C3', None), 'B5': ('C4', None),
           'B8': ('C5', None), 'B9': ('C6', None), 'B10': ('C7', None), 'B11': ('C8', None), 'B15': ('C9', None),
           'B16': ('C10', None), 'B17': ('C11', None), 'B20': ('C12', None), 'B22': ('C13', None), 'B24': ('C14', None)}
STILL = {'B7': 'S2', 'B14': 'BROKE', 'B19': 'S9', 'B21': 'URN'}
# camera move for still beats: in = push-in, out = pull-back, up = tilt up, pan = left-to-right, hold = barely moving, top = 1.2x crop
# anchored at the top (hides URNSLICE's sandy base)
MOVE = {'B7': 'up', 'B19': 'hold'}
HOLD = {'B6', 'B12'}
# beat -> (from still or 'PREV', to still, transition, crop move)
WIPE = {'B13': ('PREV', 'INSIDE', 'wipedown', 'in'), 'B18': ('PREV', 'S9', 'fade', 'hold'), 'B23': ('URNHOLES', 'URNSLICE', 'wipedown', 'top')}

def still_chain(secs, move='in'):
    n = max(1, round(secs * FPS)); base = f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
    if move == 'up':   z, x, y = "1.12", "iw/2-(iw/zoom/2)", f"(ih-ih/zoom)*(1-on/{n})"
    elif move == 'pan': z, x, y = "1.10", f"(iw-iw/zoom)*on/{n}", "ih/2-(ih/zoom/2)"
    elif move == 'out': z, x, y = f"1.08-0.08*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif move == 'hold': z, x, y = f"1.0+0.02*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif move == 'top': z, x, y = f"1.20+0.03*on/{n}", "iw/2-(iw/zoom/2)", "(ih-ih/zoom)*0.12"
    else:               z, x, y = f"1.0+0.06*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    return base + f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},trim=duration={secs:.3f},setsar=1"

def last_frame(beat):
    p = f'stills/_last_{beat}.png'
    run(['-sseof', '-0.1', '-i', f'seg/{beat}.mp4', '-frames:v', '1', '-update', '1', p]); return p

def seg_still(beat, img_path, move='in'):
    L = B[beat]['len']
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',img_path,'-vf',still_chain(L, move)] + ENC + [f'seg/{beat}.mp4'])

def seg_wipe(beat, a_path, b_path, trans='wipedown', move='in'):
    L = B[beat]['len']; t = min(1.6, L * 0.6) if trans == 'fade' else min(0.8, L * 0.35); off = 0.2 if trans == 'fade' else 0.15
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',a_path,'-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}',
         '-i',b_path,'-filter_complex',
         f"[0:v]{still_chain(L+0.2, move)}[a];[1:v]{still_chain(L+0.2, move)}[b];[a][b]xfade=transition={trans}:duration={t:.2f}:offset={off},"
         f"trim=duration={L:.3f},setpts=PTS-STARTPTS[v]",'-map','[v]'] + ENC + [f'seg/{beat}.mp4'])

def seg_clip(beat, prev):
    L = B[beat]['len']
    if beat in HOLD:
        print(f'  {beat}: hold on the last frame of {prev}'); return seg_still(beat, last_frame(prev), 'hold')
    if beat in WIPE:
        a, b, trans, mv = WIPE[beat]; a_path = last_frame(prev) if a == 'PREV' else f'stills/{a}.png'
        print(f'  {beat}: {trans} {a} -> {b}'); return seg_wipe(beat, a_path, f'stills/{b}.png', trans, mv)
    if beat in STILL:
        print(f'  {beat}: still {STILL[beat]} ({MOVE.get(beat, "in")})'); return seg_still(beat, f'stills/{STILL[beat]}.png', MOVE.get(beat, 'in'))
    clip, win = CLIPSRC[beat]; p = f'clips/{clip}.mp4'
    a0 = win[0] if win else 0.0; a1 = (win[1] if win and win[1] is not None else dur(p))
    c = a1 - a0; r = c / L
    speed = min(r, 1.25) if r >= 1 else max(r, 0.8)       # retime within 0.8x..1.25x
    played = c / speed; pad = max(0.0, L - played)
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    if pad > 0.02:   # hold the last frame but keep a slow push-in going so it never looks frozen
        n = round(L*FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {beat}: {clip} {a0:.2f}-{a1:.2f}s -> beat {L:.2f}s (speed {speed:.2f}x, hold {pad:.2f}s)')
    run(['-ss', f'{a0:.3f}', '-t', f'{c:.3f}', '-i', p, '-vf', vf] + ENC + [f'seg/{beat}.mp4'])

ALL = [b['beat'] for b in TL['beats']]
SEL = sys.argv[1].split(',') if len(sys.argv) > 1 else ALL
assert SEL == ALL[:len(SEL)], 'preview subsets must start at B1 and be contiguous'
T1 = TL['total'] if SEL == ALL else B[SEL[-1]]['end']
tag = 'final' if SEL == ALL else 'preview_' + SEL[-1]
print('Rendering beats', SEL)
prev = None
for b in SEL: seg_clip(b, prev); prev = b
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
    s = max(s, prev_end)   # every word shows >= 0.12 s and never overlaps the previous one (05-build fix)
    nxt = words[i+1][0] if i+1 < len(words) else None
    end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
    end = min(max(end, s + 0.12), T1); prev_end = end
    ev.append(f"Dialogue: 1,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,1000)\\fscx90\\fscy90\\t(0,70,\\fscx100\\fscy100)}}{clean(w)}")
allw = json.load(open('audio/words_tight.json'))
norm = [re.sub(r"[^a-z0-9']", "", w.lower()) for _, _, w in allw]
def find(beat, word, back=0):
    return next(j for j in range(B[beat]['first_word'], len(norm)) if norm[j] == word) - back
# (beat, start word, back, text, end word or None, y, font size or None); positions measured on a 100 px grid over the frames
LABELS = json.load(open('labels.json')) if os.path.exists('labels.json') else [
 ['B3','channel',0,'WATER CHANNEL',None,1440,None], ['B6','these',0,'CISTERNS',None,1300,None],
 ['B12','this',0,'ROCK-CUT\\NARCHITECTURE',None,1330,None], ['B13','indiana',0,'INDIANA JONES AND THE\\NLAST CRUSADE (1989)',None,210,66],
 ['B15','caravan',0,'INCENSE ROUTE',None,1330,None], ['B16','earthquake',0,'363 AD',None,210,None],
 ['B19','six',0,'600 YEARS',None,210,None], ['B20','1812',0,'1812',None,210,None],
 ['B22','treasury',0,'AL-KHAZNEH\\N(THE TREASURY)',None,1480,80]]
for beat, trig, back, text, endw, y, size in LABELS:
    if beat not in SEL: continue
    i = find(beat, trig, back); ls = allw[i][0]
    le = (allw[find(beat, endw)][0] - 0.06) if endw else max(B[beat]['end'] - 0.05, ls + 1.6)
    fs = f"\\fs{size}" if size else ""
    ev.append(f"Dialogue: 0,{ts(ls)},{ts(min(le, T1))},Label,,0,0,0,,{{\\an5\\pos(540,{y}){fs}\\fad(60,120)\\fscx70\\fscy70\\t(0,140,\\fscx100\\fscy100)}}{text}")
# height line: dashed white line up the side of the facade with "39 M" beside it (beats and positions in overlays.json)
OV = json.load(open('overlays.json')) if os.path.exists('overlays.json') else {}
if 'height' in OV:
    d = OV['height']; x, y0, y1 = d['x'], d['y0'], d['y1']
    for beat in d['beats']:
        if beat not in SEL: continue
        s0, s1 = B[beat]['start'] + d.get('delay', 0.0) * (beat == d['beats'][0]), min(B[beat]['end'], T1)
        dash = ''.join(f"m 0 {k} l 6 {k} l 6 {min(k+22, y1-y0)} l 0 {min(k+22, y1-y0)} " for k in range(0, int(y1-y0), 36))
        fad = '\\fad(120,0)' if beat == d['beats'][0] else ('\\fad(0,120)' if beat == d['beats'][-1] else '')
        ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Shape,,0,0,0,,{{\\an7\\pos({x-3},{y0}){fad}\\p1}}{dash}{{\\p0}}")
        for yy in (y0, y1):   # end ticks
            ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Shape,,0,0,0,,{{\\an7\\pos({x-22},{yy-3}){fad}\\p1}}m 0 0 l 44 0 l 44 6 l 0 6{{\\p0}}")
        ev.append(f"Dialogue: 0,{ts(s0)},{ts(s1)},Label,,0,0,0,,{{\\an6\\pos({d['label_x']},{d['label_y']}){fad}}}{d['text']}")
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
