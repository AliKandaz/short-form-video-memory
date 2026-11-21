#!/usr/bin/env python3
"""Speech to text on this machine, with a time for every word: for studying other people's videos and for our own word timings.
Written 21 Nov 2026 (CLAUDE.md 7.7, 12.5): huggingface is blocked from a session, GitHub release downloads are not.

    PYTHONPATH=<dir with sherpa_onnx and numpy> python3 transcribe.py <model_dir> <out_dir> <audio or video files...>

One-time setup (about 30 s):
    pip install --target <dir> sherpa-onnx numpy
    curl -L -o parakeet.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8.tar.bz2
    tar xjf parakeet.tar.bz2          # <model_dir> = the folder it makes (encoder, decoder, joiner, tokens; about 650 MB)

For each input it writes <out_dir>/<name>.json: {"text": punctuated text, "words": [[start_seconds, word], ...], "dur": seconds}
and prints the word count and pace. A 70 s narration takes about 5 s on 4 cores. English only. Nothing leaves the machine.
It gives each word's start only. Our timing scripts read [start, end, word] from Whisper, so for our own narration this is the
fallback, not the default (CLAUDE.md 6.2 Step 6).
Needs ffmpeg on PATH.
"""
import json
import os
import subprocess
import sys
import time

import numpy as np
import sherpa_onnx

SR = 16000


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    model, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    rec = sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=f"{model}/encoder.int8.onnx", decoder=f"{model}/decoder.int8.onnx", joiner=f"{model}/joiner.int8.onnx",
        tokens=f"{model}/tokens.txt", num_threads=4, sample_rate=SR, feature_dim=80, decoding_method="greedy_search",
        model_type="nemo_transducer")
    for path in sys.argv[3:]:
        x, t0 = load(path), time.time()
        pos, toks, times = 0, [], []
        while pos < len(x):                       # pieces of at most 40 s, cut at the quietest point near the boundary
            end = min(len(x), pos + 40 * SR)
            if end < len(x):
                lo, win, hop = end - 6 * SR, int(0.2 * SR), int(0.05 * SR)
                energy = [float(np.mean(x[i:i + win] ** 2)) for i in range(lo, end - win, hop)]
                end = lo + int(np.argmin(energy)) * hop + win // 2
            s = rec.create_stream()
            s.accept_waveform(SR, x[pos:end])
            rec.decode_stream(s)
            toks += list(s.result.tokens)
            times += [t + pos / SR for t in s.result.timestamps]
            pos = end
        words = []
        for tok, tm in zip(toks, times):          # a leading space or "▁" starts a new word
            if tok.startswith(" ") or tok.startswith("▁") or not words:
                words.append([round(float(tm), 2), tok.strip().lstrip("▁")])
            else:
                words[-1][1] += tok
        words = [w for w in words if w[1]]
        dur = len(x) / SR
        name = os.path.splitext(os.path.basename(path))[0]
        json.dump({"text": " ".join(w[1] for w in words), "words": words, "dur": round(dur, 2)},
                  open(os.path.join(out, name + ".json"), "w"))
        print(f"{name}: {len(words)} words in {dur:.1f} s = {len(words) / max(dur, 0.1):.2f} words a second "
              f"(done in {time.time() - t0:.1f} s)", flush=True)


if __name__ == "__main__":
    main()
