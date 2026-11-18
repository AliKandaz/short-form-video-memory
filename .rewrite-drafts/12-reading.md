## 12. Reading the platforms from a session (consolidated 18 Nov 2026)

### 12.1 TikTok
- **Tools:** `pip install --target <dir> yt-dlp` and run it with `PYTHONPATH=<dir> python3 -m yt_dlp` (no impersonation target is
  installed; the warning is harmless).
- **An account's videos with stats:** `yt-dlp --flat-playlist -J https://www.tiktok.com/@<handle>`: each entry has `view_count`,
  `like_count`, `comment_count`, `repost_count` (shares), `save_count`, `timestamp`, `duration` and the caption.
- **Followers and likes:** fetch `https://www.tiktok.com/@<handle>` with a browser user agent; the JSON in
  `<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__">` holds `webapp.user-detail` → `userInfo.stats` (`followerCount`, `heartCount`,
  `videoCount`) and the bio (`user.signature`).
- **One video's details:** fetch `https://www.tiktok.com/@<handle>/video/<id>`; `webapp.video-detail` → `itemInfo.itemStruct`
  holds `stats`, `diversificationLabels` (the category TikTok filed it under), `textExtra` and `challenges` (empty = the hashtags
  are not links), `moderationAigcLabelType` and `ShowAIGC` (TikTok's own AI label), `IsAigc` (the creator's) and `penaltyContext`
  (`display_penalty_type` 0 = no penalty shown), and `video.definition` (the served resolution: 720p for everyone on the web).
- **All of the above in one command (18 Nov 2026):** `PYTHONPATH=<dir> python3 pipeline/tiktok/tt_snapshot.py <handle> [--limit N]`
  prints followers, then per video the stats, the category, how many hashtags registered, the AI labels and any penalty.
- **Downloads:** `PYTHONPATH=<dir> python3 pipeline/tiktok/ttdl.py <out_dir> <video url>…` picks a format served from
  `v16-webapp-prime.us.tiktok.com` (the `-0`/`-1` suffix doesn't map to a fixed host). The `bytevc1` formats carry no sound; take
  the sound from an `h264` format.

### 12.2 YouTube
- The environment allows `www.youtube.com`, `i.ytimg.com`, `yt3.ggpht.com` and `yt3.googleusercontent.com`. `/shorts/<id>` and
  channel pages work; `/watch?v=` redirects to a blocked bot check, and the player is bot-gated (no captions, durations or downloads).
- Scripts in `pipeline/youtube/` (usage in each docstring; pace requests 2–3 s apart):
  - `yt_snapshot.py @handle [dir]`: channel facts, every Short's views, likes and date, comments, and a made-for-kids check.
  - `yt_saturation.py <dir> "<query>" …`: the saturation check (how many Shorts, the top Shorts and long videos per query).
  - `yt_search.py <dir> "<query>"`: the full search results; `yt_channels.py <dir> handle:@name shorts:<id>`: a channel's latest
    and most popular Shorts, or who posted a Short; `handles.py <dir> yt|tt <handle>…`: is a handle taken.
- Frames without a download: `https://i.ytimg.com/vi/<id>/frame0.jpg` (the first frame) and `oar1.jpg`, `oar2.jpg`, `oar3.jpg`
  (about 25%, 50% and 75%; `oar2` is the default cover).
- YouTube counts a Shorts view each time one starts playing, so a Short with tens of views was hardly shown.

### 12.3 Looking at a video
- **The opening:** frames at 0, 0.5, 1, 2 and 3 s (`ffmpeg -ss <t> -i <video> -frames:v 1 -vf scale=180:320 <out>.png`) side by
  side with a reference's; judge whether the scene itself changes by 1 s (1.2, 4.2).
- **The whole video:** `pipeline/analysis/contact_sheet.py` (one frame a second), `check_video.py` (share of seconds moving,
  caption size, sharpness), `camera_path.py` (the camera's moves), `under_the_voice.py` (what sits under the narration).
- Nothing has been listened to; sound is measured, not judged by ear.

### 12.4 Web research
- WebSearch summaries work; WebFetch can't open `en.wikipedia.org`, `cdc.gov`, `weather.gov`, `seller-us.tiktok.com`,
  `support.tiktok.com` and many blogs. Say when a fact rests on a search summary, and reopen the page before quoting a number.

---
