# Video 16: the bed and the effects as the mix uses them, cut from the nine sounds Higgsfield's mirelo_text_to_audio returned
# (22 Nov 2026; 39 s, 9.75 credits; job ids in 16-jobs.tsv). Nothing was listened to: each file was measured (level every
# 50 ms, strongest tones) and cut to the part that is the sound we asked for.
#   python3 16-sound.py <dir with bed.mp3 fx1.mp3 ... fx8.mp3 as downloaded> <work dir>   -> <work dir>/audio/bed.mp3, fx1..fx8.mp3
# What came back, and what is kept:
#   bed  16 s  steady at -22 dB for 10 s, then 5 dB louder: the first 10 s, made into a seamless loop (a 1 s crossfade of its
#              end into its start), so the level doesn't step every time it repeats
#   fx1   2 s  "bulbs ticking on": one click at 0 s and nothing else -> the click repeated ten times, closer and closer
#   fx2   2 s  "the breaker": four clunks (0.15, 1.0, 1.3, 1.85 s) -> the first one, 0.10-0.60 s
#   fx3   7 s  rain: a steady hiss, as asked -> whole, faded in and out
#   fx4   1 s  a click at 0 s -> 0-0.2 s (the outlet, the boxes, the injection joint and, quieter, the counter's tick)
#   fx5   3 s  "a glassy shimmer": low thumps at 70-90 Hz, not a shimmer -> left out
#   fx6   3 s  "a muffled thump and a howl": a 62 Hz thump for 1 s, no howl -> the thump, 0-1.0 s
#   fx7   3 s  "a car radio tuning in": faint static -> 0-1.5 s
#   fx8   2 s  the till: bell hits at 0.25, 1.4 and 1.9 s -> the first, 0.20-1.25 s
import subprocess, sys
import numpy as np
SRC, WORK = sys.argv[1], sys.argv[2]; SR = 44100
def load(k):
    return np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',f'{SRC}/{k}.mp3','-ac','1','-ar',str(SR),'-f','f32le','-'],
                                        capture_output=True).stdout, np.float32).astype(np.float64)
def save(k, a):
    a = np.clip(a, -1, 1).astype(np.float32)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-b:a','192k',f'{WORK}/audio/{k}.mp3'],
                   input=a.tobytes(), check=True)
    print(f'  {k}: {len(a) / SR:.2f} s')
def fade(a, fin=0.01, fout=0.05):
    a = a.copy(); n1, n2 = int(fin * SR), int(fout * SR)
    if n1: a[:n1] *= np.linspace(0, 1, n1)
    if n2: a[-n2:] *= np.linspace(1, 0, n2)
    return a
def cut(a, t0, t1): return a[int(t0 * SR):int(t1 * SR)]

b = cut(load('bed'), 0.3, 9.8); X = SR                       # a seamless loop: the end cross-fades into the start
loop = b[X:].copy(); w = np.linspace(0, 1, X); loop[-X:] = loop[-X:] * np.sqrt(1 - w) + b[:X] * np.sqrt(w)
save('bed', loop)
c = fade(cut(load('fx1'), 0.0, 0.12), 0.0, 0.03)              # ten ticks, closer and closer, a little uneven
times = [0.0, 0.16, 0.30, 0.42, 0.53, 0.62, 0.70, 0.77, 0.83, 0.88]; gains = [1.0, 0.8, 0.9, 0.75, 0.95, 0.8, 0.9, 0.7, 0.85, 1.0]
out = np.zeros(int(1.05 * SR))
for t, g in zip(times, gains): i = int(t * SR); out[i:i + len(c)] += c * g
save('fx1', out)
save('fx2', fade(cut(load('fx2'), 0.10, 0.60), 0.005, 0.12))
save('fx3', fade(load('fx3'), 0.6, 1.2))
save('fx4', fade(cut(load('fx4'), 0.0, 0.20), 0.0, 0.05))
save('fx6', fade(cut(load('fx6'), 0.0, 1.0), 0.0, 0.25))
save('fx7', fade(cut(load('fx7'), 0.0, 1.5), 0.0, 0.4))
save('fx8', fade(cut(load('fx8'), 0.20, 1.25), 0.005, 0.25))
