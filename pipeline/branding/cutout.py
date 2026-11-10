#!/usr/bin/env python3
"""Cut the mascot out of his plain studio backdrop (free, no credits).

    python3 cutout.py mascot.png mascot_rgba.png [preview.png]

Works on the locked mascot reference (seedream job f97004b9-..., 832x1248, warm sand backdrop with a vertical
gradient). Steps: model the backdrop colour row by row from the image's left and right margins, threshold the
colour difference for a rough mask, refine it with OpenCV GrabCut, keep the largest blob, then build a soft alpha
from the colour difference in a thin band along the edge and remove the sand colour from the edge pixels so no
beige halo shows on a new background. Needs numpy, Pillow and opencv-python-headless.
"""
import sys

import cv2
import numpy as np
from PIL import Image


def backdrop_model(lab, margin=60):
    """Per-row backdrop colour, interpolated between the median of the left and right margins."""
    h, w, _ = lab.shape
    left = np.median(lab[:, :margin, :], axis=1)            # (h, 3)
    right = np.median(lab[:, w - margin:, :], axis=1)        # (h, 3)
    # smooth along y so noise in the backdrop texture doesn't leak in
    left = cv2.GaussianBlur(left.reshape(h, 1, 3), (1, 61), 0).reshape(h, 3)
    right = cv2.GaussianBlur(right.reshape(h, 1, 3), (1, 61), 0).reshape(h, 3)
    t = np.linspace(0.0, 1.0, w).reshape(1, w, 1)
    return left.reshape(h, 1, 3) * (1 - t) + right.reshape(h, 1, 3) * t


def main(src, dst, preview=None):
    rgb = np.array(Image.open(src).convert("RGB"))
    h, w, _ = rgb.shape
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    lab[..., 0] *= 100.0 / 255.0
    lab[..., 1:] -= 128.0
    bg = backdrop_model(lab)
    de = np.sqrt(((lab - bg) ** 2).sum(axis=2))
    de = cv2.GaussianBlur(de, (3, 3), 0)

    rough = (de > 14).astype(np.uint8)
    rough = cv2.morphologyEx(rough, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lbl, stats, _ = cv2.connectedComponentsWithStats(rough, 8)
    keep = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    rough = (lbl == keep).astype(np.uint8)

    gc = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
    near = cv2.dilate(rough, np.ones((41, 41), np.uint8))
    gc[near == 0] = cv2.GC_BGD
    gc[rough == 1] = cv2.GC_PR_FGD
    core = cv2.erode(rough, np.ones((15, 15), np.uint8))
    gc[(core == 1) & (de > 22)] = cv2.GC_FGD
    bgm = np.zeros((1, 65), np.float64)
    fgm = np.zeros((1, 65), np.float64)
    cv2.grabCut(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), gc, None, bgm, fgm, 6, cv2.GC_INIT_WITH_MASK)
    hard = np.isin(gc, (cv2.GC_FGD, cv2.GC_PR_FGD)).astype(np.uint8)

    n, lbl, stats, _ = cv2.connectedComponentsWithStats(hard, 8)
    keep = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    hard = (lbl == keep).astype(np.uint8)
    # fill holes (e.g. the gap between arm and body stays open because it touches the backdrop)
    inv = (1 - hard).astype(np.uint8)
    n, lbl, stats, _ = cv2.connectedComponentsWithStats(inv, 4)
    for i in range(1, n):
        x, y, bw, bh, area = stats[i]
        touches = x == 0 or y == 0 or x + bw == w or y + bh == h
        if not touches and area < 400:
            hard[lbl == i] = 1

    # Skin is close to the sand colour, and the backdrop right next to the body is a little darker than at the
    # margins, so GrabCut keeps thin strips of backdrop along the neck and arms. Estimate the backdrop locally
    # (normalised blur of the pixels just outside the figure) and drop edge pixels that match it.
    outside = (1 - cv2.dilate(hard, np.ones((9, 9), np.uint8))).astype(np.float32)
    num = cv2.GaussianBlur(lab * outside[..., None], (0, 0), 12)
    den = cv2.GaussianBlur(outside, (0, 0), 12)[..., None]
    local = np.where(den > 1e-3, num / np.maximum(den, 1e-3), bg)
    de_local = np.sqrt(((lab - local) ** 2).sum(axis=2))
    rim = hard & (1 - cv2.erode(hard, np.ones((21, 21), np.uint8)))
    hard[(rim == 1) & (de_local < 10)] = 0
    hard = cv2.morphologyEx(hard, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lbl, stats, _ = cv2.connectedComponentsWithStats(hard, 8)
    keep = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    hard = (lbl == keep).astype(np.uint8)
    inv = (1 - hard).astype(np.uint8)
    n, lbl, stats, _ = cv2.connectedComponentsWithStats(inv, 4)
    for i in range(1, n):
        x, y, bw, bh, area = stats[i]
        if not (x == 0 or y == 0 or x + bw == w or y + bh == h) and area < 2000:
            hard[lbl == i] = 1
    hard = (cv2.GaussianBlur(hard.astype(np.float32), (5, 5), 1.0) > 0.5).astype(np.uint8)   # smooth stair steps

    # soft alpha: inside the hard mask = 1, outside = 0, in a 2 px band use the local colour difference
    band = cv2.dilate(hard, np.ones((5, 5), np.uint8)) - cv2.erode(hard, np.ones((5, 5), np.uint8))
    soft = np.clip((de_local - 5.0) / 12.0, 0.0, 1.0)
    alpha = hard.astype(np.float32)
    alpha[band == 1] = soft[band == 1]
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0.6)
    alpha[(band == 0) & (hard == 1)] = 1.0
    alpha[(band == 0) & (hard == 0)] = 0.0

    # remove the sand colour from semi-transparent edge pixels: F = (C - (1 - a) * B) / a
    bg = local
    bg_rgb = cv2.cvtColor(np.clip(np.dstack([bg[..., 0] * 255 / 100, bg[..., 1] + 128, bg[..., 2] + 128]), 0, 255)
                          .astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)
    a3 = alpha[..., None]
    fg = rgb.astype(np.float32)
    edge = (alpha > 0.04) & (alpha < 0.98)
    fixed = (fg - (1 - a3) * bg_rgb) / np.maximum(a3, 0.04)
    fg[edge] = np.clip(fixed[edge], 0, 255)

    out = np.dstack([fg, alpha * 255]).astype(np.uint8)
    Image.fromarray(out, "RGBA").save(dst)
    ys, xs = np.where(alpha > 0.5)
    print(f"saved {dst}: subject box x {xs.min()}-{xs.max()}, y {ys.min()}-{ys.max()}")
    if preview:
        # check on a dark blue and on a bright magenta ground, where any halo shows up
        tiles = []
        for col in ((31, 78, 140), (230, 40, 160)):
            ground = Image.new("RGBA", (w, h), col + (255,))
            ground.alpha_composite(Image.fromarray(out, "RGBA"))
            tiles.append(ground.convert("RGB"))
        sheet = Image.new("RGB", (w * 2, h))
        sheet.paste(tiles[0], (0, 0))
        sheet.paste(tiles[1], (w, 0))
        sheet.save(preview)


if __name__ == "__main__":
    main(*sys.argv[1:4])
