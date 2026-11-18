## 7. Production lessons that still apply (collected from videos 01–11; consolidated 18 Nov 2026)

### 7.1 Stills (seedream)
- **Stills take 1.6–1.8 tries each** in this look; budget for it. `seedream` takes about 8 jobs at once (more are refused with
  429, no charge).
- **The style key decides the layout; fit the plan to it** (video 10). Give the layout in its prompt ("the roof peak about 10%
  from the top, the pipe about 60% down, plain soil below") and the deep-block line (6.3).
- **Real close-ups need "Extreme close-up: the [part] fills most of the frame"**; "close-up of" gives a wide shot. "Almost touching
  the window … the frame is not in view" got the tightest one (video 10).
- **Describe parts as the camera sees them** ("the peak of the roof, at the front end of the ridge"). Seedream joins new parts to
  old ones ("stands a little to the right of the water pipe and does not touch it") and drops parts (name what stays).
- **The STYLE line leaks** into close-ups: soil under floors, cut floors, cyan water. Indoor stills carry INDOOR; rooms carry "the
  floor is solid wood and nothing is cut open; there is no water anywhere". An object named in the shared line appears in every
  shot (video 04's blue pumps).
- **Make neighbouring positions from each other**, not all from the wide (made from the wide, two room close-ups lost the ceiling).
- **A detail the wide drew wrong carries into every edit of it:** fix it with one LOCKZ edit that names the swap, with a second
  reference showing the right part (video 10).
- **Edit it out:** "Change only this: remove … Everything else identical" removes a stray object first time.
- **References copy the whole layout;** use one only for "the same scene, change X".
- **A small thing inside a pipe won't draw in a wide view:** give the pipe a see-through window or make a separate close-up.
- **A position that fails twice is dropped**, not forced. Keep edit chains to three or fewer (grain grows with each edit; denoise
  with `cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 7, 21)` if needed).
- **Lighting changes are surer in the edit** (`LIGHTS`); a lights-off re-grade came back almost as bright.
- Wording that fixed specific drift: storm skies need "the whole sky is dark grey with low, heavy storm clouds … no island, no
  smoke, no volcano, no fire"; buried things need "completely buried: above the surface there is only smooth white snow".

### 7.2 Clips (Kling)
- `kling4_0` takes 12–13 jobs at once on Ultra and finishes them in 4–17 minutes. It returns about 724×1284 at 720p.
- **Every keyframe of one clip must agree on the state of things** (a drained tub refilled on screen when a middle keyframe showed
  it full).
- **Say what must not change** ("the barrel stays dark, dry and empty"): Kling leaks the next beat's state into the clip.
- **Kling runs past the action** (foam pouring out of the cutaway): trim to the good window in the edit.
- **Indoor sets grow pits, steps or soil mid-move** though both stills are clean: the FLOOR line in every indoor clip prompt from
  the start, and a 5-frames-a-second check.
- **A move one storey up or down a wall stacks a second copy of the building:** give it a middle keyframe or splice it in the edit.
- **A change clip can come back with a dead-still camera:** add the move in the edit (`PUSH`), and ease the next clip out.
- Kling invents people unless the prompt says "No people, no characters". Electricity, water, fire, steam and smoke animate well.
- Big storms over a structure close under the waterline came out wrong twice (video 05): frame storms with plenty of water between.

### 7.3 Camera and motion
- **A crop of a still is not a camera position:** Kling zooms across a flat picture and it reads as still (video 08: 20% moving).
- **What moves must be big in the frame:** water in a thin pipe, faint haze and a fingernail-sized rat don't register.
- **Middle keyframes work:** one clip can pass through three positions or stages (wide → close → wide).
- Measure the pilots before the batch; videos 09 and 10 met every target this way.

### 7.4 Edit, captions and pointers
- ffmpeg's xfade slide transitions write junk on their first frame (a green strip): smear the edge with `fillborders` during whips.
- The clip after a hold or a push starts at that zoom and eases back (`EASE_AFTER`); never cut a clip's first frames to fit a line
  (`FULLFIT` plays it whole and faster).
- Measure pointer and arrow positions on a gridded frame of the rendered segment, not on the still (Kling drifts from the keyframe).
- Draw ASS shapes from a top-left origin with `\an7` (libass misplaces shapes around negative coordinates).
- Fonts: `npm pack @fontsource/montserrat@5.1.0`, then fontTools (`pip install fonttools brotli`) converts the 800 weight to a TTF
  named "HBX Caption".

### 7.5 Narration and sound
- Daniel's raw pace runs 2.9–3.3 words a second by take; pause tightening and `atempo` up to 1.1 bring it to ~3.5. Never speed it
  more than 1.1×; cut words instead.
- To fix a pronunciation, respell it in the text sent to the voice ("doo-er" for dewar); the captions keep the real word.
- Room-tone beds come back very quiet (mean −64 dB): set every level by measurement, never a fixed gain.
- Time each effect from its loud moment on the picture; cut a long effect short if the picture stops (the `FX` cut value).

### 7.6 Covers
- Build covers from frames of the clean master when no still holds the moment; check the arrow lands on what the words name and
  that the picture matches the claim (a cyan glint read as water at tile size).
- Sizes: YouTube 1080×1920 JPG under 2 MB; TikTok's cover upload crops to 3:4, so upload the 1080×1440 crop (y 240–1680 of the
  1920 master). Keep the headline between y ≈ 300 and 1440, clear of TikTok's buttons (x > 940 below y ≈ 950).

### 7.7 Sessions, network and tools (to 18 Nov 2026)
- **Reachable from a session:** the Higgsfield generation CDN (`d8j0ntlcm91z4.cloudfront.net`), `upload.higgsfield.ai`,
  `elevenlabsusercontent.com`, `www.youtube.com`, `i.ytimg.com`, `www.tiktok.com` and its video host
  `v16-webapp-prime.us.tiktok.com`.
- **Not reachable:** `huggingface.co` (so Whisper runs in the Higgsfield sandbox), the upload CDN `d2ol7oe51mr4n9.cloudfront.net`
  (give those links to the user), and for WebFetch `en.wikipedia.org`, `cdc.gov`, `weather.gov` and many blogs (use search
  summaries and say so).
- **The Higgsfield sandbox:** foreground calls time out at about 60 s (run Whisper and renders with `background:true`); pip fails
  there; it keeps outputs for about 24 hours.
- **Local assembly works:** ffmpeg with libass, zoompan and xfade, Python and npm; a full render takes about 2 minutes.
- **Session restarts change the scratchpad path:** keep job ids in `NN-jobs.tsv` and commit often.

### 7.8 Things that go wrong, and the fix
| What goes wrong | Fix |
|---|---|
| The opening shows a finished scene and nothing happens for 2–3 s | Rule 0: re-plan frame 0 as the "before" and put the event by 1 s (4.2) |
| A travel clip only zooms (parallax near 0) | Its two stills are one view at two sizes: make the end still a real position |
| The set changes between positions (pipes move, colours shift) | Make each position from the wide or a neighbour with POS; compare them at Gate C |
| A still of something in motion looks frozen | Give the line a clip; never cut to a still of a pour, splash or needle |
| The last frame doesn't match the first | Make the END still from the last stage still; `PULL` in the edit |
| A night or storm still redraws the set | Re-grade the day still ("the same water colour; nothing glows") or do it in the edit |
| The sound competes with the voice | Lower the bed to 18–22 dB under the voice; drop an effect that lands on a stressed word |
| The balance is below the quote | Offer a shorter script or fewer positions, and name the lines that would lose their clip; never start a run you can't finish |
| The narration runs long | Cut words; don't speed it past 1.1× |

---
