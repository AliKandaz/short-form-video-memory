# Short-Form 3D Cutaway Builds: Project Memory

**Revised on 22 Nov 2026 for the build-steps style**, on the user's word: "I like this a lot, moving forward I want to use
this animation style, update everything in the claude.md file to achieve this except the video ideas, that will be worked on
later … remove anything that is unnecessary and causing clutter in the file."
- **What changed:** how a video is animated and paced (every fix is built on screen in about four steps, each landing on its
  word: 4, 5), the runbook, the budget and the prompt lines (6), the lessons, cut down to what still applies (7), and the
  paste-in prompt (11.1, renewed 22/11/26).
- **What did not change:** the Cutaway look, the narrator, the bill, the street and the dog, the posting rules, and **the
  video ideas: 2.3, 3, 13.1 and 13.2 are word for word as they were; the user reworks them later.**
- **What was removed as clutter** (the explainer-era evidence in full, the travelling-camera rules, older scripts and
  lessons, old branding options, old file ids, the step-by-step history) is whole in **`archive/CLAUDE-2026-11-22.md`**: this
  file as it stood before the revision (also commit `549e291`). Section numbers are the same there and here. Older still:
  `a9abd35` (before the build format, 21 Nov 2026) and `1174f29` (before the rewrite of 18 Nov 2026); get one with
  `git fetch --depth=1 origin <commit>` and read it with `git show <commit>:CLAUDE.md`.

## 0. Start here (22 Nov 2026)

**What we make.** Vertical 3D build stories of about 64–68 s in the Cutaway look: a yard, pool, driveway or garage in bright
daylight, standing on a block of ground sliced open like a cake and seen from above like a stage. A one-step idea ("If you
roll turf over your pool, you have a hidden pool") is turned into the real thing one problem and one fix at a time, and
**every fix is built on screen in about four steps that each land on the word that names them**: a slab drops in, walls go
up, a roof comes down, paint sweeps across. Narrated in second person ("you") by an AI voice, with one-word captions, each
fix's real name on screen, and a price counter that ends on the bill. Nobody stands in for "you": the parts move by
themselves. The same small dog is in every video. No music.

**Why this style (22 Nov 2026).** The user on video 16, the first build-format video: "it just looks like the same videos we
have been creating." On @whatifplus's helipad video: "I like the way the video builds out the helipad, each step is
entertaining to watch, are we able to follow the videos format while keeping our visual style." A test said yes (1.9), and
the user: "I like this a lot, moving forward I want to use this animation style."

**What is ours,** so the videos are not a copy of the accounts we studied: the photoreal Cutaway look (5), the bill (4.4),
the street and the dog (4.5), checked terms and prices, and our own topics and wording (never theirs: rule 5).

**A second style** (`strategy2.md`): photoreal AI build stories with no narration. Paused since 21 Nov 2026 until the ten
build videos have been judged (2.5); a style-2 video is still made whenever the user asks. Its first video, s2-01 ("From Old
Chicken Coop to Cozy Guest Cabin", 125.00 credits), is made and not posted.

**Channels** (both US-based, the user confirmed on 13 Nov 2026). The user on 21 Nov 2026: "TikTok has slacked off and YouTube
is completely dead."
- TikTok **@overthinkingyearly** (display name "overthinkingyearly"): 54 followers, 14 videos, 50.2K views on 21 Nov 2026.
  Renaming it to match the content is still to do (8.3).
- YouTube **@LetzBuildTogether** ("LetZBuildTogether", channel id `UCNaqNT-R3K2GmISUfLdfBzA`): 314 subscribers, 14 Shorts,
  about 212K views on 21 Nov 2026, 199K of them on the fire-hydrant Short. The channel looks held back (1.6); whether the
  build videos start on a fresh channel waits for the user's check in Studio.

**The plan:** ten build videos in one lane, dream builds on what's yours ("How to turn your yard into a …"), judged at
checkpoints and not one by one (2). The ideas (3) wait for the user's rework.

**Where things live:**
- This file, `strategy2.md` (style 2, paused) and `tiktokshop.md` (the TikTok Shop affiliate project) in the GitHub repo
  `AliKandaz/short-form-video-memory`; the reusable scripts in `pipeline/` (style 2's with the prefix `s2-`), the channel
  artwork in `branding/`, the numbers behind 1.7 in `research/`, the previous memory in `archive/`.
- A live copy: the "Short-Form Video Memory" artifact, https://claude.ai/artifact/Fvbzc2HQyDxne7Y8NsrgvX (Artifact tool,
  action "read"); it carries `strategy2.md`, `tiktokshop.md` and the archive as files. **When this file changes, update both
  copies:** commit and push, then republish the artifact by its url.

**Standing rules (all in force on 22 Nov 2026):**
1. Never spend Higgsfield credits before the user approves the quote at Gate B (6.1). Script, step sheet and quote are free.
   **At most 200 Higgsfield credits a video, with the reserve, the narration and the sound inside it** (the user, 18 Nov
   2026: "I want at most 200 credits per video").
2. Stop at the four gates: A script, B quote, C stage pictures, D pilot (6.2).
3. Don't ask the user for retention or watch-time figures ("forget about the retention graphs", 15 Nov 2026). Work from what
   can be read from outside (12).
4. Fact-check every term and every price before Gate A (4.4); cut what can't be checked; never plant a mistake to bait
   comments.
5. Never reuse a reference account's wording, and never end on "Congratulations, you have built…" (How Building Explained's
   line, which @whatifplus and @youbuiltit use word for word). Our closing line is the bill (4.1).
6. When the memory changes, update both copies. **A change of direction (format, look, plan, ideas) goes into this file only
   after the user approves it** (22 Nov 2026: "don't change anything in claude.md file without my approval"). Logging
   results, status and the lessons of an approved video goes on as before; that split is my reading of the instruction.
7. The style is the build-steps style in the Cutaway look, and it doesn't change unless the user asks. Labels, the counter,
   stickers and the end card are overlays added in the edit (5); they are never asked of the image or video models.
8. The video ideas are the user's to rework (22 Nov 2026): don't rewrite 2.3, 3, 13.1 or 13.2 unasked.

**Status on 22 Nov 2026 (read this first; each bullet carries its own date):**
- **The style is decided** (22 Nov 2026): build-steps, sections 4 to 6. It is proven on one fix (1.9;
  `pipeline/steps-test.md`). **Still to prove on the first video in it, video 17:** a tester that stays the same thing from
  clip to clip; a failure clip; a step that changes the cut ground (a hole dug, a pipe laid); a cut or a whip between the
  stage view and a closer view; and whether the clips' own sounds are good enough to keep.
- **Next:** the user reworks the ideas (3); then video 17 from the prompt in 11.1.
- **Video 16** (B3, "How to Turn Your House Into a Christmas Light Show") was finished on 22 Nov 2026 in the earlier way of
  animating: 68.1 s, 197.99 credits, not posted. The user didn't like it (above). Whether it is posted is the user's call;
  if it is, by about Sat 5 Dec 2026, with the copy in `pipeline/16-post-copy.md` (its audio was measured, never heard).
- **The narrator is locked: Harrison** (22 Nov 2026), a Higgsfield preset voice (5).
- **Higgsfield: 672.01 credits** on 22 Nov 2026 (`balance`): three videos at the cap before the Ultra plan renews (3,000 a
  month since 11 Nov 2026; check the date). ElevenLabs has 34 credits left and is no longer needed (6.0).
- **Finished and not posted:** style 2's s2-01 (`pipeline/s2-01-post-copy.md`), on a day of its own.
- **Owed by the user, the in-app checks** (asked 21 Nov 2026): YouTube Studio → Content → the Restrictions column, and
  youtube.com/features (strikes); TikTok → Settings and privacy → Account → Account status. A fresh YouTube channel for the
  build videos only if the old one is in good standing, never to get around a strike.
- **72 h reads still to log** (9.2): video 13 after 23:04 UTC on 22 Nov 2026, video 14 after 20:00 UTC on 23 Nov, video 15
  after 01:45 UTC on 24 Nov.
- **Profile:** brand set v3 is live on YouTube; its wording is about explainers and wants a refresh for builds (8.3).

**Map of this file:** 1 what we know (evidence; 1.9 is the test behind the style) · 2 the build run · 3 the build ideas
(unchanged) · 4 writing the script · 5 the look · 6 production runbook · 7 production lessons · 8 posting and profile ·
9 channels, results and the video log · 10 money · 11 the paste-in prompt · 12 reading the platforms from a session ·
13 parked ideas, topics to avoid (both unchanged) and history.

---

## 1. What we know (evidence to 22 Nov 2026; the full studies are in the archive under the same numbers)

Read from public pages only (12). "My read" marks interpretation rather than measurement.

### 1.1 How the platforms decide (to 21 Nov 2026)
- **Each video is tested on a small audience first.** If enough of them keep watching, it is shown to more people; if not,
  it stops. Views land at the first ceiling or take off.
- **Our ceilings:** TikTok has stopped every video since seawater at 52–629 views. YouTube gave our first Shorts 1.2K–9K
  each, then almost no test at all (4–67 views on the last nine).
- **The same video can fail one platform and break out on the other:** the hydrant got 6.6K on TikTok and 199K on YouTube;
  seawater 34.7K and 8.8K.
- **Followers come from reach, not the profile:** about 1.2 followers per 1,000 views for us, 1.3–2.6 for the accounts we
  studied.

### 1.2 The first two seconds (measured 18 Nov 2026)
- In every reference video the scene itself changes within 0.5–2 s, on the first verb; the first frame is the "before".
- Every one of ours where something changed early passed TikTok's first test (1.9K–34K); six of the seven that opened on a
  finished, still scene stopped at 330–454.
- It is needed and not enough: videos 12–15 all opened on an event by 1 s, and none passed (2.6).
- Judge an opening by looking at its frames at 0, 0.5, 1 and 2 s; `check_video.py` can't tell (a camera gliding over a
  finished set counts as movement).

### 1.3 Topics (to 21 Nov 2026)
- For the build format, what wins and loses is in 1.7.
- From our first fifteen: everyday hidden workings with something moving through them won (the hydrant, seawater);
  landmarks, a matchup, cryonics and the mascot look lost; crowded topics lost whatever their title (1.6).
- The user on one list of ideas (16 Nov 2026): "all these are water, sea, lake related. mix it up." Water helps, but a list
  that is all water reads as one idea.
- Comments come from a choice put to the viewer ("Would you…? Yes or no."); they don't decide reach.

### 1.4 The channels we learned from (read 9–21 Nov 2026)

| Channel | What it is | What we take |
|---|---|---|
| **@whatifplus**, TikTok (the user's reference) | 42 videos in 36 days, 14.6M views, median 98K | The build format and, since 22 Nov 2026, the way a fix is built in steps (1.7, 1.9) |
| **@youbuiltit**, TikTok (You Built It on YouTube) | The format's leader: 96 videos, 119.9M views, median 659K | "If you…, you have a…", But/So/This is, a term on screen |
| **Hidden By Design**, TikTok @1hidden_by_design | 10 videos, 22.0M views; quiet since 9 Nov 2026 | Our look: the ground cut like a cake |
| **How Building Explained**, TikTok | 22 videos, 23.3M views; quiet since 3 Nov 2026 | The But/So formula. Its closing line is theirs (rule 5) |
| **You Made It**, YouTube @youmadeit3d | 13 Shorts, up to 36M | "Your yard"; quality over volume |
| **Cutaway Instinct**, YouTube | Stadium and arena cutaways in our look; best 1.3M | A direct rival: search it before any stadium or arena idea |
| **Zack D. Films**, YouTube | "What happens if you…" scenarios, 50M+ | Avoid his topics (13.2) |
| **@scapemagicc**, TikTok | Photoreal AI builds with no narration, median 467K | Style 2 (`strategy2.md`): a build shown stage by stage from one locked view |
| **NET FILES**, **@thewhatifstudio**, TikTok | Defence puzzles; what-if simulations | A place named only at the end; a choice put to the viewer |

### 1.5 Packaging (to 21 Nov 2026)
- The first frame and the first second decide most of it (1.2). The title is barely seen in the Shorts feed.
- TikTok: the hashtags must register as links (8.1). YouTube: a title under ~60 characters and "not made for kids" (8.2).
- Not the problem (checked 18 and 21 Nov 2026): a shadowban, TikTok's AI label (TikTok adds it itself, hits included), a
  watermark, the follow rate.
- YouTube's category: the hydrant Short sits under "People & Blogs", the default. Set Studio → Settings → Upload defaults →
  Category to Education or Science & Technology.

### 1.6 Banned or held back? (checked 21 Nov 2026)
- **TikTok: not banned or restricted.** Every video, the hits included, carries the same clean moderation record, and new
  videos still get a first test from strangers. They don't pass it.
- **YouTube: not banned, but the channel looks held back** (my read; strikes and restrictions show only in Studio). Our
  Shorts rank at the bottom for their own titles, and brand-new channels in our niche with 14 and 42 subscribers get 1–2K a
  Short where ours get 4–67. The cause can't be told from outside: a restriction only Studio shows, the hangover of the
  viral hydrant, YouTube's 2026 limits on low-quality AI content, or the October 2026 originality update.
- **Reach dropped; engagement per viewer didn't** (TikTok likes are 2–6% of views on the recent videos, 1.1% on seawater).
- **The topic rule:** if more than about three AI or animated videos on the same subject went up in the last 30 days, drop
  the topic. Retitling a crowded topic doesn't help: the viewer sees the same subject and the same facts, and swipes.
- **Small channels that do get reach** share a vertical with an enthusiast audience (trucks, trains, fire trucks, planes:
  448K–2.9M a Short) and "Why does this [thing you've seen] do [odd thing]?" titles.

### 1.7 The build accounts: @whatifplus and @youbuiltit (studied 21 Nov 2026)
All 42 of @whatifplus's videos were downloaded, transcribed on this machine and measured; nothing was listened to. The
per-video numbers are in `research/whatifplus-videos.tsv` and `research/youbuiltit-videos.tsv`.
- **@whatifplus** ("What If +", posts from the UK): created 13 Oct 2026; on 21 Nov 2026 25.0K followers, 42 videos in 36
  days, 14.6M views. Median 98K, lowest 6.6K, highest 2.9M. About one video a day, two or three on ten days with no visible
  harm. The caption is the title plus five tags, all registered. TikTok labels all 42 as AI and shows no penalty. Median
  length 70 s.
- **@youbuiltit** ("You Built It"): 217.2K followers, 96 videos since 11 Oct 2026, 119.9M views, median 659K, lowest 35.9K;
  titles "How a [humble thing] Becomes a [thing]"; two to three videos a day. @whatifplus is modelled on it.
- **The skeleton (42 of 42 scripts):** "If you [one naive step], you have a [thing]." Then five to eight "But [a failure you
  can see]. So you [fix]. This is a [real term]." Then "Congratulations! You have built a [thing]!" Median 216 words in
  70 s, 3.1 words a second; the premise done by about 4.2–4.5 s and the first "But" at 5.1 s (median).
- **The helipad video, the user's reference** (20 Nov 2026; 595K views in its first day; 69.0 s; 219 words). Frame 0 is a
  bucket and brush already painting the H; the first "But" lands at 4.0 s; five loops of 11.5–13.6 s, each ending "This is
  a …" with the term on screen; the last problem starts at 79% of the video and the narration ends 2 s after the last fix.
  One continuous camera with no cuts, 60 frames a second, something moving in 99% of the seconds, about 50 visible changes
  (my count), mean brightness 168 of 255. Its first "So" sentence packs five things into 7.6 s: the grass comes off, a steel
  grid goes down, a slab is poured, a clock shows two days passing, the H is painted. One "tester", the helicopter, comes
  back in every loop and fails a new way. The ground is cut open once, when the fix is a buried fuel tank.
- **Hits and flops share the skeleton; the object separates them.** What wins: things a teenager wishes they had at home,
  above all racing, defence and water (bunker 2.9M, zombie base 2.5M, slip-n-slide 2.0M, go-kart track 1.0M). What loses:
  winter scenes on white frames (ice rink 6.6K), things that aren't yours (the Golden Gate Bridge 10K), chores (gym 15K, car
  wash 19K). Sequels fade.
- **The format is a land grab, and timing decides.** New objects still break out for small channels (a doghouse hideout
  8.1M, a pond 4.0M, an airport 3.0M); later copies of a taken object get little. An object nobody has built yet is worth
  more than a better version of one that is taken (my read): count the animated build videos of the same object, and mind
  their dates.
- **What we take:** the premise line and the loop (4.1), a term on screen for each fix, the build shown step by step (1.9),
  dream-build topics about what's yours, the title as the caption (8.1). **What we don't:** their wording and closing line
  (rule 5), their topics (13.2), their house and their look.

### 1.8 How those accounts are made (21 Nov 2026)
- **They are real 3D drawn in code, not AI video** (my read, on strong signs): the geometry holds from every angle, text in
  the scene is exact, and all 60 frames a second are unique. Public kits for the genre pair Claude Code with three.js.
- **Two ways to do the same were looked at and set aside** when the user chose to keep our look (21 and 22 Nov 2026):
  three.js on this machine (a crude test yard at 0.35 s a frame, no credits) and Higgsfield's hosted Blender scene ("3D
  Jutsu", scripted in Python; its notes say building and rendering cost no credits; never run). They stay the other route
  if the AI look ever stops working (13.1).

### 1.9 Video 16 against the helipad, and the build-steps test (22 Nov 2026)
- **Video 16 matched their words and not their picture.** 224 words against 219, 3.4 words a second against 3.3, five loops
  each, the first "But" at 3.8 s against 4.0 s. But: 13 AI clips against one camera; brightness 76 of 255 (dusk) against
  168; about 30 visible changes against about 50; 13 s of narration after the last fix against 2 s; three of five loops
  ending on the term against five of five; and its subject was lights changing state, where theirs is things being built.
- **The test** (`pipeline/steps-test.md`; a garden shed as a neutral subject; 35.00 credits): one fix built in four steps
  in our look, in daylight, from one locked view, made two ways. All 6 pictures and all 5 clips were usable on the first try.
  - **A, one short `wan2_7` clip a step** (15.00 for four steps, 10 s of footage): the slab and the roof fall out of the sky
    and raise dust, the walls go up one by one, the paint sweeps across and the door swings shut. Each clip starts and ends
    on its stage picture within 0.13 px, does its step in the first second, and its own sound peaks on the impact.
  - **B, all four steps in one `kling4_0` clip** (12.50, 5 s) with the three middle stages as keyframes: the same four
    steps in order, about half a second each. One clip and no joins, but a failed step means the whole clip again.
  - Re-timed in the edit, every step landed on the word that names it.
- **Decided: A is the standard** (the steps are more physical, a bad step is cheap to redo, more footage per credit); B
  where the steps of a fix must flow without a join.
- **Where it still falls short of the helipad:** the camera holds one view while a fix is built (a slow push-in is added);
  30 frames a second, not 60; and a video costs about 185 credits, where code-drawn 3D would cost about 15–20.

---

## 2. The build run: ten videos (the plan of 21 Nov 2026, in the style of 22 Nov 2026)

### 2.1 The lane
**Dream builds on what's yours:** "How to turn your [yard, pool, driveway, garage, house] into a [thing you wish you had]",
built on one sliced-open set, one problem and one fix at a time, every fix in steps (4), with the bill running. One lane and
one style for all ten, judged at the checkpoints in 2.5 and not after each video: changing direction after almost every
video is what 9.3 warns about. The ten are counted from video 17, the first in the build-steps style; video 16, if it is
posted, is read apart.

### 2.2 Before the next video (22 Nov 2026)
1. **The ideas:** the user reworks section 3 for this style. An idea now also needs a tester that can come back five times,
   and fixes that can each be built in about four visible steps (4.3). Until then 2.3 and 3 stand as they were written.
2. **Post what is finished:** style 2's s2-01, on a day of its own. Video 16 is the user's call (0).
3. **The in-app checks** still owed (0). They decide where the build videos go on YouTube (1.6).
4. **The TikTok handle and the profile wording** (8.3).

Done: the narrator (Harrison), the voice and the sound on Higgsfield (6.0), the dog (4.5).

### 2.3 The ten, in order (21 Nov 2026)
Every idea was checked on 21 Nov 2026 against @whatifplus's 42 and @youbuiltit's 96 videos (none is on either list) and on
YouTube with both title shapes (12.2). Check again at each Gate A: objects are being taken within days (1.7).

| # | Idea (section 3) | The naive step, on frame 0 | Demand, and who is near (21 Nov 2026) | Why this slot |
|---|---|---|---|---|
| B1 | How to Hide a Swimming Pool Under Your Lawn | turf unrolls over a tarp stretched across the pool | real moving-floor pools 17.2M and 1.6M; pools are the format's biggest object (13.4M on TikTok, 9.1M on YouTube); no build video of a hidden pool found | water and a cutaway are what our look does best; the motion is simple |
| B2 | How to Turn Your Yard Into a Motocross Track | a dirt bike carves a circle in the lawn, turf flying | real backyard tracks 11M, 469K, 249K; racing is the format's steadiest cluster; no build video found | racing, and nothing like B1 |
| B3 | How to Turn Your House Into a Christmas Light Show → **video 16, the first build video: finished on 22 Nov 2026 (68.1 s, 197.99 credits), not posted yet** | one string of lights is clipped to the gutter and comes on | pixel-light Shorts 13.5M and 559K; one small build copy (1.2K, 11 Nov) | seasonal: post by about Sat 5 Dec 2026 |
| B4 | How to Turn Your Driveway Into a Soapbox Derby | a wagon rolls down the driveway | the 1973 magnet cheat 4M; soapbox Shorts 96K, 35K; no build video found | racing for kids, with a true story built in |
| B5 | How to Turn Your House Into a Flood-Proof House | sandbags thump down at the door as water crosses the lawn | real flood Shorts 28M, 9.2M, 4.8M; one build video, The Building Box 874K (4 Nov) | defence and water; the cutaway shows the ground water |
| B6 | How to Turn Your Yard Into a Railroad | a cart is pushed along two planks | garden railways 7.4M, 744K, 504K; "How a Log Road Becomes a Railroad" 413K; none in a yard | an enthusiast audience (1.6) |
| B7 | How to Turn a Doghouse Into a Mansion | a door is cut in a cardboard box and the dog walks in | real dog mansions 6.1M, 2.3M; "How a Doghouse Becomes a Secret Hideout" 8.1M (16 Nov, a different build) | the dog's own episode |
| B8 | How to Turn Your Pool Into an Olympic Diving Pool | a plank is bolted to the pool's edge | diving Shorts 50M, 17M; no build video found | water and sport |
| B9 | How to Turn Your Yard Into a Demolition Derby | two old cars bump on the lawn | derby Shorts 3.4M, 242K; no build video found | racing; the hardest motion to draw, so late |
| B10 | How to Turn Your Garage Into a Fire Station | a red truck backs into the garage | weak on the search page (15K); fire trucks carry enthusiast channels (448K–705K, 1.6); no build video found | the set is a building cut open, our look's best case |

### 2.4 Budget and cadence
- **At most 200 Higgsfield credits a video, everything inside it** (6.1). A video in this style prices at about 185 with the
  reserve (6.1). The balance was 672.01 on 22 Nov 2026: three videos at the cap before the Ultra plan renews (3,000 a month
  since 11 Nov 2026; check the date).
- **One video every one to two days** as credits allow; early evening, US Eastern, on both platforms (8).

### 2.5 How we'll judge (from outside; never ask the user for retention)
- **Each video at 72 h** (8.4): more than ~2K on TikTok = it passed the first test; more than ~1K on YouTube = it was tested
  normally; 10K+ = a breakout for us. Record both in 9.2 with the first-second verdict. For scale: @whatifplus's weakest
  video has 6.6K and @youbuiltit's 35.9K, but both started with a hit and we start from 54 followers.
- **Checkpoint after four:** if two or more passed TikTok's first test, keep the lane and the style. If none did, compare
  each video's object and first five seconds with 1.7 before spending on a fifth, and ask the user whether the look or the
  account is the block.
- **After ten:** review with the user: which objects passed, the follower and subscriber change, the bill and the end card
  (did comments per view move?), and the next ten. Don't change the format in the middle on one result.

### 2.6 What became of the explainer plan of 18 Nov 2026
Ten videos on "the hidden inside of something everyone uses or walks past", each opening on an event in the first second.
Four were made and posted (videos 12–15); none passed either platform's first test (9.2), and each topic turned out to have
5–20 AI Shorts on the same facts (1.6). The rest are parked (13.1).

---

> **22 Nov 2026:** section 3 below is kept word for word as it stood before this revision (rule 8); the user reworks the
> ideas later. Its draft scripts and ladders follow the earlier script rules (the "That's why…" and "Add…" lines, about
> 220 words, camera lists for the travelling camera): when an idea is used or reworked, rewrite it to section 4.

## 3. The ten build ideas (proposed 21 Nov 2026; the user picks, and Gate A settles each)

All ten are in the lane of section 2 and the format of section 4. Order and timing are in 2.3. B1–B4 have a full draft script
(about 220 words, written before the narrator was chosen: trim to about 210 at Gate A, 4.3); B5–B10 have the ladder a
script is written from. Facts and prices marked ⚠ are unchecked and every one is
checked before Gate A (rule 4); a bill lists what gets a price, never a made-up figure. No line below comes from a reference
account.

### 3.0 How an idea gets on the list (from 1.7)
1. **The premise fits one line and three seconds:** "If you [one naive step], you have a [thing]." The step must be something
   that can be seen happening from frame 0, and harmless to copy.
2. **The thing is a wish:** something a teenager, or their dad, would love to have at home. Racing, defence and water did
   best for the accounts we studied; chores, snow-white scenes, shops and famous landmarks did worst.
3. **It is yours:** your yard, pool, driveway, garage, house.
4. **Five failures you can see, five fixes with real names and real prices.** Each failure happens to a thing, not to a
   person.
5. **The cutaway earns its place:** something under the ground or inside a wall is part of at least two fixes. It is what
   our look shows and theirs doesn't.
6. **A bright first frame:** grass, water, sky. No opening on snow or at night unless lights are the subject.
7. **Nobody has built it:** not on the lists in 13.2, and the topic rule of 1.6 and 1.7 on YouTube with both title shapes. If
   more than about three animated build videos of the same object went up in the last 30 days, drop it; don't retitle it.

**B1. How to Hide a Swimming Pool Under Your Lawn** (a back yard with a pool)
- **Title** (both platforms): "How to Hide a Swimming Pool Under Your Lawn". **Caption:** the title, "Guess the bill 💸", the
  four standing tags, #Pool. **Pinned comment:** "Would you swim under your own lawn? And what do we build next?" (the dog is
  named on video 16, the first build video, 4.5).
- **Set:** one back yard cut open like a cake through the pool: the lawn and patio on top, the pool's concrete shell and
  cyan water in the cut face, the floor's steel frame with its floats, the cables and pulleys on the pool bottom, a small
  plant room with a hydraulic cylinder beside it under the lawn; the back of the house and its door behind.
- **First second:** frame 0 the open pool with a tarp pulled tight across it, a roll of turf at one end, big in the frame;
  by 1 s the turf is unrolling across the tarp by itself and the pool is disappearing under lawn. The dog trots after the roll.
- **Script** (draft, about 221 words with the total):
  > If you stretch a tarp over your pool and roll turf across it, you have a hidden pool.
  >
  > But the first lawn chair you set on it sinks straight to the bottom. So you swap the tarp for a solid deck. But now it
  > weighs as much as a truck, and nothing can lift it. So you let the pool do the lifting. The deck floats, and cables on
  > the pool's bottom pull it down. This is a movable floor. But as it rises, a pool's worth of water rides on top. So you
  > leave a slot along every edge, and the water pours off as the floor comes up. But that slot is just wide enough to
  > swallow a foot. So a flap swings across it the moment the floor reaches the top. But a floor that floats bobs like a
  > raft when you walk on it. So spring-loaded pins shoot out of its edges and lock into the walls. These are locking
  > pins. And with the lid shut, the heat stays in: most of a pool's heat escapes from its surface. That's why a covered
  > pool is still warm in the morning. Add turf on top, a table and chairs, and one button by the back door. That's your
  > hidden pool. The bill: about [TOTAL].
- **Labels:** MOVABLE FLOOR, LOCKING PINS (two so far: name the deck and the edge flap too if Gate A finds their real
  names). **The bill** (each ⚠ to source): a tarp and a roll of turf (the starting
  figure); a structural pool deck; the movable floor with its floats, cables and hydraulic drive (the big one); edge flaps;
  locking pins; artificial turf and patio furniture; the control. The total is said in round words.
- **The dog:** follows the turf roll in frame 0; in the last shot the floor stops ankle-deep and he paddles across it.
- **Camera (8):** the pool from the back door, wide (frame 0 and the last shot) → the tarp and the sinking chair, close → down
  the cut face to the deck's floats → the cables and pulleys on the pool bottom → the plant room under the lawn → the edge
  slot with water pouring off, close → the flap, extreme close → a pin sliding into the wall, close → the lawn at dusk with
  steam under the lid's edge → back to the first position.
- **Sounds:** bed: a quiet back yard in summer, a pool pump's hum; effects: turf unrolling, a splash, a winch whirr under
  water, water pouring off, a flap's clack, pins thunking home, the counter's tick, the till.
- **Demand, and who is near (21 Nov 2026):** real footage "A swimming pool that turns into a floor" 17.2M, "Innovative Hidden
  Swimming Pool with a Movable Floor" 1.6M, "He Built A Secret Swimming Pool Inside His House" 3.3M. Pools as builds:
  @youbuiltit's swimming pool 13.4M (TikTok), Low Poly Films 9.1M (YouTube), CUTAWAY's "How a Swimming Pool Becomes a Secret
  Bunker" 556K (18 Nov). No build video of a hidden or moving-floor pool found.
- **Checked ✔ (a search summary, 21 Nov 2026):** the floor is a stainless frame with foam buoyancy packs, so it floats;
  steel cables run through pulleys on the pool bottom to a hydraulic cylinder that pulls it down; at the set depth
  spring-loaded tapered pins lock it (WaterShapes, Building magazine, patent US10072432).
- **⚠ before Gate A:** how the water passes the floor as it moves (a slot at the edge, or gaps in the deck) and what closes
  the edge gap; the weight of a deck this size; the load a raised floor carries; "most of a pool's heat escapes from its
  surface" (the US Department of Energy gives evaporation about 70%: reopen it); every price.
- **Watch out:** nobody falls in; the chair sinks, not a person; no maker's name on the floor.

**B2. How to Turn Your Yard Into a Motocross Track** (a big back yard)
- **Title:** "How to Turn Your Yard Into a Motocross Track". **Caption:** the title, "Guess the bill 💸", the standing tags,
  #Motocross #DirtBike. **Pinned comment:** "Would your neighbors survive this? And what do we build next?"
- **Set:** one large yard cut open like a cake: lawn at first, then a clay track with banked corners, a tabletop jump whose
  packed core shows in the cut face, a drain pipe under the low spot, a steel starting gate, the house and a fence behind.
  Riders are small and anonymous, in helmets.
- **First second:** frame 0 a dirt bike already carving a tight circle on the green lawn, low and close, turf spraying off
  the back tire; by 1 s the circle is a brown ring and the dog is chasing the bike.
- **Script** (draft, about 222 words with the total):
  > If you ride your dirt bike in circles on the lawn, you have a motocross track.
  >
  > But the back tire chews the grass into a mud pit, and you slide out on every turn. So you scrape the lawn off, truck in
  > clay, and pack it into a banked wall around each corner. This is a berm. But a track with no jumps is just a muddy
  > road. So you build a ramp and a landing. But come up short, and you slam into the face of the landing. So you fill the
  > gap between them flat. This is a tabletop. But the first storm turns every low spot into a pond. So you bury a pipe
  > under each one to carry the water away. This is a culvert. But everyone takes off when they feel like it, and it's a
  > pile-up at the first corner. So a steel gate holds every front wheel and drops them all at once. This is the starting
  > gate. But a rider goes down behind a jump, where the next one can't see him. So someone stands on every jump with a
  > yellow flag. These are flaggers. Add a row of bumps called whoops, foam blocks to mark the lanes, and a checkered flag.
  > That's your motocross track. The bill: about [TOTAL].
- **Labels:** BERM, TABLETOP, CULVERT, STARTING GATE, FLAGGERS. **The bill** (each ⚠): a tank of gas (the starting figure);
  clay by the truckload and a day of a small bulldozer; the tabletop's dirt; drain pipe; a starting gate; flags, foam
  blocks and a water hose.
- **The dog:** chases the bike in frame 0; in the last shot he sits on the tabletop with the checkered flag in his mouth.
- **Camera (8):** the lawn low by the bike (frame 0) → up and over the yard as the track appears → a berm, low on the
  outside → the ramp and the gap from the side → down the cut face through the tabletop's core → the low spot and the pipe
  under it (the cutaway) → the starting gate from in front, low → a jump's crest with the flag → the first position, wide.
- **Sounds:** bed: a breezy back yard, a far-off two-stroke; effects: an engine rasp, dirt spraying, a truck tipping, a
  thump on the landing, water in a pipe, the gate's clang, the counter's tick, the till.
- **Demand, and who is near (21 Nov 2026):** real builds lead: a backyard pump track 11M, "landscaping, but make it moto"
  469K, a pit-bike track 308K, "Dream Backyard Motocross Track" 249K, long videos 2.4M and 997K. Racing builds on TikTok:
  go-karts 1.0M, NASCAR 851K, F1 532K, MotoGP 262K (@whatifplus). No motocross build video found on either list or on
  YouTube.
- **⚠ before Gate A:** that a tabletop is the safer jump because a short landing meets flat ground; what tracks are built
  from (clay or a clay and sand mix); the yellow flag's meaning in the rule book; the starting gate's action (it drops
  toward the riders); "whoops"; every price.
- **Watch out:** nobody hurt: the fallen rider sits up; no bike brands, numbers or sponsor colours; don't reuse the
  go-kart video's "neighbor calls the police" beat.

**B3. How to Turn Your House Into a Christmas Light Show** (a house on a street at dusk; post by about Sat 5 Dec 2026)
- **Title:** "How to Turn Your House Into a Christmas Light Show". **Caption:** the title, "Guess the bill 💸", the standing
  tags, #Christmas #ChristmasLights. **Pinned comment:** "Guess the power bill. And what do we build next?"
- **Set:** one two-storey house cut open like a cake at dusk: the roof line and gutter, the breaker panel in the garage,
  the oven in the kitchen, the outlets on the outside wall, a controller box in the attic, the front yard and the street
  with a few parked cars. The night look is a re-grade of the day still (6.3 NIGHT); the lights are the subject, so this
  one may open at dusk (3.0 rule 6).
- **First second:** frame 0 a dark house against a deep blue sky, one string of lights half clipped along the gutter, big
  in the frame; by 1 s the clips have run to the corner and the string comes on bulb by bulb. The dog is wrapped in a
  spare string.
- **Script** (draft, about 225 words with the totals):
  > If you clip one string of lights to your gutter, you have a Christmas light show.
  >
  > But one bulb burns out and the whole string goes dark. So each bulb gets a tiny bypass wire that takes over when it
  > dies. This is a shunt. But you hang fifty more strings, and the breaker trips and takes the oven with it. So you swap
  > every bulb for an LED, which sips about a tenth of the power. But the first wet snow gets into the plugs, and the
  > outlet shuts itself off. This is a ground-fault outlet: it cuts the power before a wet wire can shock you. So every
  > connection goes in a sealed box. But lights that only switch on and off are boring by the second night. So every bulb
  > gets its own chip, and a controller plays them like a screen, in time with music. These are pixels. But the music
  > wakes the whole street. So you send it out from a tiny radio transmitter, and the cars out front tune in. That's why
  > light-show houses put a radio station on a sign in the yard. Add a tree made of lights, arches over the driveway, and
  > a snowman that sings. That's your light show. The bill: about [TOTAL], plus [X] a night in power.
- **Labels:** SHUNT, GROUND-FAULT OUTLET, PIXELS (named in the script); LED and FM TRANSMITTER on the words "LED" and
  "transmitter". **The bill** (each ⚠): one string of lights (the
  starting figure); fifty strings of LEDs; weatherproof boxes and outdoor cords; pixel strings, power supplies and a
  controller; the transmitter; the tree, the arches and the snowman; and the nightly electricity, worked out from the
  wattage.
- **The dog:** tangled in a blinking string in frame 0; in the last shot he wears antlers that light in time with the house.
- **Camera (8):** the gutter and the string, close (frame 0) → along the string to the dead bulb, extreme close (the
  shunt) → through the wall to the breaker panel and the dark oven → the outside outlet in the snow, close → one pixel,
  extreme close, then the whole wall changing colour → the attic controller → the street with the cars → the house, wide.
- **Sounds:** bed: a quiet street on a winter evening; effects: clips clicking, a bulb's pop, a breaker's clunk, a hiss of
  wet snow, a soft chord as the pixels come on (not a tune), a car radio's static, the counter's tick, the till.
- **Demand, and who is near (21 Nov 2026):** "Animated Pixel Christmas Lights" 13.5M (a month old), light-kit Shorts 559K and
  311K, "Use the extra red tip bulbs to make the Christmas lights twinkle" 103K. Build copies: "How One String of Lights
  Becomes a $2.3 Billion Christmas Display" 1.2K (Sticker Shovel, 11 Nov) and nothing else. Winter topics flopped for
  @whatifplus on white frames (1.7); this one is dark blue and full of colour.
- **⚠ before Gate A:** which strings go dark with one dead bulb (old series-wired mini lights) and how the shunt works; LED
  strings' share of the power (the US Department of Energy says at least 75% less); what trips first with fifty
  incandescent strings on a 15-amp circuit (do the sum); that a GFCI trips on wet connections; "pixels" and the controller;
  the low-power FM transmitter that light shows use and its rules; every price and the nightly cost.
- **Video 16 (`pipeline/16-*`): Gate A approved by the user on 21 Nov 2026.** The user picked B3 as the first build video.
  What the checks changed in the draft above: **the shunt loop is out** (five small AI Shorts on "one bulb kills the string"
  and "the hidden wire in every bulb" went up on 8–15 Nov, best 8.5K) and **power injection is in** (halfway along the roof
  white turns pink as the voltage sags; power is fed into the middle of the line); rain for snow, so the set keeps its
  colours; "takes the oven with it" became "the porch and the living room go dark" (an oven has its own circuit; living
  room and porch outlets often share one); the loops' terms are LED, GROUND-FAULT OUTLET, PIXELS, POWER INJECTION and FM
  TRANSMITTER; the closing line is "The bill: about two thousand dollars, and less than a dollar a night in power" ($2,107.22
  in `16-bill.md`; $0.19–$0.96 a night). The pinned comment names the dog. The set is at blue dusk: one phrase of the STYLE
  line changes for this video (proved at Gate C: 6.3 DUSK).
- **Resolved at Gate A (21 Nov 2026, search summaries; no seller's or agency's page opens from a session, 7.7):** a
  100-count incandescent mini string draws about 40 W and an LED one 4–7 W; a 15-amp circuit carries 1,800 W (1,440 W
  continuous), so 51 incandescent strings (about 2,040 W) trip it; a GFCI trips on a 4–6 mA imbalance in a fraction of a
  second (the "1/40 of a second" often quoted wasn't found, so it isn't said) and rain in the plugs is the usual cause; a
  smart pixel is an addressable RGB light with its own WS2811 chip; "pinking" at the end of a run is voltage drop and the fix
  is called power injection (no "every N pixels" rule found, none said); unlicensed FM is limited to 250 microvolts a metre
  at 3 metres (47 CFR 15.239), about 200 feet, and shows post the frequency on a yard sign. Saturation: neither build account
  has a Christmas or lights build; on YouTube no animated build under either title shape, one near copy (Sticker Shovel,
  1.2K); real footage 13.5M, 4.5M, 626K.
- **Watch out:** no carols or any tune (no music, 5); no brand names; no Santa from a film; the sign carries no words in
  the generated picture (the frequency is an overlay, 5).

**B4. How to Turn Your Driveway Into a Soapbox Derby** (a sloping driveway and street)
- **Title:** "How to Turn Your Driveway Into a Soapbox Derby". **Caption:** the title, "Guess the bill 💸", the standing
  tags, #SoapboxDerby #Racing. **Pinned comment:** "Would you have used the magnet? Yes or no."
- **Set:** one sloping driveway and the street below it, cut open like a cake along the hill: the house and garage at the
  top, a wooden starting ramp with steel paddles, two painted lanes, a finish line with a light beam, hay bales at the
  bottom; one racer cut open to show the steering cable, the weights bolted to its floor and the brake pad.
- **First second:** frame 0 a red wagon already rolling down the driveway toward the camera, low and close, the dog
  sitting in it; by 1 s it is wobbling and he hops out as it tips into the hedge.
- **Script** (draft, about 223 words with the total):
  > If you roll down your driveway in a wagon, you have a soapbox derby.
  >
  > But the wagon wobbles, swerves, and tips you into the hedge. So you build a long, low car, lie back inside it, and
  > steer with a cable. But one kid gets a shove and the other doesn't. So both cars lean on steel paddles that drop at
  > the same instant. This is the starting gate. But the heavier car always wins. So every car goes on a scale with its
  > driver, and the lighter ones bolt in weights until they match. But one lane is always a little faster. So you race
  > twice, swap lanes and wheels in between, and add up the times. But two cars cross the line together and everyone
  > argues. So a beam of light across the finish times each one to a thousandth of a second. But at the bottom you're
  > doing thirty miles an hour with no engine and no way to stop. So a pedal shoves a rubber pad down onto the road. This
  > is a drag brake. In 1973, the champion hid a magnet in the nose of his car to pull it off the steel gate. He was
  > caught. Add hay bales, a finish banner, and a trophy. That's your soapbox derby. The bill: about [TOTAL].
- **Labels:** STARTING GATE, DRAG BRAKE (named in the script); the year 1973 on the true story; the weights and the timer
  get labels only if Gate A finds what racers call them. **The bill** (each ⚠): a wagon (the starting figure); a racer
  kit with wheels; the starting ramp and gate; a scale and weights; the finish-line timer; hay bales, a banner and a
  trophy.
- **The dog:** rides the wagon in frame 0 and hops out; in the last shot he sits in the winning car wearing goggles.
- **Camera (8):** the wagon low on the driveway (frame 0) → the hedge → the racer cut open, close → the gate's paddles, low
  and in front → the scale → down the lanes with the cars → the finish beam, close → the brake pad on the road, extreme
  close → the hill, wide.
- **Sounds:** bed: a suburban street on a summer morning; effects: wagon wheels on concrete, a hedge's rustle, the paddles'
  clack, a scale's clunk, wheels humming, a beep at the line, rubber dragging, the counter's tick, the till.
- **Demand, and who is near (21 Nov 2026):** "The Genius Cheat With a Hidden MAGNET" 4M; "Why Soapbox Driver Sit in Such a
  Tiny Space!" 96K; "85 Year Old Grandpa WINS Soapbox Derby" 35K. No soapbox build video found.
- **⚠ before Gate A:** the starting gate's paddles; the weight limits by division; the lane and wheel swap and how the
  times are combined; the finish timer's precision; top speed on a derby hill; how the brake works; the 1973 magnet (how it
  was switched on, and that the winner was disqualified); what racers call the added weights and the finish timer; every
  price.
- **Watch out:** the 1973 racer was a child: never named or shown, one sentence only; no derby logos; the dog is out of
  the wagon before it tips.

**B5. How to Turn Your House Into a Flood-Proof House** (a house by a river)
- **Title:** "How to Turn Your House Into a Flood-Proof House". **Tags:** #Flood #Engineering. **Pinned comment:** "Would you
  let the water in? Yes or no."
- **Set:** one house with a basement, cut open like a cake down to the ground water, a river behind it; brown flood water
  that rises stage by stage; the sewer pipe, the floor drain and the toilet in the cut.
- **First second:** frame 0 brown water creeping across the lawn toward the front door, low and close; by 1 s sandbags are
  thumping into a wall at the door and the dog is watching from the top step.
- **Ladder:** premise "If the river's rising and you stack sandbags at the door, you have a flood-proof house." → water
  seeps between the bags and under the door → a steel barrier that clamps into the door frame on a rubber seal (FLOOD
  BARRIER) → the flood comes up through the floor drain and the toilet instead → a flap in the sewer pipe that only opens
  outward (BACKWATER VALVE) → ground water pushes up through the basement floor → a pit in the lowest corner and a pump
  (SUMP PUMP) → the storm cuts the power and the pump stops → a battery that takes over (BACKUP) → six feet of water
  outside leans on the walls until they crack → openings that let the water flow through the bottom level so the pressure
  is the same on both sides (FLOOD VENTS), with everything that matters moved upstairs → the fix beyond all of those: the
  house floats up on four posts (AMPHIBIOUS FOUNDATION). **Add:** the furnace on a platform, the outlets at chest height, a
  boat tied to the porch. **Close:** "That's your flood-proof house. The bill: about [TOTAL]."
- **The bill** (each ⚠): sandbags (the starting figure); a door barrier; a backwater valve fitted; a sump pit and pump; a
  battery backup; flood vents; raising or floating a house (the big one).
- **The dog:** on the top step in frame 0; in the last shot on the porch of the floating house, tail going.
- **Demand, and who is near (21 Nov 2026):** real footage 28M (a door dam), 9.2M, 8.6M, 4.8M, 4.4M. One build video: The
  Building Box's "How to Protect Your House From A Flood.." 874K (4 Nov); also "How a Tree in Your Yard Becomes a Flood-Proof
  Treehouse" 22K. One recent build video is inside the topic rule; count again at Gate A.
- **⚠ before Gate A:** sewer backflow in floods and the valve that stops it; what flood vents are for and where the building
  code asks for them; amphibious foundations that really exist (the Netherlands, Louisiana); wall failure from water
  pressure; every price.
- **Watch out:** nobody in the water; no real town, river or disaster named; water is the enemy here, so mind the user's
  note about lists that are all water (1.3): B1, B5 and B8 are spaced out.

**B6. How to Turn Your Yard Into a Railroad** (a big yard with a slope)
- **Title:** "How to Turn Your Yard Into a Railroad". **Tags:** #Trains #Railroad. **Pinned comment:** "Steam or diesel? Pick
  one."
- **Set:** one yard cut open like a cake along the track: lawn, a bed of crushed stone under wooden ties and steel rails, a
  shallow cutting through a rise and the dirt piled into the dip beyond it, a side track with a switch, a ride-on train.
- **First second:** frame 0 a wooden cart on two planks laid across the lawn, the dog sitting in it, low and close; by 1 s
  it is rolling and the planks are bowing into the grass.
- **Ladder:** premise "If you lay two planks across the lawn and push a cart along them, you have a railroad." → the cart
  slides off at the first bend → steel rails, and a lip on the inside of every wheel (FLANGE) → the rails sink into the wet
  lawn and spread apart → wooden ties on a bed of crushed stone that locks them and lets the rain through (BALLAST) → the
  yard has a hill and steel wheels just spin on steel rails → dig through the top and pile the dirt into the dip (CUT AND
  FILL): that's why railways look so flat → a second train is coming the other way → a side track and a moving piece of
  rail (SWITCH, SIDING) → a loaded train takes the whole yard to stop, and a coupling can break → brakes that air pressure
  holds off, so a broken hose puts them on (AIR BRAKE). **Add:** a platform, a water tower, a whistle. **Close:** "That's
  your railroad. The bill: about [TOTAL]."
- **The bill** (each ⚠): two planks and a cart (the starting figure); rail by the foot; ties and stone; a day of digging; a
  switch; a ride-on locomotive and cars (the big one); brakes.
- **The dog:** in the cart in frame 0; in the last shot he rides the locomotive's roof with his ears back.
- **Demand, and who is near (21 Nov 2026):** garden and backyard railways 7.4M, 744K, 718K, 504K (real footage); "How a Log
  Road Becomes a Railroad" 413K and "How a Plank on Wheels Becomes a Train" 104K are history builds, not a yard. @youbuiltit
  has a railroad crossing (617K): leave the crossing out.
- **⚠ before Gate A:** flanges and why wheels stay on; what ballast does; the steepest grade a train climbs; how a switch
  works; the fail-safe air brake; every price (ride-on trains run on 7½-inch track: check).
- **Watch out:** train wheels as cones is crowded on Shorts (13.2): one clause at most; no railway company colours.

**B7. How to Turn a Doghouse Into a Mansion** (a corner of a back yard)
- **Title:** "How to Turn a Doghouse Into a Mansion". **Tags:** #Dogs #DogHouse. **Pinned comment:** "What would your dog
  add? And what do we build next?"
- **Set:** one corner of a yard cut open like a cake through a doghouse: the lawn and cold wet ground below, the house's
  raised floor and insulation in the cut face, the inner wall behind the door, a heated pad, a flap door, a small porch.
  The set is small, so every shot is close.
- **First second:** frame 0 a cardboard box on the lawn with a door half cut in it, a blade finishing the cut, big in the
  frame; by 1 s the flap falls out and the dog walks in and turns round.
- **Ladder:** premise "If you cut a door in a cardboard box, you have a doghouse." → the first rain turns it to mush →
  timber walls and a sloped shingle roof with an overhang → the cold ground pulls the heat out through the floor → the
  floor raised on legs with insulation under it (RAISED FLOOR) → the wind blows straight in at the door → the door moved
  to one side with a wall inside it (WINDBREAK) → you build it huge and he still shivers, because his body is the only
  heater → a snug sleeping room and a pad that warms when he lies on it (HEATED PAD): that's why good doghouses are small →
  a raccoon moves in and eats his dinner → a door that reads the chip under his skin and opens only for him (MICROCHIP
  DOOR). **Add:** a porch, a fan for August, a camera that throws him a treat. **Close:** "That's his mansion. The bill:
  about [TOTAL]."
- **The bill** (each ⚠): a cardboard box (the starting figure, nothing); timber and shingles; insulation; a heated pad; a
  microchip door; a porch, a fan and a camera.
- **The dog:** the client: in every shot, never cold or scared for more than a beat.
- **Demand, and who is near (21 Nov 2026):** real builds 6.1M ("DOG MANSION?!"), 2.3M, 1.5M, 1.4M. The nearest build video is
  hole story 3d's "How a Doghouse Becomes a Secret Hideout" 8.1M (16 Nov) and a 22K copy: a hideout for a child under a
  doghouse, not a house for the dog. Count again at Gate A.
- **⚠ before Gate A:** that a doghouse should be only a little bigger than the dog; raised and insulated floors; the offset
  door; pads that heat under the dog's weight; doors that read a microchip; every price.
- **Watch out:** the raccoon is unhurt; no pet brands.

**B8. How to Turn Your Pool Into an Olympic Diving Pool** (a back-yard pool)
- **Title:** "How to Turn Your Pool Into an Olympic Diving Pool". **Tags:** #Diving #Olympics. **Pinned comment:** "Would you
  jump from the top? Yes or no."
- **Set:** one pool cut open like a cake: shallow at first, then dug to a deep blue well; a springboard on its stand, a
  concrete tower, sprayers at the surface, a pipe grid in the pool floor that sends up bubbles, a small hot tub at the side.
  Divers are small and anonymous.
- **First second:** frame 0 a plank being bolted to the pool's edge, close; by 1 s it springs and a cannonball splash
  fills the frame (the dog shakes off the spray).
- **Ladder:** premise "If you bolt a plank to the edge of your pool, you have a diving pool." → the plank barely bends and
  you belly-flop → a board on a roller that slides to set the bounce (SPRINGBOARD, FULCRUM) → you go in head first and the
  bottom is five feet down → dig the pool to sixteen feet (the depth under a ten-metre platform) → a tower as high as a
  three-storey house (PLATFORM) → from up there the water looks like glass and you can't tell where it starts → sprayers
  ripple the surface so you can see it (SURFACE SPRAYERS) → a new dive gone wrong hits like a slap at thirty miles an
  hour → a machine in the floor sends up a cushion of bubbles while you learn (BUBBLER) → you wait your turn wet and your
  muscles go cold → a hot tub and showers by the pool: that's why divers shower between dives. **Add:** judges' chairs, a
  scoreboard, a tiny towel. **Close:** "That's your diving pool. The bill: about [TOTAL]."
- **The bill** (each ⚠): a plank and bolts (the starting figure); a competition springboard and stand; digging and lining a
  deep well (the big one); a concrete tower; sprayers; a bubble machine; a hot tub.
- **The dog:** shakes off the splash in frame 0; in the last shot he stands at the end of the springboard and thinks about it.
- **Demand, and who is near (21 Nov 2026):** "Why they make pools 5FT deep…" 50M; extreme high diving 17M; "How To Dive for
  Swimming" 12M. No diving-pool build video found.
- **⚠ before Gate A:** the depth the rules ask for under a 10 m platform; the speed at the water from 10 m; surface sprayers
  and why; the bubble machine's real name and use; why divers shower and use a small towel; every price.
- **Watch out:** the naive step is a plank at the pool's edge, never a jump from a roof (nothing a child could copy and get
  hurt, 4.3); nobody hits the bottom on screen.

**B9. How to Turn Your Yard Into a Demolition Derby** (a muddy yard)
- **Title:** "How to Turn Your Yard Into a Demolition Derby". **Tags:** #DemolitionDerby #Cars. **Pinned comment:** "Which
  car would you bring? One word."
- **Set:** one yard cut open like a cake: lawn, then a watered mud arena inside a ring of concrete blocks; old cars, one
  of them cut open to show the small fuel tank strapped where the back seat was and the battery on the passenger floor.
- **First second:** frame 0 two old cars nose to nose on the lawn, close; by 1 s one has backed into the other and a
  bumper is spinning across the grass.
- **Ladder:** premise "If you bump two old cars together in your yard, you have a demolition derby." → the windows burst and
  the yard is full of glass → every pane comes out before the start (NO GLASS) → a hit from behind splits the fuel tank →
  a small steel tank strapped inside the car where the back seat was (FUEL CELL) → one hit in the driver's door and it's
  over → the door is painted bright and nobody is allowed to hit it (the DRIVER'S DOOR rule) → the cars are too fast on
  dry ground → a water truck turns the arena to mud: that's why derbies are always muddy → the radiator bursts in the
  first head-on hit → drivers hit with the back of the car: that's why they drive backwards → a car slides toward the
  crowd → a ring of concrete blocks (BARRIER). **Add:** a stick on the roof to snap when you give up, a flag man, a trophy
  for the last car moving. **Close:** "That's your demolition derby. The bill: about [TOTAL]."
- **The bill** (each ⚠): two old cars (the starting figure); a fuel cell; paint; a water truck for a day; concrete blocks;
  a trophy.
- **The dog:** watches from the porch roof in frame 0 and the last shot, in ear muffs.
- **Demand, and who is near (21 Nov 2026):** "A Demo Derby Secret They Don't Want You To Know!" 3.4M; derby prep 242K; 185K.
  No derby build video found. Sequels to racing faded on @whatifplus (1.7), so judge it against B2's result first.
- **⚠ before Gate A:** each rule (glass out, the tank moved, the battery moved, the painted door, hitting with the rear,
  the watered arena, the stick on the roof, the time limit between hits): they differ by track, so say "most"; every price.
- **Watch out:** drivers are helmets behind mesh, nobody hurt, no fire on a person; no car makes or badges; this is the
  hardest motion on the list for the video model (many cars): prove it at Gate D before the batch.

**B10. How to Turn Your Garage Into a Fire Station** (a house with a garage)
- **Title:** "How to Turn Your Garage Into a Fire Station". **Tags:** #FireTruck #Firefighter. **Pinned comment:** "Pole or
  stairs? Pick one."
- **Set:** one two-storey building cut open like a cake: the bunk room upstairs, a brass pole through a hole in the floor,
  the truck bay below with folding doors, a hose on the truck's exhaust pipe, boots standing inside their trousers by the
  truck, a hose tower at the back, a traffic light on the street outside.
- **First second:** frame 0 a red fire truck backing into an ordinary garage with an inch to spare, close; by 1 s the door
  is rolling down behind its bumper and the dog jumps into the cab.
- **Ladder:** premise "If you back a red truck into your garage, you have a fire station." → the call comes at three in the
  morning and the stairs take forever → a hole in the bedroom floor and a brass pole (FIRE POLE; the first one, Chicago,
  1878) → the garage door takes twenty seconds to roll up → doors that fold open sideways in a few seconds (FOUR-FOLD
  DOORS) → the engine fills the garage and the bedroom above with exhaust → a hose that clamps on the tailpipe and lets go
  by itself as the truck pulls out (EXHAUST CAPTURE) → getting dressed takes longer than the drive → boots standing inside
  the trousers, ready to step into (TURNOUT GEAR) → the truck meets every red light → a signal from the truck turns the
  lights green ahead of it (PREEMPTION) → wet hoses rot → a tower to hang them in: that's why old fire stations have
  towers. **Add:** a bell, a kitchen table for the crew, a spot on the truck for the dog. **Close:** "That's your fire
  station. The bill: about [TOTAL]."
- **The bill** (each ⚠): nothing for parking (the starting figure); a fire truck (the big one, new or used); a pole; fold
  doors; an exhaust system; turnout gear; a signal emitter; a tower.
- **The dog:** in the cab from frame 0; in the last shot he rides up front in a small helmet.
- **Demand, and who is near (21 Nov 2026):** weak on the search page (15K, 3K); enthusiast channels do well with fire trucks
  (Tick & Click: a hose popping off a fire truck 448K, 1.6). No fire-station build video found. Unproven demand: make it
  last, or swap in a reserve.
- **⚠ before Gate A:** the 1878 pole; fold doors' opening time against a roll-up door's; exhaust hoses that release as the
  truck leaves; signal preemption; hose towers; every price.
- **Watch out:** no department names, numbers or badges; firefighters small and anonymous.

### 3.1 Reserves and what the check ruled out (21 Nov 2026)
- **Reserves** (open on 21 Nov 2026, weaker or harder): a UFC octagon in your garage (real Shorts 1.2M and "How Much A UFC
  Octagon Cost To Build!" 260K; two fighters are hard for the video model); a music festival in your yard (little proven
  demand); a rally stage or a lawn-mower race track (racing sequels); a zoo in your yard (animals are hard to hold steady).
- **Ruled out, already built by others** (YouTube, 21 Nov 2026): a rocket launch pad (seven videos, the best 110K); a skate
  bowl (4.5M and 600K); an airport or runway (3.0M, 287K, 77K); an NBA arena (Built From Scraps 1.7M, 15 Nov); a zip line
  (You Build This 149K, 20 Nov); a drive-in cinema (Low Poly Films 253K, 14 Nov); a koi pond (4.0M); a secret room behind a
  closet or wardrobe (five videos, to 413K); a Mars base (four); a bathtub submarine (six, the best 1.7M); a storm shelter
  or tornado room (3.4M, 531K, 461K); a hurricane-proof house (two small). The lists of @whatifplus and @youbuiltit are in
  13.2.

---

## 4. Writing the script: the build-steps format (22 Nov 2026)

The "If you…, you have a…" format the user asked for on 21 Nov 2026, tightened on 22 Nov 2026 to the way the helipad video
builds (measured against video 16 in 1.9). Video 16's script, the last under the older rules, is `pipeline/16-script.txt`.

### 4.1 The formula
```
PREMISE (0-4 s)    "If you [one naive step], you have a [THING]."
                   The step is being done on frame 0, by a tool or a part moving by itself. The counter shows what it costs.
LOOP x5            BUT   one sentence: the tester arrives and something breaks, in plain sight.
(12-13 s each,     SO    one sentence: "So you [step], [step], [step] and [step]." About four building steps; each part
 all the same            drops, rises, slides, swings or sweeps into place on the word that names it.
 length)           NAME  "This is a [REAL TERM]." The term goes on screen, its price lands on the counter, and the tester
                         tries again: this time it works.
CLOSE (about 3 s)  "That's your [THING]. The bill: about [TOTAL]." Over the finished build.
END CARD (1.5 s)   The street (4.5). No narration.
```
- Never "Congratulations, you have built…" (rule 5) and never a spoken call to action. The comment question goes in the
  caption or a pinned comment (8.1).
- **Gone since 22 Nov 2026:** the "Add [three finishing touches]" line and the "That's why…" line (they gave video 16 13 s
  of talk after its last fix), and any sentence that explains something the picture can't show.

### 4.2 The opening rules (the evidence is 1.2 and 1.7)
1. **Frame 1 is the naive step being done:** the "before", with its first verb already moving. Never an establishing shot
   and never the finished build.
2. **The scene changes by 1.0 s**, not just the camera: something unrolls, pours, drops, rolls or lights up, big in the frame.
3. **The first word is "If", and the line names what the picture is doing.** Never "If you want…", never a remark.
4. **The subject fills at least a third of the frame** in the first second, readable on a phone.
5. **The premise is finished by about 4 s and the first "But" lands by about 5 s** (the helipad: 4.0 s), with the tester
   arriving on the word.
6. **A bright first frame, in daylight** (5).
7. **It is checked twice:** at Gate A as three lines (frame 0; what has changed by 1.0 s; the premise line and when the
   first "But" lands), and at Gate D on the hook's frames at 0, 0.5, 1 and 2 s (6.2).

### 4.3 Writing rules (22 Nov 2026)
- **Second person, present tense:** "you" build it. The cast is you, your family, your friends, the neighbours and the dog,
  named in the words and shown small and anonymous, or by their things (a lawn chair, a parked car).
- **One tester.** One thing that uses the build (their helicopter on the helipad) comes back in every loop. Each "But" is
  that thing failing in a new way you can watch: physical, a little funny, and it happens to a thing. Nobody is hurt.
- **Every "So" is about four building steps.** Each step is one physical change, big in the frame, that adds to the one
  before, so the fix grows in place. Write them as short verb phrases that end on the part ("pour a slab, stand up four
  walls, lower on a roof, and paint it red"): the part arrives on that word.
- **Only what can be seen.** No numbers, no "about a tenth of the power", no cause that happens inside a wire. A fix that
  can't be built in steps on the set is the wrong fix, or the wrong idea.
- **Each fix is a real thing with a real name,** said after it ("This is a berm.") in all five loops; it goes on screen (5).
- **The loops are the same length** (about 12–13 s) and escalate: a nuisance → damage → danger → the crowd (now everyone
  wants in). The last "But" starts at about 80% of the video.
- **Leave the beats:** about half a second of silence after the premise and before each "But", so the last step can land and
  the tester can arrive. Those pauses are not tightened (6.2 Step 6).
- **Under the ground at least twice:** two of the five fixes put something in the ground or inside a wall, where the cut
  face shows it. (A step that changes the cut ground is still to be proven: 1.9.)
- **Every term and every price is checked** (rule 4, 4.4).
- **Length: about 210 words** (205–215): 64–68 s at Harrison's pace with the beats kept (7.5), which is also what the
  200-credit cap buys in clips (6.1). Never under 61 s (TikTok's Creator Rewards pays only on videos over a minute).
- **Nothing a child could copy and get hurt:** the naive step is harmless or plainly make-believe, and a danger is shown as
  the "But", never as the instruction. TikTok keeps "activities that may lead to moderate physical harm" off the For You feed.
- **Real people:** one sentence, never named if a child, nobody shown hurt; no faces, brand names, logos or team colours.
- **Never reuse a reference account's wording; write every line fresh** (rule 5). Their recurring beats are theirs too: the
  neighbours who peek over the fence and are sold tickets, the neighbour who calls the police, "a queue of your friends".

### 4.4 The bill (ours; accepted 21 Nov 2026, kept on 22 Nov 2026)
A small price counter starts at the cost of the naive step and jumps as each fix is named; the video ends on the total
instead of "Congratulations". My read of why it helps: it plants a question in the first second that only the end answers,
gives people a number to argue about, uses the fact-checking the copies don't do, and gives us a closing line of our own.
1. **One price per fix:** what it costs in the US in 2026 to buy and fit a yard-sized version, from a source that can be
   reopened. Round it; the closing line says "about".
2. **The counter starts at the naive step's cost and jumps once per fix, as its name appears** ("This is a …"). Video 16's
   jumped on "So", which in this style would land on top of the first step.
3. **Where sources disagree,** take the middle and keep the range in the bill file. Where no source can be found, the fix
   stays in the story, adds nothing to the counter, and the bill file says so. Never invent a figure (rule 4).
4. **The total is spoken in round words** in the closing line ("about four hundred thousand dollars") and shown in digits.
5. **The bill file** is `pipeline/NN-bill.md`: item, price, source, date read. Gate A shows it. From a session, prices can
   only be read through web-search summaries (7.7): the file says so, and the user is asked to look at its biggest lines in
   a browser.
6. **It is a story device, not a quote:** the YouTube description says "Rough US prices, 2026." and the caption invites a
   guess ("Guess the bill 💸", 8.1).

How it looks on screen is in 5. Judged after ten videos (2.5): comments per 1,000 views (ours 0.23, theirs 0.26).

### 4.5 The street and the dog (ours; accepted 21 Nov 2026)
- **The street.** An end card of 1.5 s after the closing line: every build so far as a tile (each video's last clean frame,
  `pipeline/street/NN.jpg`), the new one dropping into its place, empty lots for what is still to come, and "WHAT DO WE
  BUILD NEXT?" under them, in our navy and yellow. Made in the edit with no credits (`street_card()` in `16-build.py`). The
  pinned comment asks what to build next (8.1); an idea taken from a comment gets credit in that video's caption.
- **The dog.** The same small dog in every video: in the first shot and the last, and reacting to one failure in between.
  He is never hurt, and never frightened for more than a beat. His words: "a small scruffy tan terrier with a cream chest
  and muzzle, soft folded ears and a red collar". His key is Higgsfield job `51460339-c4b8-4537-9078-bd28de9305f8`
  (`pipeline/16-dog.jpg`), approved by the user on 21 Nov 2026, and it is a reference in every picture he is in (6.3). The
  first build video that is posted asks viewers to name him (8.1).

---

## 5. The look: Cutaway in daylight, built in steps (the look locked 15 Nov 2026 and kept; the stage and the steps 22 Nov 2026)

**What it is.** A bright, clean, photoreal 3D render of one place standing on a block of ground sliced open like a cake, in
soft daylight, with translucent cyan water where there is water. "You" is the viewer and nobody stands in for them: parts
and tools move by themselves, and small anonymous workers or machines appear only where a step needs them. The same dog
every time (4.5). The user locked the look on 15 Nov 2026, after the two videos without the mascot took 90% of our TikTok
views, and kept it on 21 and 22 Nov 2026 ("while keeping our visual style").

**Rule 0. The first second.** The scene changes by 1.0 s, big in the frame, on the first word (4.2). The hook is planned,
priced and checked before any other clip.

**Rule 1. Daylight.** Bright soft daylight on grass, water and sky. Video 16, at dusk, measured 76 of 255 in brightness
against the helipad's 168. Dusk or night only where light is the subject (3.0 rule 6), or when the user asks.

**Rule 2. The stage view.** Fixes are built in one view: the camera high, at about the height of the roof edge and looking
down at about 45 degrees, so the yard fills the middle of the frame like a stage, the house runs across the top, and the cut
face of the ground runs across the bottom fifth with plain ground under it (the caption sits there). What is built is big:
about a third of the frame wide or more. In the test the lawn ran from 13% to 70% of the frame and the shed was 62% wide.

**Rule 3. Built in steps.** Every fix is a stage ladder: the same view, one picture a step, each an edit of the one before.
Each step is its own short clip between two neighbouring pictures, in which the part drops, rises, slides, swings or sweeps
into place by itself, with dust or a bounce where it lands (6.2). One thing changes at a time.

**Rule 4. Something happens about every two seconds.** A build step, the tester failing, a label, the counter's jump: about
35–40 visible changes in a video (the helipad about 50, video 16 about 30), with something moving in 80% or more of the
seconds (`check_video.py`). No frozen pictures: a rest between steps lasts about a second at most, on a finished step,
under the push-in.

**Rule 5. The camera.** Locked while a fix is built, with a slow push-in added in the edit (about 1% a second) so the view
is never dead. Between views (the stage, a closer view of a failure, the last shot) it cuts on the word or takes a 0.3 s
whip; a flight clip only where it earns its cost (`kling4_0`, 6.0). A view inside the ground or a wall is its own picture.

**Rule 6. Hold the look steady.** Every picture is an edit of the set key or of the stage before it, so the set keeps its
parts, colours and materials. The shared style line names no objects and no place.

**Rule 7. Captions:** one word at a time, ALL CAPS, Montserrat ExtraBold ("HBX Caption"), white with a 7 px black stroke
and a soft shadow, letters about 57 px tall at 1080×1920 (ASS `Fontsize` 114), centred about 75% down (y 1440), long words
fitted to 900 px. In the stage view that line sits on the cut face of the ground.

**Rule 8. Pointers** (seldom needed now): solid white arrows about 200 px long with a soft shadow, or one ring with a ~16 px
stroke; one device per beat, pinned to its detail.

**Overlays.** Added in the edit as text and shapes, never asked of the image or video models (their prompts say "No text").
Besides the caption and the counter, one at a time. The code is `16-overlays.py` (labels, counter) and `16-build.py`
(captions, the sign, the card).
- **Term labels:** as the narrator names a fix ("This is a …"), the term appears in ALL CAPS in the caption face, in our
  yellow (#FFD62E) with the caption's black stroke, letters about 70 px tall (`Fontsize` 140), centred about 20% down
  (y 384), for the length of that sentence, with a quick pop in. A term wider than 940 px goes on two lines, and the block
  never starts above y 296, under the counter. A label waits for its picture.
- **The bill counter** (4.4): a small pill centred 11.5% down (y 222, clear of TikTok's tabs), yellow digits about 44 px
  tall (`Fontsize` 88) on ink (#101A33) with a 3 px yellow rim. It shows the running total from frame 0. At a jump the
  fix's price ("+$305", white with the caption's black stroke) slides in at the pill's right over 0.15 s, waits 0.5 s and
  slides into the pill, and the total rolls up over 0.4 s with a tick and a small pop. On the closing line the total grows
  where the last shot is calm, usually the sky above the build, never over the build or the dog (video 16: digits about
  92 px tall, `Fontsize` 184, centred 14.5% down), and holds until the card.
- **Stickers** (22 Nov 2026): flat signs for what can't be built, such as a clock for time passing, a dial or wind arrows.
  One at a time, for a sentence, in ink and yellow, inside the safe box.
- **The street card** (4.5): ink background, yellow tile borders, six lots in two rows of three.
- **The safe box:** overlays stay between 9% and 80% of the height and left of x = 940 below y ≈ 950 (TikTok's buttons).
- **Words inside the scene** (a frequency on a yard sign, a scoreboard, a painted letter that must be exact) are overlays
  warped onto the object in perspective, frame by frame (`sign_pass()` in `16-build.py`), never generated text.
- **The caption may sit lower for one shot** (78% down) when the dog or the subject ends up on its line (`CAP_Y_AT`).

**Sound.** A quiet, steady bed that fits the place, with no tune, 18–22 dB under the voice in the quiet moments
(`under_the_voice.py`). **The steps bring their own sounds:** every `wan2_7` clip comes with sound, and in the test its
loudest moment sat on the impact, so that moment is placed on the step's landing (6.2 Step 6b). Plus the counter's tick and
the till on the final bill. No music, never a copyrighted or trending track. Keep a voice-only master. Claude measures sound
and cannot hear it: the user is the ear, at Gate D.

**Narrator (locked 22 Nov 2026): Harrison.** The user chose him from three audition takes. He is a Higgsfield preset voice,
voice_id `573e5163-59b3-4926-aab1-951ef2985f81`, read by the model `elevenlabs_v4` through Higgsfield (6.0), so the narration
costs Higgsfield credits (5.52 a take of 1,161 characters). Median pitch about 144 Hz; 2.9–3.0 words a second raw, 3.41
once the pauses are tightened and the take plays at 1.1× (7.5). One continuous take of the whole script. Daniel (ElevenLabs
`rFhx8PVgXxOyaeAGq9fq`) narrated videos 01–15 and is retired for builds. Higgsfield's presets are not ElevenLabs' library:
its "Marcus" is a different voice from ElevenLabs' Marcus (7.5).

**Format:** 9:16, 1080×1920, 30 fps, H.264 + AAC, about −14 LUFS. Clips at 720p are upscaled with a light sharpen.

**Retired (the rules are in the archive):** the mascot look (15 Nov 2026); the loop ending and Daniel's voice (21 Nov 2026);
and on 22 Nov 2026 the travelling camera as the way to carry a whole video, with its targets (the old Rule 7: the camera
moving in 65% of seconds, parallax 0.3 px; `camera_path.py` still measures a flight clip), and dusk as an ordinary choice.

---

## 6. Production runbook (for Claude: follow it when asked to make a video; rewritten 22 Nov 2026 for the build-steps style)

> Trigger phrases: "make video #N", "run the runbook on [idea]", or the paste-in prompt (11.1).
> **Never generate anything (pictures, clips, audio) before Gate B is approved.** Script, step sheet and quote are free.
> The method is proven on one fix (1.9). What is marked "to prove" is settled at the first video's Gates C and D; write what
> happens into section 7.

### 6.0 Tools and prices (checked 22 Nov 2026; re-check on the day, prices change)
| Job | Tool | Settings | Cost |
|---|---|---|---|
| Pictures (set key, stage view, stages, keys) | Higgsfield `generate_image_batch`, `seedream_v5_pro` | `resolution:"1k"`, `aspect_ratio:"9:16"`; references as `medias` with role `image_references` (job ids) | **1.25 a picture** |
| Step clips, failures, the hook (the standard since 22 Nov 2026) | `generate_video_batch`, **`wan2_7`** | `resolution:"720p"`, `aspect_ratio:"9:16"`, `duration` 2–15 s, `start_image` + `end_image`; it makes its own sound, so the prompt ends with a "Sound: …" line | **1.50 a second: 3.00 a 2 s clip, 4.50 a 3 s** |
| All the steps of a fix in one clip, or a camera flight | `generate_video_batch`, `kling4_0` | `mode:"image-to-video"`, `resolution:"720p"`, `aspect_ratio:"9:16"`, `duration` 3–30 s, `start_image` + `end_image`, the middle stages in order as `image_references` | 2.50 a second (12.50 for 5 s); it bills at least 3 s |
| Narration | `generate_audio_batch`, `elevenlabs_v4`: `dialogue` = one turn with the whole script, `voice_type:"preset"`, `voice_id` Harrison's (5), `batch_size:1`; one request a take | `estimate_audio_cost` first | 5.52 a take of 1,161 characters |
| Bed, tick, till and spare effects | `generate_audio_batch`, `mirelo_text_to_audio`: a `prompt` and a `duration` in seconds | `estimate_audio_cost` first | 0.25 a second; measure and cut every file (7.5) |
| Price checks | `estimate_image_cost`, `estimate_video_cost`, `estimate_audio_cost` | one call per model, resolution and duration | free |
| Word timings | Higgsfield `sandbox_exec`, faster-whisper `small.en` | `background:true` (foreground calls time out at ~60 s) | free |
| Word timings on this machine | `pipeline/analysis/transcribe.py` (sherpa-onnx with the Parakeet model from GitHub releases) | word starts only | free |
| Assembly, captions, mix | local ffmpeg with libass, Python with OpenCV | — | free |
| Checks | `pipeline/steps-test-check.py` (a clip against its pictures, and when its step happens), `pipeline/analysis/check_video.py`, `under_the_voice.py`, `contact_sheet.py`; `camera_path.py` for a flight | `pip install numpy opencv-python-headless` | free |
| Upload | `media_upload` → PUT (headers `Content-Type`, `If-None-Match: *`) → `media_confirm` | — | free |
| Not used | ElevenLabs (34 credits left since 21 Nov 2026, and Harrison is not in its library; how its speech and sound flows were called is in the archive, 6.0 and 6.2); `minimax_h3` (every queued job failed); `use_unlim` unless the user asks; `virality_predictor` and `tiktok_prepare_publish` only if asked | | |

Other clip models priced on 20 Nov 2026 and never tested: `veo3_1_lite` 6.00 a 4 s clip, `kling3_0` 2.00 a second,
`seedance_2_0` 4.50, `grok_video_v15_lite` 1.00 (no sound). Pictures: `gpt_image_2_6` medium 1k 0.50.

### 6.1 Budget and credit rules (hard; the cap was set by the user on 18 Nov 2026)
0. **At most 200 Higgsfield credits a video, with the 15% reserve, the narration and the sound inside it.** A plan that
   prices above 200 is cut before it is shown (fewer steps, shorter clips, fewer pictures), never shown as is.
1. Script, step sheet, prompts and the quote are free; do them first.
2. Before Gate B, price the exact plan (one estimate per model, resolution and duration), add a **15% reserve**, show the
   total and the balance after it, and wait for approval. Stop and ask if a run will go more than 10% over its quote.
3. Pictures before clips: fix the look, the view and the layout in pictures (1.25), never by re-rolling clips.
4. Pilot first: the hook and one whole fix, shown before the rest (Gate D).
5. One generation per request (no variants). Re-render a bad clip **once**, with a corrected prompt; if it fails again, cut
   the step or rest on the last good frame (a second at most), and tell the user which step lost its clip.
6. Clip length: 2 s for a step that is one simple part, 3 s for a step with several parts or for a failure. The clips in
   total come to about the length of the video.
7. Never auto-retry after a transport timeout; check the job id first.
8. After the run, call `transactions` and report the spend against the quote.

**What videos have cost under the cap:** video 12 186.50, 13 188.00, 14 161.50, 15 196.25, 16 197.99 (its voice and sound,
24.24, came out of a reserve that no re-render had used: luck, not a plan). The build-steps test: 35.00 for one fix made
both ways.

**The standard plan (22 Nov 2026; an estimate from the test, priced again and approved at each Gate B):**

| Item | Plan | Credits |
|---|---|---|
| Clips (`wan2_7`, 720p) | about 68 s: 20 build steps (2 s or 3 s each, about 48 s), five failures of 3 s, the hook 3 s, the last shot 2 s | 102.00 |
| Pictures | the set key, the stage view, the hook's two, five failures, 20 stages, the tester key, one or two closer views: about 32, at most 38 tries | 47.50 |
| Narration | one take of the whole script (about 210 words) | 5.52 |
| Sound | a 10 s bed, the tick, the till and two or three spares, about 20 s; the steps' sounds come with their clips | 5.00 |
| Base | | 160.02 |
| Reserve (15%) | a second narration take, three or four step re-renders, a few picture retries | 24.00 |
| **Quote** | | **184.02** |

- Spend the reserve only on what breaks; a run that has used it stops and asks before going further.
- If the plan has to shrink, take a step out of the weakest fix before touching the hook or the first two loops.
- `kling4_0` only where the quote has room: on that model alone a video in this style does not fit under 200.

### 6.2 Step by step (22 Nov 2026)

**Step 0: Start.** `balance` (and the plan's renewal date if the balance is low). Read the idea and its ⚠ items. Re-fetch
the two build accounts' lists (`PYTHONPATH=<dir> python3 -m yt_dlp --flat-playlist -J https://www.tiktok.com/@whatifplus`,
and the same for `@youbuiltit`; 12.1) and drop the idea if either has made it.

**Step 1: Script (free). GATE A.**
- Choose the tester first; then five failures and five fixes of about four steps each. Write to the formula (4.1), the
  opening rules (4.2) and the writing rules (4.3): about 210 words.
- Fact-check every term and price with web search (7.7); cut what can't be checked. Write the bill (4.4) as
  `pipeline/NN-bill.md`.
- Saturation check with both title shapes: `python3 pipeline/youtube/yt_saturation.py <dir> "how to turn your <place> into
  a <thing>" "how a <humble thing> becomes a <thing>" "<thing> build"` (12.2), and date the near ones with
  `yt_channels.py <dir> shorts:<id>`. The topic rule (1.6, 1.7): more than about three animated build videos of the same
  object in the last 30 days, drop the idea; don't retitle it.
- **Show at Gate A:** the title; the script; the first 5 seconds as three lines (frame 0; what has changed by 1.0 s; the
  premise line and the second its first "But" lands); the loop table (`what breaks, with the tester | the four steps and
  the word each lands on | term on screen | price and its source`); the bill's total; where the dog appears; the facts
  checked; the saturation numbers and the two lists' verdict.

**Step 2: Step sheet (free).**
- One row a clip: `clip | the words it covers | est. s (words ÷ 3.3) | view | start picture → end picture | what moves, in
  the order it moves | the word each step lands on | label | counter | its "Sound:" line`.
- **The stage ladder is the build:** S0 the yard before; H the naive step done (the hook ends on it); then for each loop F,
  the tester having failed, and the stages of the fix, about four, the last one with the tester using it; the last stage of
  the last loop is the finished build.
- **The clips:** the hook (S0 → H, 3 s); for each loop a failure clip (3 s) and one step clip a stage (2 s or 3 s: 6.1
  rule 6); the last shot (2 s). About 68 s in all.
- **The views:** the stage view for every fix (5). A closer view, one extra picture, only where a failure is too small to
  read from the stage.
- **The dog:** the first picture, the last, and one reaction; every other prompt says "No animals".

**Step 3: Quote (free). GATE B.**
- `balance`; an estimate for every picture, every clip length, the narration (the script's characters) and the sound (by
  durations). All of it is Higgsfield credits and inside the quote.
- **The quote with its reserve must be 200 or less** (6.1); if it isn't, cut before showing it.
- Show: pictures, clips by the second, narration, sound, the total with the reserve and the balance after. **Wait for
  approval.**

**Step 4: Project, set key, stage view.**
- `create_project` named `HBX – [title]` and reuse its folder on every generation.
- **The set key:** the place in the Cutaway look in daylight (STYLE, WIDE, one SET line with the place and its colours, one
  CAMERA line with the layout in % of the frame: 6.3), empty of everything that will be built.
- **The stage view:** an edit of the set key that raises the camera (STAGE, 6.3). Check it before going on: the yard fills
  the middle of the frame, the cut face is in the bottom fifth, and nothing on the yard is cut open.
- **The keys:** the dog's exists (4.5). The tester's is one picture of it alone on plain ground, made here and used as a
  reference in every picture it is in.

**Step 5: The stage pictures. GATE C.**
- Each stage is a LOCK edit of the one before (6.3): one change, with its size and place in % of the frame, WHOLE and "No
  people" (and, to try against the colour drift, "the lawn keeps exactly the same bright green": 7.1). Make them one at a
  time and look at each before the next: a wrong stage carries into every later one.
- Re-make a wrong stage once. A stage that fails twice is rethought (a simpler step, or two stages), not forced.
- **Show at Gate C:** the ladder in order as a strip; how well the view holds from stage to stage (the shift in px, as
  `steps-test-check.py` measures it); the tester and the dog against their keys; frame 0 and the last frame.

**Step 6: Narration (after Gate B).**
- Harrison, the whole script as one continuous take (6.0). Order one take, check it, and order a second only if it fails.
- **The check and the word timings are one job:** faster-whisper `small.en` in the Higgsfield sandbox (a background job of
  about a minute; it reads the take's result URL directly), with the rare words in `initial_prompt`. A take passes when
  Whisper returns the script word for word (an extra word is a stray sound, a missing one a swallowed word) and "So you…"
  reads straight through. The script supplies the caption text, Whisper only the timing.
- Tighten the pauses to 0.15 s, **except the beats: keep about half a second after the premise and before each "But"**
  (4.3). Then `atempo` up to 1.1, never more. `16-timing.py` does the tightening (it tightens every pause today: add the
  beats); its `EST` mode gives word times from the script, for the pilot before the voice exists.

**Step 6b: Sound (after Gate B).**
- **The steps' sounds come from their clips.** For each step, cut the clip's sound from a little before its loudest moment
  to about half a second after, and place the loud moment on the step's landing in the video. Leave out a clip's sound if
  it is nearly silent or carries a voice. To prove on video 17.
- **The rest from `mirelo_text_to_audio`,** one request a sound: a 10 s bed (it is looped), the counter's tick (a short, dry
  click), the till for the final bill, and a spare or two. Prompts name the sound, its texture and the space, with no visual
  words; one plain sound a file. Never submit again to retry (it bills again).
- **Measure every file before it goes in the mix** (`16-sound.py` is the pattern): the level every 50 ms and the strongest
  tones. Cut each to the part that is the sound asked for; make the bed a seamless loop.
- **Mix:** set levels from measured loudness on the mono fold-down (`rms_db()`): the bed 19 dB and effects 11 dB under the
  voice; the mono voice on both channels. Then measure the result, not the settings: `under_the_voice.py` for the bed
  (18–22 dB), and the encoded file's loudness and true peak (about −14 LUFS, under −1 dB).

**Step 7: The pilot. GATE D.**
- Render the hook and one whole fix: its failure clip and its step clips. If a `kling4_0` clip is planned (a flight, or a
  fix in one clip), render one of those too.
- Check each clip (`steps-test-check.py`): it starts and ends on its pictures (under half a pixel), the step happens and
  when, and there is no pit, person or text.
- **Show at Gate D, as the edit will play it** (`steps-test-demo.py` is the pattern): the fix with every step on its word,
  with captions, its label and the counter; the hook's frames at 0, 0.5, 1 and 2 s; and the same clips at natural speed
  with their own sound, for the user's ear.
- Don't render the rest until the pilot passes. Fix a failing clip's prompt or its pictures and render it once more.

**Step 8: The rest of the clips.** Batches of up to 12, `jobs_wait`, one `show_generation_by_ids`. Write each job id into
`NN-jobs.tsv` as it is submitted. Check every clip on a sheet at 8 frames a second, as in Step 7.

**Step 9: Assembly (free).**
- **The time map.** For each clip, read when each step lands (the check's numbers and sheet) and place that moment on the
  word that names it (the narration's word times). Between steps the picture rests on the finished step, for a second at
  most. Speed a clip's tail up rather than cutting dust in mid-air.
- Take the nearest source frame, never a blend of two (7.4).
- Shift every frame's colours back to the first picture's (7.4).
- A slow push-in on each locked view, about 1% a second, eased back at a cut. Between views, a cut on the word or a 0.3 s
  whip.
- Upscale the 720p clips to 1080×1920 with a light sharpen (`unsharp=5:5:0.6`).
- Narration at full level, sound under it (Step 6b). Keep a voice-only mix and a clean master (no captions, labels, counter
  or stickers).
- **Check the master:** something moving in 80% or more of the seconds (`check_video.py`); every step within about 0.2 s of
  its word; the bed 18–22 dB under the voice; a sheet of the first 2 s.

**Step 10: Captions, labels, the counter, stickers and the end card (free).** To section 5's spec: one caption cue a word
from the word timings, with the text from the script; a label for the length of its "This is a …" sentence, and the
counter's jump with it; the total's grow on "The bill"; the card after the last word. Verify: every word once, every label
spelled as in the script, the counter's last number equal to the bill file's total, three spot frames readable and inside
the safe box.

**Step 11: Delivery.** Upload the final, the voice-only version and the clean master (`media_upload` → PUT →
`media_confirm`) and give the links. Report the length, credits quoted against spent (`transactions`), the first-second
check, each step against its word, and any step that lost its clip.

**Step 12: Covers and post copy (free).** Three covers (`16-thumbnail.py`), one of them a plain frame; a build cover can
pair the naive step with the finished build, or carry the counter's pill. TikTok and YouTube copy per 8.1 and 8.2. Save the
last clean frame as the street tile (`pipeline/street/NN.jpg`). Log the video in 9.2, add its lessons to 7, and update both
copies of the memory.

### 6.3 Prompt lines (22 Nov 2026; the stage and clip lines ran in the test and are whole in `steps-test-prompts.py`)
- **STYLE** (every picture, and every `kling4_0` clip): "Photoreal 3D cutaway render: the ground is sliced open like a cake
  toward the camera, showing clean layers and what is buried in them. Bright soft daylight, warm tones, soft shadows, mild
  depth of field, clean realistic materials, translucent cyan water, tidy and uncluttered. No text, no letters, no numbers,
  no captions, no logos, no watermark." For a set with no water, drop "translucent cyan water" and add "There is no water
  anywhere."
- **WIDE** (the set key): "Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is
  plain, calm, low-detail ground."
- **SET and CAMERA** (one of each a video): SET carries the place and its colours, never the things to be built, and ends
  "The yard stands on a deep block of ground cut straight down like a slice of cake toward the camera, so the cut face
  shows dark topsoil over even layers of brown earth". CAMERA gives the layout in % of the frame and ends "There is no
  ground in front of the block".
- **POS** (a new view of the same set): "The same [yard, house, …] and block of ground as the reference image, with the same
  parts, colours, materials and light."
- **STAGE** (the stage view, a POS edit of the set key): "New camera position: much higher and a little closer, as if from a
  drone at the height of the house's roof edge, looking down at about 45 degrees. The house's roof and upper floor are cut
  off by the top of the frame: only its ground floor … show, in the top fifth of the frame. The lawn is seen from above and
  fills the frame from about 20% to 64% down, wide and open … Its front edge runs straight across the frame about 64% down;
  below it the cut face of the block of ground … runs down to about 84%, and under that is the same plain pale ground.
  Nothing in view changes: the lawn is empty …"
- **LOCK** (a stage: an edit of the stage before): "Same scene as the reference image. Keep exactly the same camera position,
  zoom and framing as that image: [the house, the hedge, the fence, the lawn and the cut face of the ground] stay exactly
  where they are and the same size. [What is already built] stays exactly where it is. Change only this: [the one change,
  with its size and its place in % of the frame]. [WHOLE] Everything else identical. No people. No animals."
- **WHOLE:** "The lawn stays whole around it: no hole, pit or trench is dug anywhere, and the cut face of the ground at the
  front does not change." For a fix that is buried, name the one opening that is wanted and keep the rest whole.
- **A step clip** (`wan2_7`; from the stage before to the stage after): "[The part and its motion, in the order things move.]
  Nobody is there: the parts move by themselves. The camera is locked and never moves. [STAY] Real speed. Motion starts on
  frame 1. No people, no characters. No animals. No text, no captions, no letters. Sound: [the sounds, in order]." Motions
  that worked as written: "drops straight down out of the sky and lands flat … with a heavy thud: it bounces once, very
  slightly, and a small ring of dust puffs out from under its edges"; "shoot up out of the edges of the slab one after
  another, the back wall first, then the left, the right and the front"; "a wave of barn-red paint sweeps across … from
  left to right"; "swings into the empty doorway and clicks shut".
- **STAY:** "The house, the hedge, the fence, the lawn and the cut face of the ground stay exactly as they are: no hole, pit
  or trench opens anywhere, and no soil appears on the lawn."
- **A whole fix in one clip** (`kling4_0`, 5 s; from the stage before the fix to the fix finished, with the middle stages in
  order as `image_references`): "[STYLE] [The thing] builds itself on the lawn in four quick steps of about one second each.
  First, … Second, … Third, … Fourth, … Nobody is there: the parts move by themselves. The camera is locked and never
  moves. [STAY] Real speed. Motion starts on frame 1. No people, no characters. No animals. No text, no captions, no letters."
- **DOG** (ran on video 16; only the pictures and clips the dog is in): the dog key as an image reference, and "The dog is
  the same dog as in the dog reference: a small scruffy tan terrier with a cream chest and muzzle, soft folded ears and a
  red collar. He is small in the frame, [where he is and what he is doing]." Everywhere else, "No animals." The **tester**
  is to be handled the same way, its key as a reference and the same words every time (to prove on video 17).
- **INDOOR** (ran on videos 10–13; a view indoors): "This is an indoor close-up: nothing is cut open, and there is no soil,
  no ground, no pit and nothing buried anywhere in the frame." On a clip of an indoor set: "The floor is solid grey and
  nothing is cut open: no soil, no pit, no steps, no wooden layers."
- **DUSK** (video 16; only where light is the subject): in STYLE, "Bright soft daylight, warm tones, soft shadows" and
  "translucent cyan water" become "Blue dusk just after sunset: a deep blue sky with a soft orange glow low on the horizon,
  soft even light with no hard shadows, warm light from bulbs and windows". **NIGHT** (a re-grade of a day picture): "IT IS
  NIGHT, with no daylight at all (the daylight described above does not apply to this picture)."
- **A flight** (ran on videos 09–16; `kling4_0`, between two pictures of two different views): "[STYLE] [The move in plain
  words, e.g. The camera swoops down and forward from high above the house to a low, close view of …, and slows as it
  arrives]. [What happens on the way]. Motion starts on frame 1. No people, no characters. No text, no captions."

### 6.4 Scripts to copy (22 Nov 2026)
- **The method** (`pipeline/steps-test-*`): `steps-test-prompts.py` (the stage ladder and the clip requests for both models;
  it reads job ids from its `-jobs.tsv`), `steps-test-check.py` (a clip against its pictures; when each step happens; a
  sheet at 8 frames a second), `steps-test-demo.py` (the time map, the nearest frame, the colour shift, the push-in, the
  captions) and `steps-test.md` (the log).
- **From video 16** (`pipeline/16-*`): `16-timing.py` (pause tightening, the clip plan, `EST`), `16-overlays.py` (labels and
  the counter as ASS events), `16-build.py` (captions, words warped onto a sign, the street card, the mix with `on()` to
  place a sound on its picture, `POST_GAIN` and `LIMIT`, `REUSE=1`), `16-sound.py` (cutting generated sounds),
  `16-thumbnail.py`, `16-post-copy.md`, `16-bill.md`, `16-beat-sheet.md` (the log of every step).
- **Still to write, on video 17:** `17-build.py`, which joins the two: the demo's time map and colour shift with video 16's
  overlays, card and mix, plus placing each clip's own sound on its landing; and the beats in the timing script.
- **Tools:** `pipeline/analysis/` (`check_video.py`, `contact_sheet.py`, `under_the_voice.py`, `camera_path.py`,
  `transcribe.py`, `labels.py`, `hooks_sheet.py`, `voiceprint.py`), `pipeline/tiktok/`, `pipeline/youtube/`,
  `pipeline/branding/` (12). Earlier per-video files stay in `pipeline/` for the record.

---

## 7. Production lessons that still apply (cut down on 22 Nov 2026; the full lists from videos 01–16 are in the archive)

### 7.1 Pictures (seedream)
- **A stage ladder holds the view.** In the test every stage was usable on the first try and the view moved 0.35 px over
  four chained edits; on s2-01 under 1 px over eight. One reference each: the stage before.
- **Chained edits drift in colour:** each came back a little lighter and less yellow (the lawn L 173 → 189, b 160 → 139 over
  four edits; siding, soil and ground about half as much). Try "the lawn keeps exactly the same bright green" in the stage
  prompts (untried); the edit shifts the colours back either way (7.4).
- **The set key decides the layout; fit the plan to it.** Give the layout in % of the frame. A set key can come back from
  head height, where a slab on the lawn would be a sliver: raise the camera with a POS edit (STAGE).
- **The set key can float** over pale ground instead of reaching the bottom edge: keep it, it is a calm place for the caption.
- **The STYLE line's cut ground leaks** into close, aerial and indoor views as pits, trenches and soil under floors. Name
  what stays whole on every picture (WHOLE; INDOOR indoors).
- **Describe parts as the camera sees them,** give sizes against something in the frame ("as tall as a person"), and say
  what a new part stands on or is joined to, and what stays.
- **A LOCK edit that adds big things can pull the camera back:** say the framing stays, or add less per stage.
- **A wrong detail carries into every later edit:** fix it with one edit that names only the swap, before going on. "Change
  only this: remove … Everything else identical" removes a stray object.
- **Real close-ups need "Extreme close-up: the [part] fills most of the frame";** "close-up of" gives a wide shot.
- **The dog held** across pictures with his key as a second reference and the same words; a pose asked for in words held too.
- `seedream` takes about 8 jobs at once (more are refused with 429, no charge). Pictures took 1.1–1.2 tries each on videos
  12 and 16, s2-01 and the test; 1.6–1.8 before every picture was an edit of a neighbour.
- Lighting changes are surer in the edit than in a re-drawn picture.

### 7.2 Clips (wan2_7 and kling4_0)
- **`wan2_7` starts and ends on its pictures** (under 0.15 px in the test, 0 px on s2-01), **does its step in the first
  second** and then holds or settles for 0.5–1.5 s: speed up or cut the tail. 2 s is enough for one simple part, 3 s for a
  step with several. It returns 720×1276 at 30 frames a second, in a few minutes.
- **Its sound follows the picture:** the loudest moment sat on the impact in all four test clips. Quiet prompts come back
  nearly silent (s2-01).
- **Name the motion and the order, and say the parts move by themselves:** both models then did what the words said, and no
  person appeared. Without "No people, no characters" the models invent workers; a time-lapse can show one builder twice.
- **`kling4_0` takes three middle keyframes** and passes through all of them in order: four steps in 5 s, about half a second
  each. It returns 724×1284 at 24 frames a second, makes sound too, and takes 12–13 jobs at once on Ultra (4–17 minutes a
  batch).
- **Every keyframe of one clip must agree on the state of things,** and the prompt says what must not change.
- **What moves must be big in the frame:** a line of small lights read as 0% moving (video 16's hook).
- **A clip between two pictures of one view comes back with a still camera,** whatever the prompt says. For a step that is
  what we want; the push is added in the edit. A start-only clip can really move the camera, and can also drift off the set
  late: use its clean window.
- **A flight, if one is used** (`kling4_0`): each end is a real picture of the set from there, never a crop of another; a
  middle keyframe on the path stops the model inventing its own route; outdoors, name the ground whole in the prompt; and
  an event at the end of a flight lands late against its words. The cases are in the archive (7.2).
- Never auto-retry after a transport timeout; check the job id first.

### 7.3 Pace
- **Count what changes on screen:** the helipad about 50 times in 69 s, video 16 about 30 in 68 s (1.9). Aim for 35–40.
- **A step should take about a second on screen.** Both models do one in 0.3–1 s; the walls took 1.7 s and still read.
- **Judge the pilot as the edit will play it,** not as the clips came: steps on their words, with captions.

### 7.4 Edit, captions and overlays
- **The time map:** a list of (clip, source from, source to, video from, video to), so each step's landing sits on its word
  and the rests between are short (`steps-test-demo.py`).
- **Never blend two source frames when re-timing:** a blend doubled the falling slab. Take the nearest frame. Slow only a
  rest, never a moving part.
- **Take the colour drift out:** shift each frame back to the first picture, read from two patches the build never covers
  (the lawn patch for green pixels, the pale ground for the rest).
- **A push of about 1% a second** keeps a locked view alive; about 3.5% a second reads as a camera move.
- **RAMP** (`16-build.py`): play a clip's first seconds faster and the rest slower so its event lands earlier (video 16's
  lit roof edge moved from 2.0 s to 1.4 s). Slow only a near-still tail.
- **A still made into a segment needs `-framerate 30` on its input,** or zoompan gets 25 frames a second and the segment
  comes out short.
- **Overlays are ASS events:** draw shapes from a top-left origin with `\an7`; take text widths from PIL with the same font
  file (`Fontsize` × 1000 / 1219 = the em in px for Montserrat); a roll-up or a grow is one event a frame.
- **The caption font is rebuilt in each new container:** `npm pack @fontsource/montserrat@5.1.0`, then fontTools
  (`pip install fonttools brotli`) turns `package/files/montserrat-latin-800-normal.woff2` into a TTF named "HBX Caption"
  (name records 1, 4 and 16), saved as `fonts/HBXCaption.ttf`.
- **A long spoken number makes a tiny caption:** show it as digits (`CAPMAP`, `MERGE` in `15-build.py`).
- **Words on an object in the scene** (`sign_pass()` in `16-build.py`): the object's four corners found in every frame,
  followed from the frame where it is biggest, the words warped onto them. It runs before the overlays, so the clean master
  has the words too.
- **`REUSE=1`** keeps the rendered segments and redoes only the overlays, the card and the mix.
- ffmpeg's xfade slide transitions write junk on their first frame: smear the edge with `fillborders` during a whip.

### 7.5 Narration and sound
- **Harrison's numbers** (video 16): 224 words ran 77.56 s raw (2.89 words a second); pauses tightened to 0.15 s and
  `atempo` 1.1 gave 65.69 s, 3.41 words a second. With the beats kept (4.3) about 210 words make 64–68 s. Both takes read
  "The bill:" with a rise, like a question; kept.
- **Never speed a take past 1.1×;** cut words instead. To fix a pronunciation, respell it in the text sent to the voice;
  the captions keep the real word.
- **Choose the take from Whisper's transcript:** an extra word is a stray sound in the audio (take B of video 16), a missing
  one a swallowed word.
- **A voice with the same name is not the same voice:** Higgsfield's preset "Marcus" scored 0.59–0.62 against ElevenLabs'
  Marcus on a voice print (`pipeline/analysis/voiceprint.py`), under what two different ElevenLabs men score against each
  other. The print proves a clear miss; it can't tell two similar voices apart, and it never replaces the user's ear.
- **Preset voices can be screened for nothing** in the Higgsfield sandbox, where their preview files can be fetched; then
  the nearest few get a real take of the video's first lines (1.15 credits each) for the user to choose from.
- **`mirelo_text_to_audio` returns roughly what was asked:** plain single sounds came back right (rain, one click, static, a
  bell); a "run of ticks" came back as one click, "one clunk" as four, "a shimmer" as low thumps. Measure and cut every file
  (`16-sound.py`); ask for one sound a file and a 10 s bed, made into a seamless loop.
- **A new voice needs the mix measured again:** the gain that suited Daniel gave −12.1 LUFS with true peaks over 0 dB on
  Harrison; `POST_GAIN` 0.6 and `LIMIT` 0.79 gave −13.9 LUFS and −2.0 dB. `BED_UNDER` 15 put the bed 21 dB under him.
- **Check the bed with `under_the_voice.py`, not by its setting;** every bed differs. Remix only the audio onto the
  finished picture.
- **Place each effect on its picture:** `on(seg, t)` turns a moment read off a clip into video time.
- **The picture can be finished before the voice exists:** `16-timing.py EST` gives word times from the script, and the
  build runs silent when there is no narration.

### 7.6 Covers
- Build covers from frames of the clean master; check the picture matches the claim at tile size.
- Sizes: YouTube 1080×1920 JPG under 2 MB; TikTok's cover upload crops to 3:4, so upload the 1080×1440 crop (y 240–1680 of
  the 1920 frame). Keep the headline between y ≈ 300 and 1440, clear of TikTok's buttons (x > 940 below y ≈ 950), and the
  subject inside the 3:4 crop too.

### 7.7 Sessions, network and tools (to 22 Nov 2026)
- **Reachable from a session:** the Higgsfield generation CDN (`d8j0ntlcm91z4.cloudfront.net`), `upload.higgsfield.ai`,
  `www.youtube.com`, `i.ytimg.com`, `www.tiktok.com` and its video host `v16-webapp-prime.us.tiktok.com`, GitHub release
  downloads, `raw.githubusercontent.com`, the npm and PyPI registries, `fonts.googleapis.com`, `storage.googleapis.com`.
- **Not reachable:** `huggingface.co` (so Whisper runs in the Higgsfield sandbox); the upload CDN
  `d2ol7oe51mr4n9.cloudfront.net` (give those links to the user); Higgsfield's voice previews (`cdn.higgsfield.ai`,
  `d1xarpci4ikg0w.cloudfront.net`; they open inside the Higgsfield sandbox); TikTok's picture and caption hosts; free 3D
  model sites; `en.wikipedia.org` and most reference sites.
- **No seller's or agency's page opens from a session** (home-improvement stores, hobby shops, `energy.gov`, `fcc.gov`…), by
  WebFetch or curl. Prices and facts rest on WebSearch summaries (extended mode for prices): say so in the bill, and ask the
  user to check its biggest lines in a browser. Don't send a fetch agent after prices (two came back empty).
- **The Higgsfield sandbox:** foreground calls time out at about 60 s (`background:true` for Whisper and renders); it has
  ffmpeg, numpy, onnxruntime and faster-whisper; pip fails there; it keeps outputs for about 24 hours.
- **Local assembly works:** ffmpeg with libass, Python (numpy, OpenCV and PIL by `pip install --target <dir>`), npm, and a
  preinstalled headless Chromium.
- **Session restarts change the scratchpad path:** keep job ids in `NN-jobs.tsv` and commit often. Another session can push
  while a video is in progress: fetch (`--depth=50`) and rebase before each push, and read what changed.
- **Uploading other people's audio to Higgsfield was refused** by the session's safety check (21 Nov 2026). Don't route
  around it; transcribe on this machine (`transcribe.py`).
- **Prices move:** `kling4_0` went from 2.25 to 2.50 a second on 21 Nov 2026. Price every plan on the day.
- **ElevenLabs:** 34 credits left since 21 Nov 2026 (the quota shown is 30,354); a failed run costs nothing;
  `account_get_usage` needs the connector reconnected with more permissions.
- Counting cuts: ffmpeg `select='gt(scene,0.28)',showinfo`, merging cuts under 0.4 s apart. Reading words off a picture:
  `labels.py` (`pip install --target <dir> rapidocr-onnxruntime`). TikTok comments can't be read from a session.

### 7.8 Things that go wrong, and the fix
| What goes wrong | Fix |
|---|---|
| The opening shows a finished scene and nothing happens for 2–3 s | Re-plan frame 0 as the "before" with the step being done, and the change by 1 s (4.2) |
| A step doesn't read: it is too small, or two things change at once | One change a step, about a third of the frame; split it into two stages or cut it |
| A stage picture moves the view or changes the set | Re-make it once from the stage before, with LOCK and what stays named; never build on a wrong stage |
| The lawn pales from stage to stage | "The lawn keeps exactly the same bright green" in the stage prompts; shift the colours back in the edit (7.4) |
| A pit, a trench or soil appears where the ground should be whole | WHOLE on the picture, STAY on the clip (6.3) |
| A person appears | "Nobody is there: the parts move by themselves" and "No people, no characters" |
| A step lands off its word | Read its landing off the clip and move it in the time map; never stretch a moving part (7.4) |
| The picture rests for more than about a second | Speed the clip's tail, bring the next step forward, or add the tester, a sticker or a cut to a closer view |
| The tester or the dog changes between clips | Its key as a reference in every picture it is in, with the same words every time (6.3) |
| The narration makes the video longer than planned | Cut words; never past 1.1×; write for the narrator's measured pace (4.3) |
| The premise runs past 5 s | Cut words from the premise or shorten the naive step |
| A label or the counter sits under TikTok's tabs or buttons | Keep overlays inside the safe box (5) and check three frames on a phone-sized sheet |
| A price can't be sourced | The fix stays in the story, the counter doesn't move for it, and the bill file says so (4.4) |
| A generated sound is not the sound asked for | Measure it; cut the part that is the sound, build a run from one hit, or leave it out (7.5) |
| The finished file is louder than −14 LUFS or its true peak is over −1 dB | Lower `POST_GAIN` and `LIMIT`, remix the audio only, measure again (7.5) |
| The balance is below the quote | Offer fewer steps or a shorter script and name what would be lost; never start a run you can't finish |

---

## 8. Posting and profile (approved by the user on 18 Nov 2026 unless marked; build copy 21 Nov 2026)

### 8.1 TikTok, every video
- **Caption:** the title as a plain line ("How to hide a swimming pool under your lawn"), then "Guess the bill 💸", then
  `#HowItWorks #Engineering #LearnOnTikTok #3DAnimation` and one or two topic tags.
- **The hashtags must turn into links.** Type each tag in the app, or tap it from the suggestion list after typing "#",
  and check that it shows as a link before posting. Afterwards `tt_snapshot.py` shows how many registered (12.1). None did
  from video 02 to video 10; all did on videos 12–15.
- **AI label:** turn on "AI-generated content" when posting. TikTok adds its own label to most of our videos anyway, and
  it didn't stop seawater.
- **Cover:** TikTok Studio on desktop → Edit cover → upload the 1080×1440 crop (7.6).
- **Pin a comment:** "What do we build next?" with the idea's own question. The first build video posted also asks for the
  dog's name (4.5). Reply to every comment in the first day.
- **When:** early evening, US Eastern (our two best went out at about 6–7 pm ET). One video a day as a rule, and never two
  a few hours apart (videos 08 and 09 went out 2.4 h apart and split their first tests). @whatifplus posted two or three a
  day on ten days with no visible harm (1.7), so two in a day are allowed if two are ever ready.
- Don't delete a video that stalls.

### 8.2 YouTube Shorts, every video
- **Title:** the same as TikTok's caption line ("How to Turn Your … Into a …"), under ~60 characters, no hashtags, no call
  to action.
- **Description:** two or three sentences that retell the premise with the named problems, one question for the comments,
  "Rough US prices, 2026.", then at most three hashtags.
- **Audience:** "No, it's not made for kids" on the upload and as the channel default (made-for-kids mode killed video 02
  at 7 views until it was fixed).
- **Altered or synthetic content: leave it unticked** for these cutaways: clearly unrealistic animation is exempt, and no
  source says the label changes reach (18 Nov 2026). Tick it only for a scene that could pass for real footage.
- **Cover:** pick the frame at upload (custom covers need the Partner Program): the most satisfying moment, on a caption
  word that names the picture.
- Pin the comment question, reply to every comment in the first day, and post the same day as TikTok.

### 8.3 Profile (to do; nothing changes until the user says so)
- **Wording for builds** (proposed 21 Nov 2026). The banner: `make_brand_v3.py --line1 "YOUR YARD." --line2 "ANY BUILD."
  --highlight "ANY" --pill "ONE PROBLEM AT A TIME · NEW BUILD EVERY 2 DAYS"`. The TikTok bio on two lines: "Your yard. Any
  build. One problem at a time 🔨" / "New 3D build every 2 days" (72 of 80 characters). The YouTube description, opening
  "Your yard. Any build. One problem at a time." and then "Short 3D builds that turn something you own into something you
  wish you had, with every fix named and the bill added up. Every fact and price is checked. New build every 2 days."
- **Rename the TikTok account:** the handle @overthinkingyearly tells a visitor nothing. The natural pick is the YouTube
  name: check `@letzbuildtogether` with `pipeline/youtube/handles.py <dir> tt letzbuildtogether`. TikTok allows a username
  change once every 30 days.
- **Live now: brand set v3** (drawn in code on 20 Nov 2026, with nothing from the videos): a white cube with its top corner
  cut away, on hi-vis yellow (#FFD62E) with ink (#101A33) outlines; the banner says "YOU'VE SEEN IT. / NOW SEE INSIDE IT."
  and "NEW 3D EXPLAINER EVERY 2 DAYS". On YouTube since 21 Nov 2026 (picture, banner, description); the TikTok bio is v3's;
  TikTok's picture can't be read from a session. Files: `branding/avatar-v3-1080.png`, `avatar-v3-800.png`,
  `banner-v3-2560x1440.jpg`; `pipeline/branding/make_brand_v3.py` and `live_brand_check.py`. The older sets are in
  `branding/` and listed in the archive (8.3).
- **Pin the three best TikTok videos:** seawater, the hydrant, and the best new one as it emerges.

### 8.4 After posting
- Read the views at about 24 h and 72 h on both platforms (12.1, 12.2) and add them to the log (9.2).
- **The bars:** more than ~2K on TikTok within 72 h means it passed the first test; more than ~1K on YouTube means it was
  tested normally; 10K+ is a breakout for us.

---

## 9. Channels, results and the video log

### 9.1 Snapshot (21 Nov 2026, about 22:00 UTC; read from public pages, 12)
- TikTok @overthinkingyearly: 54 followers (44 on 13 Nov), 762 likes, 14 videos, 50.2K views.
- YouTube @LetzBuildTogether: 314 subscribers (282 on 15 Nov), 14 Shorts, about 212K views.
- TikTok shows its own AI label on 12 of the 14 videos and no penalty on any. It files five of them under "Science,
  Education" and gave four no category; one mascot video went under "Anime & Comics". The YouTube uploads are not in
  made-for-kids mode.

### 9.2 Video log (views as read on 21 Nov 2026; the per-video notes and older file ids are in the archive, 9.2)

| # | Title | Made | Look | Credits | Scene changes by 1–2 s? | TikTok views | YouTube views |
|---|---|---|---|---|---|---|---|
| 01 | How Mud Becomes a House in the Desert | 7 Nov | mascot | 106.25 | yes | 3,272 | 2,111 |
| 02 | How a Fallen Tree Becomes a Canoe | 7 Nov | mascot | 202.00 | yes | 1,953 | 203 |
| 03 | Why Don't Fire Hydrants Freeze? | 8 Nov | cutaway | 123.25 | yes | 6,594 | 198,986 |
| 04 | How Seawater Becomes Drinking Water (Without Boiling It) | 10 Nov | cutaway | 111.75 | water flows from frame 1 | 34,700 | 8,833 |
| 05 | How a Steel Tank Becomes a House at the Bottom of the Sea | 11 Nov | mascot | 176.00 | no | 461 | 1,279 |
| 06 | How a Crack in a Cliff Becomes the Hidden City of Petra | 12 Nov | mascot | 158.75 | no | 331 | 67 |
| 07 | 1959 Car vs 2009 Car: Only One Driver Walks Away | 14 Nov | mascot | 157.25 | no | 485 | 52 |
| 08 | Why Your House Doesn't Smell Like the Sewer | 15 Nov | cutaway, one view | 203.50 | no | 363 | 43 |
| 09 | What Lightning Does Inside Your House | 15 Nov | cutaway, travelling camera | 264.25 | no | 383 | 25 |
| 10 | Why These People Are Frozen Upside Down | 17 Nov | cutaway, travelling camera | 278.00 | no | 429 | 16 |
| 11 | Why This Castle Was Built Like a Maze (Himeji) | — | — | quoted 271.69 | stopped by the user at Gate B, 18 Nov | — | — |
| 12 | Why Some Manhole Covers Are Full of Holes | 18 Nov | cutaway, travelling camera | 186.50 | yes | 209 at 72 h | 10 at 72 h |
| 13 | Why Firefighters Drop Frozen Turkeys Into Fryers | 19 Nov | cutaway, travelling camera | 188.00 | yes | 629 at 47 h | 27 at 47 h |
| 14 | Why It Rains Inside a Nuclear Cooling Tower | 20 Nov | cutaway, travelling camera | 161.50 | yes | 52 at 26 h | 9 at 26 h |
| 15 | Why This NFL Field Is Sitting on 546 Wheels | 21 Nov | cutaway, travelling camera | 196.25 | yes | 302 at 20 h | 4 at 20 h |
| 16 | How to Turn Your House Into a Christmas Light Show (B3) | 21–22 Nov | cutaway build at dusk, Harrison's voice, 68.1 s | 197.99 (quoted 199.81) | yes, but thin; first "But" at 3.73 s; bill $2,107 | not posted | not posted |

- **Posted on TikTok** (for the 72 h reads still owed): video 13 on 19 Nov at 23:04 UTC, video 14 on 20 Nov at 20:00 UTC,
  video 15 on 21 Nov at 01:45 UTC (5 h 45 min after video 14). Build videos are logged here from video 17, with the bill's
  total and each read at 24 h and 72 h.
- **Video 16's files** (Higgsfield storage, `https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<id>.mp4`;
  not reachable from a session, so give the links to the user): final `a28f4631-2293-409a-9826-b46a5fe85f65`; voice-only
  `f50c94df-d6ce-4fba-900f-44619fe452b6`; clean master `c3b51b0e-9bc0-467f-8bec-5d83142a9a43`; Higgsfield folder
  `5499c25c-bcd8-441c-9b78-0efb488ac8fe` (the build-steps test is filed there too); job ids in `pipeline/16-jobs.tsv` and
  `pipeline/steps-test-jobs.tsv`; covers in `pipeline/16-covers/`; street tile `pipeline/street/16.jpg`.
- Every video's script, sheet, prompts, job ids and build script are in `pipeline/NN-*`.

### 9.3 What the results taught (to 22 Nov 2026)
- **Our two hits were our two cheapest videos** (the hydrant 123.25, seawater 111.75), and our three most expensive
  (203–278) stalled at about 350 views on TikTok. Spending more on the middle didn't buy reach. Hence the 200-credit cap.
- **The mascot videos did worst;** the topic and the look changed at the same time, so the mascot alone is not proven to be
  the cause.
- **Opening on an event was not enough** (videos 12–15), and their topics were crowded before we made them: a new title on
  the same subject changed nothing (1.6).
- **The audit of 18 Nov 2026 missed the biggest account in our own format** by looking for it under its YouTube handle.
  Check a name several ways (`handles.py`, with and without the underscore) before saying an audience is unserved.
- **In the build format, structure and polish don't separate hits from flops; the object does** (1.7). The effort goes
  into the idea and the first five seconds.
- **Changing direction after almost every video** left each one tested on a different audience (my read). There have been
  seven directions since 6 Nov 2026: mascot builds, cutaway explainers, famous places, matchups, the one-lane explainer
  plan, the build format, and the build-steps style. The build run holds for ten videos (2.5).

---

## 10. Money and monetisation (figures from web searches on 9–21 Nov 2026; re-check before quoting)

- **TikTok Shop affiliate** is a separate project with its own memory, `tiktokshop.md`: 1,000 followers to apply in the US.
  Our animated videos can build followers but can't be the product videos.
- **TikTok Creator Rewards:** 10K followers, 100K views in the last 30 days, 18+, a personal account, videos over 1 minute;
  quoted at about $0.40–1.00 per 1,000 qualified views (third-party figures).
- **YouTube Partner Program:** 1,000 subscribers plus 4,000 watch hours in a year or 10M Shorts views in 90 days; from
  1 Feb 2027 new applicants need 8,000 hours or 20M Shorts views (announced 10 Aug 2026). Shorts pay about $0.03–0.07 per
  1,000 views.
- **"$3,000 a month?"** (answered 11 Nov 2026): not from Shorts ads alone (that is 43–100M views a month); realistic only
  as a mix led by TikTok Creator Rewards and longer videos, once one or two videos a month reach several million views.
- **YouTube's "inauthentic content" rule** (guidance of 16 Jul 2026): generic or template-based videos are not eligible
  for ads, judged across the whole channel. It weighs more in a format hundreds of channels share: the Cutaway look, the
  bill and checked prices are our case that these are not template videos (my read).
- **How the build accounts earn:** each sells a how-to or a kit from the link in its bio (public kits for code-drawn 3D
  shorts sell for about $12–49). A possible later line for us, not a plan.
- **Cost side:** at most 200 Higgsfield credits a video, everything inside it (6.1); the Ultra plan gives 3,000 a month.

---

## 11. The paste-in prompt

### 11.1 Kickoff prompt (renewed 22/11/26: the build-steps style)
Fill in the line in angle brackets and paste the whole block into a new session. Earlier versions are listed in 13.3. For a
style-2 video (paused) the kickoff prompt is `strategy2.md` 11.1, not this one.
```
KICKOFF PROMPT (renewed 22/11/26: the build-steps style)

Read CLAUDE.md in AliKandaz/short-form-video-memory (or the "Short-Form Video Memory"
artifact) first, all sections. Then make the video with the section 6 runbook.

IDEA:   <the idea: "turn your ___ into a ___">
SOUND:  bed and effects (unless I say voice only)

Budget (6.1): at most 200 Higgsfield credits for this video, with the 15% reserve,
the narration and the sound inside it. Check the balance first. If the plan prices
above 200, cut it (fewer steps, shorter clips, fewer pictures) before you show me the
quote.

The style (sections 4 and 5): our Cutaway look in daylight, with the yard seen from
above like a stage. The script opens "If you [one naive step], you have a [thing]."
with that step being done on frame 1, and the first "But" by about 5 s. Then five
loops of the same length: "But [something breaks, in plain sight]. So you [about four
building steps in one sentence]. This is a [real term]." Then the close: "That's your
[thing]. The bill: about [total]." About 210 words, 64-68 s.

Every fix is built on screen in about four steps. Each step is its own short clip
from one fixed view, the part moves into place by itself, and it lands on the word
that names it. One "tester" comes back in every loop and breaks the build a new way.
Only what can be seen: no numbers and no explanations in the narration. Never
"Congratulations..."; never a reference account's wording; no spoken call to action;
nothing a child could copy and get hurt.

Ours: the price counter and the final bill (every price sourced), each real term on
screen for 1-2 s, the street end card, and the dog in the first and last shots and in
one reaction. One-word ALL CAPS captions, 75% down. Narrator: the voice named in
section 5. Step clips on wan2_7 at 720p. Labels, the counter and the end card are
added in the edit, never asked of the image or video models.

Before Gate A: re-fetch @whatifplus's and @youbuiltit's video lists and drop the idea
if either has made it; run the YouTube saturation check with both title shapes ("how
to turn your ... into a ..." and "how a ... becomes a ..."); if more than about three
animated build videos of the same object went up in the last 30 days, drop the idea,
don't retitle it. Fact-check every term and every price.

Stop for my approval at:
- Gate A: the title; the script; the first 5 seconds as three lines (frame 0 / what
  has changed by 1 s / the premise line and when the first "But" lands); the loop
  table (what breaks, with the tester / the four steps and the word each lands on /
  term on screen / price and source); the bill's total; where the dog appears; the
  facts checked; the saturation numbers.
- Gate B: the quote (pictures, clips by the second, narration, sound), 200 or less
  with the reserve, and the balance after.
- Gate C: the stage pictures in order as a strip; how well the view holds from stage
  to stage; the tester and the dog against their reference pictures; the first and
  last frames.
- Gate D: the pilot as the edit will play it: the hook's frames at 0, 0.5, 1 and
  2 s; one whole fix built on its words, with captions, its label and the counter;
  and the same clips at natural speed with their own sound, for me to hear.
Spend nothing before Gate B, and don't render the rest until the pilot passes.

When it's done, give me: the final MP4 link and the voice-only version; the
first-second check and each step against its word; credits quoted against spent; any
step that lost its clip; 3 covers (one a plain frame); TikTok copy (the title, "Guess
the bill", the hashtags for me to type in the app, and the pinned comment) and
YouTube copy (the same title under ~60 characters, a 2-3 sentence description with
"Rough US prices, 2026", not made for kids, altered content unticked). Then log the
video in 9.2, save its street tile, add any new lessons to section 7, and update both
copies of the memory.
```

### 11.2 Re-cut prompt (parked)
The prompt for re-cutting an old video's opening from its existing clips (18/11/26) is parked with the explainer plan; its
text is in the archive (11.2).

---

## 12. Reading the platforms from a session (to 21 Nov 2026)

### 12.1 TikTok
- **Tools:** `pip install --target <dir> yt-dlp`, run with `PYTHONPATH=<dir> python3 -m yt_dlp` (no impersonation target is
  installed; the warning is harmless).
- **An account's videos with stats:** `yt-dlp --flat-playlist -J https://www.tiktok.com/@<handle>`: views, likes, comments,
  shares (`repost_count`), saves, timestamp, duration and caption for each.
- **Everything in one command:** `PYTHONPATH=<dir> python3 pipeline/tiktok/tt_snapshot.py <handle> [--limit N]`: followers
  and the account's flags, then per video the stats, TikTok's category, how many hashtags registered, the AI labels, any
  penalty and the moderation state.
- **Saved for later reading:** `pipeline/tiktok/tt_items.py <handle> <out_dir>` (the list, the profile, each video's detail).
- **Downloads:** `pipeline/tiktok/ttdl.py <out_dir> <video url>…` (it picks a format served from
  `v16-webapp-prime.us.tiktok.com`; the `bytevc1` formats carry no sound).
- **Compare a flop with a hit, not with an ideal:** on 21 Nov 2026 every one of ours carried the same moderation record.
  What only the owner sees: Settings and privacy → Account → Account status.
- TikTok's own captions and its comments can't be fetched from a session: transcribe the sound (`transcribe.py`).

### 12.2 YouTube
- **Reachable:** `www.youtube.com` (`/shorts/<id>` and channel pages), `i.ytimg.com`, `yt3.ggpht.com`,
  `yt3.googleusercontent.com`. `/watch?v=` redirects to a blocked bot check: no captions, durations or downloads.
- **Scripts in `pipeline/youtube/`** (usage in each docstring; pace requests 2–3 s apart): `yt_snapshot.py @handle [dir]`
  (channel facts, every Short's views, likes and date, comments, a made-for-kids check); `yt_saturation.py <dir> "<query>"
  …` (the saturation check: how many Shorts, and the top Shorts and long videos, per query); `yt_search.py <dir>
  "<query>"`; `yt_channels.py <dir> handle:@name shorts:<id>` (a channel's latest and most popular Shorts, or who posted a
  Short and when); `handles.py <dir> yt|tt <handle>…` (is a handle taken; try several spellings).
- `pipeline/branding/live_brand_check.py`: which file in `branding/` is the live picture and banner.
- **Frames without a download:** `https://i.ytimg.com/vi/<id>/frame0.jpg` (the first frame) and `oar1.jpg`, `oar2.jpg`,
  `oar3.jpg`.
- YouTube counts a Shorts view each time one starts playing, so a Short with tens of views was hardly shown.
- **Is a channel held back?** Search each Short's exact title unquoted and in quotes, and benchmark against brand-new
  channels in the niche. **Fetch once and take what comes; never loop requests to get past "Sign in to confirm you're not a
  bot"** (refused on 21 Nov 2026 as unauthorized access). Strikes, age restrictions and claims are read by the owner in
  Studio.

### 12.3 Looking at a video
- **The opening:** frames at 0, 0.5, 1, 2 and 3 s (`ffmpeg -ss <t> -i <video> -frames:v 1 -vf scale=180:320 <out>.png`)
  beside a reference's.
- **The whole video** (`pipeline/analysis/`): `contact_sheet.py` (a frame a second), `check_video.py` (the share of seconds
  moving, caption size, sharpness), `under_the_voice.py` (what sits under the narration), `camera_path.py` (the camera's
  moves), `hooks_sheet.py` (the first seconds of every video of an account), `transcribe.py` (speech to text with a time
  for every word, on this machine), `labels.py` (the words on the picture).
- **Nothing has been listened to;** sound is measured, not judged by ear. A voice is chosen by the user's ear.

### 12.4 Web research
- WebSearch summaries work; WebFetch can't open most reference and seller sites (7.7). Say when a fact rests on a search
  summary.

### 12.5 Studying a reference account end to end (the method of 21 Nov 2026; about an hour for 42 videos, no credits)
`tt_items.py` for the list and the spread of views; `ttdl.py` and `hooks_sheet.py` for the first seconds, ranked by views;
`transcribe.py` on every video, then count words, pace, "But"s, named terms and when the first "But" lands; `check_video.py`
and the cut count on a sample; who else makes it (`handles.py`, `yt_saturation.py`, `yt_channels.py`); and how it is made
(frame rate, whether every frame is unique, the bio link). Compare the top ten with the bottom ten before believing any
rule. Write what was measured, what is "my read", and what couldn't be checked.

---

## 13. Parked ideas, topics to avoid, and history

13.1 and 13.2 are unchanged since 21 Nov 2026 (rule 8).

### 13.1 Parked ideas (X and F ideas: approved 16–18 Nov 2026, parked 18 Nov; the explainer plan's: parked 21 Nov 2026)
Their full entries (draft scripts or story beats, sets, camera positions, checked facts, sources) are in section 2 of the file at
commit `1174f29`. If one comes back, rewrite its opening to Rule 0 first: frame 1 the "before" or the event, a change by 1 s.
- **X1 There Are More People Under Paris Than In It** (the catacombs): footage leads (22M); no animated cutaway. Built-in event: the
  street dropping into the quarries (1774).
- **X2 The Town That's Been On Fire Since 1962** (Centralia): a facts Short has 20.9M. Event: the ground opening in a back yard.
- **X3 This Car Split in Half and Caught Fire. The Driver Walked Out.** (Grosjean and the halo, 2020): footage 2.4M. Event: the
  impact. Real person: helmet only, no logos.
- **X4 The Alaska Town That Lives in One Building** (Whittier): a 13.8M long video. Weakest event of the four.
- **F1 Why This Rock Has More Tunnels Than Roads** (Gibraltar) and **F2 This Castle Beat an Army. Then Its Own Guards Sold It.**
  (Malbork): story beats only, place named at the end (NET FILES' device).
- **F3 Why This Castle Was Built Like a Maze** (Himeji): script approved at Gate A and beat sheet in `pipeline/11-*`; quoted at
  271.69 and stopped by the user on 18 Nov 2026. Under the cap it would need about 220 words and 7–9 positions.
- **Parked on 21 Nov 2026 with the explainer plan** (titles, draft scripts, sets and checked facts are in section 3 of this
  file at commit `a9abd35`): V4 The Ice Under This Court Cancelled an NBA Game (Cutaway Instinct has the court at 1.3M; Built
  From Scraps built an NBA arena, 1.7M, 15 Nov); V5 Why Water Heaters Can Launch Through the Roof; V7 What's Hiding Under a
  Wave Pool (@youbuiltit's wave pool 1.8M, 8 Nov); V8 What's Hiding Behind the Pins at a Bowling Alley (@youbuiltit 226K);
  V9 The Airport Baggage System That Ate Suitcases (@youbuiltit 158K); V10 How Do Fish Get Past a Dam? (@youbuiltit's dam
  1.4M); and the reserves (the grease fire, roller coasters, NFL fields that don't freeze, frozen pipes, fire sprinklers).
  Their checked facts can feed a build video's "that's why" lines.
- **The free re-cut test** of videos 09, 10 and 07 (new openings from their existing clips; prompt 11.2): parked on 21 Nov
  2026.
- **Code-drawn 3D** (1.8): tested on 21 Nov 2026 and set aside when the user kept the look; an option if credits become
  the limit. **The floating-block look** (the yard as a cut cube, like our logo) was offered the same day and not taken.

### 13.2 Topics to avoid
- **Made by us:** the mud house, the canoe, the fire hydrant, seawater to tap water, the underwater habitat (Aquarius), Petra, the
  1959 vs 2009 crash, the sewer trap, lightning in a house, cryonics, the manhole covers (video 12), frozen turkeys in the fryer
  (video 13), the rain inside a nuclear cooling tower (video 14), the NFL field that rolls outside on 546 wheels (video 15).
- **Made by Hidden By Design:** the storm drain, the water well and water tower, a road tunnel under a river, a landfill into a
  park, a bridge foundation (cofferdam), the sewer and treatment works, power lines, the gas station, the roof, the beach.
- **Made by How Building Explained:** the nipa hut, an Amazon floating house, the igloo, the levee, a nuclear bunker, a nuclear
  plant (our cooling tower is the tower only, never a plant), Chernobyl, the White House, the Kremlin, a particle accelerator, an
  armored truck, the gas station, the car wash, an oil well, the septic tank, a drive-thru, a slot machine, a car engine,
  fire-, volcano- and earthquake-proof houses, a Halloween station.
- **Made by @scapemagicc** (photoreal AI builds; all 86 videos to 21 Nov 2026 are listed in `strategy2.md` 10): tiny houses inside
  septic tanks, pipes, dumpsters, containers, buses, tires, pallets and pools, and in caves, pits and gardens.
- **Made by @whatifplus** (all 42 to 20 Nov 2026; `research/whatifplus-videos.tsv`; re-fetch before each Gate A): a bunker, a
  hot tub, a slip-n-slide, a treehouse, an underground trampoline pit, a sauna, an underground garage, a gaming room, a
  bouncy castle, a go-kart track, a golf course, an underground aquarium, a bumper-car arena, a drive-thru car wash, a
  waterpark, a backyard gym, an F1 circuit, a NASCAR track, a football stadium, a MotoGP track, an indoor skydiving tunnel, a
  monster-truck arena, a ninja-warrior course, a drag strip, the Louvre from the Mona Lisa, a roller coaster, a paintball
  arena, a log cabin, a zombie base, a zombie escape vehicle, an alien-proof house, a warm house in winter, a dinosaur-proof
  house, a last-person-on-Earth survival base, a ski resort, an NFL stadium from a street, a WWE arena from a mattress, the
  Golden Gate Bridge, a bank vault from a mattress, a Black Friday sale, an ice rink, a helipad.
- **Made by @youbuiltit** (all 97 to 21 Nov 2026; `research/youbuiltit-videos.tsv`; re-fetch before each Gate A). *Home and
  street:* a swimming pool, a toilet, running water, a fireplace, a septic tank, a refrigerator, a washing machine, a road, a
  roof, a stove, an air conditioner, a shower, a dishwasher, a clothes dryer, central heating, house electricity, a garage
  door, a foundation, a hot tub, a front door, a vending machine, a water tower, a car wash, a gas station, a sprinkler
  system, an escalator, a fire hydrant (twice), a storm shelter, a bank vault, a traffic light, an ATM, a railroad crossing, a
  tower crane, an automatic door, a garbage truck, an elevator, an airport baggage system, a concrete mixer truck, an airplane
  toilet, a fire sprinkler, a subway, a burglar alarm, a rain gutter, a chicken coop, a treehouse, a lawn mower (21 Nov).
  *Fun:* a roller coaster (twice), a bowling alley, a claw machine, a soft-serve machine, an ice rink, a water slide, a ski
  chairlift, a carousel, a wave pool, a lazy river, an infinity pool, a Ferris wheel, a splash pad. *Survival and history:* a
  log cabin, a pyramid, a Viking ship, the Colosseum, a lighthouse, a Roman aqueduct, a shelter in the woods, a trebuchet, a
  campfire, a fish trap, a windmill, clean drinking water, an island shelter, Stonehenge, a rope bridge, a Roman bath, the
  Great Escape tunnel, an igloo, a dam, a smokehouse, a castle, a cathedral, a raft, drinking water from sand, the Great Wall,
  the Statue of Liberty, a drawbridge, a jungle stilt hut, a dugout canoe, the Easter Island heads, a tipi, maple syrup, a
  reed boat, a bark canoe, an earth oven, a cooking pot.
- **Built by other channels on YouTube** (found 21 Nov 2026; 1.7, 3.1): a bunker (a dozen), a rocket launch pad, a skate
  bowl, an airport, an NBA arena, a zip line, a drive-in cinema, a pond and a koi pond, a secret room behind a wardrobe, a
  closet or a fridge, a hideout under a doghouse, a Mars base, a bathtub submarine and cruise ship, a storm shelter and a
  tornado room, a hurricane-proof house, flood protection (one), a pool turned into a bunker, and YouTube copies of
  @whatifplus's F1, NASCAR, MotoGP, bumper-car, go-kart and helipad titles.
- **Zack D. Films' scenarios** (16 Nov 2026): falling off a cruise ship, through ice, into a grain bin; an avalanche; a tar pit;
  sinkholes; a plane losing oxygen and its masks; straightening Pisa; a power line on your car; the meteorite that hit a woman; the
  microwave's metal screen and ice in a microwave; the gold vault under Manhattan. Taken by others: quicksand, Niagara Falls in a
  barrel, the Thai cave rescue, opening a plane door in flight, Lake Nyos.
- **Crowded on Shorts** (9–18 Nov 2026): train wheels as cones, airplane toilets, undersea cables, McDonald's Coke, New York's street
  steam, Tokyo's flood tunnel, escaping a sinking car, tsunami builds and survival, the Fudai floodgate, oil-well fires, the Kola
  borehole, the Costa Concordia, the Persian yakhchal, Biosphere 2, a sunken-submarine escape, Kansai airport, ice roads, Machu
  Picchu's underground, Cheyenne Mountain, the Chile miners, floating bridges, the Hanging Temple, Ski Dubai, Troll A, the inside of
  a fire extinguisher; as builds: castles, the Panama Canal, wells, cave homes, lighthouses, the Hoover Dam, bank vaults, pyramids,
  cranes, elevators, traffic lights; fortress stories already told: Château Gaillard's toilet, Mont-Saint-Michel's siege, Sigiriya's
  elephant, Janjira's fresh water.
- **Weak on Shorts** (small proven demand): escalator steps, frozen pipes, potholes, fire sprinklers (15 Nov 2026); Apollo 13's
  filter, stalling on a railroad crossing, Detroit's salt mine, a mine cooled with ice, oxygen-mask bags (16 Nov 2026).
- **Don't propose unless the user asks:** a race car driving on the ceiling ("I don't like p5", 14 Nov 2026); landing a jet on an
  aircraft carrier (swapped out 15 Nov 2026). **Turned down as a set** (all water, 16 Nov 2026): the pool at the edge of Victoria
  Falls, Dubai's deepest pool, the slot-canyon flood, the Qiantang bore, Monticello Dam's spillway hole; one could come back in a
  mixed list.

### 13.3 History (one line a phase; the step-by-step history is in the archive, 13.3)
- **6–10 Nov 2026:** videos 01–04: How Building Explained's formula with a mascot, then Hidden By Design's cutaway look. The
  hydrant (199K on YouTube) and seawater (34.7K on TikTok) are still our only hits.
- **11–17 Nov:** videos 05–10: famous places, a matchup, the travelling camera. The Cutaway look locked without a character
  (15 Nov); sound approved.
- **18–21 Nov:** the growth audit, the 200-credit cap and the explainer plan; videos 12–15, none past the first test; brand
  set v3; style 2 (`strategy2.md`) and its first video; the reach check (1.6).
- **21 Nov:** the user asked to shift to @whatifplus's style: both build accounts studied (1.7), the build format, ten build
  ideas, the bill, the street and the dog; the look kept; a new voice asked for.
- **21–22 Nov:** video 16 (B3) made: Harrison chosen, the voice and the sound moved to Higgsfield, 197.99 credits.
- **22 Nov:** the user didn't like video 16; it was measured against the helipad video (1.9); the build-steps test worked
  (35.00 credits); the user chose the style and asked for this revision, with the ideas left for later.
- **Paste-in prompts before this one:** 11/11/26 (`f8bf298`), 15/11/26 (`db03adc`), 15/11/26 v2 (`309d785`), 18/11/26
  (`1174f29`), 18/11/26 v2 (`a9abd35`), 21/11/26 with its update of 22/11/26 (`549e291`, and the archive).
