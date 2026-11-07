# Assemble video 01 (desert adobe): beats -> clean master -> audio -> labels + one-word captions.
# Usage: python3 build.py            (uses clips/<beat>.mp4 when present, else falls back to the start still)
import json, os, subprocess, re
W, H, FPS = 1080, 1920, 24
os.makedirs('seg', exist_ok=True); os.makedirs('out', exist_ok=True)
TL = json.load(open('timeline.json')); B = {b['beat']: b for b in TL['beats']}
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']

def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

def still_chain(label, secs, z0=1.0, z1=1.07, pan=False):
    n = max(1, round(secs * FPS))
    zx = f"{z0}+({z1}-{z0})*on/{n}"
    x = f"(iw-iw/zoom)*on/{n}" if pan else "iw/2-(iw/zoom/2)"
    return (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='{zx}':x='{x}':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},trim=duration={secs:.3f},setsar=1")

def seg_still(beat, img, pan=False):
    L = B[beat]['len']
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{img}.png','-vf',still_chain('a',L,pan=pan)] + ENC + [f'seg/{beat}.mp4'])

def seg_wipe(beat, a, b, trans):
    L = B[beat]['len']; td = max(0.5, min(0.9, L*0.3)); off = (L - td) / 2
    fc = (f"[0:v]{still_chain('a', L, 1.0, 1.05)}[a];[1:v]{still_chain('b', L, 1.0, 1.05)}[b];"
          f"[a][b]xfade=transition={trans}:duration={td:.3f}:offset={off:.3f},trim=duration={L:.3f}[v]")
    run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{a}.png',
         '-loop','1','-framerate',str(FPS),'-t',f'{L+0.2:.3f}','-i',f'stills/{b}.png','-filter_complex',fc,'-map','[v]'] + ENC + [f'seg/{beat}.mp4'])

def seg_clip(beat, clip, fallback):
    L = B[beat]['len']; p = f'clips/{clip}.mp4'
    if not os.path.exists(p):
        print(f'  {beat}: clip missing -> still fallback ({fallback})'); return seg_still(beat, fallback)
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

PLAN = [('B1','clip','B1','S0'),('B2','still','S1HEAT'),('B3','clip','B3','BRICK'),('B4','pan','DRYING'),
        ('B5','wipe','S2','S3','wipeup'),('B6','still','CUTAWAY'),('B7','still','NIGHT'),('B8','clip','B8','S3'),
        ('B9','clip','B9','STORM'),('B10a','clip','B10a','CANALE'),('B10b','still','STONE'),('B11','wipe','S5','S6','wiperight'),
        ('B12','clip','B12','FLOOD'),('B13','clip','B13','PAYOFF'),('B14','clip','B14','END')]
print('Rendering beats...')
for p in PLAN:
    k = p[1]
    if k == 'clip': seg_clip(p[0], p[2], p[3])
    elif k == 'still': seg_still(p[0], p[2])
    elif k == 'pan': seg_still(p[0], p[2], pan=True)
    elif k == 'wipe': seg_wipe(p[0], p[2], p[3], p[4])
with open('seg/list.txt','w') as f:
    for p in PLAN: f.write(f"file '{p[0]}.mp4'\n")
run(['-f','concat','-safe','0','-i','seg/list.txt','-c','copy','out/video_clean.mp4'])

# Audio: narration + tail, loudness-normalised for TikTok
T = TL['total']
run(['-i','audio/narration_tight.wav','-af',f'apad=whole_dur={T:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000',
     '-ac','2','-c:a','pcm_s16le','out/audio_final.wav'])

# Captions (one word, centred ~52%) + labels (ALL CAPS, upper third)
words = json.load(open('audio/words_tight.json'))
def ts(t):
    t = max(0, t); h = int(t//3600); m = int(t%3600//60); s = t%60
    return f"{h}:{m:02d}:{s:05.2f}"
def clean(w):
    w = re.sub(r"[^A-Za-z0-9'’\-]", "", w)
    return w[:1].upper() + w[1:]
ev = []
for i, (s, e, w) in enumerate(words):
    nxt = words[i+1][0] if i+1 < len(words) else None
    end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
    end = max(end, s + 0.12)
    ev.append(f"Dialogue: 1,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,1000)\\fscx90\\fscy90\\t(0,70,\\fscx100\\fscy100)}}{clean(w)}")
script = [re.sub(r"[^a-z0-9']", "", w.lower()) for _, _, w in words]
LABELS = [('B2','hundred','100°F+',0),('B3','adobe','ADOBE',2),('B5','two','2 FT',0),('B6','thermal','THERMAL MASS',2),
          ('B9','three','3 OUT OF 4',0),('B10a','canale','CANALE',3),('B10b','stone','STONE BASE',0)]
for beat, trig, text, back in LABELS:
    i = next(j for j in range(B[beat]['first_word'], len(script)) if script[j] == trig) - back
    lend = max(B[beat]['end'] - 0.05, words[i][0] + 1.6)
    ev.append(f"Dialogue: 0,{ts(words[i][0])},{ts(lend)},Label,,0,0,0,,"
              f"{{\\an5\\pos(540,560)\\fad(60,120)\\fscx70\\fscy70\\t(0,140,\\fscx100\\fscy100)}}{text}")
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
open('out/captions.ass','w').write(ass)
run(['-i','out/video_clean.mp4','-i','out/audio_final.wav','-vf','ass=out/captions.ass:fontsdir=fonts',
     '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k',
     '-movflags','+faststart','-shortest','out/final.mp4'])
print('final', round(dur('out/final.mp4'),2), 's; clean', round(dur('out/video_clean.mp4'),2), 's; target', T)
