# Runs in the Higgsfield sandbox (v02/). Assemble video 02 (outrigger canoe): beats -> clean master -> audio -> labels + one-word captions.
# Usage: python3 build02.py [B1,B2,B3]  (optional contiguous beat subset from B1 -> out/preview_<last>.mp4; no argument -> out/final.mp4)
# Inputs: timeline.json + audio/narration_tight.wav + audio/words_tight.json (02-timing.py), clips/<beat>.mp4 (falls back to the
# beat's start still with a push-in), stills/*.png, fonts/HBXCaption.ttf + fonts/HBXLabel.ttf.
import json, os, subprocess, re, sys
W, H, FPS = 1080, 1920, 24
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def still_chain(secs, z0=1.0, z1=1.07):
    n = max(1, round(secs * FPS)); zx = f"{z0}+({z1}-{z0})*on/{n}"
    return (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='{zx}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},trim=duration={secs:.3f},setsar=1")
def seg_still(beat, img):
    L = B[beat]['len']
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{img}.png','-vf',still_chain(L)] + ENC + [f'seg/{beat}.mp4'])
def seg_clip(beat, fallback):
    L = B[beat]['len']; p = f'clips/{beat}.mp4'
    if not os.path.exists(p):
        print(f'  {beat}: no clip -> still fallback ({fallback})'); return seg_still(beat, fallback)
    c = dur(p); r = c / L
    speed = min(r, 1.25) if r >= 1 else max(r, 0.8)       # retime within 0.8x..1.25x
    played = c / speed; pad = max(0.0, L - played)
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    if pad > 0.02:   # hold the last frame but keep a slow push-in going so it never looks frozen
        n = round(L*FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {beat}: clip {c:.2f}s -> beat {L:.2f}s (speed {speed:.2f}x, hold {pad:.2f}s)')
    run(['-i', p, '-vf', vf] + ENC + [f'seg/{beat}.mp4'])
START = {'B1':'S0','B2':'S1','B3':'FIRE','B4':'S2','B5':'TIP','B6':'STEAM','B7':'CRACK','B8':'SINK','B9':'LAKEBED','B10':'WAVES',
         'B11':'S3','B12':'CROC','B13':'CAPSIZE','B14':'S4','B15':'STORM','B16':'PAYOFF','B17':'S5'}
ALL = [b['beat'] for b in TL['beats']]
SEL = sys.argv[1].split(',') if len(sys.argv) > 1 else ALL
assert SEL == ALL[:len(SEL)], 'preview subsets must start at B1 and be contiguous'
T0, T1 = 0.0, (TL['total'] if SEL == ALL else B[SEL[-1]]['end'])
tag = 'final' if SEL == ALL else 'preview_' + SEL[-1]
print('Rendering beats', SEL)
for b in SEL: seg_clip(b, START[b])
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
ev = []
for i, (s, e, w) in enumerate(words):
    nxt = words[i+1][0] if i+1 < len(words) else None
    end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
    end = min(max(end, s + 0.12), T1)
    ev.append(f"Dialogue: 1,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,1000)\\fscx90\\fscy90\\t(0,70,\\fscx100\\fscy100)}}{clean(w)}")
allw = json.load(open('audio/words_tight.json'))
norm = [re.sub(r"[^a-z0-9']", "", w.lower()) for _, _, w in allw]
def find(beat, word, back=0):
    return next(j for j in range(B[beat]['first_word'], len(norm)) if norm[j] == word) - back
# (beat, start word, back, text, end word or None)
LABELS = [('B4','dugout',3,'DUGOUT','almost'), ('B4','almost',0,'10,000 YEARS',None), ('B11','washstrakes',2,'WASHSTRAKES',None),
          ('B13','eight',0,'800 A DAY',None), ('B14','outrigger',3,'OUTRIGGER',None)]
for beat, trig, back, text, endw in LABELS:
    if beat not in SEL: continue
    i = find(beat, trig, back); ls = allw[i][0]
    le = (allw[find(beat, endw)][0] - 0.06) if endw else max(B[beat]['end'] - 0.05, ls + 1.6)
    ev.append(f"Dialogue: 0,{ts(ls)},{ts(min(le, T1))},Label,,0,0,0,,{{\\an5\\pos(540,560)\\fad(60,120)\\fscx70\\fscy70\\t(0,140,\\fscx100\\fscy100)}}{text}")
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

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f'out/{tag}.ass','w').write(ass)
run(['-i',f'out/{tag}_clean.mp4','-i',f'out/{tag}_audio.wav','-vf',f'ass=out/{tag}.ass:fontsdir=fonts',
     '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k',
     '-movflags','+faststart','-shortest',f'out/{tag}.mp4'])
print(tag, round(dur(f'out/{tag}.mp4'),2), 's; target', round(T1,2))
