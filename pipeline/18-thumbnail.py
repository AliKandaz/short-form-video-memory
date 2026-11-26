# Covers for video 18 (B20, "How to Launch a Ship From Your Back Yard"), built from frames of the video's clean master (no
# generation credits; 17-thumbnail.py's helpers). Runs from the work dir:  python3 18-thumbnail.py [A B C]
# Inputs (frames of work/18-final-clean.mp4, saved by 18-build.py's 'covers' mode): frames/splash.png (failure 3: through the
# neighbor's dock), frames/start.png (frame 0: the hull on its blocks, the pickup straining), frames/finished.png (the
# finished yard: a sailboat in the hoist), frames/lifted.png (the last shot), fonts/HBXCaption.ttf.
# Words and subject inside TikTok's 3:4 grid crop (y 240-1680).
#   A  the launch through the dock with the format's hook: "GUESS / THE BILL" and the pill "$???,???"
#   B  before and after with the bill: the hull on its blocks ("$50") above, the finished yard ("$???,???") below
#   C  plain frame with no text: the launch through the dock
import importlib.util, os, sys
from PIL import Image, ImageDraw
_s = importlib.util.spec_from_file_location('t17', os.path.join(os.path.dirname(os.path.abspath(__file__)), '17-thumbnail.py'))
T = importlib.util.module_from_spec(_s); _s.loader.exec_module(T)
W, H, YEL, WHT, GRID = T.W, T.H, T.YEL, T.WHT, T.GRID

def concept_A():   # failure 3, the most violent moment, with the format's hook
    cv = T.grade(T.place('frames/splash.png', W, H, fx=0.50, fy=0.50, ty=0.48, zoom=1.30), c=1.08, s=1.12)
    cv = T.vignette(cv, 0.20).convert('RGBA')
    T.pill(cv, 540, 345, '$???,???')
    T.backdrop(cv, (60, 1370, 1020, 1670), 150, blur=40)
    T.word(cv, 540, 1452, 'GUESS', 136, WHT)
    T.word(cv, 540, 1592, 'THE BILL', 136, YEL)
    return cv
def concept_B():   # before and after, one above the other, inside the 3:4 crop
    top = T.grade(T.place('frames/start.png', W, 960, fx=0.50, fy=0.28, ty=0.50, zoom=1.0), c=1.06, s=1.08)   # hull and truck in the 3:4 crop
    bot = T.grade(T.place('frames/finished.png', W, 960, fx=0.36, fy=0.60, ty=0.50, zoom=1.0), c=1.08, s=1.10)
    cv = Image.new('RGB', (W, H), (16, 26, 51)); cv.paste(top, (0, 0)); cv.paste(bot, (0, 960)); cv = cv.convert('RGBA')
    ImageDraw.Draw(cv).rectangle((0, 952, W, 968), fill=YEL)
    T.pill(cv, 540, 880, '$50', size=96)
    T.pill(cv, 540, 1062, '$???,???', size=96)       # over the lawn, above the hoist and the boats
    return cv
def concept_C():   # plain frame, no text
    cv = T.grade(T.place('frames/splash.png', W, H, fx=0.50, fy=0.50, ty=0.48, zoom=1.15), c=1.05, s=1.06)
    return T.vignette(cv, 0.12).convert('RGBA')
CONCEPTS = {'A': concept_A, 'B': concept_B, 'C': concept_C}

if __name__ == '__main__':
    os.makedirs('thumb', exist_ok=True)
    for n in (sys.argv[1:] or list(CONCEPTS)):
        im = CONCEPTS[n]().convert('RGB')
        im.save(f'thumb/cover_{n}.png'); im.save(f'thumb/cover_{n}_9x16.jpg', quality=92)
        im.crop((0, GRID[0], W, GRID[1])).save(f'thumb/cover_{n}_3x4.jpg', quality=92)
        print('cover', n)
