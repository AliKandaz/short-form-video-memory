# Gate D helper (video 09): python3 pilot_measure.py clip.mp4 [...] clip.mp4 [...] -> camera_path.py and check_video.py numbers per clip, next to the power-lines reference
import subprocess, sys, json, os
A = '/home/user/short-form-video-memory/pipeline/analysis'
print(f"{'video':28s} {'cam moving':>10s} {'parallax':>9s} {'big-move s':>10s} {'still cam':>9s} {'zoom %/s':>8s} {'pan %/s':>7s} {'moving (pic)':>12s}")
print(f"{'power-lines ref (88 s)':28s} {'66%':>10s} {'0.46':>9s} {'22 (1 in 4)':>10s} {'5 s':>9s} {'5.5':>8s} {'4.1':>7s} {'70%':>12s}")
print(f"{'targets (Rule 7 / Rule 1)':28s} {'>=65%':>10s} {'>=0.3':>9s} {'>=1 in 8':>10s} {'<=5 s':>9s} {'':>8s} {'':>7s} {'>=80%':>12s}")
for v in sys.argv[1:]:
    j1 = v + '.cam.json'; j2 = v + '.chk.json'
    subprocess.run(['python3', f'{A}/camera_path.py', v, '--json', j1], capture_output=True)
    subprocess.run(['python3', f'{A}/check_video.py', v, '--json', j2], capture_output=True)
    c = json.load(open(j1))['summary']; k = json.load(open(j2))
    mv = k.get('moving_pct', k.get('summary', {}).get('moving_pct'))
    print(f"{os.path.basename(v):28s} {str(c['camera_moving_pct'])+'%':>10s} {c['median_parallax_px']:>9} "
          f"{str(c['big_move_seconds'])+' of '+str(c['seconds']):>10s} {str(c['longest_still_camera_s'])+' s':>9s} "
          f"{c['median_zoom_pct']:>8} {c['median_pan_pct']:>7} {str(mv)+'%':>12s}")
