# Build-steps test (22 Nov 2026)

**Why.** After video 16 the user said it "just looks like the same videos we have been creating" and pointed again at
@whatifplus's helipad video: "I like the way the video builds out the helipad, each step is entertaining to watch, are we
able to follow the videos format while keeping our visual style". This test answers that with pictures. It is not a video
and its subject (a garden shed) is not a video idea. The user approved it on 22 Nov 2026 at about 42 credits with the reserve.
`CLAUDE.md` was not changed (the user: "don't change anything in claude.md file without my approval").

**What was made.** One fix built in four visible steps in our Cutaway look, in daylight, from one locked view, two ways:
- **A, one short clip a step:** four `wan2_7` clips, each between two neighbouring stage stills (2 s, 3 s, 3 s, 2 s).
- **B, all four steps in one clip:** one `kling4_0` clip of 5 s from the empty lawn to the finished shed, with the three
  middle stages as ordered keyframes (`image_references`).

Files: `steps-test-prompts.py` (every prompt and request), `steps-test-jobs.tsv` (job ids), `steps-test-check.py` (the
measurements), `steps-test-demo.py` (the demo edit), `steps-test-sheet.jpg` (both versions at the same moments).

## Result: both ways worked on the first try

| | Stills | A: `wan2_7`, a clip a step | B: `kling4_0`, one clip |
|---|---|---|---|
| Made / usable first try | 6 / 6 | 4 / 4 | 1 / 1 |
| Credits | 7.50 | 15.00 | 12.50 |
| Starts and ends on its stills | view held within 0.35 px over four chained edits | within 0.13 px | within 0.05 px |
| Frames a second | | 30 | 24 |
| Its own sound | | yes, loudest on each impact | yes, loud throughout |

**Spent: 35.00 credits of the 41.69 approved** (`transactions`); the balance is 672.01.

**What each clip does** (read off sheets at 8 frames a second):
- **W1 the slab** (2 s): it falls out of the sky from 0.27 s with its shadow on the lawn, lands at 0.50 s, and a ring of dust
  puffs out and clears by about 1.5 s. The sound peaks at 0.50 s.
- **W2 the walls** (3 s): they go up one after another: the back wall 0.27–0.63 s, the left 0.73–1.0 s, the right and the
  front with its doorway and window 1.4–1.9 s. Knocks in the sound at 0.25, 0.55, 1.0 and 1.6 s.
- **W3 the roof** (3 s): it falls from 0.37 s, is on by 0.75–0.87 s, dust under the eaves until about 1.6 s. The sound peaks
  at 0.75–0.85 s.
- **W4 the paint and the door** (2 s): red paint sweeps left to right from 0.13 to about 0.75 s, then the white door swings
  shut at 1.0–1.3 s. A swoosh at 0.2–0.35 s and a click at 1.5 s.
- **K1, all four** (5 s): slab falls 0.25–0.75 s (no dust); walls shoot up 1.38–1.88 s; roof falls 2.38–2.75 s; paint
  3.25–3.62 s; door 3.75–4.12 s; then a second of rest. About half a second a step with half a second between.

**The demo edit** (`steps-test-demo.py`, free): each version re-timed so every step lands on the word that names it in a
test sentence ("So you drop in a slab, stand up four walls, lower on a roof, and paint it red.", 18 words, estimated word
times at 3.25 words a second), with our one-word captions, a slow push-in on the locked view, and the colour drift taken out.

## What it teaches (for section 7 of the memory, if the user approves the change)
- **A stage ladder holds our look.** Each stage is a LOCK edit of the stage before, with "the lawn stays whole: no hole, pit
  or trench" on every one: no soil leak, no pit, no person, and the house, hedge, fence and cut face stayed put (0.35 px).
- **Raise the camera for a build.** The first set key came back from head height, where a slab on the lawn would be a
  sliver. A POS edit to "a drone at the height of the roof edge, looking down at about 45 degrees" made the lawn a stage
  (13% to 70% of the frame) and kept the cut face in the bottom of the frame.
- **Chained edits drift in colour:** each edit came back a little lighter and less yellow (the lawn L 173 → 189, b 160 → 139
  over four edits; siding, soil and ground about half as much). The demo shifts every frame back to the first still (grass
  on green pixels, the pale ground elsewhere). In a video, add "the lawn keeps exactly the same bright green" to the stage
  prompts and keep the correction in the edit.
- **Name the motion and the order, and say the parts move by themselves.** "Drops straight down out of the sky and lands
  flat … a small ring of dust puffs out", "one after another, the back wall first", "sweeps … from left to right": both
  models did what the words said. "Nobody is there: the parts move by themselves" kept people out.
- **`wan2_7` does its step in the first second** and then holds or settles, so a 2 s clip is enough for one simple step
  (3.00 credits) and 3 s for a step with several parts (4.50). Cut or speed up the tail in the edit.
- **`kling4_0` takes three middle keyframes** and passes through all of them in order in 5 s. One clip, no joins; if a step
  fails the whole 12.50 is re-rendered, where a wan step is 3.00–4.50.
- **Never blend two source frames when re-timing:** a blend doubled the falling slab. Take the nearest frame.
- **Not tested here:** a step that changes the cut ground (a hole dug, a pipe laid), a camera flight on `wan2_7`, a returning
  "tester", and how the models' own sounds sound (they were measured, not heard).

## What it means for a whole video (my estimate, to be priced at a Gate B)
A build video with five fixes of about four steps each, a failure before each fix, a hook and a closing shot is about 67 s
of footage. All on `wan2_7` at 1.50 a second that is about 100 credits of clips, plus about 32 stills (about 38 tries,
47.50), the voice (5.52) and sound (about 5): about 158, or about 182 with the 15% reserve. On `kling4_0` alone it does not
fit under 200.
