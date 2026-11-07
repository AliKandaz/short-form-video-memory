# usage: python3 fetch.py KEY=URL [KEY=URL ...]  -> downloads to stills/KEY.png and writes a preview sheet
import sys, urllib.request, os
from PIL import Image
keys=[]
for a in sys.argv[1:]:
    k,u=a.split('=',1); p=f'stills/{k}.png'
    urllib.request.urlretrieve(u,p); keys.append(k)
h=700; ims=[Image.open(f'stills/{k}.png').convert('RGB') for k in keys]
ims=[im.resize((int(im.width*h/im.height),h)) for im in ims]
W=Image.new('RGB',(sum(i.width for i in ims)+10*(len(ims)-1),h),'white'); x=0
for im in ims: W.paste(im,(x,0)); x+=im.width+10
out='/tmp/claude-0/-home-user/c60ca624-d246-53d7-b831-c8092838acc4/scratchpad/prev_'+'_'.join(keys)+'.jpg'
W.save(out,quality=85); print(out)
