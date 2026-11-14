# Video 07 (P4, 1959 car vs 2009 car, Classic look, one arena in one main view). Assemble: segments -> clean master -> audio ->
# ALL CAPS labels + scoreboard counters + one-word captions. Runs locally (ffmpeg with libass). Work dir layout: timeline.json,
# audio/narration_tight.wav, audio/words_tight.json (07-timing.py), clips/C<n>.mp4, stills/<KEY>.png, fonts/HBXCaption.ttf +
# fonts/HBXLabel.ttf (Fredoka 700 / Montserrat 800, families renamed), labels.json (07-labels.json).
# Usage: python3 07-build.py [B4]  (optional last beat: renders B1..B4 -> out/preview_B4.mp4; none -> out/final.mp4)
# New in 07: a segment can span several beats (one clip carries B2+B3, B6+B7, B10+B11, B14+B15), labels take an x position
# (the cars fill the middle of the frame, so labels sit in the side margins or on the red car's roof), counters roll a number up,
# and captions sit at y 1330 on the old car's trunk instead of 1000 (the impact point is at mid-frame).
import json, os, subprocess, re, sys
W, H, FPS = 1080, 1920, 24
CAP_Y = 1330
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
for d in ('seg', 'out'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

# (beats, kind, source): clip = kling clip played over the beats (retimed 0.8x-1.25x, then a held last frame with a push-in);
# hold = the last frame of the segment before with a slow push-in; wipe = (from still or 'PREV', to still, transition, move);
# still = (still, move). Moves: in, hold, ('focus', fx, fy) = push-in toward a point given as fractions of the frame.
SEGS = [
 (['B1'], 'clip', 'C1'), (['B2', 'B3'], 'clip', 'C2'), (['B4'], 'hold', None), (['B5'], 'clip', 'C3'),
 (['B6', 'B7'], 'clip', 'C4'), (['B8', 'B9'], 'wipe', ('PREV', 'CAGE', 'fade', 'hold')), (['B10', 'B11'], 'clip', 'C5'),
 (['B12'], 'clip', 'C6'), (['B13'], 'hold', None), (['B14', 'B15'], 'clip', 'C7'), (['B16'], 'hold', None),
 (['B17'], 'wipe', ('PREV', 'COLUMN', 'fade', 'hold')), (['B18'], 'still', ('COLUMN', ('focus', 0.45, 0.58))),
 (['B19'], 'still', ('COLUMN', ('focus', 0.55, 0.30))), (['B20'], 'clip', 'C8'), (['B21'], 'clip', 'C9'),
 (['B22'], 'clip', 'C10'), (['B23'], 'clip', 'C11'),
]
def span(beats): return B[beats[0]]['start'], B[beats[-1]]['end']

def still_chain(secs, move='in'):
    n = max(1, round(secs * FPS)); base = f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
    if isinstance(move, (tuple, list)) and move[0] == 'focus':
        fx, fy = move[1], move[2]; z = f"1.0+0.30*on/{n}"
        x = f"max(0,min(iw-iw/zoom,{fx}*iw-iw/zoom/2))"; y = f"max(0,min(ih-ih/zoom,{fy}*ih-ih/zoom/2))"
    elif move == 'hold': z, x, y = f"1.0+0.02*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    else:                z, x, y = f"1.0+0.06*on/{n}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    return base + f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},trim=duration={secs:.3f},setsar=1"

def last_frame(tag):
    p = f'stills/_last_{tag}.png'
    run(['-sseof', '-0.1', '-i', f'seg/{tag}.mp4', '-frames:v', '1', '-update', '1', p]); return p

def seg_still(tag, L, img_path, move='in'):
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',img_path,'-vf',still_chain(L, move)] + ENC + [f'seg/{tag}.mp4'])

def seg_wipe(tag, L, a_path, b_path, trans='fade', move='hold'):
    t = min(1.2, L * 0.4) if trans == 'fade' else min(0.8, L * 0.35); off = 0.15
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',a_path,'-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}',
         '-i',b_path,'-filter_complex',
         f"[0:v]{still_chain(L+0.2, move)}[a];[1:v]{still_chain(L+0.2, move)}[b];[a][b]xfade=transition={trans}:duration={t:.2f}:offset={off},"
         f"trim=duration={L:.3f},setpts=PTS-STARTPTS[v]",'-map','[v]'] + ENC + [f'seg/{tag}.mp4'])

def seg_clip(tag, L, clip):
    p = f'clips/{clip}.mp4'; c = dur(p); r = c / L
    speed = min(r, 1.25) if r >= 1 else max(r, 0.8)       # retime within 0.8x..1.25x
    played = c / speed; pad = max(0.0, L - played)
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    if pad > 0.02:   # hold the last frame but keep a slow push-in going so it never looks frozen
        n = round(L*FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {tag}: {clip} {c:.2f}s -> {L:.2f}s (speed {speed:.3f}x, hold {pad:.2f}s)')
    run(['-i', p, '-vf', vf] + ENC + [f'seg/{tag}.mp4'])

ALL = [b['beat'] for b in TL['beats']]
LAST = sys.argv[1] if len(sys.argv) > 1 else ALL[-1]
SEL = ALL[:ALL.index(LAST) + 1]
T1 = TL['total'] if LAST == ALL[-1] else B[LAST]['end']
tag = 'final' if LAST == ALL[-1] else 'preview_' + LAST
print('Rendering beats', SEL[0], '->', SEL[-1])
prev = None; tags = []
for beats, kind, src in SEGS:
    if beats[0] not in SEL: break
    assert all(b in SEL for b in beats), f'preview must end on a segment boundary ({beats})'
    s, e = span(beats); L = e - s; t = beats[0]
    if kind == 'clip': seg_clip(t, L, src)
    elif kind == 'hold': print(f'  {t}: hold on {prev}'); seg_still(t, L, last_frame(prev), 'hold')
    elif kind == 'wipe':
        a, b, trans, mv = src; a_path = last_frame(prev) if a == 'PREV' else f'stills/{a}.png'
        print(f'  {t}: {trans} {a} -> {b}'); seg_wipe(t, L, a_path, f'stills/{b}.png', trans, mv)
    elif kind == 'still': print(f'  {t}: still {src[0]} {src[1]}'); seg_still(t, L, f'stills/{src[0]}.png', src[1])
    prev = t; tags.append(t)
with open('seg/list.txt','w') as f:
    for t in tags: f.write(f"file '{t}.mp4'\n")
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
    ev.append(f"Dialogue: 1,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAP_Y})\\fscx90\\fscy90\\t(0,70,\\fscx100\\fscy100)}}{clean(w)}")
allw = json.load(open('audio/words_tight.json'))
norm = [re.sub(r"[^a-z0-9']", "", w.lower()) for _, _, w in allw]
def find(beat, word, back=0):
    return next(j for j in range(B[beat]['first_word'], len(norm)) if norm[j] == word) - back
# labels.json: [beat, start word, end beat (label stays to that beat's end; null = its own beat), text, x, y, size, count]
# count: [from, to, unit] rolls the number up over 0.9 s (the scoreboard); text may hold \N line breaks.
LABELS = json.load(open('labels.json'))
for beat, trig, endbeat, text, x, y, size, count in LABELS:
    if beat not in SEL: continue
    ls = allw[find(beat, trig)][0]
    eb = endbeat or beat; le = min(B[eb]['end'] - 0.05 if eb in SEL else T1, T1)
    st = f"\\an5\\pos({x},{y})\\fs{size}"
    if count:
        a, b, unit = count; steps = 12
        for k in range(steps + 1):
            v = a + (b - a) * k / steps; t0 = ls + 0.9 * k / steps; t1 = ls + 0.9 * (k + 1) / steps if k < steps else le
            num = f"{v:.0f}" if float(b).is_integer() else f"{v:.1f}"
            ev.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},Label,,0,0,0,,{{{st}}}{text.replace('#', num + ' ' + unit)}")
    else:
        ev.append(f"Dialogue: 0,{ts(ls)},{ts(le)},Label,,0,0,0,,{{{st}\\fad(60,120)\\fscx70\\fscy70\\t(0,140,\\fscx100\\fscy100)}}{text}")
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,HBX Caption,116,&H00FFFFFF,&H00FFFFFF,&H00000000,&H8C000000,0,0,0,0,100,100,0,0,1,8,5,5,60,60,0,1
Style: Label,HBX Label,104,&H00FFFFFF,&H00FFFFFF,&H50000000,&H78000000,0,0,0,0,100,100,3,0,1,5,6,5,20,20,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f'out/{tag}.ass','w').write(ass)
run(['-i',f'out/{tag}_clean.mp4','-i',f'out/{tag}_audio.wav','-vf',f'ass=out/{tag}.ass:fontsdir=fonts',
     '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k',
     '-movflags','+faststart','-shortest',f'out/{tag}.mp4'])
print(tag, round(dur(f'out/{tag}.mp4'),2), 's; target', round(T1,2))
