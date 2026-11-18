## 5. The look: Cutaway, no character, a travelling camera (locked 15 Nov 2026; Rule 0 added 18 Nov 2026)

**What it is.** A bright, clean, photoreal-leaning 3D render of one place sliced open like a cake, in soft daylight, with
translucent cyan water where there is water, seen by a camera that flies around and into it like a drone. "You" is the viewer and
nobody stands in for them: hands, small anonymous workers or machines appear only where the work needs them. One small living
thing per video is welcome (a dog, a yellow fish). Captions are one word at a time; nothing else is written on the picture. The
video ends on its first frame, so it loops. The user locked this on 15 Nov 2026 after the two videos without the mascot took 90%
of our TikTok views and 98% of our YouTube views; the camera rules came the same day, modelled on Hidden By Design's power-lines
video ("as long as it accomplishes the same video as the one I referenced").

**Rule 0. The first second (18 Nov 2026).** The scene changes by 1.0 s, big in the frame, on the first word (4.2). The hook clip
is planned, priced and checked before any other clip.

**Rule 1. Animate nearly all of it.** Every line is a clip; plan no holds. A hold is only the fallback for a lost clip: the last
frame of the clip before, with a slow push-in, 3 s at most. Never show a frozen splash, pour, plume of smoke or gauge needle.
Target: something moves inside the picture in 80% or more of the seconds (`check_video.py`).

**Rule 2. One set, a travelling camera.** One sliced-open set for the whole video; each fix is added to it. 7–9 camera positions
under the 200-credit cap (18 Nov 2026; it was 8–12):
the wide view only to open (unless the opening event is a close one), to close the loop and to step back once or twice; every
problem and every fix seen up close from its own position. Anything that needs another place is shown on the set or cut.

**Rule 3. Every clip flies the camera** from one position to another, and each position is a real still of the set from there,
never a crop of another still (a crop makes Kling zoom across a flat picture, which reads as still). On "But" the camera pushes in
or swoops to the problem; the change plays out close while the camera keeps drifting; on "So" it pulls away or flies on. No
cross-fades between different pictures; a whip (a fast swing with motion blur) only for a far jump; a hard cut only where the
setting truly changes.

**Rule 4. Hold the look steady.** Every still is an edit of the wide still or of a neighbouring position, so the set keeps its
parts, colours and materials from every angle. The shared style line names no objects and no place. Night and storm are re-grades
of the same picture (or made in the edit). The first and last frames match part for part.

**Rule 5. Captions:** one word at a time, ALL CAPS, Montserrat ExtraBold, white with a 7 px black stroke and a soft shadow, letters
about 57 px tall at 1080×1920, centred about 75% down the frame. Wide shots keep the subject in the upper 60% with plain ground
below; in close-ups the caption sits over whatever is there.

**Rule 6. Pointers:** solid white arrows about 200 px long with a soft shadow, three or four at a time sliding along the flow, or one
ring with a ~16 px stroke. One device per beat. A pointer appears when the camera arrives and slows, and stays pinned to its detail
while the camera drifts; the camera never stops for a pointer.

**Rule 7. Measure the camera** with `pipeline/analysis/camera_path.py`: moving in 65% or more of the seconds, median parallax 0.3 px
or more, a big move (a quarter of the frame in a second) at least one second in eight with no gap over 15 s, and never still for
more than 5 s. Reference (power-lines video): 66%, 0.46 px, 22 big-move seconds in 88 s, 5 s. Videos 09 and 10 met every target
(78% and 91%, 0.44 and 0.40 px).

**Sound (approved 15 Nov 2026: "yes on the sound").** A quiet, steady bed that fits the place, with no tune, about 19 dB under the
voice for the whole video; four to eight short effects on the moments where something visibly happens, about 11 dB under the voice;
no music, never a copyrighted or trending track. Keep a voice-only master too. Check with `under_the_voice.py`: the quietest
moments 18–22 dB under the voice.

**Narrator (locked 7 Nov 2026):** ElevenLabs, model `eleven_v4`, "Daniel's Voice - Warm, Low, Confident", voice_id
`rFhx8PVgXxOyaeAGq9fq`. One continuous take of the whole script.

**Format:** 9:16, 1080×1920, 30 fps, H.264 + AAC, about −14 LUFS. Kling clips at 720p are upscaled with a light sharpen (6.2 Step 9).

**Retired (for the record):** the mascot look of videos 01–02 and 05–07 (retired 15 Nov 2026; its reference image, Higgsfield job
`f97004b9-f63f-4971-ab16-e0519314a404`, is kept for the channel artwork only); on-screen term labels (15 Nov 2026); cross-fades
between stills (15 Nov 2026).

---
