# Gate C sheets for video 18: the stage ladder in playing order with what changed from each picture to the next, the tester
# against its key, and the first and last frames. Free; reads <scratch>/v18/stills.
import cv2, numpy as np, sys, json
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/tmp/claude-0/-home-user-short-form-video-memory/c916d411-dad6-5b75-ab84-87c4db23dfd2/scratchpad/bin'); import cutlib as C
D = '/tmp/claude-0/-home-user-short-form-video-memory/c916d411-dad6-5b75-ab84-87c4db23dfd2/scratchpad/v18/'
LADDER = [  # key, view, what it shows, the clip that ends on it
 ('S0', 'stage', 'frame 0: hull on blocks, pickup pulling', ''),
 ('H', 'stage', 'hook ends: truck dug in, slewed', 'HOOK'),
 ('F1', 'stage', 'fail 1: rope snapped, truck gone', 'FC1'),
 ('S1_1', 'stage', 'piles', 'W1_1 "piles"'),
 ('S1_2', 'stage', 'rails', 'W1_2 "rails"'),
 ('S1_3', 'stage', 'cradle', 'W1_3 "cradle"'),
 ('S1_4', 'stage', 'hull on the cradle', 'W1_4 "hull"'),
 ('F2', 'stage', 'fail 2: crept onto the barbecue', 'FC2'),
 ('CV2_0', 'close', 'cut in: the cradle\'s back corner', ''),
 ('CV2_1', 'close', 'trigger pile', 'W2_1 "pile"'),
 ('CV2_2', 'close', 'iron hook', 'W2_2 "hook"'),
 ('CV2_3', 'close', 'release lever', 'W2_3 "lever"'),
 ('S2_T', 'stage', 'cut back: the trigger holds it', ''),
 ('F3', 'stage', 'fail 3: set free, through the dock', 'FC3'),
 ('S3_1', 'stage', 'winched back up the rails', 'W3_1 "rails"'),
 ('S3_2', 'stage', 'two heaps of chain, wired on', 'W3_2 "chain"'),
 ('S3_3', 'stage', 'two more heaps', 'W3_3 "heaps"'),
 ('S3_L', 'stage', 'the launch that works', 'W3_L'),
 ('CV4U', 'close', 'cut in: afloat, hatch open', ''),
 ('CV4_0', 'close', 'fail 4: it leans, the deck floods', 'FC4'),
 ('CV4_1', 'close', 'a row of iron blocks', 'W4_1 "blocks"'),
 ('CV4_2', 'close', 'a second row', 'W4_2 "row"'),
 ('CV4_3', 'close', 'hatch cover on; level again', 'W4_3 "cover"'),
 ('S4_T', 'stage', 'cut back: hatch closed', ''),
 ('F5', 'stage', 'fail 5: small boats want a lift', 'FC5'),
 ('S5_1', 'stage', 'two concrete piers', 'W5_1 "piers"'),
 ('S5_2', 'stage', 'the yellow hoist', 'W5_2 "crane"'),
 ('S5_3', 'stage', 'two slings', 'W5_3 "slings"'),
 ('S5_U', 'stage', 'last frame: a sailboat lifted', 'W5_U'),
]
def font(n):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
        try: return ImageFont.truetype(p, n)
        except Exception: pass
    return ImageFont.load_default()
def change(a, b):
    A = cv2.resize(cv2.imread(D + f'stills/{a}.png'), (360, 638), interpolation=cv2.INTER_AREA)
    B = cv2.resize(cv2.imread(D + f'stills/{b}.png'), (360, 638), interpolation=cv2.INTER_AREA)
    m = C.changed(B, A, 12); m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) > 0
    return 100.0 * m.mean(), m
def strip(rows_per_sheet=10, tw=216):
    th = int(tw * 1360 / 768); out = []; F, f2 = font(15), font(13)
    for s0 in range(0, len(LADDER), rows_per_sheet):
        part = LADDER[s0:s0 + rows_per_sheet]; cols = 5; rows = (len(part) + cols - 1) // cols
        sheet = Image.new('RGB', (cols * (tw + 12) + 12, rows * (th + 86) + 12), (18, 20, 24)); d = ImageDraw.Draw(sheet)
        for i, (k, view, what, clip) in enumerate(part):
            n = s0 + i; x = 12 + (i % cols) * (tw + 12); y = 12 + (i // cols) * (th + 86)
            im = cv2.imread(D + f'stills/{k}.png'); prev = LADDER[n - 1] if n else None
            tile = cv2.resize(im, (tw, th), interpolation=cv2.INTER_AREA)
            note = ''
            if prev and prev[1] == view and clip:
                pc, m = change(prev[0], k); note = f'changed {pc:.1f}%'
                red = cv2.resize(m.astype(np.uint8), (tw, th), interpolation=cv2.INTER_NEAREST) > 0
                edge = cv2.morphologyEx(red.astype(np.uint8), cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8)) > 0
                tile[edge] = (40, 40, 235)
            elif prev and prev[1] != view: note = 'cut to a new view'
            elif not prev: note = 'first frame'
            sheet.paste(Image.fromarray(cv2.cvtColor(tile, cv2.COLOR_BGR2RGB)), (x, y))
            d.text((x, y + th + 4), f'{n + 1}. {k}', font=F, fill=(255, 214, 46))
            d.text((x, y + th + 23), what[:34], font=f2, fill=(235, 235, 235))
            d.text((x, y + th + 41), (clip + '  ' if clip else '') + note, font=f2, fill=(160, 200, 255))
        p = D + f'sheets/18-gateC-ladder-{s0 // rows_per_sheet + 1}.jpg'; sheet.save(p, quality=86); out.append(p)
    return out
if __name__ == '__main__':
    print('\n'.join(strip()))

def tester():
    """The boat's key (KH) beside the boat as it stands in the ladder: the same boat, the same size where it should be."""
    F = font(16); tiles = []
    kh = cv2.imread(D + 'stills/KH.png'); kh = cv2.resize(kh, (360, int(360 * kh.shape[0] / kh.shape[1])))
    tiles.append(('KH: the key', kh))
    crops = [('S0 frame 0', 'S0', (0.20, 0.80, 0.10, 0.31)), ('S1_4 on the cradle', 'S1_4', (0.20, 0.80, 0.17, 0.38)),
             ('F2 crept down', 'F2', (0.18, 0.82, 0.24, 0.46)), ('F3 through the dock', 'F3', (0.15, 0.85, 0.50, 0.72)),
             ('S3_L afloat', 'S3_L', (0.15, 0.85, 0.52, 0.72)), ('CV4U close view', 'CV4U', (0.0, 1.0, 0.33, 0.66)),
             ('CV4_0 leaning', 'CV4_0', (0.0, 1.0, 0.33, 0.66)), ('S5_U last frame', 'S5_U', (0.15, 0.85, 0.52, 0.72))]
    for lab, k, (x0, x1, y0, y1) in crops:
        im = cv2.imread(D + f'stills/{k}.png')
        if im is None: continue
        h, w = im.shape[:2]; c = im[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)]
        tiles.append((lab, cv2.resize(c, (360, int(360 * c.shape[0] / c.shape[1])))))
    cols = 3; rows = (len(tiles) + cols - 1) // cols; th = max(t.shape[0] for _, t in tiles)
    sheet = Image.new('RGB', (cols * 372 + 12, rows * (th + 30) + 12), (18, 20, 24)); d = ImageDraw.Draw(sheet)
    for i, (lab, t) in enumerate(tiles):
        x = 12 + (i % cols) * 372; y = 12 + (i // cols) * (th + 30)
        sheet.paste(Image.fromarray(cv2.cvtColor(t, cv2.COLOR_BGR2RGB)), (x, y)); d.text((x, y + t.shape[0] + 4), lab, font=F, fill=(255, 214, 46))
    p = D + 'sheets/18-gateC-tester.jpg'; sheet.save(p, quality=86); return p
def firstlast():
    a = cv2.imread(D + 'stills/S0.png'); b = cv2.imread(D + 'stills/S5_U.png')
    pair = np.hstack([a, np.zeros((a.shape[0], 16, 3), np.uint8) + 24, b]); p = D + 'sheets/18-gateC-first-last.jpg'
    cv2.imwrite(p, cv2.resize(pair, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 88]); return p
