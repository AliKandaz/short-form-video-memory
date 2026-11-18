#!/usr/bin/env python3
"""Download TikTok videos, preferring formats served from the allowed v16 host. Usage: ttdl.py <out_dir> <url> [url...]"""
import json, subprocess, sys, os, urllib.parse
out = sys.argv[1]
env = dict(os.environ)
for url in sys.argv[2:]:
    vid = url.rstrip('/').split('/')[-1]
    dest = os.path.join(out, vid + '.mp4')
    if os.path.exists(dest) and os.path.getsize(dest) > 100000:
        print('have', vid); continue
    j = subprocess.run([sys.executable, '-m', 'yt_dlp', '-J', url], capture_output=True, text=True, env=env)
    try:
        info = json.loads(j.stdout)
    except Exception:
        print('FAIL info', vid, j.stderr[-300:]); continue
    fmts = [f for f in info.get('formats', []) if f.get('vcodec') not in (None, 'none')]
    def score(f):
        host = urllib.parse.urlparse(f.get('url', '')).hostname or ''
        return (('v16-webapp-prime' in host), f.get('vcodec', '').startswith('h264'), f.get('height') or 0)
    fmts.sort(key=score, reverse=True)
    ok = False
    for f in fmts[:6]:
        r = subprocess.run([sys.executable, '-m', 'yt_dlp', '-q', '-f', f['format_id'], '-o', dest, url], capture_output=True, text=True, env=env)
        if os.path.exists(dest) and os.path.getsize(dest) > 100000:
            print('ok', vid, f['format_id'], urllib.parse.urlparse(f.get('url','')).hostname); ok = True; break
    if not ok:
        print('FAIL dl', vid, r.stderr[-200:])
