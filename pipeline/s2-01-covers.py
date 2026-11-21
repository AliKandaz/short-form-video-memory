# usage: python3 s2-01-covers.py <work dir>  -> s2-01-covers/: the cozy room and a before-and-after split, each as 1080x1920
# (YouTube, where a frame is picked at upload until the Partner Program) and 1080x1440 (TikTok crops covers to 3:4: y 240-1680).
# No text, as the video has none. The cozy room is a frame of cut B (the lamp just on, shot 31); the split stacks the same crop of
# frame 0 (O0) over the payoff (P), the locked view making the change read at a glance, with a thin white line between.
import os, sys, cv2, numpy as np
D = sys.argv[1]; OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s2-01-covers"); os.makedirs(OUT, exist_ok=True)
cap = cv2.VideoCapture(os.path.join(D, "out", "s2-01-cutB.mp4")); fps = cap.get(cv2.CAP_PROP_FPS)
cap.set(cv2.CAP_PROP_POS_FRAMES, int(round((35.2 + 1.3) * fps))); ok, cozy = cap.read()   # shot 31 starts at 35.2 s
cv2.imwrite(os.path.join(OUT, "cover-cozy-1080x1920.jpg"), cozy, [cv2.IMWRITE_JPEG_QUALITY, 92])
cv2.imwrite(os.path.join(OUT, "cover-cozy-1080x1440.jpg"), cozy[240:1680], [cv2.IMWRITE_JPEG_QUALITY, 92])
def half(key, h):
    im = cv2.imread(os.path.join(D, "stills", key + ".png"))           # 768x1360
    x0, w = 0, 768; hh = int(round(w * h / 1080))                      # full width; the 3:4 halves are shallower, so lower
    y0 = 250 if h > 800 else 380                                         # them onto the cabin and its porch
    return cv2.resize(im[y0:y0 + hh, x0:x0 + w], (1080, h), interpolation=cv2.INTER_LANCZOS4)
for H, name in ((1920, "1080x1920"), (1440, "1080x1440")):
    a, b = half("O0", H // 2 - 3), half("P", H // 2 - 3)
    split = np.vstack([a, np.full((6, 1080, 3), 255, np.uint8), b])
    cv2.imwrite(os.path.join(OUT, f"cover-beforeafter-{name}.jpg"), split, [cv2.IMWRITE_JPEG_QUALITY, 92])
print(sorted(os.listdir(OUT)))
