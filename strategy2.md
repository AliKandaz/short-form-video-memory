# Style 2: Photoreal AI Build Stories (strategy2.md)

**Created on 21 Nov 2026** at the user's request: "create a step by step prompt to create videos similar or inspired by this
video I shared. pretty much I want the same thing as claude.md but for this style video on a different file so I can alternate
between video styles". The video is @scapemagicc's septic-tank tiny house (1.2). This file is the second style's memory, laid out
like `CLAUDE.md` (style 1, the 3D cutaway explainers). Every section carries a date; "my read" marks interpretation rather than
measurement. Nothing in this style has been made yet: the plan, the prompt lines and the prices are drafts until the first video
proves them.

## 0. Start here (21 Nov 2026)

**What we make in style 2.** A vertical photoreal AI video of about 50 s, with no narration and no words on screen: one humble,
unloved thing (an old ski gondola, a derelict signal box, a broken windmill) turned into a cozy little home, filmed as a
time-lapse from fixed cameras. Frame 0 is the "before"; something big happens to it by 1 s; the outside gets built stage by
stage from one locked view; about half the video is the inside going from a bare shell to a warm, finished room; a last touch at
real speed; the outside at dusk to close. Build sounds only, no music. Our own recurring builder, the same person in every
shot. The AI label is on every time.

**How the two styles share the work.**
- **Read `CLAUDE.md` section 0 first, every time.** Its standing rules apply to both styles: never spend Higgsfield credits
  before the user approves the quote at Gate B; **at most 200 Higgsfield credits a video, the 15% reserve included**; stop at the
  four gates (A story, B quote, C stills, D pilot clips); work from what can be read from outside (no retention figures); never
  reuse a reference account's wording; when the memory changes, update both copies.
- **Used as they are from `CLAUDE.md`:** 6.0 (the tools and how to call them), 6.1 (the credit rules), 7.1–7.2 and 7.4–7.5 (the
  lessons about seedream, Kling, the edit and the sound; this file's section 7 lists the ones that carry over), 7.7 (what a
  session can reach), 12 (reading TikTok and YouTube from a session).
- **Replaced by this file for style 2:** CLAUDE.md 2–5 (plan, ideas, script, look), 6.2–6.4 (the steps, prompt lines and
  scripts), 8 (posting) and 9 (the log).
- **Where things live:** this file next to `CLAUDE.md` in the repo `AliKandaz/short-form-video-memory`, and attached to the
  "Short-Form Video Memory" artifact (https://claude.ai/artifact/Fvbzc2HQyDxne7Y8NsrgvX, Artifact tool, action "read", path
  "strategy2.md"). Scripts for style-2 videos go in `pipeline/` with the prefix `s2-NN-` (s2-01, s2-02, …).

**Status on 21 Nov 2026.**
- **s2-01 at Gate B (21 Nov 2026):** the kickoff asked for I1 (the gondola) with builder b and cut B plus A. I1 failed the Gate A
  check and was dropped (3); I5, the chicken coop, was approved at Gate A and quoted at 195.79 (`pipeline/s2-01-beat-sheet.md`).
  Nothing generated. The paste-in prompt is section 11.
- **The hold in CLAUDE.md section 0 comes first:** the user's in-app checks of both accounts (YouTube Studio → Restrictions and
  youtube.com/features; TikTok → Account status). They decide whether a new YouTube channel is allowed (only if the old one is in
  good standing; never to get around a strike).
- **Decisions (21 Nov 2026):** builder b (5); the first video is I5 (I1 was dropped at Gate A, 3); posting on TikTok and
  YouTube (the user). **Still open:** the main accounts or a new style-2 pair (2.1 recommends a new pair).
- **Credits:** 1,030.00 on 21 Nov 2026, shared by both styles: about five videos at 185–200 before the Ultra plan renews (3,000 a
  month since 11 Nov 2026; check the date).

**Map of this file:** 1 what works (evidence) · 2 the plan · 3 ideas · 4 the story · 5 the look · 6 runbook · 7 lessons ·
8 posting · 9 video log · 10 topics to avoid · 11 paste-in prompt · 12 history.

---

## 1. What works in this style (evidence, 20–21 Nov 2026)

Read from public pages only (CLAUDE.md 12). Four videos were measured frame by frame; the rest is account-level numbers.

### 1.1 The reference account (read 20–21 Nov 2026)
- **@scapemagicc** (display name "Aiworkflows2"), TikTok: 722.5K followers (20 Nov), 86 videos from 11 Jun to 21 Nov 2026.
  **All 86: median 467K views, 30 over 1M, 7 under 50K**; 57–86 s long, median 62 s. Posts about once a day, at about 23:00 UTC
  (6 pm ET). The bio sells their workflow, so part of the business is teaching (my read: their numbers are a daily machine with
  a 35% hit rate, not one lucky video).
- **Their biggest:** a mud cave turned into a tiny house 91.5M (23 Jul), a small garden into a modern tiny house 76.5M (27 Sep),
  a flooded sea cave 49.3M (27 Jul), a house from old tires 28.3M (6 Aug), the septic-tank tiny house 20.2M (17 Nov; 9.8M on 20
  Nov), a house inside a square pipe 17.0M, an underwater bunker 16.6M, a two-storey bunker under a rock overhang 14.3M, a dirty
  pool into a bunker 12.3M.
- **They re-make winners:** septic and plastic tanks five times (238.9K in Aug, 2.0M, 64.7K, 2.4M on 13 Nov, then 20.2M on 17
  Nov), pools seven times, school buses four times, dumpsters three times.
- **Packaging:** captions are one plain line, mostly first person ("I build Cozy bunker inside …", sometimes naming a person who
  doubted or annoyed the builder; for ten days in mid-September emoji-heavy hook lines instead), then "Build of …" from 12 Nov,
  with 4–5 tags (#offgrid #build #tinyhouse #bunker #cozy). TikTok filed all 29 videos checked on 20 Nov under "Home & Garden, Daily Life, Lifestyle" and put its own AI-generated
  label on 27 of them; the creator's own label was off on all 29. No penalty shown on any.
- **Engagement on the septic-tank video** (20 Nov, at 9.8M): likes 3.2% of views, saves 0.31%, shares 0.06%, 0.22 comments per
  1,000 views (ours run 0.23).

### 1.2 The four videos measured (cuts counted with ffmpeg scene detection at 0.28, cuts under 0.4 s apart merged)
| Video (views on 21 Nov 2026) | Length | Hard cuts | Frame 0 → by 1 s | Inside share | Witness |
|---|---|---|---|---|---|
| Septic tanks → tiny house, 20.2M, https://www.tiktok.com/@scapemagicc/video/7709278780715535630 (the user's pick) | 80.5 s | 50 shots, median 1.42 s, longest 4.27 s | a junk yard next to a pool party → the neighbours splash him; at 1.4 s his face, black eye, dripping | from 44 s (45%) | the pool guys at the fence all video; the last shot repeats the first with them staring |
| Small front garden → container tiny house, 76.5M, …/video/7690339464568261902 | 72.2 s | 70 shots, median 0.76 s | an overgrown front garden → a flamethrower burns it from 0.5 s | from ~31 s (57%) | an old neighbour at the fence |
| Mud cave → tiny house, 91.5M, …/video/7665848503767207182 | 63.4 s | 6 shots (median 7.4 s) | a mud-filled pit under a rock overhang → the builder pumps it out from 0.5 s | from ~22 s (65%) | none |
| Old tires → tiny house, 28.3M, …/video/7671057998814399758 | 62.3 s | 4 shots (one 44.7 s long) | an empty marked plot on a prairie → a dump truck tips a load of tires at 0.5 s | from 25 s (60%) | none |

- **Sound** (measured on the septic-tank video only): no narrator (faster-whisper found only a laugh from the neighbours at about
  27 s) and no music that a spectrogram shows: build sounds (sawing, hammering, digging, drilling) that change with every cut,
  loudness jumping between about −55 and −18 dB from second to second. Nothing has been listened to (CLAUDE.md 12.3).
- **No words on screen** in any of the four. **The builder changes between videos:** a long-bearded man in a plaid shirt (septic
  tanks), a long-haired man in a white T-shirt and black overalls (the garden), and a man in a grey T-shirt and a cap in both the
  mud cave and the tires (perhaps one recurring look). No strong recurring character.

### 1.3 The devices all four share (21 Nov 2026)
1. **Frame 0 is the "before"**, big in the frame: the junk yard, the overgrown garden, the mud pit, the empty plot.
2. **Something big happens to it by 0.5–1 s:** a splash, a flamethrower, a pump, a dump truck. The same rule as our Rule 0 (CLAUDE.md
   4.2), and it holds in every one.
3. **Locked cameras and time-lapse:** the camera stays put while the builder works fast (blurred and ghosting in places) and the
   place changes stage by stage: clear, base, walls, roof, door, finish.
4. **About half the video or more is the inside:** a bare shell → membrane and insulation → floor → walls and ceiling → paint →
   lights → furniture → a warm, cozy room (rugs, lamps, plants, blankets). The cozy room is the payoff.
5. **No narration, no captions, no music:** build sounds carry it (measured on one).

My read: the fast cuts in the two cut-heavy videos also hide the AI's drift (the septic tanks change shape between shots; a drill
shows a gibberish brand; the rooms inside are far bigger and brighter than the tanks could hold).

### 1.4 Two cuts of the same spine (21 Nov 2026)
- **Cut A, the one-take time-lapse** (the mud cave 91.5M and the tires 28.3M): 4–8 shots; each locked view plays as one
  continuous take while the build happens in it. The cheapest to make: a chain of stage stills from one camera, each clip joining
  two stages.
- **Cut B, the fast-cut story** (the septic tanks 20.2M, the user's pick, and the garden 76.5M): 50–70 shots of 0.8–1.4 s; the
  locked views come back again and again with tool close-ups between, and a witness (the neighbours) at the start and the end.
- **The same stills and clips can make both:** the locked-view clips are a chain, so they play straight through (cut A) or chopped
  up between close-ups (cut B). The edit is free, so every style-2 video gets both cuts (4.1).

### 1.5 What we take, what we don't, and the risks (21 Nov 2026)
- **Take:** the spine (1.3), both cuts, the cozy payoff, the no-words sound design, the posting time, the habit of re-making a
  topic that worked.
- **Don't take:** their topics (section 10: all 86), their wording, their builders' looks, their exact openings (the pool-party
  splash, the flamethrower in a front garden, the tire truck, the mud pump), and violence (the black eye).
- **Risks:**
  - **It is fantasy shown as real footage.** The AI label goes on every video and YouTube's altered or synthetic content box gets
    ticked (8). The captions never claim it's real or that the poster built it.
  - **It doesn't fit style 1's promise** ("Every fact is checked before it's animated", in the YouTube channel's description). That's
    one more reason for separate accounts (2.1).
  - **Nothing in a video may hurt someone who copies it** (4.3).
  - **YouTube's "inauthentic content" rule** (CLAUDE.md 10) is judged across the channel: mass-produced templates aren't eligible
    for ads. One recurring builder, our own ideas and real variety between videos are the defence.

---

## 2. The plan for style 2 (proposed 21 Nov 2026; the user decides)

### 2.1 Where to post (open: the user decides)
**Recommended: a separate TikTok account and a separate YouTube channel for style 2.**
- Style 1's 10-video plan judges one lane on the main accounts (CLAUDE.md 2.1, 2.5). A second style on them would mix the test
  audiences again, the problem CLAUDE.md 9.3 describes.
- The audiences differ: TikTok files this style under "Home & Garden, Daily Life, Lifestyle" (1.1) and ours mostly under
  "Science, Education" (CLAUDE.md 9.1).
- YouTube looks held back at the channel level (CLAUDE.md 1.6), and a fresh channel is already being weighed: only if the old
  one is in good standing, never to get around a strike.

If the user posts both styles on the same accounts: never two videos the same day, alternate days, and read each style's
numbers separately in its own log.

### 2.2 Cadence and alternating
- One video a day at most across both styles, in the early evening US Eastern (6–7 pm ET, the reference account's slot too).
- Alternate by the plan's checkpoints, not after each video: style 1's ten keep their order (CLAUDE.md 2.3); style-2 videos go in
  between them.

### 2.3 Budget
- At most 200 Higgsfield credits a video, the reserve included (CLAUDE.md 6.1), the same cap as style 1. The standard plan is
  about 185 (6.1 here).
- **One balance for both styles:** 1,030.00 on 21 Nov 2026, about five videos of either style before the Ultra plan renews.
- ElevenLabs credits are separate: no narration in this style, so only the sound (about 200–230 a video with a silent model; 6.1).

### 2.4 How we'll judge (from outside, as CLAUDE.md 2.5)
- **Each video at 72 h:** TikTok over ~2K = passed the first test; YouTube over ~1K = tested normally; 10K+ = a breakout. Log
  both in section 9 with the cut, the model, the shot count and median, and the frames-0–2 s verdict.
- **Checkpoint after three style-2 videos** (proposed): if none passes TikTok's first test, stop and review the opening, the object
  and the cut before making a fourth. A new account starts from zero, so compare with our own bars, not with @scapemagicc's.

---

## 3. Ideas (21 Nov 2026), in the suggested order

Each is one humble thing turned into a cozy home, checked on 21 Nov 2026 against all 86 of @scapemagicc's videos (none is on it)
and against YouTube (CLAUDE.md 12.2: `yt_saturation.py`; it counts real and AI Shorts alike). **Before Gate A, every idea is
checked again:** re-fetch @scapemagicc's list (they post daily), rerun the saturation check, and apply CLAUDE.md 1.6's topic rule:
if more than about three AI build videos on the same object went up in the last 30 days, drop it; don't retitle it.

For each: frame 0 → the event by 1 s; the outside ladder (one locked view); the inside ladder (one locked view from the door); the
last touch; the witness for cut B; watch-outs; demand.

**Re-checked later on 21 Nov 2026 with the content farms' own phrasing** ("abandoned / old <object> turned into a cozy / tiny
home", "restoring old <object>"), which the first check missed, and with the Shorts dated (`yt_channels.py shorts:<id>`): **the
genre is farmed on YouTube.** Seven of the eight objects have a cluster of AI build Shorts (most at 0.5–3K views) and long AI
story videos from the last few weeks: I1 the gondola (about 20 Shorts from Feb to Oct, the best 1.8M; five long ones 5 days to 4
weeks old), I2 the signal box (about 12; long ones 11 days, 13 days and 3 weeks old), I3 the fire lookout (about 20; a long one 8
days old), I4 the turbine blade (about 8), I6 the windmill (about 14; long ones 5 days to a month old), I8 the grain silo (about 14,
the best 155K, labelled AI; long ones a day to a month old): all over the topic rule. I7 the glass cottage is at the limit (three
since 14 Nov). **I5 the chicken coop passes** (six AI coop-to-home Shorts, 27 Jul to 21 Oct, 1.0K–6.0K; one in the last 30 days, a
kitten cottage) and became s2-01.

**I1. The ski gondola that became a treehouse** (a snowy backyard; ski season, post in December). **Dropped 21 Nov 2026: crowded.**
- **Frame 0:** a snowy backyard with a bare oak; a dented, faded red gondola cabin on a flatbed truck, the builder beside it.
  **By 1 s:** a crane lifts it and it swings toward the camera, snow sliding off its roof.
- **Outside:** a platform built between the oak's branches → the gondola set on it → a ladder and a small railed deck → the
  windows cleaned, a wooden door → string lights and fresh snow at dusk.
- **Inside:** the bare cabin with its old benches → benches out, insulation in → wood-lined walls and floor → a cushioned bench
  bed under the windows and a fold-down table → sheepskins, a lantern and a book; snow falling outside. **Last touch:** the
  lantern lit.
- **Witness (cut B):** the neighbour in a dressing gown, coffee in hand, laughing at frame 0; at the end staring at the glowing pod.
- **Watch out:** no resort names, lift-maker logos or brand colours; a rail round the platform.
- **Demand:** "Restoring an old mountain cable car into a cozy tiny cabin" 1.8M (a Short), a ski-village Short 989K; no other
  gondola builds on the page.

**I2. The railway signal box that became a home** (a country branch line). **Crowded (21 Nov 2026).**
- **Frame 0:** an abandoned brick-and-timber signal box beside the tracks, boarded windows, ivy. **By 0.5 s:** a train thunders
  past in the foreground; the box shakes, leaves and dust fly.
- **Outside** (locked view from across the tracks, low, behind a fence): ivy off → new windows → the roof re-slated → paint in
  dark green and cream → a strip of garden → lamps lit at dusk as the next train streams past.
- **Inside:** a dusty room with a row of rusty levers → cleaned, the levers kept as a feature → a wood floor → a long window desk
  and a reading nook → a kitchen corner → warm light; a passing train's lights sweep the room. **Last touch:** the kettle on.
- **Witness (cut B):** the train driver who laughs in frame 0 and waves at the lit home at the end.
- **Watch out:** no real railway names, logos or liveries; the builder never on the tracks with a train coming.
- **Demand:** railway-enthusiast Shorts (a signalman 467K), a night in a signal box 11K (Short) and 273K (long); no conversion
  builds on the page. An enthusiast audience, the kind CLAUDE.md 1.6 found gets reach.

**I3. The fire lookout that became a sky cabin** (a forested ridge). **Crowded (21 Nov 2026).**
- **Frame 0:** a rickety wooden fire lookout on a ridge in fog, its glass cab broken. **By 1 s:** a gust rips the old tin roof off
  the cab and it tumbles away down the slope (nobody near it).
- **Outside** (locked view from a rock beside it, the tower filling the frame): new stairs → a new cab frame → wraparound windows
  → a railed catwalk → the roof → warm light at sunset above a sea of clouds.
- **Inside:** the bare cab → floor → a bed in the middle of the room → a small wood stove with its flue through the roof, maps and
  binoculars → dusk over the clouds. **Last touch:** the stove lit.
- **Witness (cut B):** a hiker who shakes his head at frame 0 and drinks tea on the catwalk at the end.
- **Watch out:** a harness and rails at height; no agency badges or logos.
- **Demand:** lookout-life Shorts 5.6M, 2.6M, 1.6M; restorations in long videos 2.7M (two months old) and 2.7M (one month): a hot
  topic, with no AI build Shorts on the page.

**I4. The wind-turbine blade that became a cabin** (a windy hill by the sea). **Crowded (21 Nov 2026).**
- **Frame 0:** an empty grassy hill by the sea, cows grazing. **By 1 s:** a giant white blade on an extra-long truck swings round
  the bend; the cows scatter.
- **Outside:** a section of the blade set on a stone base → glass at both ends → a deck at the round end → lights at dusk, the wind
  bending the grass.
- **Inside:** the hollow white tube → a floor → curved wood lining → a bed at the big round window → a kitchenette → cozy while
  the wind howls. **Last touch:** a blanket thrown on the bed.
- **Witness (cut B):** the cows, staring at frame 0 and lined up at the deck at the end (the joke).
- **Watch out:** dust masks when cutting fibreglass; no turbine-maker logos.
- **Demand:** nothing on the page (the results are small home turbines): untested, and the most novel picture of the eight.

**I5. The chicken coop that became a guest cabin** (a suburban backyard). **Passes (21 Nov 2026): s2-01, at Gate A.**
- **Frame 0:** a sagging old wooden coop with hens pecking. **By 1 s:** its roof gives way in a puff of straw and feathers; the
  hens scatter, unhurt.
- **Outside:** the hens moved to a new little coop beside it → the old coop's frame rebuilt bigger → windows → a porch → paint →
  lights.
- **Inside:** bare boards → insulation → wood lining → a bed → a small desk → cozy. **Last touch:** a hen hops onto the porch rail
  and peers in (the joke; the hens' new coop matches the cabin).
- **Witness (cut B):** the family at the back door laughing at frame 0 (the caption can carry a mother-in-law joke).
- **Watch out:** animals unharmed; no real people named.
- **Demand:** coop builds are big on Shorts (5.2M, 2.4M, 1.0M); a coop turned into a guest cabin isn't on the page.

**I6. The broken windmill that became a round home** (a hill in farmland). **Crowded (21 Nov 2026).**
- **Frame 0:** a derelict brick windmill with broken sails. **By 1 s:** a broken sail snaps in the wind and crashes into the field
  (nobody near it).
- **Outside:** scaffolding → a new cap → new sails turning → windows → a railed balcony round the middle → lights.
- **Inside:** the bare round stone room → a floor → a spiral stair → a curved kitchen → cozy. **Last touch:** the lights on as the
  sails turn past the window.
- **Witness (cut B):** a farmer on a tractor.
- **Watch out:** no real mill names; a harness at height.
- **Demand:** little conversion content (a windmill stay 4.6K); "He Built A Windmill From Junk" 15M is a different topic.

**I7. The heap of old windows that became a glass cottage** (a garden in late autumn). **At the limit (21 Nov 2026).**
- **Frame 0:** a muddy garden and a big tarp over a heap. **By 1 s:** the builder whips the tarp off: hundreds of old wooden
  windows.
- **Outside:** a timber frame → the windows fitted as a patchwork wall → a roof of old glass doors → the frames painted in colours
  → plants → it glows in the rain at dusk.
- **Inside:** a glass room with a wood floor, citrus trees, a reading chair, a rug and fairy lights. **Last touch:** rain on the
  glass, the builder sits down with a book.
- **Witness (cut B):** neighbours laughing at the "window hoarder" over the fence.
- **Watch out:** gloves for glass; nothing shatters near anyone.
- **Demand:** modest: real DIY Shorts 22K–116K; long videos 1.6–3.5M.

**I8. The grain bin that became a round home** (a farm field). **Crowded (21 Nov 2026).**
- **Frame 0:** a rusty corrugated grain bin in stubble. **By 1 s:** pigeons burst out of its door as the builder pulls it open.
- **Outside:** windows cut (sparks) → a wraparound deck → a new roof cone with a skylight → stain → lights.
- **Inside:** the round shell → insulation → floor and a spiral stair → a ring kitchen → a loft bedroom under the cone → cozy.
- **Witness (cut B):** a farmer on a tractor.
- **Watch out:** no manufacturer logos on the bin.
- **Demand:** about seven small silo and grain-bin tiny-house Shorts (best 67K; several look AI-made): check their dates at Gate A
  and drop it under the topic rule if more than three are from the last 30 days.

**Reserve:** the clock tower that became an apartment (the bedroom behind the glowing clock face; no conversions on the page,
demand unproven). **Dropped:** the storm-felled tree that became a log cabin (crowded: "How a Fallen Tree Becomes a Log Cabin" 2.2M
and more fallen-tree cabin Shorts at 1–3.5M).

---

## 4. The story (replaces CLAUDE.md 4 for style 2; 21 Nov 2026)

### 4.1 The skeleton (about 50 s; cut B shot lengths)
```
FRAME 0 (0 s)      The "before": the humble thing in its place, big in the frame, the builder in shot. Cut B: the witness too.
EVENT (by 1 s)     Something big happens to it: lifted by a crane, a train roars past, a roof torn off, a tarp whipped away.
REACTION (cut B)   1-1.5 s: the builder's face or the witness's grin. Cut A skips it.
OUTSIDE (~2-20 s)  One locked view, 5-6 stages (clear, base, shell, roof, finish, lights), the builder in time-lapse.
                   Cut B: each stage seen 1-2.5 s at a time, 1-2 tool close-ups (0.5-1.5 s) between.
INSIDE (~20-42 s)  One locked view from the door, 7 stages: bare, insulation, floor, walls, ceiling and lights, furniture, cozy.
                   About half the video, as in all four reference videos (1.2).
LAST TOUCH (~4 s)  At real speed: a lamp or a stove lit, a blanket thrown on the bed, the kettle on.
PAYOFF (~3 s)      Outside at dusk, the windows glowing, the outside view of frame 0 so it loops. Cut B: the witness staring.
```
- **Cut B** (make first): 25–40 shots, median about 1–1.5 s, nothing over 4 s. **Cut A** (from the same clips): 4–8 shots, each
  view played straight through with no close-ups.

### 4.2 The opening rules (style 2; the evidence is 1.3)
1. **Frame 0 is the "before"**, never a finished thing: the humble thing fills at least a third of the frame, the builder in it.
2. **Something big happens to it by 1.0 s**, in the picture, not just a camera move: it is lifted, struck, torn, uncovered or
   flooded with light.
3. **Nothing that hurts anyone,** people or animals: the event never lands on a person; animals scatter unhurt.
4. Checked twice: at Gate A as frame 0 / the event by 1 s / what follows at 1–2 s, and at Gate D on the hook clip's frames at 0,
   0.5, 1, 1.5 and 2 s.

### 4.3 Story rules (21 Nov 2026)
- **One humble thing, one place, two locked views** (outside, inside) plus 2–4 close-ups. Anything that needs another place is cut.
- **The stage ladders are the script:** write the outside ladder (O0 → O6) and the inside ladder (I0 → I7) before anything else;
  each stage is a visible change, big in the frame.
- **Half the video inside, ending cozy:** warm lamps, soft blankets, a rug, plants, dusk outside. The cozy room is the payoff.
- **The witness (cut B)** doubts or laughs at frame 0 and stares at the end, roles reversed. Mockery, never violence. A
  neighbour, a hiker, a train driver, or animals (cows, hens) for the joke.
- **One small joke** near the end, shown not told (the hen peering in, the cows at the deck).
- **No words:** no narration, no captions, no signs or text anywhere in the picture.
- **Nothing that would hurt someone who copied it:** no sleeping in sealed or buried containers; no fuel-burning heater in a small
  closed room (a wood stove only with its flue through the roof); a harness and rails at height; gloves and masks for glass and
  fibreglass; nobody near anything that falls.
- **Optional signature (untested):** at the reveal, the finished build is sliced open like a cake for 1–2 s to show every room at
  once: style 1's look as a calling card. It costs one still and one clip (about 10 credits); try it once and judge it.

---

## 5. The look (21 Nov 2026; drafts until the first video's Gates C and D)

- **Photoreal, like a phone or drone video:** natural light (golden hour or overcast), true colours, real textures and wear, a
  slightly wide lens. Not a cutaway, not cartoonish, nothing cut open (except the optional signature, 4.3).
- **Locked cameras:** the outside view at eye level or a little above it, from where the whole build stays in frame; the inside
  view from the doorway, wide, at chest height. The framing never changes between stages.
- **Time-lapse:** the builder moves fast and blurs a little; tools and materials come and go; the light stays steady within a
  view (it may warm toward dusk across the outside ladder).
- **Close-ups at real speed:** gloved hands, a tool and a material, filling most of the frame (sawing, screwing, plastering,
  rolling paint).
- **The cozy end:** warm practical lights, wood, white plaster, a thick rug, plants, blankets, a window with dusk or snow.
- **Our builder, the same in every shot** (a recurring character, unlike @scapemagicc's; my read: it builds recognition and saves
  stills, since one builder key serves every video). **To choose at the first Gate A:** (a, recommended) a woman in her thirties
  with a dark braid, a mustard beanie, a faded denim work shirt and brown work trousers; or (b) a man in his forties with a short
  salt-and-pepper beard, a navy beanie, an orange work jacket and grey cargo trousers. Neither looks like any of @scapemagicc's
  builders. The builder key's job id goes in section 9 once made.
- **Sound:** build sounds and one ambience, no narration, no music (never a copyrighted or trending track): a time-lapse build bed
  for each view (hammering, drilling, sawing, sped up), 6–8 effects on the events (the crane, the train, the roof, the door, a lamp
  click, the stove), and the place's ambience under the last touch and the payoff (wind, birds, rain on glass, snow quiet).
- **Format:** 9:16, 1080×1920, 30 fps, H.264 + AAC, about −14 LUFS; 720p clips upscaled with a light sharpen (as CLAUDE.md 5).
- **No text anywhere:** no captions, pointers, logos, brand names, signs, flags or numbers. Tools show no brand.

---

## 6. Production runbook (style 2; for Claude, when asked to make a style-2 video; 21 Nov 2026)

> Trigger phrases: "make a style 2 video", "make I1", "make strategy2 video #N", or the paste-in prompt (11).
> **Never generate anything (images, clips, audio) before Gate B is approved.** The story, the shot list and the quote are free.

### 6.0 Tools and prices (checked 21 Nov 2026; re-check on the day, prices change)
The tools and how to call them are CLAUDE.md 6.0. For style 2:
| Job | Tool | Cost on 21 Nov 2026 |
|---|---|---|
| Stills: the builder key, the two view keys, the stage ladders, the close-ups | `seedream_v5_pro`, `resolution:"1k"`, `aspect_ratio:"9:16"`, references as `image_references` | 1.25 an image (`gpt_image_2_6` medium 1k is 0.5, untested) |
| Clips, the standard model | `kling4_0`, image-to-video, `start_image` + `end_image`, 720p, 9:16 | **7.50 a 3 s clip** (2.50 a second; it bills at least 3 s) |
| Clips, the challenger (tested at the first video's Gate D) | `wan2_7`, start and end frames, 720p, makes its own sound, 2–15 s | 4.50 a 3 s clip (1.50 a second) |
| Other clip models priced, not tested | `kling3_0` 6.00 a 3 s clip; `grok_video_v15_lite` 3.00 (no sound); `veo3_1_lite` 6.00 a 4 s clip | |
| Build sounds and ambience | ElevenLabs flow of sfx nodes (CLAUDE.md 6.2 Step 6b) | about 3.33 ElevenLabs credits a second of sound |
| Assembly, checks, uploads | local ffmpeg; `pipeline/analysis/`; `media_upload` → PUT → `media_confirm` | free |

### 6.1 The standard plan under the cap (21 Nov 2026 prices)
| Item | Plan | Credits |
|---|---|---|
| Clips (`kling4_0`, 720p) | 17 clips, 52 s: the hook 3 s (O0 → O1); outside chain 5 × 3 s (O1 → O6); inside chain 7 × 3 s (I0 → I7); 2 close-ups × 3 s; the last touch 4 s (I7, start only); the payoff 3 s (O6 → dusk) | 130.00 |
| Stills (`seedream_v5_pro`) | 19 keyframes: the builder key, O0–O6, I0–I7, 2 close-ups, the dusk payoff; about 25 tries | 31.25 |
| Base | | 161.25 |
| Reserve (15%) | one or two clip re-renders, a few still retries; on the first video, the `wan2_7` pilot pair (9.00) | 24.19 |
| **Quote** | | **185.44** |

- **The video comes out at about 48–52 s** (the clips played at 1.0–1.1×; cut B reuses each clip for 1–3 shots). Shorter than
  @scapemagicc's 62 s median, in line with the 30–45 s that small channels' Shorts get reach at (CLAUDE.md 1.6).
- **If `wan2_7` wins the first pilot:** the same plan costs about 125 with the reserve, or the cap buys a longer video: about 26
  clips (78 s of clips, 117.00) and 26 keyframes (about 42.50), about 183 with the reserve, a ~65 s video, with the model's own
  build sounds (fewer ElevenLabs credits).
- **ElevenLabs (outside the cap):** with a silent model, about 60–70 s of sound (two build beds, 6–8 effects, one ambience), about
  200–230 ElevenLabs credits; budget from the durations (the estimate overstates, CLAUDE.md 7.5).
- The credit rules are CLAUDE.md 6.1: quote first, the 15% reserve, stop and ask if a run will go 10% over, one generation per
  request, re-render a bad clip once, never auto-retry after a timeout, `transactions` after the run.

### 6.2 Step by step

**Step 0: Start.** `balance` (and the renewal date if it's low). Read CLAUDE.md section 0, then this file. Re-fetch @scapemagicc's
list (`PYTHONPATH=<dir> python3 -m yt_dlp --flat-playlist -J https://www.tiktok.com/@scapemagicc`, CLAUDE.md 12.1) and rerun the
idea's saturation check (`pipeline/youtube/yt_saturation.py <dir> "<object> tiny house build" "<object> turned into home"`).
**Search the farms' phrasing too** (`yt_search.py <dir> "abandoned <object> turned into cozy cabin" "old <object> turned into tiny
home" "restoring old <object>"`), date the Shorts (`yt_channels.py <dir> shorts:<id>`), and count long AI story videos too (3).

**Step 1: The story (free). GATE A.**
- The idea (section 3 or the user's), and why it passed the checks: not on @scapemagicc's list, the topic rule, demand.
- **The opening as three lines:** frame 0; the event by 1.0 s; what's on screen at 1–2 s.
- **The two stage ladders:** O0 → O6 (outside) and I0 → I7 (inside), each stage one visible change.
- **The shot list for cut B** (25–40 shots, with times) and how cut A comes out of the same clips.
- The witness, the joke, the last touch; the sound list; the builder's look (first video only, 5).

**Step 2: The shot list in full (free).** One row per shot: `shot | time | length | view (OUT, IN, CLOSE) | clip and the part of it
used | start still → end still | what happens, big in the frame | sound`. Then the clip list (17 for the standard plan): each clip,
its stills, its length and its shots. The chains: the end still of each outside clip is the start still of the next, and the same
inside, so cut A plays them straight through.

**Step 3: Quote (free). GATE B.** `balance`; `estimate_video_cost` for each clip model and length on the day, `estimate_image_cost`
for the stills; the sound by durations (ElevenLabs, outside the cap). **The quote with its reserve must be 200 or less;** if it
isn't, drop stages or close-ups before showing it. Show the clips and seconds, the stills, the total with the reserve and the balance
after. **Wait for approval.**

**Step 4: Project and keys.** `create_project` named `S2 – [title]`, its folder on every generation. **The builder key** (first video
only, then reused: a full-length photo of the builder in work clothes, plain background, face clear). **The outside view key O0**
(frame 0, the "before") and **the inside view key I0** (the bare shell from the door), each with the builder in it, made with the
builder key as a reference.

**Step 5: Stills. GATE C.**
- Each stage is an edit of its view's key with the previous stage as a second reference: VIEW (6.3) plus the change, naming
  everything built so far. This keeps edit chains short (CLAUDE.md 7.1: grain grows with each edit).
- Close-ups: CLOSE (6.3), with the builder key as a reference for the gloves and sleeves.
- Batches of up to 8, `jobs_wait`, one `show_generation_by_ids`. Re-make a drifted still once; a stage that fails twice is merged
  into the next.
- **Show at Gate C:** one sheet of every still (the stills sheet that `13-flightmap.py` writes): the
  builder the same in every still; each view's stages side by side with nothing fixed moving (the trees, the fence, the horizon,
  the door frame); no text or logos anywhere; hands with five fingers.

**Step 6: Sound (can start right after Gate B).** One ElevenLabs flow ("S2 NN [title]: sound"): the outside build bed and the
inside build bed (`loop: true`, ~20 s each), 6–8 effects and one ambience, as CLAUDE.md 6.2 Step 6b (`estimate_only:true` first,
then `generations_count:1`; never rerun to retry). Skip the beds if `wan2_7`'s own sound wins at Gate D.

**Step 7: Pilot clips. GATE D.**
- Render two: **the hook** (O0 → O1, the event by 1.0 s) and **one inside chain clip** (I0 → I1 or later).
- **First style-2 video only:** render the same two on `kling4_0` and on `wan2_7` from the same stills, and pick the model on the
  result (the builder the same, hands, the event by 1 s, the joins, the sound).
- **Show at Gate D:** the hook's frames at 0, 0.5, 1, 1.5 and 2 s (`contact_sheet.py --every 0.5`); the chain clip's last frame
  against the next still (the join must not jump); a face check.

**Step 8: The rest of the clips.** Batches of up to 12, `jobs_wait`, one `show_generation_by_ids`. Check every clip on a sheet at
about 5 frames a second: the builder the same person; no extra people; nothing fixed moves; the stage is reached by the last
frame; no text or logos; hands and tools hold their shape.

**Step 9: Assembly (free).** The first style-2 video writes `pipeline/s2-01-build.py` from `15-build.py`, keeping its clip
loading, speed fitting, upscale, sound placing (`on()`) and loudness, and dropping captions, pointers and whips:
- **Cut B:** hard cuts only; each shot an in-point, an out-point and a speed (1.0–1.3× on time-lapse, 1.0× on close-ups and the
  last touch); close-ups between outside stages; the witness at the start and the end.
- **Cut A:** the same clips with each view's chain played straight through; a 2–3 frame blend at a join only if it jumps.
- Upscale to 1080×1920 with `unsharp=5:5:0.6`; sound per shot (the bed under each view, effects on their picture); about
  −14 LUFS; keep a clean master of each cut.

**Step 10: Checks (free).** For each cut: the shot count and median (ffmpeg scene detection, CLAUDE.md 7.7); a sheet of the
first 2 s; a sheet of every shot's middle frame (faces, hands, text); `check_video.py` (something moves in 90%+ of seconds);
the loudness.

**Step 11: Delivery.** Upload both cuts and the clean masters (`media_upload` → PUT → `media_confirm`); give the links; report
the lengths, the shot counts and medians, credits quoted against spent (`transactions`), the first-2-s check and any shot that lost
its clip.

**Step 12: Covers and post copy (free).** Two covers (the cozy room; a before-and-after split of O0 and the dusk payoff), the
TikTok and YouTube copy (8). Then log the video in section 9, add lessons to section 7, and update both copies of the memory.

### 6.3 Prompt lines (drafts, 21 Nov 2026; to be proven at the first video's Gates C and D)
- **REAL** (every still): "Photorealistic photo, like a frame from a phone video shot with a slightly wide lens: natural light,
  true-to-life colours, real textures and wear. No text, no letters, no numbers, no signs, no logos, no brand names, no flags, no
  watermark."
- **BUILDER** (every still with the builder): "The builder is the same person as in the builder reference: [the chosen look, 5]."
- **ONLY** (every still and clip): "The only people in the scene are the builder[ and the witness]: no other people." (Kling
  invents workers otherwise, CLAUDE.md 7.2.)
- **VIEW** (each stage): "Locked camera: exactly the same position, lens, height and framing as the first reference image. Show
  the same place at a later stage of the build: [everything built so far]. Change only this from the second reference image:
  [this stage's change]. Everything else identical, including the light and the weather."
- **CLOSE** (close-ups): "Extreme close-up: the builder's gloved hands [doing X] fill most of the frame; the [material] in sharp
  focus, the background soft. The tool has no text, no logos and no brand colours."
- **COZY** (the last inside stage): "Finished and cozy: warm lamps and string lights, a thick rug, soft blankets, plants, wood and
  white plaster; tidy and lived-in; [dusk / snow / rain] outside the windows."
- **TIMELAPSE** (chain clips): "Time-lapse from a locked camera that never moves: between the first and the last frame the
  builder [does this stage], moving fast and slightly blurred, tools and materials appearing and disappearing; the light stays the
  same. Motion starts on frame 1. The builder stays the same person. [ONLY] No text, no logos."
- **REALSPEED** (close-ups, the last touch): "Real speed, handheld with a slight drift: [the action]. The hands have five fingers;
  the tool keeps its shape. [ONLY] No text, no logos."
- **HOOK** (the first clip): "On the first frame [the event] starts, and by one second it is big in the frame: [what happens].
  Motion starts on frame 1. [ONLY] No text, no logos." Say what must not change ("the house behind stays exactly as it is").

### 6.4 Checks (21 Nov 2026)
- **Gate C:** the stills sheet (5, 6.2 Step 5). **Gate D:** the hook's first 2 s and one join (Step 7).
- **The master:** shot count and median against 4.1 (cut B 25–40 shots, median 1–1.5 s, none over 4 s; cut A 4–8); frames 0–2 s;
  every shot's middle frame; something moving 90%+ of seconds; −14 LUFS.
- `camera_path.py`'s travelling-camera targets (CLAUDE.md 5 Rule 7) don't apply: style 2's cameras are locked on purpose.

---

## 7. Production lessons (style 2)

Add each lesson with its date and the video it came from.
- **The genre is farmed on YouTube** (21 Nov 2026, s2-01 Gate A): searched with the farms' own titles ("abandoned X turned into a
  cozy cabin"), seven of our eight objects had 8–20 AI build Shorts (most at 0.5–3K views) and long AI story videos from the last
  few weeks; the first check, with plainer phrasing, missed them. Search their phrasing, date the Shorts, count the long ones (6.2
  Step 0). An object with real DIY demand and few AI copies (the chicken coop) is the opening.

**Carried over from CLAUDE.md 7** (they're about the tools, not the look):
- Seedream (7.1): references copy the whole layout, so use them for "the same scene, change X"; "Extreme close-up: the [part]
  fills most of the frame" gets a real close-up; "Change only this: remove …" removes a stray; a still that fails twice is dropped;
  keep edit chains to three or fewer.
- Kling (7.2): every keyframe of a clip must agree on the state of things; say what must not change; Kling runs past the action, so
  trim to the good window; it invents people unless told who is in the scene; never auto-retry after a timeout.
- Edit and sound (7.4–7.5): round clip lengths to the nearest second; set every sound level by measurement; place each effect on
  its picture (`on()` in `13-build.py`); the sound estimate overstates, budget from the durations.

---

## 8. Posting (style 2; proposed 21 Nov 2026)

**TikTok, every video**
- **Caption:** one short line in our own words naming the before and the after ("An old ski gondola became a treehouse 🚡"), one
  emoji, then 4–5 tags typed in the app so they register as links (CLAUDE.md 8.1), e.g. `#build #tinyhouse #cozy #transformation
  #offgrid` (settle the set at the first post). Never claim it's real or that the poster built it.
- **"AI-generated content" on, every time:** realistic AI people and places need it under TikTok's rules.
- **Cover:** the cozy room, or the before and after side by side (TikTok crops covers to 3:4, CLAUDE.md 7.6).
- **Pin a comment** with a choice ("Would you sleep in it? Yes or no.") and reply to every comment in the first day.
- **When:** early evening US Eastern (6–7 pm ET); never two videos the same day, either style.

**YouTube Shorts, every video**
- **Title:** the before and the after, under ~60 characters ("From Old Ski Gondola to Cozy Treehouse"), no hashtags.
- **Description:** two sentences on the build, then "Made with AI.", a question for the comments and at most three hashtags.
- **Altered or synthetic content: ticked.** A realistic person and place that could pass for real footage is what the box is for
  (CLAUDE.md 8.2 leaves it unticked only for the cutaways).
- "No, it's not made for kids"; pick the cover frame at upload; pin the comment question.

**After posting:** the 24 h and 72 h reads (CLAUDE.md 8.4, 12.1–12.2) into section 9.

---

## 9. Video log (style 2)

The builder key (job id): not made yet. The accounts: TikTok and YouTube (the user, 21 Nov 2026); the main pair or a new
style-2 pair still to confirm (2.1).

| # | Title | Made | Cut | Clip model | Credits (quoted) | Length; shots, median | Posted (where, when) | TikTok at 72 h | YouTube at 72 h |
|---|---|---|---|---|---|---|---|---|---|
| s2-01 | (I5) the chicken coop that became a guest cabin | at Gate B, 21 Nov | B and A | kling4_0 or wan2_7 (Gate D) | (quoted 195.79) | | | | |

---

## 10. Topics to avoid (style 2; 21 Nov 2026)

- **Made by @scapemagicc** (all 86 videos, 11 Jun–21 Nov 2026; re-fetch before each Gate A, they post daily):
  - *Inside or from things:* septic tanks (four videos), a plastic pipe, concrete pipes, a square pipe, dumpsters (three), a skip,
    shipping containers (several), an old container, an abandoned tank, two old water tanks, two green plastic tanks, school buses
    (four), a double-decker bus, a van, a trailer, a wagon, a buried old plane, a buried private jet, a jet engine, a boat,
    a tent, old tires (a house and a dog house), pallets (two), orange crates, energy-drink cans, a raft of beer bottles, a raft
    house of wooden barrels, straw bales, sandbags, giant dinosaur ribs, an American skyscraper.
  - *Places:* a mud cave, a flooded sea cave, a flooded ice cave, a rock overhang, a rock wall, a cliff, a waterfall, a river, a
    mangrove forest, a desert, a desert pit, a desert well, a pit, a hole, a ditch by the road, a frozen dirt wall, underground
    bunkers, an underwater bunker and bedroom, a hidden room, a man cave under a driveway, a wine cellar, a rooftop, a rooftop
    garden, a front yard, gardens, a flooded garden, backyard pools (built, restored, and dirty pools into bunkers or an oasis), a
    pool and sauna, a guest room and a living room next to a house, an old house rebuilt, a concrete structure.
  - *Openings and devices not to reuse:* the pool party next door splashing the builder, the black eye, a flamethrower clearing a
    front garden, a dump truck tipping tires, pumping out a mud pit, grandma calling the police, the son-in-law, the jealous
    neighbour, building for a homeless person.
- **Crowded on YouTube** (21 Nov 2026): a fallen tree into a log cabin.
- Style 1's topic list (CLAUDE.md 13.2) doesn't bind style 2, but don't make the same object in both styles.

---

## 11. Paste-in prompt (style 2)

### 11.1 Kickoff prompt (21/11/26, style 2 v1)
Fill in the lines in angle brackets and paste the whole block into a new session.
```
KICKOFF PROMPT, STYLE 2 (21/11/26 v1)

Read CLAUDE.md in AliKandaz/short-form-video-memory (or the "Short-Form Video Memory"
artifact) first: section 0 and its standing rules. Then read strategy2.md, all
sections, and make the video with its runbook (strategy2.md section 6).

IDEA:     <I1 ... I8 from strategy2.md section 3, or my own humble thing -> cozy home>
CUT:      B, the fast-cut story, plus cut A from the same clips   <or: A only>
POST TO:  <the style-2 accounts | the main accounts>
BUILDER:  <a | b from strategy2.md section 5, first video only; after that the key>

Budget: at most 200 Higgsfield credits for this video, the 15% reserve included.
Check the balance and price every clip and still on the day (kling4_0 bills at
least 3 s). If the plan prices above 200, drop stages or close-ups before you show
me the quote. Clips at 720p.

Before Gate A: re-fetch @scapemagicc's full video list and drop the idea if it's on
it; run the saturation check on the object, and drop it (don't retitle it) if more
than about three AI build videos on it went up in the last 30 days.

The opening: frame 0 is the "before" (the humble thing, big in the frame, the
builder in shot); something big happens to it by 1.0 s (lifted, struck, torn off,
uncovered). Never a still establishing shot, and nothing that hurts anyone.

The look (strategy2.md 4-5): photoreal, natural light; two locked views (outside,
inside) built as stage ladders, each clip joining two stages; the builder in
time-lapse; 2-4 tool close-ups at real speed; about half the video inside, going
from a bare shell to a warm cozy room; a last touch at real speed; the outside at
dusk to end, back at frame 0's view. Our builder, the same in every shot. No
narration, no captions, no text, signs or logos anywhere, no music: build sounds
and one ambience. Nothing someone could copy and get hurt by.

Stop for my approval at:
- Gate A: the idea and its checks; the opening as three lines (frame 0 / the event
  by 1 s / what's on screen at 1-2 s); the outside and inside stage ladders; the
  shot list for cut B with times, and how cut A comes from the same clips; the
  witness, the joke and the last touch; the sound list.
- Gate B: the quote at 720p, 200 or less with the reserve, and the balance after.
- Gate C: one sheet of every still: the builder the same, each view's stages side
  by side with nothing fixed moving, no text or logos, hands right.
- Gate D: the hook clip's frames at 0, 0.5, 1, 1.5 and 2 s, and one chain clip's
  join; on the first style-2 video, the same two clips on kling4_0 and wan2_7 so I
  can pick the model.
Spend nothing before Gate B, and don't render the rest until the pilots pass.

When it's done, give me: the MP4 links for cut B and cut A and their clean
masters; the lengths, shot counts and median shot lengths; credits quoted against
spent; two covers (the cozy room; the before and after); TikTok copy (one line
naming the before and the after, one emoji, 4-5 tags for me to type in the app,
and a reminder to switch on the AI-generated label) and YouTube copy (a title under
~60 characters, two sentences with "Made with AI.", not made for kids, altered or
synthetic content ticked). Then log it in strategy2.md section 9, add any new
lessons to section 7, and update both copies of the memory.
```

---

## 12. History (style 2)

- **20 Nov 2026:** the user shared @scapemagicc's septic-tank tiny house (then 9.8M) and asked what it would take; watched frame by
  frame and priced (no credits spent): about 280–500 as a 1:1 copy, about 190 under the cap (CLAUDE.md 1.4, 13.3).
- **21 Nov 2026:** this file created at the user's request, to alternate between the two styles. Read all 86 of @scapemagicc's
  videos and measured three more of their top four (the 91.5M mud cave, the 76.5M garden, the 28.3M tires): one spine, two cuts
  (1.3–1.4). Eight ideas checked against their list and YouTube (3). Priced at the day's rates (kling4_0 2.50 a second): the
  standard plan 185.44 with the reserve (6.1). Nothing made.
- **21 Nov 2026 (later):** s2-01 started from the kickoff prompt (I1, builder b, cut B plus A). I1 dropped at the Gate A check (the
  gondola is farmed: about 20 AI Shorts and five long AI videos); I2–I4, I6 and I8 crowded too on a re-check with the farms'
  phrasing; I5, the chicken coop, passes and is at Gate A (`pipeline/s2-01-beat-sheet.md`).
