# Short-Form Video Memory

Project memory for vertical 3D cutaway explainers: the hidden inside of things everyone uses or walks past.

- `CLAUDE.md`: the project memory, rewritten on 18 Nov 2026 for the 10-video plan: what works in the format (with evidence from our channels and the successful ones), the plan and the ten ideas with draft scripts, the script rules, the Cutaway look, the Higgsfield + ElevenLabs runbook (at most 200 credits a video), lessons, posting, results and the paste-in prompts.
- `pipeline/`: each video's script, beat sheet, prompts, job ids and build scripts (`NN-*`); start a new video from the latest set (section 6.4 of `CLAUDE.md`).
- `branding/`: the channel's profile picture, banner, fit check and a transparent mascot cutout (10 Nov 2026), and three profile pictures without the character with their fit check (18 Nov 2026); rebuilt by `pipeline/branding/`, where `live_brand_check.py` tells which picture and banner are live on YouTube (section 8.3 of `CLAUDE.md`).
- `pipeline/tiktok/`: read-only TikTok checks (`tt_snapshot.py`: followers, per-video stats, category, whether hashtags registered, AI labels, penalties; `ttdl.py`: downloads). See section 12 of `CLAUDE.md`.
- `pipeline/youtube/`: read-only YouTube checks (channel snapshot with a made-for-kids check, competitor benchmarks, topic saturation search, handle availability). See section 12 of `CLAUDE.md`.
- `pipeline/analysis/`: checks for a finished video or one we study: how much of it really moves, caption size, sharpness (`check_video.py`), how the camera moves (`camera_path.py`, the travelling-camera targets of Rule 7 in section 5), what sits under the voice (`under_the_voice.py`), and timestamped contact sheets (`contact_sheet.py`). See sections 6 and 12 of `CLAUDE.md`.

- `tiktokshop.md`: memory for the sister project, TikTok Shop affiliate (US rules for joining, the plan to reach 1,000 followers, and how realistic $5,000 a month is).

Live copy: the "Short-Form Video Memory" artifact on claude.ai. Keep both in sync.
