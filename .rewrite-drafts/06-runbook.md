## 6. Production runbook (for Claude: follow it when asked to make a video; rewritten 18 Nov 2026 from videos 08–11)

> Trigger phrases: "make video #N", "make V3", "run the runbook on [topic]", or the paste-in prompt (11.1).
> **Never generate anything (images, clips, audio) before Gate B is approved.** Script, beat sheet and quote are free.

### 6.0 Tools and prices (checked 15–18 Nov 2026; re-check, prices change)
| Job | Tool | Settings | Cost |
|---|---|---|---|
| Stills (style key, camera positions, stages) | Higgsfield `generate_image` / `generate_image_batch`, `seedream_v5_pro` | `resolution:"1k"`, `aspect_ratio:"9:16"`; references as `medias` with role `image_references` | **1.25 an image** |
| Clips | `generate_video` / `generate_video_batch`, **`kling4_0`** | `mode:"image-to-video"`, `aspect_ratio:"9:16"`, `duration` 3–30 s, `start_image` + `end_image`, ordered middle frames in `image_references` | **2.25 a second at 720p, 3.25 at 1080p** |
| Price checks | `estimate_image_cost`, `estimate_video_cost` (used for video 11 on 18 Nov 2026), or `get_cost:true` | one call per model, resolution and duration | free |
| Narration | ElevenLabs `creative_generate_speech`, `eleven_v4`, Daniel (5) | `estimate_only:true` first | about 1 ElevenLabs credit a character: 1,400–1,540 a take |
| Sound bed and effects | ElevenLabs flow: one `creative_add_flow_node` per sound (`node_type:"sfx"`, `model_id:"eleven_text_to_sound_v2"`), then one `creative_run_flow_nodes` | `estimate_only:true`, then `generations_count:1` | about 3.33 ElevenLabs credits a second of sound (the estimate prices each effect at its default length and overstates: budget from the durations) |
| Word timings | Higgsfield `sandbox_exec`, faster-whisper `small.en` | `background:true` (foreground calls time out at ~60 s) | free |
| Assembly, captions, mix | local ffmpeg with libass, zoompan, xfade | — | free |
| Checks | `pipeline/analysis/check_video.py`, `camera_path.py`, `under_the_voice.py`, `contact_sheet.py` | `pip install numpy opencv-python-headless` | free |
| Upload | `media_upload` → PUT (headers `Content-Type`, `If-None-Match: *`) → `media_confirm` | — | free |
| Not used | `minimax_h3` (every queued job failed, 7–10 Nov 2026); `use_unlim` unless the user asks; `virality_predictor` and `tiktok_prepare_publish` only if asked (ask about cost first) | | |

### 6.1 Budget and credit rules (hard; the cap was set by the user on 18 Nov 2026)
0. **At most 200 Higgsfield credits a video, the 15% reserve included** ("I want at most 200 credits per video", 18 Nov 2026).
   A plan that prices above 200 is cut before it is shown (shorter script, fewer positions, shorter clips), never shown as is.
   ElevenLabs credits (narration and sound) are separate.
1. Script, beat sheet, prompts and the quote are free; do them first.
2. Before Gate B, price the exact plan (one estimate per model, resolution and duration), add a **15% reserve**, show the total
   and the balance after it, and wait for approval. Stop and ask if a run will go more than 10% over its quote.
3. Images before video: fix the look, the drift and the layout in stills (1.25), never by re-rolling clips (7–20).
4. Pilot first: render two clips (the hook and one travel clip) and show them before the batch (Gate D).
5. One generation per request (no variants). Re-render a bad clip **once**, with a corrected prompt; if it fails again, hold the
   last good frame (3 s at most) and tell the user which line lost its clip.
6. Clip `duration` = the line's measured length rounded up (minimum 3 s on `kling4_0`); the clips in total come to no more than
   about 1 s over the lines (the edit plays clips at 0.8–1.15× to fit).
7. Never auto-retry after a transport timeout; check the job id first.
8. After the run, call `transactions` and report the spend against the quote.

**What a video cost before the cap:** video 08 203.50 (79.5 s), 09 264.25 (75 s), 10 278.00 (76 s); video 11 was quoted at
271.69 and stopped. About 80% is clips, and the clips ran long: video 10 planned 86 s of clips for a 76 s video, plus 18 s of
re-renders.

**The standard plan under the cap (18 Nov 2026; my estimate from the prices above):**

| Item | Plan | Credits |
|---|---|---|
| Clips | every line a clip, 720p, about 64 s in total for a 62–64 s video (no more than ~1 s over the lines) | 144.00 |
| Stills | 7–9 camera positions and their stages: about 16 keyframes on screen, at most 22 tries | 27.50 |
| Base | | 171.50 |
| Reserve (15%) | one clip re-render, a few still retries | 25.73 |
| **Quote** | | **197.23** |

- Spend the reserve only on what breaks; a run that has used it stops and asks before going further.
- **Where the savings come from:** about 220-word scripts instead of 270 (4.3); clips planned at the length of their lines (6.1
  rule 6) and played at 0.8–1.15× (`FULLFIT`); 7–9 positions instead of 9–12; the FLOOR line and middle keyframes up front so
  fewer clips are re-rendered (7.2); positions made from neighbours so fewer stills are retried (7.1).
- **Not at the expense of the opening:** the hook clip is planned first and gets the most care (Rule 0). 1080p for the hook (+3–6)
  only if the quote has room under 200.

### 6.2 Step by step

**Step 0: Start.** `balance` (and the plan's renewal date if the balance is low). Read the idea in section 3 and its ⚠ items.

**Step 1: Script (free). GATE A.**
- Start from the idea's draft script (section 3). Keep about 220 words (4.3), the opening rules (4.2) and the formula (4.1).
- Fact-check every ⚠ with web search; cut what can't be checked.
- Saturation check on the exact title: `python3 pipeline/youtube/yt_saturation.py <dir> "<title>" "<topic>" "zack d films <topic>"`
  (12.2). Report near-identical Shorts and the best views; if the topic has been animated in our format since the idea was
  written, change the angle.
- **Show at Gate A:** the title (TikTok and YouTube), the script, **the first second as three lines (frame 0; what has changed by
  1.0 s; the first line)**, where the camera is on each line, the lines cut or moved onto the set, the facts checked, and the
  saturation numbers.

**Step 2: Beat sheet (free).**
- One beat per sentence or But/So unit: `beat | words | est. s (words ÷ 3.5) | camera position and the move to the next | start
  still → end still | what moves (big in the frame) | pointer | sound | clip`. Every beat is a clip; plan no holds.
- **The stage ladder:** the set's state after each fix (S0 → S_n). The last frame matches the first.
- **The camera path:** 7–9 positions under the cap (wide only to open if the event is wide, to close, and once to step back); on
  "But" push in or swoop, on "So" pull away or fly on; a big move at least every 8 s on average and never more than 15 s apart; no
  still camera for more than 5 s; moves named (swoop, rise, push in, pull away, fly along, orbit, drift, whip).
- **The hook clip:** its own row, with frame 0, the event and the state at 1.0 s.

**Step 3: Quote (free). GATE B.**
- `balance`; estimates for every still and clip length at 720p; the narration (`creative_generate_speech` with
  `estimate_only:true`) and the sound (by durations, ~3.33 a second; ElevenLabs credits, outside the cap).
- **The quote with its reserve must be 200 or less** (6.1); if it isn't, cut before showing it.
- Show: positions and stills, clips and seconds, the total with the reserve, the balance after. **Wait for approval.**

**Step 4: Project and style key.**
- `create_project` named `HBX – [title]` and reuse its folder on every generation.
- STYLE, WIDE and the other prompt lines are in 6.3, byte-identical in every prompt. One SET line per video carries the place and
  its colours (colours, not objects).
- The style key is frame 0 of the video: the "before" of the opening event (or the wide, if the event starts wide). **Fit the plan
  to the style key's layout** rather than fighting it (7.1).

**Step 5: Stills. GATE C.**
- Each camera position is an edit of the style key or of a neighbouring position (POS, 6.3); each change at a position is an edit
  of that position's still (LOCK for wides, LOCKZ for close-ups). Indoor close-ups carry INDOOR. "Extreme close-up: the [part]
  fills most of the frame" gets a real close-up.
- Batches of up to 8 (`seedream` refuses more with 429; resend later), `jobs_wait`, one `show_generation_by_ids`. Re-make a drifted
  still once.
- **Show at Gate C:** a flight map (the positions in order, the move between each pair, the stages at each), the set matching from
  every angle, and the first and last frames matching part for part. (`10-flightmap.py` draws it.)

**Step 6: Narration (can start right after Gate B).**
- Daniel, the whole script as one continuous take; two takes come back; pick the one that reads "So you…" straight through.
- Pause tightening to 0.15 s (`10-timing.py`), then `atempo` up to 1.1 to reach about 3.5 words a second. Daniel's raw pace has
  run 2.9–3.3 words a second.
- Word timings: faster-whisper `small.en` in the Higgsfield sandbox (background job, about a minute), with the rare words in
  `initial_prompt`; the script supplies the text, Whisper only the timing (`10-whisper.py`). These timings replace the estimates.

**Step 6b: Sound.**
- One ElevenLabs flow ("HBX NN [title]: sound"); one sfx node per sound with `model_parameters`
  `{"duration_seconds": N, "loop": false, "prompt_influence": 0.5}` (`loop: true` for the bed, ~20 s); `estimate_only:true`; then the
  same run with `generations_count:1`. Poll `creative_get_flow_run_status`; never run again to retry (it bills again).
- Prompts name the sound, its texture and the space, no visual words ("Small metal flap swinging shut inside a plastic pipe, short
  hollow clank").
- Mix: loop the bed (`-stream_loop -1`) with short fades; set levels from measured loudness on the mono fold-down (`rms_db()` in
  `08-build.py`): bed 19 dB and effects 11 dB under the voice; copy the mono voice to both channels (`pan=stereo|c0=c0|c1=c0`) and
  give every sound `aformat=channel_layouts=stereo` before `amix`. Place each effect's loud moment on its picture (measure the
  frame), not just on the word.

**Step 7: Pilot clips. GATE D.**
- Render two: **the hook** (frame 0 → the event by 1.0 s → the first camera move) and **one travel clip** between two positions.
- **Show at Gate D:** each pilot with its `camera_path.py` and `check_video.py` numbers next to the reference's (66%, 0.46 px,
  a big move one second in four) **and the hook's frames at 0, 0.5, 1 and 2 s** (`contact_sheet.py`): the event must be visible
  by 1 s and big in the frame. A pilot that zooms across a flat picture (parallax near 0) fails however it looks. Fix the stills or
  the prompt and render once more; don't batch the rest until both pass.

**Step 8: The rest of the clips.**
- Batches of up to 12 (`kling4_0` takes 12–13 at once on Ultra; 4–17 minutes), `jobs_wait`, one `show_generation_by_ids`.
- Check every clip on a sheet at about 5 frames a second: the right stage, no drift, no text, motion from frame 1, the thing the
  line describes really moves, the planned camera move (`camera_path.py`), and no pit, step or soil opening in an indoor floor.

**Step 9: Assembly (free; template `pipeline/10-build.py`).**
- Fit each clip to its measured line: play at 0.8–1.15×; a 3 s clip over a ~2 s line plays whole at up to 1.7× (`FULLFIT`).
- Edit tools: `PUSH` (add a push-in to a still-camera clip, 3% a second or more) with `EASE_AFTER` on the next clip, `PULL` (the
  last clip pulls back to frame 0's framing so the loop lands), `SPLICE` (cut a bad stretch out of a clip and join the clean parts
  with a 0.3 s whip or a 0.25 s dissolve), `WHIP` (with `fillborders` against the junk first frame of ffmpeg's slide transitions),
  `LIGHTS` (a lights-out dip made in the edit), `POINTERS` with tracking (`09-build.py`).
- Upscale the 720p clips to 1080×1920 with a light sharpen (`unsharp=5:5:0.6`).
- Narration at full level, sound under it (Step 6b), about −14 LUFS. Keep a voice-only mix and a clean master (no captions or
  pointers).
- Check the master: `check_video.py` (80%+ moving), `camera_path.py` (Rule 7), `under_the_voice.py` (18–22 dB), and **a sheet of the
  first 2 s** (Rule 0).

**Step 10: Captions and pointers (free).** One word per cue from the Whisper timings, text from the script, ALL CAPS "HBX Caption"
(Montserrat 800), ASS `Fontsize` 114 (57 px letters), centred at `CAPY` ≈ 1440, long words fitted to 900 px (`MAXW`); a short
word pushes the next one back so two words never share the screen (`07-build.py` cue timing). Pointers per Rule 6, drawn as ASS
shapes from a top-left origin (`\an7`). Verify: duration within 0.2 s of the master, every word once, three spot frames readable.
Fallback: deliver the clean master and an `.srt` for CapCut.

**Step 11: Delivery.** Upload the final, the voice-only version and the clean master (`media_upload` → PUT → `media_confirm`); give the
links; report the length, credits quoted against spent (`transactions`), the motion and camera numbers, the first-second check and
any line that lost its clip.

**Step 12: Covers and post copy (free).** Three covers (`10-thumbnail.py`), one of them a plain frame with no text; TikTok and
YouTube copy per 8.1 and 8.2. Then log the video in 9.2 and update both copies of the memory.

### 6.3 Prompt lines (paste byte-identical; collected 15–17 Nov 2026)
- **STYLE** (every still and clip): "Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing
  clean layers and what is buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic
  materials, translucent cyan water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark."
  For a set with no water, drop "translucent cyan water" and add NOWATER: "There is no water anywhere."
- **WIDE** (wide shots only): "Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is
  plain, calm, low-detail ground."
- **Deep block** (style keys): "the block of ground is deep: below the [lawn/street] its front is cut straight down all the way to
  the bottom edge of the frame … there is no ground in front of the block."
- **POS** (a new camera position): "The same [set] as the reference, with the same parts, colours and materials. New camera
  position: [where the camera is, how high, which way it looks, what fills the frame]. Nothing in view changes."
- **LOCK** (a change seen from a wide): "Keep exactly the same camera position, zoom and framing as the reference image. Change
  only this: [the change]. Everything else identical." **LOCKZ** (a change in a close-up): "… everything in view stays exactly
  where it is."
- **INDOOR** (indoor stills): "This is an indoor close-up: nothing is cut open, and there is no soil, no ground, no pit and
  nothing buried anywhere in the frame."
- **FLOOR** (every clip of an indoor set): "The floor is solid grey and nothing is cut open: no soil, no pit, no steps, no wooden
  layers."
- **NIGHT** (night re-grades): "IT IS NIGHT, with no daylight at all (the daylight described above does not apply to this
  picture)." Lights-off changes are surer in the edit (`LIGHTS`).
- **Travel clip:** "[STYLE] [the move, in the camera column's words, e.g. The camera swoops down and forward from high above the
  house to a low, close view of the kitchen sink, passing close to the wall, and slows as it arrives]. [What happens on the way].
  Motion starts on frame 1. No people, no characters. No text, no captions."
- **Change clip** (one position): the before still → the after still; the prompt names the change and a slow drift ("the camera
  pushes in slowly"); add what must NOT change ("the barrel stays dark, dry and empty, and the valve stays closed").
- **Hook clip** (18 Nov 2026): frame 0 → the state at 1.0 s as a middle keyframe → the first camera position; the prompt names
  the event first ("On the first frame the manhole cover bursts upward on a column of smoke…") and says it starts on frame 1.
- Every prompt without people ends "No people, no characters" (Kling invents figures otherwise).

### 6.4 Scripts to copy (18 Nov 2026)
Start each video from the latest set and rename the prefix: `10-prompts.py` (STYLE without water, WIDE, SET, CAMERA, POS, LOCK,
LOCKZ, INDOOR, REFS), `10-mk.py` (still requests), `10-clips.py` (clip requests, the floor line, middle keyframes), `10-whisper.py`,
`10-timing.py` (pause tightening, beats, the clip plan), `10-build.py` (all the edit tools of Step 9), `09-build.py` (pointers with
tracking), `10-thumbnail.py`, `10-flightmap.py`, `10-post-copy.md`; `pipeline/analysis/` (the checks) and `pipeline/youtube/`
(12.2). Video 11's `11-beat-sheet.md` is the latest beat sheet layout. Earlier per-video files stay in `pipeline/` for the record.

---
