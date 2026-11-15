#!/usr/bin/env python3
"""What sits under the narration of a video: nothing, a steady bed, or separate sounds?

    python3 under_the_voice.py <video.mp4> [more videos...] [--sheet spectrograms.jpg]

It measures; it does not listen. For each video it prints
- how far the mix drops in the quietest moments, compared with the voice (a dry voice drops 30 dB or more;
  a bed holds the pauses within about 20 dB of the voice);
- the side channel (left minus right) against the whole mix. A narrator is mixed to the centre, so the side
  channel is what is left when the voice cancels: the bed, music and effects. Below about -45 dB the track is
  mono and there is nothing but the voice;
- how much of the time that non-voice sound is present, and how many separate bursts it has. Present nearly
  all the time with few bursts is a bed; present a third of the time in many bursts is separate effects.
--sheet also writes spectrograms of the side channel, one row per video: an even grey texture is a bed,
horizontal lines are music or a tone, bright vertical stripes are effects.

Measured 15 Nov 2026 (CLAUDE.md 7.5)
  ours 03, 04                   voice only: mono, quietest moments 37-42 dB below the voice
  @1hidden_by_design (3)        a steady bed: present 71-93% of the time, quietest moments 19-20 dB below the voice
  @howbuildingexplained (2)     no bed: short quiet sounds in the gaps, present 34-39% of the time in 44-91 bursts
  @thewhatifstudio (2)          music or drones and effects, loud: side channel only 11 dB below the mix
The one-line verdict cannot tell a bed from music; look at the --sheet spectrograms for that.

Needs ffmpeg on PATH and: pip install numpy pillow
"""
import argparse
import subprocess

import numpy as np

SR = 16000


def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32).reshape(-1, 2) / 32768


def env_db(x, win):
    n = len(x) // win
    return 20 * np.log10(np.sqrt((x[:n * win].reshape(n, win) ** 2).mean(1) + 1e-12))


def spectrogram(x, n=1024, hop=400):
    fr = 1 + (len(x) - n) // hop
    idx = np.arange(n)[None, :] + hop * np.arange(fr)[:, None]
    return np.abs(np.fft.rfft(x[idx] * np.hanning(n), axis=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('videos', nargs='+'); ap.add_argument('--sheet')
    a = ap.parse_args()
    rows = []
    for path in a.videos:
        x = load(path); mid = x.mean(1); side = (x[:, 0] - x[:, 1]) / 2
        win = int(0.05 * SR)
        core = slice(int(1 / 0.05), -int(2 / 0.05))                      # skip the head and the tail
        em, es = env_db(mid, win)[core], env_db(side, win)[core]
        gap = np.percentile(em, 90) - np.percentile(em, 3)
        side_rel = 10 * np.log10((side ** 2).mean() / max((mid ** 2).mean(), 1e-12) + 1e-12)
        stereo = side_rel > -45
        if stereo:
            present = 100 * float((es > np.percentile(es, 95) - 20).mean())
            thr = np.median(es) + 12
            bursts, i = 0, 1
            while i < len(es):
                if es[i] > thr and es[i - 1] <= thr:
                    bursts += 1; i += 8
                else:
                    i += 1
            kind = ('a steady bed' if present > 75 else 'separate sounds, no steady bed' if present < 50 else 'a bed with gaps')
            print(f'{path}: quietest moments {gap:.0f} dB below the voice; side channel {side_rel:.0f} dB below the mix; '
                  f'non-voice sound present {present:.0f}% of the time in {bursts} bursts: {kind}')
        else:
            print(f'{path}: quietest moments {gap:.0f} dB below the voice; mono (side channel {side_rel:.0f} dB): voice only')
        if a.sheet:
            M = spectrogram(side if stereo else mid)[:, :int(5000 / (SR / 1024))]
            ref = np.percentile(20 * np.log10(spectrogram(mid) + 1e-6), 99.5)
            img = np.clip((20 * np.log10(M + 1e-6) - (ref - 70)) / 70, 0, 1)
            rows.append((path + ('  (side channel)' if stereo else '  (mono: the voice itself)'), (255 * img.T[::-1]).astype(np.uint8)))
    if a.sheet and rows:
        from PIL import Image, ImageDraw
        sheet = Image.new('RGB', (1520, 10 + len(rows) * 190), (250, 250, 248)); d = ImageDraw.Draw(sheet)
        for k, (label, img) in enumerate(rows):
            y = 8 + k * 190
            d.text((10, y), label, fill=(20, 20, 20))
            im = Image.fromarray(img).resize((1500, 150))
            sheet.paste(Image.merge('RGB', (im, im, im)), (10, y + 26))
        sheet.save(a.sheet, quality=88); print(a.sheet)


if __name__ == '__main__':
    main()
