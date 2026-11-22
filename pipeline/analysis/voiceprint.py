#!/usr/bin/env python3
"""Is it the same voice? A voice print, the median pitch, the pitch range and the brightness of each audio file.
Written 22 Nov 2026 (CLAUDE.md 7.5), when Higgsfield's preset "Marcus" had to be checked against ElevenLabs' "Marcus": the
names matched and the voices didn't.

    python3 voiceprint.py <campplus model .onnx> <out.json> <audio files...>

The model is the 3D-Speaker CAM++ speaker model from the sherpa-onnx GitHub releases (30 MB; GitHub releases are reachable):
    curl -L -o campplus_en.onnx https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/3dspeaker_speech_campplus_sv_en_voxceleb_16k.onnx
It needs only ffmpeg, numpy and onnxruntime (Kaldi-style filter-bank features are computed here in numpy), so the same file
runs on this machine and in the Higgsfield sandbox, where the preset voices' preview files can be fetched; the numbers then
compare. out.json holds, per file: dur (s), pitch (median, Hz), range_st (10th to 90th percentile, semitones), centroid
(brightness, Hz) and emb (512 numbers, length 1). The cosine of two emb vectors is the likeness.

How to read the likeness (measured 22 Nov 2026): two takes of one voice scored 0.80-0.81; two different American men of
similar pitch (ElevenLabs' Marcus and Todd) 0.75-0.81, so a high score does not prove one voice; a man against a woman
0.05-0.23. Higgsfield's "Marcus" against ElevenLabs' "Marcus" scored 0.59-0.62, lower than Marcus against Todd: not the same
voice. Previews of under about 5 s give noisy numbers. Nothing is listened to; a voice is still chosen by the user's ear.
"""
import json, subprocess, sys, numpy as np, onnxruntime as ort
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',p,'-ac','1','-ar','16000','-f','f32le','-'], capture_output=True).stdout, np.float32).astype(np.float64)
def fbank(w, sr=16000, nm=80, N=400, hop=160, nfft=512, lo=20.0, hi=8000.0):
    n = 1 + (len(w) - N) // hop; idx = np.arange(N)[None, :] + hop * np.arange(n)[:, None]; fr = w[idx] * 32768.0
    fr = fr - fr.mean(1, keepdims=True); fr = np.concatenate([fr[:, :1] * (1 - 0.97), fr[:, 1:] - 0.97 * fr[:, :-1]], 1)
    fr = fr * (0.5 - 0.5 * np.cos(2 * np.pi * np.arange(N) / (N - 1))) ** 0.85
    P = np.abs(np.fft.rfft(fr, nfft)) ** 2
    mel = lambda f: 1127.0 * np.log(1 + f / 700.0); pts = np.linspace(mel(lo), mel(hi), nm + 2); fm = mel(np.arange(nfft // 2 + 1) * sr / nfft)
    FB = np.zeros((nm, nfft // 2 + 1))
    for m in range(nm):
        l, c, r = pts[m], pts[m + 1], pts[m + 2]; FB[m] = np.clip(np.minimum((fm - l) / (c - l), (r - fm) / (r - c)), 0, None)
    F = np.log(np.maximum(P @ FB.T, 1e-10)); return (F - F.mean(0)).astype(np.float32)
def pitch(a, sr=16000):
    f0 = []; n = int(0.04 * sr); hop = int(0.01 * sr)
    for i in range(0, len(a) - n, hop):
        x = a[i:i+n]
        if np.sqrt((x**2).mean()) < 0.02: continue
        x = x - x.mean(); ac = np.correlate(x, x, 'full')[n-1:]; lo, hi = sr // 400, sr // 70; k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.5 * ac[0]: f0.append(sr / k)
    f0 = np.array(f0) if f0 else np.array([0.0, 0.0])
    return float(np.median(f0)), float(12 * np.log2(max(np.percentile(f0, 90), 1) / max(np.percentile(f0, 10), 1)))
def centroid(a, sr=16000):   # brightness: spectral centroid of the loud frames, Hz
    n = 512; fr = a[:len(a) // n * n].reshape(-1, n); e = np.sqrt((fr**2).mean(1)); fr = fr[e > 0.3 * e.max()]
    S = np.abs(np.fft.rfft(fr * np.hanning(n), n)); f = np.arange(n // 2 + 1) * sr / n; return float((S * f).sum() / S.sum())
sess = ort.InferenceSession(sys.argv[1], providers=['CPUExecutionProvider']); inp = sess.get_inputs()[0].name; out = {}
for p in sys.argv[3:]:
    a = load(p); e = sess.run(None, {inp: fbank(a)[None]})[0][0]; e = e / np.linalg.norm(e); med, rng = pitch(a)
    out[p.split('/')[-1]] = {"dur": round(len(a) / 16000, 2), "pitch": round(med, 1), "range_st": round(rng, 1), "centroid": round(centroid(a)), "emb": [round(float(x), 4) for x in e]}
json.dump(out, open(sys.argv[2], 'w')); print('wrote', len(out))
