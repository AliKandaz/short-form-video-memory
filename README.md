# Short-Form Video Memory

Project memory for vertical 3D cutaway build videos: "If you [one naive step], you have a [thing]", then one problem and one fix at a time, with the bill running. (Cutaway explainers until 21 Nov 2026.)

- `CLAUDE.md`: the project memory, revised on 21 Nov 2026 for the build format: what works (with evidence from our channels, the successful ones and the build accounts @whatifplus and @youbuiltit), the build run and the ten build ideas with draft scripts, the script rules, the bill, the street and the dog, the Cutaway look (unchanged) and its overlays, the Higgsfield + ElevenLabs runbook (at most 200 credits a video), lessons, posting, results and the paste-in prompt (renewed 21/11/26). The explainer plan it replaced is at commit `a9abd35`.
- `strategy2.md`: style 2, photoreal AI build stories with no narration (created 21 Nov 2026; paused the same day while the build format is tested, unless a style-2 video is asked for).
- `research/`: the numbers behind the study of 21 Nov 2026 (section 1.7 of `CLAUDE.md`): every video of @whatifplus (42, with script measurements) and of @youbuiltit (96), with stats.
- `pipeline/`: each video's script, beat sheet, prompts, job ids and build scripts (`NN-*`); start a new video from the latest set (section 6.4 of `CLAUDE.md`).
- `branding/`: the channel's profile picture, banner, fit check and a transparent mascot cutout (10 Nov 2026), and three profile pictures without the character with their fit check (18 Nov 2026); rebuilt by `pipeline/branding/`, where `live_brand_check.py` tells which picture and banner are live on YouTube; and brand set v3 (20 Nov 2026), a cut-cube profile picture, banner and fit check drawn from scratch by `make_brand_v3.py`, with nothing from the videos (section 8.3 of `CLAUDE.md`).
- `pipeline/tiktok/`: read-only TikTok checks (`tt_snapshot.py`: followers, per-video stats, category, whether hashtags registered, AI labels, penalties; `tt_items.py`: an account's whole list, profile and per-video detail saved as JSON; `ttdl.py`: downloads). See section 12 of `CLAUDE.md`.
- `pipeline/youtube/`: read-only YouTube checks (channel snapshot with a made-for-kids check, competitor benchmarks, topic saturation search, handle availability). See section 12 of `CLAUDE.md`.
- `pipeline/analysis/`: checks for a finished video or one we study: how much of it really moves, caption size, sharpness (`check_video.py`), how the camera moves (`camera_path.py`, the travelling-camera targets of Rule 7 in section 5), what sits under the voice (`under_the_voice.py`), timestamped contact sheets (`contact_sheet.py`), the first seconds of every video of an account ranked by views (`hooks_sheet.py`), speech to text with word times on this machine (`transcribe.py`) and the words on the picture (`labels.py`). See sections 6, 7.7 and 12 of `CLAUDE.md`.

- `tiktokshop.md`: memory for the sister project, TikTok Shop affiliate (US rules for joining, the plan to reach 1,000 followers, and how realistic $5,000 a month is).

Live copy: the "Short-Form Video Memory" artifact on claude.ai. Keep both in sync.
