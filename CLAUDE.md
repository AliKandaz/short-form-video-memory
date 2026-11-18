# Short-Form 3D Cutaway Explainers: Project Memory

**Rewritten from scratch on 18 Nov 2026** at the user's request: "with everything you've learned and found out, I want you to
completely redo my claude.md file … set the file up for success, I will be creating 10 videos with the recommendations you made
in this session … get inspiration from the successful channels … mark the date on all the new information in the file and remove
any irrelevant or dated information." Every section carries a date. What was removed (the mascot look, old idea lists, per-video
notes from videos 01–07, superseded tool notes) is in the repo history: the last version before the rewrite is commit `1174f29`.

## 0. Start here (18 Nov 2026)

**What we make.** Vertical 3D explainers, about 62–64 s: one real place sliced open like a cake, seen by a camera that flies in
to each change and away again, narrated in second person ("you") by an AI voice, with one-word captions. Each video answers one
question about the hidden inside of something everyone uses or walks past, one problem and one fix at a time, and loops back to
its first frame. No character, no on-screen labels, no music (a quiet bed and a few sound effects).

**Channels** (both US-based, the user confirmed on 13 Nov 2026):
- TikTok **@overthinkingyearly** (display name "overthinkingyearly"; it was "OT" until 18 Nov 2026): 54 followers, 10 videos,
  46.4K views on 18 Nov 2026. Renaming it to match the content is part of the plan (8.3).
- YouTube **@LetzBuildTogether** ("LetZBuildTogether", channel id `UCNaqNT-R3K2GmISUfLdfBzA`): 310 subscribers, 10 Shorts, about
  209K views on 18 Nov 2026, 196K of them on the fire-hydrant Short.

**The plan (approved by the user on 18 Nov 2026): 10 videos in one lane, each opening on something happening in the first
second.** The lane is the hidden inside of things everyone uses or walks past. The ideas, with draft scripts, are section 3; the
plan, the order and the budget are section 2; the evidence behind it is section 1.

**Where things live:**
- This file and `tiktokshop.md` (the TikTok Shop affiliate project) in the GitHub repo `AliKandaz/short-form-video-memory`, with
  the reusable scripts in `pipeline/` and the channel artwork in `branding/`.
- A live copy: the "Short-Form Video Memory" artifact, https://claude.ai/artifact/Fvbzc2HQyDxne7Y8NsrgvX (Artifact tool, action
  "read"). **When this file changes, update both copies:** commit and push, then republish the artifact by its url.
- The old visual reference for How Building Explained's look (mascot era, kept for the record only):
  https://claude.ai/artifact/MPEu5jqcnUDLSsz3fiBc8N.

**Standing rules (all still in force on 18 Nov 2026):**
1. Never spend Higgsfield credits before the user approves the quote at Gate B (6.1). Script, beat sheet and quote are free.
   **At most 200 Higgsfield credits a video, reserve included** (the user, 18 Nov 2026: "I want at most 200 credits per video").
2. Stop at the four gates: A script, B quote, C stills, D pilot clips (6.2).
3. Don't ask the user for retention or watch-time figures ("forget about the retention graphs", 15 Nov 2026). Work from what can
   be read from outside (12).
4. Fact-check every number before Gate A; cut what can't be checked; never plant a mistake to bait comments.
5. Never reuse a reference account's wording, and never end on "Congratulations, you have built…" (How Building Explained's line).
6. When the memory changes, update both copies (above).

**Status on 18 Nov 2026:**
- Videos 01–10 are made and posted on both platforms (9.2). Credits: 1,762.25 after video 10 (check `balance`).
- **Video 11 (Himeji Castle, parked idea F3) was stopped by the user on 18 Nov 2026** at its quote (271.69 at 720p), with the
  message "I want at most 200 credits per video". Its approved script and beat sheet stay in `pipeline/11-*` (13.1).
- **A new profile picture and YouTube banner without the mascot** were made on 18 Nov 2026 (the user asked for eye-catching
  ones), from the videos' own stills, no credits; the user hasn't picked yet (8.3).
- **Video 12 (V1, "Why Some Manhole Covers Are Full of Holes") was made on 18 Nov 2026**, the first of the ten and the first
  under the cap: 63.7 s, 186.50 credits against a 194.64 quote; balance 1,575.75 after it. Not posted yet (9.2; copy in
  `pipeline/12-post-copy.md`). Its title changed at Gate A because the plain road-salt angle already had about nine small Shorts
  (3, V1).
- **Next:** post video 12 (8.1, 8.2); V2 (the turkey) has to be posted by Tue 24 Nov 2026; the free re-cut test and the profile
  fixes (2.2) are still to do. Each video quoted at 200 or less.

**Map of this file:** 1 what works (evidence) · 2 the 10-video plan · 3 the ten ideas with draft scripts · 4 writing the script
· 5 the look · 6 production runbook · 7 production lessons · 8 posting and profile · 9 channels, results and the video log ·
10 money · 11 paste-in prompts · 12 reading the platforms from a session · 13 parked ideas, topics to avoid and history.

---

## 1. What works in this format (evidence to 18 Nov 2026)

Read from public pages only (12). "My read" marks interpretation rather than measurement.

### 1.1 How the platforms decide (18 Nov 2026)
- **Each video is tested on a small audience first.** If enough of them keep watching, it is shown to more people; if not, it
  stops. Views therefore land at the first ceiling or take off; they don't spread evenly.
- **Our first ceilings:** TikTok stops a failed video at about 330–454 views (all six videos since seawater). YouTube gave our first
  Shorts 1.2K–9K each, then gave the last five almost no test at all (11–64 views; YouTube counts a view every time a Short starts,
  so that means it was hardly shown).
- **The reference accounts' floors are 30–150 times ours** (TikTok, 18 Nov 2026): Hidden By Design's weakest video has 49K, How
  Building Explained's 10.8K. Their spread is as wide as ours (200 to 1,000 times between best and worst): inconsistency is
  normal; what differs is how often a video passes the first test.
- **The same video can fail one platform and break out on the other:** the hydrant got 6.3K on TikTok and 196K on YouTube;
  seawater 33.9K on TikTok and 8.8K on YouTube. A video that fails once is not proven bad.
- **Followers come from reach, not the profile:** we turn 1.2 followers per 1,000 views, How Building Explained 1.3 and Hidden By
  Design 2.6.
- **After a breakout, YouTube seems to test the next Shorts on people like the breakout's viewers** (my read, from creator
  reports, nothing official). Our collapse to 11–64 views began with Petra (12 Nov), while the hydrant was going viral, and the
  five Shorts that followed were off its topic. The 300 subscribers came for "how the stuff on your street works".

### 1.2 The first two seconds (measured 18 Nov 2026; the biggest finding)
Frames at 0, 0.5, 1, 2 and 3 s of all ten of our videos against six reference videos (Hidden By Design's storm drain 10.1M, roof
4.5M, landfill 4.2M and beach 49K; How Building Explained's nipa hut 12M and car wash 10.8K).
- **In every reference video the scene itself changes within 0.5–2 s, on the first verb:** a hole is cut in the street and fills
  with rain; plywood covers the roof; a trench is dug and a truck dumps trash; a truck dumps sand; a bamboo raft appears; a hole is
  dug and soap poured in. The first frame is the "before". Even their flops do this.
- **Ours, mostly, open on a finished scene that sits still:** lightning shows no lightning in its first 3 s; the car video is a
  frozen frame for 3 s; the sewer picture doesn't change for 3 s; cryonics glides over a finished lab, then cuts to a covered body.
- **Every one of ours where something changes early passed TikTok's first test:** the mud house (a wall goes up), the canoe (the
  log rolls into the river) and the hydrant (water bursts out at about 2 s) got 1.9K–6.3K. Six of the seven without it stopped at
  330–454; the exception is seawater, with water flowing from the first frame (33.9K).
- **The first lines drifted the same way:** "If you stick a pipe on the water main…" (an action you can see) became "If you want
  to cheat death…", "If you want a hidden city…", "Everyone's heard it…" (wishes and remarks the picture can't show).
- **The animation upgrade went into the middle of the video.** Videos 09 and 10 met every whole-video motion and camera target
  (84% and 90% of seconds moving) and stopped at the same ~350 views as 05–08 (my read: the middle is where most people never get).
- `check_video.py` on the first 3 s does not separate these: a camera gliding over a finished set counts as movement. Judge
  openings by looking at frames 0–2 s (4.2, 6.2 Gate D).

### 1.3 Topics that win and topics that lose (to 18 Nov 2026)
- **Win:** the hidden workings of something everyone uses or walks past, with something moving through it that the camera can
  follow (water, fire, power, a ball): Hidden By Design's storm drain 10.1M, roof 4.5M, landfill 4.2M, water well 1.0M; our hydrant
  196K and seawater 33.9K. On YouTube, "your yard" builds and true escape stories (You Made It's Cu Chi tunnels 36M, You Built It's
  swimming pool 8.3M).
- **Win when the place is the payoff:** a defense puzzle with the place named only at the end (NET FILES' fortress 1.3M in 33 h).
- **Lose for us:** famous landmarks and remote places (Aquarius 454, Petra 330), a matchup (the car crash 364), a far-off subject
  (cryonics 359), the cartoon mascot (TikTok filed Petra as "Anime & Comics"), and mundane things whose workings are already visible
  (the gas station flopped on both reference accounts).
- **Comments** come from a choice put to the viewer ("Would you…? Yes or no.") and from subjects people argue about (14 Nov 2026:
  @thewhatifstudio 0.66 comments per 1,000 views, us 0.23). They don't decide reach on their own: Hidden By Design has the fewest
  comments per view and the steadiest views.
- **Water helps:** Hidden By Design's five best mature videos all have water as the payload or the enemy. But a list that is all
  water reads as one idea to the user ("all these are water, sea, lake related. mix it up", 16 Nov 2026).

### 1.4 The successful channels and what we take from each (18 Nov 2026)

| Channel | Numbers (date read) | What we take |
|---|---|---|
| **Hidden By Design**, TikTok @1hidden_by_design | 57.5K followers, 10 videos, 22.0M views; median 689K, lowest 49K; storm drain 10.1M, roof 4.5M, landfill 4.2M; no post since 9 Nov (18 Nov) | Our look comes from it: everyday hidden workings, the ground cut like a cake, a travelling camera, a quiet bed, no labels, a loop ending, titles about "your street" or "your house", the build starting in the first second |
| **How Building Explained**, TikTok @howbuildingexplained | 31.4K followers, 22 videos, 23.3M; nipa hut 12M, levee 1.9M; bio now "It was a good run, Zach was here"; no post since 3 Nov (18 Nov) | The But/So formula, a short tight script (the 12M hit is 66 s), the build visibly starting by 2 s. Mundane utilities flopped (car wash 10.8K) |
| **You Made It**, YouTube @youmadeit3d | 128K subscribers, 13 Shorts; Cu Chi tunnels 36M, cave home 23.5M, hole in your yard → basement 8.8M (9 Nov) | Quality over volume ("about 12 hours a video"); true escape and war stories; "your yard" |
| **You Built It**, YouTube @youbuilt_it | 64.7K subscribers, 60 Shorts; swimming pool 8.3M, road 5.6M, roof 3.4M (9 Nov) | Things you'd want at your own house |
| **NET FILES**, TikTok @net.files6 | 276 videos, 72.2M views; quicksand tomb 10.2M; mountain fortress 1.3M in 33 h; most recent videos 5K–15K (17 Nov) | A defense puzzle, the place named only at the end; volume plus a few hits |
| **Cutaway Instinct** (YouTube Shorts) | stadium and arena cutaways in our style; best Shorts 1.3M; Lambeau's heated field 123K (4 Nov 2026), then copied five times (18 Nov) | A direct rival in our look: search it before any stadium or arena idea (V4, V6) |
| **Zack D. Films** (YouTube Shorts) | owns "what happens if you…" survival scenarios: cruise ship 50M, falling through ice 64M (16 Nov) | Avoid his topics; check every idea against him |
| **@thewhatifstudio**, TikTok | 60.9K followers; what-if simulations median 457K, its builds median 35K (14 Nov) | A choice put to the viewer drives comments |

Both reference accounts on TikTok have gone quiet, so the format's biggest TikTok audience has nobody posting to it right now
(my read: an opening for an account that posts steadily). The YouTube side is crowded: hundreds of channels copied "How a ___
Becomes ___" from mid-October 2026.

### 1.5 Packaging that matters, and what doesn't (18 Nov 2026)
- **The first frame and the first second decide most of it** (1.2). The title is barely seen in the Shorts feed.
- **TikTok:** the caption is a question with one emoji plus 4–6 hashtags that must register as hashtags (8.1): from video 02 on,
  none of ours did.
- **YouTube:** a title under ~60 characters that asks the question the video answers; a 2–3 sentence description; "not made for
  kids". Our best YouTube result had none of the packaging advice (hashtags in its title, no description): the video did the work.
- **Covers:** a frame of the most satisfying cutaway moment. YouTube only lets us pick a frame until the channel joins the Partner
  Program, so pick one without a stray caption word (8.2).
- **Not the problem** (checked 18 Nov 2026): a shadowban (no TikTok video shows a penalty), TikTok's AI label (TikTok added it
  itself to 9 of 10 videos, seawater included), a watermark on the YouTube uploads (none), the follow rate.

---

## 2. The 10-video plan (approved by the user on 18 Nov 2026)

The user: "I will be creating 10 videos with the recommendations you made in this session following the updates you gave me";
then "I stopped video 11 I want at most 200 credits per video". The recommendations were those of the growth audit (1.1–1.3).

### 2.1 The lane
**The hidden inside of something everyone uses or walks past**, cut open, with something moving through it and a big event in
the first second. It is what both platforms rewarded for us (the hydrant, seawater) and for Hidden By Design (the storm drain, the
roof, the landfill), and what the hydrant's 300 YouTube subscribers came for. **One lane for all ten,** judged at the checkpoints
in 2.5, not after each video: in eleven days the account had three looks, five idea lists and four reference accounts (9.3).
The approved earlier ideas (X1–X4, F1–F3) are parked (13.1), not dropped.

### 2.2 Before the ten (free; do these first)
1. **The profile fixes** (8.3) and the posting fixes (8.1, 8.2): hashtags typed in the app, "altered content" unticked on YouTube,
   a chosen cover frame.
2. **The re-cut test.** Re-cut stalled videos so they open on their event, using the clips, timings and build scripts that exist
   (9.2), with no Higgsfield credits; paste-in prompt 11.2. Post each as a new video on both platforms and make the old one
   private. If they clear ~2K on TikTok and get a normal test on YouTube, the opening was the block (the old versions sit at
   330–364 on TikTok and 11–42 on YouTube).
   - **09 Lightning:** the first strike lands at about 3 s (the end of clip C1, beat B2, "Here's what the bolt actually does."). Cut
     B1–B2 and start on the frame where the bolt hits the ridge, with a new first line in Daniel's voice ("Lightning just hit this
     house. Watch where it goes."), then B3 onwards ("It hits your roof, hunting for the ground…").
   - **10 Cryonics:** a 2 s cold open on the pods hanging head down in the cut-open tank (clips C12–C13, beats B16–B17, about 45–52 s
     into the original), with a new first line ("These people are frozen. Upside down."), then the video from its start.
   - **07 Car** (optional): a 1.5 s cold open on the crash itself, under the original first line ("Only one of these drivers walks
     away."), then the video from its start.
   Log them in 9.2 as 09b, 10b and 07b.

### 2.3 The ten, in order (18 Nov 2026)
| # | Idea (section 3) | The first second | Best proven demand | Why this slot |
|---|---|---|---|---|
| V1 | Why Manhole Covers Explode → **made 18 Nov 2026 as video 12, "Why Some Manhole Covers Are Full of Holes"** | a manhole lid blasts up on a column of flame | 2.0M (a Short); about nine small copies since Aug 2026, all under 3.2K (3, V1) | Street-level like the hydrant, winter |
| V2 | Why Frozen Turkeys Explode in the Fryer | a frozen turkey hits the oil; fireball | 5.6M, 3.1M | Thanksgiving: post by Tue 24 Nov 2026 |
| V3 | Why Nuclear Cooling Towers Are Empty Inside | the tower's wall slices open: empty | 72M (footage); nobody has animated the inside | The simplest set to draw; cold-day plumes |
| V4 | The Ice Under This Court Cancelled an NBA Game | a floor panel lifts off white ice | 7.4M; 386K this month | NBA and NHL in season |
| V5 | Why Water Heaters Can Launch Through the Roof | the tank rockets through the roof | small Shorts; MythBusters 1.65M long | The hydrant's audience: your house |
| V6 | Why This NFL Field Rolls Outside | the whole field slides out of the stadium | 2.8M, 2.6M, 1.7M | NFL season |
| V7 | What's Hiding Under a Wave Pool | a wave bursts out of the dark opening | 47.6M, 24.6M, 4.35M | The biggest demand of the ten |
| V8 | What's Hiding Behind the Pins at a Bowling Alley | a strike; the camera follows the ball | 62M, 25M | Hardest machinery: after the set-building is routine |
| V9 | The Airport Baggage System That Ate Suitcases | a cart crashes and a suitcase bursts | 18.4M (footage) | Before Christmas travel (mid-December) |
| V10 | How Do Fish Get Past a Dam? | a salmon fired out of a tube | 24.6M, 16.4M | The most 3D competition: last |

### 2.4 Budget and cadence
- **At most 200 credits a video** (6.1), so the ten cost at most 2,000. The balance after video 10 was 1,762.25 (video 11 was
  stopped at its quote; check `balance`): about eight videos at the cap, or all ten at an average of 176. The Ultra plan's monthly
  credits (3,000 since 11 Nov 2026; check the renewal date) cover the rest.
- **One video every one to two days**, never two the same day; post in the early evening, US Eastern, on both platforms. Fixed
  dates: V2 by Tue 24 Nov 2026; V9 before mid-December.

### 2.5 How we'll judge (from outside; never ask the user for retention)
- **Each video at 72 h** (8.4): more than ~2K on TikTok = it passed the first test; more than ~1K on YouTube = it was tested
  normally; 10K+ = a breakout for us. Record both in 9.2, with the frames-0–2 s verdict.
- **Checkpoint after five:** if three or more passed TikTok's first test, keep the lane and the formula. If not, look at the
  openings first (frames 0–2 s against 1.2) before touching the topics.
- **After ten:** review with the user: which openings and topics passed, the follower and subscriber change, and the next ten.
  Don't change the plan in the middle on one result.

---

## 3. The ten ideas, with draft scripts (18 Nov 2026)

All ten are in the lane of section 2: the hidden inside of something everyone uses or walks past, one place cut open, with a big
event for the first second. Order and timing are in 2.3. For each: the titles, the comment question, the set, **the first second**
(Rule 0), a draft script (about 220 words; the user approved the plan, so these are drafts for Gate A), draft camera positions,
the sounds, the demand on 18 Nov 2026, and the facts: ✔ checked by web search on 15–18 Nov 2026 (search summaries: reopen a page
before quoting a number), ⚠ still to check before Gate A. **Rerun the saturation check on the exact title before Gate A:** four of
these topics gained small 3D copies between 15 and 18 Nov 2026.

**V1. Why Manhole Covers Explode** (a city street in winter; make first)
- **Titles:** YouTube "Why Manhole Covers Explode"; TikTok "Why do manhole covers explode? 💥" + the four standing tags, #Manhole
  #Winter. **Comment question:** "Would you still step on one? Yes or no."
- **Set:** one winter city street cut open like a cake: slushy asphalt and a round iron lid on top; below it the concrete vault,
  thick power cables on wall racks, salty meltwater dripping in, the duct bank running off under the street; a salt truck passing;
  a pigeon on the lid. Water only as slush and drips.
- **First second:** frame 0 the pigeon on the lid, low and close; by 0.5 s the lid blasts upward on a column of flame and smoke and
  the pigeon flaps off; the camera rises with the lid, then dives into the hole.
- **Script** (draft, 214 words):
  > That iron lid weighs up to three hundred pounds, and it just flew fifty feet into the air. It wasn't sewer gas. It was road
  > salt.
  >
  > If you run a city's power under its streets, you put the cables in concrete rooms below the road, with a round iron lid on
  > top. This is a manhole. But in winter, trucks salt the road, and salty meltwater drips through the lid onto the cables. So
  > the cables wear thick insulation. But salt water eats it, slowly, for years. One day the current jumps the gap. This is an
  > arc. The insulation smoulders, and the little room fills with gas. Then one more spark lights it. In New York there are
  > thousands of smoking manholes a year, and a few dozen explode. That's why it happens most from January to March. So the
  > power company swaps solid lids for lids full of holes, so the gas leaks out before it builds up. It locks some lids in
  > place. And it hangs sensors below that smell the gas first. And the pigeon that was sitting on this one? It's fine. The lid
  > is round for a reason: a circle can't fall through its own hole. Wire the street, vent the lid, and keep it on the ground.
- **Camera (8):** the street low by the lid → up with the lid → down into the vault → the cables on their racks → the drip through
  the lid (close) → the arc (extreme close) → the vault filling with gas → the vented lid from below → the street, wide.
- **Sounds:** bed: a city street in slush, distant traffic; effects: the blast, the lid clanging down, dripping, an electrical
  crackle, wings.
- **Demand (corrected at Gate A, 18 Nov 2026):** the earlier check missed Shorts (12.2). About nine small Shorts on the plain
  road-salt angle since Aug 2026, all under 3.2K: one with this exact title (114 views), Baguette Lab 3.1K, How Things Work in
  Motion 2.0K (a labelled cutaway), Grid Matters 1.3K (the same 300-lb road-salt hook), Unseen Machines 1.3K (latches), Futurecraft
  1.3K (photoreal 3D, a flaming lid in frame 0, 17 Nov). The topic's best, "Why do manhole covers explode?" 2.0M (Oct 2024), is a
  Short with a sewer-gas explanation; long videos: Half as Interesting 5.5M, Tom Scott 1.9M. Zack D. Films: none.
- **Made on 18 Nov 2026 as video 12, "Why Some Manhole Covers Are Full of Holes"** (no Shorts with that title): the script was
  rewritten to 222 words with the fixes as But/So pairs (vented lids, "but holes let salt water in too", sensors, latches) and the
  pigeon landing back on the lid for the loop. Script, beat sheet and everything else in `pipeline/12-*`.
- **Checked ✔:** covers weigh 70–300 lb (Con Edison); in Boston on 2 Apr 2017 a cover flew at least 50 ft and nobody was hurt; the
  cause: salty meltwater wears down cable insulation, current arcs, the insulation smoulders, gas builds up and an arc lights it;
  Con Edison logged 3,369 "manhole events" in 2014, 32 of them explosions, about 90% from failed insulation; most happen January to
  March (FDNY data); vented covers since 2005 (more than 121,000 by about 2016), latched covers, gas and heat sensors (1,000 by
  2017, more than 3,600 later); a round lid can't fall through its own hole.
- **Resolved at Gate A (18 Nov 2026, search summaries):** New York averages about 2,240 smoking manholes and 29 explosions a year
  (Con Edison five-year averages); 50 ft (Boston, 2017) used, not 200–300 ft; latches: one design lifts slightly and settles back
  once the pressure evens out (T&D World), about 3,300 latched covers (CBS New York); vent holes let more water and salt in (patent
  background); sensors detect heat, gas and CO (about 4,800 devices, 2019); cable failure causes most manhole incidents, but the gas
  is sometimes sewer or natural gas, so "it wasn't sewer gas" is said about one lid, never in a title.
- **Watch out:** no utility name, city landmark or logo; don't show New York's steam stacks (a different system); nobody hurt.

**V2. Why Frozen Turkeys Explode in the Fryer** (a back yard at Thanksgiving; post by Tue 24 Nov 2026)
- **Titles:** YouTube "Why Frozen Turkeys Explode in the Fryer"; TikTok "Why does a frozen turkey explode in the fryer? 🦃🔥" + #Thanksgiving
  #TurkeyFryer. **Comment question:** "Fried, roasted or smoked? Pick one."
- **Set:** a back yard cut open like a cake: a propane fryer on the lawn, its pot sliced open to show the oil and the turkey with
  ice in its cavity; a few steps away the wooden deck and the back of the house, cut open to show the kitchen fridge with a bird
  thawing on a tray; a bucket of water and a marker for the oil line; an uncle in a lawn chair on the deck. Water only in the
  bucket (the oil is golden).
- **First second:** frame 0 a frozen turkey on a hook an inch above shimmering oil, big in the frame; by 0.5 s it touches, the oil
  foams over the rim onto the flame, and a fireball rolls up past the camera.
- **Script** (draft, 212 words):
  > Lower a frozen turkey into 350-degree oil, and this happens. It's the ice inside the bird.
  >
  > Water is heavier than oil, so the ice sinks to the hot bottom and turns to steam in an instant. Steam takes up about 1,700
  > times more room than water. So it shoves the oil up and over the rim. This is a boil-over. But right under the pot is an
  > open flame. The oil hits it, and you get a fireball. So you thaw the bird in the fridge for days, and pat it dry. But even a
  > thawed bird pushes the oil up. So before you heat anything, you lower it into plain water and mark the line. That's all the
  > oil you need. But it's cold out, so you set up on the wooden deck. So you move it out to the middle of the yard. And you
  > turn the flame off before the bird goes in, then lower it slowly. Here's the catch: Thanksgiving is the number one day of
  > the year for kitchen fires. That's why firefighters drop frozen turkeys into fryers on the news every November. And your
  > uncle still wants to do it on the deck. Thaw the bird, measure the oil, and keep the fire in the yard.
- **Camera (8):** the pot (the fireball) → inside the pot (the ice sinking, the steam bubble) → the rim → the burner → the fridge
  through the cut wall → the bucket and the line → the deck → the middle of the yard (the burner valve, the slow lowering) → the
  yard, wide.
- **Sounds:** bed: a suburban back yard in late November, a game on a TV indoors; effects: the oil roar, the fireball's whoosh, the
  burner, a splash in the bucket.
- **Demand:** "The Dangerous Truth Behind Deep Frying a Frozen Turkey" 5.6M; "How to fry a turkey SAFELY" 3.1M; a Thanksgiving fryer
  warning 2.1M; "Frying Frozen Turkey Explodes Into Fireball" 335K; long videos 1.08M and 446K. Zack D. Films has turkey recipe
  gags (13–14M), and his "Water On A Grease Fire 🤯" (6.75M, 3D) covers the same physics in a pan: ours is the turkey, the yard
  and the fixes, at Thanksgiving.
- **Checked ✔:** water is denser than oil (1.00 against 0.91–0.93 g/cm³) and sinks; steam takes about 1,700 times the water's
  volume; the ice flashes to steam and drives the oil over the rim (NPR and PBS NewsHour, Nov 2023); thaw the bird in the fridge
  and dry it; turn the burner off before lowering; fry outdoors on level ground away from buildings and decks; never put water on
  an oil fire (US Fire Administration); Thanksgiving is the No. 1 day for US home cooking fires (1,446 on Thanksgiving 2023, NFPA);
  deep frying runs at 350–375 °F.
- **⚠ before Gate A:** the water method for measuring the oil (common advice; find a source); "for days" (USDA's fridge thawing
  time is about a day per 4–5 lb; check); two examples of fire departments' yearly fryer demos; TikTok's rules on fire in videos
  (this is a safety demonstration).
- **Watch out:** nobody hurt; the uncle is small and anonymous; no brand names on the fryer or the propane tank.

**V3. Why Nuclear Cooling Towers Are Almost Empty Inside** (a cooling tower by a river; the user's own pick on 15 Nov 2026)
- **Titles:** YouTube "Why Nuclear Cooling Towers Are Empty Inside" (the nearest title, "What's Inside A Nuclear Cooling Tower?",
  has 173K); TikTok "What's actually inside a nuclear cooling tower? ☁️" + #Nuclear #CoolingTower. **Comment question:** "Did you
  think it was smoke? Yes or no."
- **Set:** one curved cooling tower sliced open like a cake beside a river, with a plain plant building behind it (never the
  reactor) and two more towers in a row: the open base with air rushing in, the rain falling through the fill near the bottom, the
  pool under it, and nothing above but rising mist up to the mouth; the pipes from the condenser.
- **First second:** frame 0 the tower huge and close, its white plume rolling; by 1 s its near wall slices away top to bottom and
  the inside is empty air, with rain falling only near the bottom.
- **Script** (draft, 227 words):
  > This giant tower is almost completely empty inside. And that isn't smoke.
  >
  > If you boil water to spin a turbine, the steam has to turn back into water. So you run cold water past it. This is the
  > condenser. But that water comes out hot, thousands of gallons a minute. So you cool it: you rain it down over stacks of
  > slats near the bottom, and a little of it evaporates and carries the heat away. This is the fill. But still air cools
  > nothing, and giant fans would eat your power. So you build a chimney around the rain. Warm, wet air rises on its own and
  > pulls cool air in at the open base. This is natural draft. But a tube this tall has to stand up to a gale. So you pinch its
  > waist. That curve keeps a concrete shell about seven inches thick stiff enough to stand. In 1965, in England, three towers
  > built close together blew down in one storm. Now they're built stronger. But the wind carries drops out of the top. So
  > baffles catch them, and a few percent of the water still floats away each pass. That's why the cloud on top is biggest on
  > cold, damp days. It's just water, and it never touches the reactor. Rain it down, pull the air up, and let it drift away.
- **Camera (8):** the tower close (the wall slicing open) → the condenser pipes at the base → the rain over the fill → the open
  base, air pulled in → up through the empty shell → the waist → the row of three towers in a gale (a storm re-grade, for 1965) →
  the baffles at the mouth → the tower, wide, on a cold day.
- **Sounds:** bed: rain falling inside a huge concrete hall (the echo the 72M Short is about); effects: pumps starting, a gust, a
  deep rumble for 1965.
- **Demand:** real footage "Inside a Nuclear Plant Cooling Tower: The Wildest Natural Reverb" 72M and another at 71M; "What Really
  Happens Inside a Cooling Tower" 1.9M; a Hindi animation 1.1M; the nearest title 173K; nobody has animated the empty inside (one
  1.5K cartoon of the whole plant, 17 Nov 2026). Long: Practical Engineering 9.5M.
- **Checked ✔:** natural draft (warm, moist air rises and pulls cool air in at the base; no fans); the fill spreads the water and
  evaporation does most of the cooling; the fill and rain zone sit in roughly the bottom 10 m and the shell above is empty; drift
  eliminators are baffles; the plume is condensed water, biggest on cold, humid days; shells about 16–18 cm (6–7 in) thick at the
  waist; Ferrybridge, England, 1 Nov 1965: three of eight towers blew down in a gale; the tower's water only cools the condenser
  and never touches the reactor; a few percent of the water leaves on each pass (about 1% for every 10 °F of cooling; up to 5%
  by the World Nuclear Association); about 420 gallons evaporated per MWh (EPA), thousands of gallons a minute for a big unit.
- **⚠ before Gate A:** what changed in tower design after Ferrybridge ("now they're built stronger"); "seven inches" (6–7 in is
  safe).
- **Watch out:** How Building Explained built a nuclear plant: ours is the tower only; no radiation symbols and no real plant names;
  call the plume a cloud.

**V4. The Ice Under This Court Cancelled an NBA Game** (an arena floor)
- **Titles:** YouTube "The Ice Under This Court Cancelled an NBA Game"; TikTok "This NBA game got cancelled because of what's under
  the court 🏀🧊" + #NBA #NHL. **Comment question:** "Hockey or basketball: which would you rather watch here?"
- **Set:** an arena floor cut open like a cake: the concrete slab with brine pipes, an inch of white-painted ice, the insulated
  panels, the hardwood court; the boards and glass; the seats rising behind; a big air-drying duct.
- **First second:** frame 0 the court close and gleaming, a ball bouncing; by 1 s a crew lifts a square of the floor and white ice
  shines under it, and a hockey puck slides out.
- **Script** (draft, 215 words):
  > There's an ice rink under this basketball court. One night, it cancelled an NBA game.
  >
  > If you want hockey and basketball in one building, you freeze the floor and never let it melt. Pipes in the concrete carry
  > brine colder than ice, and an inch of ice sits on top, painted white. But you can't dribble on ice. So you cover it:
  > insulated panels first, then the court, piece by piece, like a puzzle. But the hockey boards are in the way. So they lift
  > out in sections. But the cold still seeps up through the floor. Warm, wet air from the crowd hits the cold wood and turns to
  > water. This is condensation. So giant dryers pull the water out of the air. But in Philadelphia, in 2016, hockey was played
  > the night before, the day was warm and damp, and the floor wouldn't stay dry. Players kept slipping, and the game was called
  > off. And tomorrow is hockey again. So the court comes up, the panels come off, and the ice is scarred. So a machine shaves a
  > thin layer off and lays down hot water that freezes glass smooth. That's why the ice looks so white: it's painted, under the
  > top. Freeze the floor, cover it over, and swap it by morning.
- **Camera (8):** the court (the panel lifting) → down into the cut layers → the brine pipes → the panels going down → the court
  pieces, top-down → the boards lifting out → the cold wood beading with water → the 2016 night, players slipping (small figures)
  → the resurfacer → the arena, wide.
- **Sounds:** bed: an empty arena's hum; effects: a bouncing ball, panels dropping, sneakers squeaking and sliding, the
  resurfacer's motor.
- **Demand:** real changeover time-lapses 7.4M, 2M, 495K; "Lakers' Court Is Hiding GIANT ICE" 386K (real, 13 Nov 2026); explainers
  78K and 43K. Since 23 Oct 2026 about six small 3D copies of the plain idea, all at 3.1K or less (one, "There's an Ice Rink Under
  This NBA Court", 15 Nov, 658 views): hence the story title.
- **Checked ✔:** the ice stays down all season under insulated panels with the court on top; the boards and glass come out in
  sections; changeovers take a few hours; arenas run dehumidifiers to stop condensation; the ice is painted white and sealed; NHL
  ice is about an inch thick ("typically less than an inch", NHL.com; others give ¾–1¼ in); a resurfacer shaves about 1/16 in and
  lays hot water at about 140–160 °F; the Kings–76ers game in Philadelphia on 30 Nov 2016 was called off at 8:03 pm because the
  court was slippery, after the Flyers had played the night before; it was made up on 30 Jan 2017.
- **⚠ before Gate A:** search Cutaway Instinct (stadium and arena cutaways in our style, 1.4) for the ice under the court;
  "brine colder than ice" (rinks run brine or glycol at roughly 16–18 °F: check); "players kept slipping"
  (reports say the floor was slick; keep the wording to what they say).
- **Watch out:** no team names, logos or colours on the court or the ice; players and crew small and anonymous.

**V5. Why Water Heaters Can Launch Through the Roof** (a house with a basement)
- **Titles:** YouTube "Why Water Heaters Can Launch Through the Roof" (a 1.7K 3D cutaway is titled "Your Water Heater Can Go Through
  the Roof."); TikTok "Can your water heater really launch through the roof? 🚀" + #WaterHeater #HomeSafety. **Comment question:**
  "Have you ever checked yours? Yes or no."
- **Set:** a two-storey house cut open like a cake, the water heater in the basement up front (its tank cut open to show the water,
  the thermostat, the backup cut-off, the brass valve on top and its pipe down to the floor, the small tank on the cold pipe); a car
  in the driveway; the neighbour's yard beside.
- **First second:** frame 0 the house at rest, the tank big in the frame; by 0.5 s the tank splits at its base and a jet of steam
  drives it up through the floors and out of the roof, over the car.
- **Script** (draft, 219 words):
  > This water heater just went through the roof. All it had inside was hot water.
  >
  > If you want hot water on tap, you heat it in a sealed steel tank. But a thermostat can fail, and the heat keeps coming.
  > Under pressure, water doesn't boil at 212 degrees. It just gets hotter, past 300, and stays liquid. This is superheated
  > water. But a tank can only hold so much. When a seam splits, the pressure drops, the water flashes to steam all at once, and
  > the tank becomes a rocket. One small tank holds enough energy to throw a car 125 feet up. So you add a backup switch that
  > cuts the heat. And a brass valve on top that opens at 210 degrees or 150 pounds of pressure, and lets it all out. This is a
  > T&P valve. But it sprays scalding water. So a pipe carries it down to six inches above the floor. That's why your water
  > heater has a pipe that stops just above the floor. But the valve drips, so someone screws a cap on it. In 1993, in
  > Minnesota, a heater whose valve didn't work blasted out of a basement, through the roof, and landed in the neighbor's yard.
  > Nobody was hurt. Heat the tank, trust the valve, and never cap the pipe.
- **Camera (8):** the basement (the blast) → up through the floors after the tank → back down into the tank cutaway → the water past
  300 (shimmering) → the seam → the backup switch → the brass valve on top → the pipe down to the floor (and the cap) → the tank in
  the neighbour's yard (1993) → the house, wide.
- **Sounds:** bed: a quiet basement with a furnace hum; effects: a rumble and hiss, the blast, a valve hissing, water on concrete, a
  car alarm.
- **Demand:** the on-topic Shorts are small (MythBusters clips at 45.6K and 30.0K, a 3D one at 29.1K, 25.7K); several tiny 3D
  copies (one tells the 2001 Burien story); long: MythBusters 1.65M and 1.34M. Zack D. Films: none. A modest ceiling, a strong
  opening, and it is the hydrant's YouTube audience (the hidden stuff in your house).
- **Checked ✔:** at 90 psi water boils at about 331 °F (Watts); a 30-gallon tank at 90 psi and 332 °F holds about 314,000 ft-lb,
  enough to lift a 2,500-lb car about 125 ft (National Board); when the tank splits, the water flashes to steam; a backup high-limit
  cut-off; the T&P valve opens at no more than 150 psi or 210 °F; its pipe ends no more than 6 in above the floor so scalding water
  isn't aimed at anyone (ICC); South St. Paul, Minnesota (UPI, 2 Jun 1993): a 50-gallon heater shot out of a basement, through the
  roof, and landed about 150 ft away in a neighbour's yard; the two adults inside weren't hurt; fire officials blamed a relief
  valve that didn't work.
- **⚠ before Gate A:** "throw a car 125 feet up" (the source says lift; keep "a small tank" and "lift"); a source for capping a
  dripping valve as a known bad fix, or keep it as the joke without a claim. Never use the 1982 Spencer, Oklahoma school
  explosion.
- **Watch out:** nobody hurt; no brand names on the heater.

**V6. Why This NFL Field Rolls Outside** (a desert stadium; NFL season)
- **Titles:** YouTube "Why This NFL Field Rolls Outside"; TikTok "Why does this NFL field roll outside? 🏈☀️" + #NFL #Stadium.
  **Comment question:** "Real grass or turf? Pick one."
- **Set:** a desert stadium cut open like a cake: the closed roof, the seats, the end wall with a giant door, the field as a steel
  tray on rails (cut open to show the grass, the sand and gravel, the drain pipes, the wheels on the rails), the bare concrete floor
  where the tray sits, and the sunny lot outside where the field basks. A tortoise by the rail.
- **First second:** frame 0 the stadium from outside, its end wall open; by 1 s (sped up) the whole field slides out through the
  door into the sun.
- **Script** (draft, 212 words):
  > This whole football field just rolled out of the stadium. It goes outside to get some sun.
  >
  > If you want real grass in a desert stadium, you need a roof against the heat. But grass under a roof dies. So you grow the
  > field on a giant steel tray, and roll the whole thing outside. The tray is 234 feet by 403, and with the grass and the soil,
  > it weighs about 19 million pounds. But nothing that heavy slides on its own. So it rides on 546 steel wheels, along 13
  > rails. It moves about fifteen feet a minute. A tortoise could keep up. So the trip takes about an hour. But grass needs
  > water, and water has to drain. So the tray is forty inches deep: grass on top, then sand and gravel, with pipes underneath
  > that carry the water away. But on game day, the grass has to come in. So it rolls back inside, and the roof closes over it.
  > And when the field is out, the bare floor underneath hosts concerts and trade shows. Here's the twist: Las Vegas has one
  > too, inside a stadium whose roof never opens. Its grass lives outside and only comes in for games. Grow it outside, roll it
  > in, and play.
- **Camera (8):** outside, the field sliding out → along the tray's edge (wheels on rails) → the cut tray (the layers and pipes) →
  the tortoise beside the rail → back inside, the roof closing → the bare floor with a concert stage → the Las Vegas line over a
  pull-back → the stadium, wide.
- **Sounds:** bed: a desert breeze and a big empty stadium; effects: motors humming, steel wheels on rails, the roof closing, a
  crowd for game day.
- **Demand:** "The INSANE Retractable Grass Field for Super Bowl 58" 2.8M; "This 19-Million-Pound Football Field Can MOVE🤯" 2.6M;
  "Incredible retractable football field, the entire lawn is hidden underground" 1.7M; "Real Madrid's RETRACTABLE Pitch Explained"
  566K; long: "University Of Phoenix - Moving field" 1.05M, the Raiders' tray 807K. Zack D. Films: none. Check at Gate A which of the
  top Shorts are 3D.
- **Checked ✔** (search summaries, 18 Nov 2026): Arizona's stadium (State Farm Stadium, Glendale) grows its field on a tray about 234
  × 403 ft and 40 in deep that weighs nearly 19 million lb, rides 546 steel wheels on 13 tracks and travels about 740 ft at about 15
  ft a minute (60–70 minutes; an operator keeps pressing a button); it spends days outside in the sun and comes in for games and
  cold nights; Allegiant Stadium in Las Vegas has a 9,500-ton tray (540 wheels) under a roof that doesn't open.
- **⚠ before Gate A:** search Cutaway Instinct (a YouTube channel of stadium cutaways in our style, 1.4) for a rolling-field
  video; that grass dies under the roof (the reason given is sunlight; word it as "grass needs sun"); the drain pipes in
  the tray; concerts and trade shows on the bare floor; "a tortoise could keep up" (giant tortoises walk about 0.2 mph, ~18 ft a
  minute: check); how the tray is driven (motors).
- **Watch out:** no team names, logos or colours, and no stadium name on screen.

**V7. What's Hiding Under a Wave Pool** (a water park)
- **Titles:** YouTube "What's Hiding Under a Wave Pool" (no match found); TikTok "What's behind that dark hole in the wave pool? 🌊"
  + #WavePool #WaterPark. **Comment question:** "Deep end or shallow end? Pick one."
- **Set:** a wave pool sliced lengthwise like a cake: the deep-end wall with its barred openings, the tall concrete chambers behind
  it, the blower room with fans and valves, the floor sloping up to a beach, the side grates and the return channel; small
  swimmers; a lone flip-flop.
- **First second:** frame 0 the flat, calm pool from the water line, the dark barred opening big in the deep-end wall; by 0.5 s a
  surge bursts out of it and a wall of water rolls toward the camera.
- **Script** (draft, 224 words):
  > Every wave in this pool comes out of that dark hole in the wall.
  >
  > If you want waves in a pool, the deep end can't just be a wall. So behind it you hide a row of tall concrete rooms, open at
  > the bottom to the pool. These are the chambers. But water won't move by itself. So giant fans blow air into a chamber, and
  > it shoves the water down and out through the hole. That surge is your wave. But one surge is a splash, not a wave. So the
  > chambers fire one after another, and valves open and shut them on a timer. But a wave in deep water just rolls. So the floor
  > slopes up to a beach, and the wave trips and breaks. But all that water piles up at the shallow end. So grates along the
  > sides drain it back behind the wall for the next one. That's why the waves always start at the deep end, and why that barred
  > opening is there. In 1969, in the Arizona desert, the first surf pool in North America made its waves with a giant flush:
  > fifteen gates, like toilet flappers, dumping a whole reservoir into the pool. And somebody's flip-flop is still riding every
  > wave. Blow the air, trip the wave, and pull it back for the next one.
- **Camera (8):** the opening at water level (the surge) → through the bars into a chamber → the blower room → the valves → the row
  of chambers firing, from the side → the sloped floor (the wave tripping) → the beach → the side grates → the pool, wide (the 1969
  line plays over the pull-back; the flip-flop rides the last wave).
- **Sounds:** bed: a water park, distant splashing and voices; effects: fans spinning up, a rush of air, the surge, a wave
  breaking.
- **Demand:** footage "Korea Wave Pool" 47.6M and 24.6M; "Never Go Near This In A Wave Pool 😰" 4.35M (a talking head whose first
  frame is the barred opening: our angle); explainers 449K and 140K; 3D rivals: "How a wave pool works, one failure at a time"
  115.5K (29 Oct 2026, our formula, with a character) and 40.7K. Zack D. Films: none (his 41.8M pool Short is about a drain).
- **Checked ✔:** air-powered chambers are by far the most common: fans push air into chambers behind the deep-end wall, the water
  inside drops and surges out through underwater openings (Watershapes); valves fire the chambers in sequence; the floor slopes up
  so the waves break at the shallow end; the water comes back through side grates and channels; Big Surf, Tempe, Arizona, 1969: the
  first inland surfing facility in North America (ASME landmark), its 15 underwater gates working "much like a toilet flapper",
  dumping a raised reservoir into a 2.5-million-gallon lagoon; closed 2020, demolished 2022.
- **⚠ before Gate A:** "on a timer" (sequence control ✔; check the word); leave out Action Park's "Grave Pool" (listicles only) and
  "vacuum" wave makers (not confirmed).
- **Watch out:** swimmers small and anonymous; nobody hurt; no park names or logos.

**V8. What's Hiding Behind the Pins at a Bowling Alley** (a bowling lane)
- **Titles:** YouTube "What's Hiding Behind the Pins at a Bowling Alley"; TikTok "What's actually behind the pins at a bowling
  alley? 🎳" + #Bowling. **Comment question:** "Hook or straight: how do you bowl?"
- **Set:** the far end of a lane sliced lengthwise like a cake: the pin deck, the hanging curtain and the pit, the machine above
  (wheel, turret, table, sweep bar), the ball lift and the return track under the floor between lanes; the lane's surface with a
  faint sheen of oil on its front part under a raking light. The pin boy is a re-grade of the same pit (old, sepia).
- **First second:** frame 0 the ball an arm's length from the head pin, low and close; at 0.5 s a strike, pins exploding toward the
  camera; the camera follows the ball into the dark behind them.
- **Script** (draft, 223 words):
  > Where does your bowling ball go after this? Behind the pins is a machine with a second set waiting inside.
  >
  > For decades, a pin boy sat above the pit, dodging flying pins, and set them back up by hand. So you build a machine to do
  > his job. But the ball has to stop. So it slams into a heavy hanging curtain and drops into the pit. This is the cushion. But
  > it has to get back to you. So a spinning wheel lifts it, and a fast belt fires it down a track under the floor, between the
  > lanes. That's why there's a pause before it pops out. But the pins are a jumbled heap. So a wheel scoops them up, and a
  > turret drops each one into its own slot. But three are still standing. So a table comes down and lifts them clear, a bar
  > sweeps the fallen pins away, and the table puts the three back exactly where they stood. But the next frame can't wait. So
  > the second set is already loaded and drops into place. Here's the twist: the lane hides something too. A film of oil you
  > can't see covers more than half of it, so your ball slides, then hooks on the dry end. Catch the ball, lift the pins, and
  > set them up again.
- **Camera (8):** the pins (the strike) → behind them, the curtain → the pit (the pin-boy re-grade) → the ball lift → the track
  under the floor → the turret dropping pins → the table coming down → the sweep → the lane's oil, low and raking → the lane, wide.
- **Sounds:** bed: a bowling alley's hum; effects: the strike, the curtain's thud, the ball rumbling under the floor, the sweep,
  pins dropping into the turret.
- **Demand:** footage 62M ("Ever wondered how the pins got put back?"), 25M, 24M; "How does a bowling pinsetter work?" 2.6M; an
  animated ball's-eye view, "Where Do Bowling Balls Really Go?", 959K (Dec 2025); "How you invented the bowling pinsetter!" 579K;
  small 3D copies of "Where Does Your Bowling Ball Go?" since October (one 1.9K on 17 Nov 2026): hence the new title. Long:
  Veritasium 19.1M.
- **Checked ✔:** pin boys set pins by hand before machines; the ball hits a hanging cushion and drops into the pit; a lift raises it
  and an accelerator sends it back on a track under the floor between lanes; a wheel lifts the pins to a turret that fills ten
  slots; the table lifts the standing pins, the sweep clears the fallen ones and the table puts them back; oil covers only the front
  of the 60-ft lane (a 34-ft pattern leaves 26 ft dry), so the ball skids, then hooks.
- **⚠ before Gate A:** "a second set waiting inside" (patents describe a reserve set; 20 pins not reconfirmed); "a fast belt fires
  it" (the accelerator's mechanism); Zack D. Films on pinsetters (not checked on 18 Nov).
- **Watch out:** machinery is the hardest thing to draw: keep six parts (curtain, pit, lift, track, turret, table and sweep) and
  prove them at Gate C; no brand names on the machine.

**V9. The Airport Baggage System That Ate Suitcases** (an airport, 1994 and now; post before Christmas travel)
- **Titles:** YouTube "The Airport Baggage System That Ate Suitcases"; TikTok "This airport's baggage system ate suitcases 🧳" +
  #Airport #Travel. **Comment question:** "Has an airline ever lost your bag? Yes or no."
- **Set:** one airport cut open like a cake, seen at two times on the same set: in 1994 a test track with little carts under the
  floor; now the belt dropping from the check-in desk, the scanner tunnel, the early-bag racks, the tilt-tray loop, the chutes to
  the gates and a baggage cart on the apron. A lone sock on the belt.
- **First second:** frame 0 a little cart carrying a suitcase races along a track; by 0.5 s it slams into a bend, the suitcase
  bursts open and clothes fly.
- **Script** (draft, 216 words):
  > In 1994, this airport's brand-new baggage system ate suitcases in front of the press.
  >
  > If you check a bag, it has to find one plane out of hundreds. So it gets a tag with a ten-digit number and a barcode. But
  > nobody can read thousands of tags by hand. So your bag drops onto a belt, and scanners read the tag as it rolls past. But
  > every bag has to be checked for explosives. So it rides through a scanner, and if anything looks wrong, it's pulled aside
  > for a person to open. But bags show up hours early. So they wait in racks until their flight is called. Then trays tilt and
  > drop each bag down a chute to its gate, where handlers load the carts. Big airports hide miles of these belts under the
  > floor. Denver tried to skip the belts: four thousand little carts racing around 21 miles of track. In the demo, carts
  > crashed, bags jammed, and clothes went flying. The airport opened sixteen months late, and the system was scrapped in 2005.
  > That's why the number on your tag stub matters. It's how a lost bag gets found. And somewhere down there, one sock is still
  > riding the belt alone. Tag it, scan it, and let the belts do the rest.
- **Camera (9):** the cart crash (1994) → the check-in desk (the tag) → the belt dropping under the floor → the scanner tunnel →
  the side room where a bag is opened → the racks → the tilt trays → the chute and the handlers → the 1994 track again → the sock on
  the belt → the airport, wide.
- **Sounds:** bed: rollers and belts in a long basement; effects: the cart crash, belt motors, a scanner's beep, a tray tipping, a
  bag thumping down a chute.
- **Demand:** crowded right now: about 25 Shorts with nearly the plain title ("where your suitcase goes"), most 1–5 weeks old at 2.4K
  or less, the best 662K (22 Oct 2026); animated ones: You Built It 39K (28 Oct), Pocket Factory 23.6K; the topic's biggest Shorts
  are real footage, 18.4M and 4.7M; long: a GoPro ride 5.2M. Zack D. Films: none. Hence Denver leads.
- **Checked ✔:** the tag's 10-digit number (a leading digit, the airline's 3-digit code and a 6-digit serial; IATA); tracking at four
  points since 1 Jun 2018 (IATA Resolution 753); every US checked bag screened for explosives since the 2001 security act;
  early-bag storage (Dubai T3: 4,500 slots); tilt-tray sorters; Heathrow T5 has about 11 miles of conveyor; Denver: at an April 1994
  press demonstration the system chewed up bags and spilled clothes; the airport opened in February 1995, 16 months late; 4,000
  carts on 21 miles of track; the delay cost about $1.1M a day; United scrapped the system in 2005; 4.9 mishandled bags per 1,000
  passengers in 2025 (SITA).
- **⚠ before Gate A:** Denver's total cost (sources give $186M–$232M: don't say it); the month it was scrapped (one source); don't give
  a share of bags hand-searched (the 5% figure is old).
- **Watch out:** no airline or airport names or logos on screen (the narration names Denver); people small and anonymous.

**V10. How Do Fish Get Past a Dam?** (a river dam)
- **Titles:** YouTube "How Do Fish Get Past a Dam?" (a near title, "How Fish Climb Dams", has 22.9K); TikTok "How do fish get past a
  dam? 🐟💨" + #Salmon #Dam. **Comment question:** "Would you ride the salmon cannon? Yes or no."
- **Set:** one river dam cut open like a cake: the reservoir above, the river below, a fish ladder of step pools down one side (cut
  open to show water spilling pool to pool), a fish-lift tank, a truck on the bank, the cannon's tube over the dam, a far taller dam
  upriver in the haze, and an underwater viewing window with a counter clicking a tally.
- **First second:** frame 0 a salmon in a dark tube; by 0.5 s it shoots out of the end over the dam and splashes into the
  reservoir.
- **Script** (draft, 225 words):
  > This salmon just got fired over a dam. On purpose.
  >
  > If you're a salmon, you swim back up the river you were born in, to lay your eggs and die. But someone built a dam. So the
  > dam gets a staircase of little pools, each a step higher than the last. This is a fish ladder. But a ladder climbs only
  > about a foot for every ten feet of length. On a really tall dam, it would be nearly a mile long. So some dams build an
  > elevator instead: fish swim into a tank, and it lifts them over the top. But some dams are too tall even for that. So people
  > catch the fish, load them into trucks, and drive them around. But that's slow. So someone took a tube built for moving
  > apples and tried it on fish. It carries them on a rush of air, up to 22 miles an hour. This is the salmon cannon. But one
  > dam got nothing at all. Grand Coulee was built with no way past, and for about 80 years no salmon got above it, until 2019,
  > when tribes trucked thirty of them around and let them go. That's why at Bonneville Dam you can stand at an underwater
  > window and watch salmon climb the ladder. Build the steps, lift the tank, and fire the fish.
- **Camera (8):** the tube's end (the shot) → down the dam face to the river → the ladder pools → along the ladder (its length) →
  the lift tank rising → the truck → the tube → the tall dam upriver (Grand Coulee) → the viewing window and the counter → the dam,
  wide.
- **Sounds:** bed: a river below a dam; effects: a rush of air, a splash, water spilling down the ladder, a lift motor, a tally
  counter clicking.
- **Demand:** footage leads: "Salmon Cannon" 24.6M (Jun 2024), a natural fishway 16.4M; 3D rivals since Aug 2026 with the
  ladder-to-cannon chain: "The Salmon That Shoots Over a Dam" 147.7K (5 Oct), 85.8K, 34.9K; long: Last Week Tonight 5.7M, Practical
  Engineering 2.8M and 1.7M. Zack D. Films: none. Our edge: the cut-open ladder, the apple tube and Grand Coulee.
- **Checked ✔:** Pacific salmon return to their home streams, spawn once and die within a week or two; ladders rise about 1 ft per 10
  ft of length, impractical on very tall dams (US Army Corps of Engineers); fish lifts raise a hopper of fish over a dam (Conowingo,
  since 1972); trap and haul (Cowlitz River, since 1996); the salmon cannon moves fish on air pressure at 11–22 mph, 40–60 a minute,
  and began as a tube for apples; Grand Coulee (about 550 ft, completed 1942) got no fish passage and cut salmon off from 1,140
  miles of spawning grounds; on 16 Aug 2019 the Colville Tribes released 30 Chinook above it, the first salmon there in about 80
  years; underwater viewing windows at Bonneville Dam.
- **⚠ before Gate A:** "trucked thirty of them around" (they were released above the dam: say "carried thirty of them above it" if
  the trip isn't confirmed); the year Grand Coulee cut the runs (say "when it was built").
- **Watch out:** real tribes named, nobody shown; no agency logos.

### 3.1 Reserves (18 Nov 2026)
- **Why You Never Throw Water on a Grease Fire:** big demand, but Zack D. Films has it in 3D (6.75M) and four small copies came out in
  Oct–Nov 2026. Only with a new angle: the sensor button in the middle of new electric coil burners (a UL 858 rule: a pan of oil on
  high for 30 minutes must not ignite; coil cooktops made after June 2018). The checked facts are in V2's.
- **Why Roller Coasters Don't Fly Off the Track:** weak (about 25 small copies, best 28.5K; a 3D "Movies Lied: Coasters Can't Fly Off
  the Track" from 15 Nov 2026 at 23.8K). Good material if it comes back: three sets of wheels (the up-stop wheel patented by John A.
  Miller in 1919), the anti-rollback ratchet that clicks on the lift hill, and the twist that America's first coaster was a coal
  railway at Mauch Chunk, Pennsylvania (1827), where mules rode down in their own car.
- **Why NFL Fields Don't Freeze** (heating pipes under the grass): **already made in our style.** Cutaway Instinct's "Why Lambeau
  Field's Frozen Tundra Never Freezes Solid" (4 Nov 2026, 123K: pipes, boilers, SubAir, stitched fibres) was followed by five small
  copies (2–17 Nov), one of them with the 1967 Ice Bowl twist. Parked; only ever as a story-led video, with "Frozen Tundra" and
  "never freezes" kept out of the title.
- **Seasonal and small:** frozen pipes (the burst happens away from the ice; best Short 26K), fire sprinklers (only the one over the
  fire goes off; 5.6K). Both fit the hydrant's YouTube audience if the ten go well.

## 4. Writing the script (18 Nov 2026)

### 4.1 The formula
```
OPENING (0-1 s)  The scene itself changes on the first word: a burst, a strike, a floor lifting, a fireball.
                 The line says what the picture is doing (a physical verb, or a claim the picture proves right now).
HOOK (1-4 s)     The surprise or the stakes ("It wasn't sewer gas. It was road salt."). In the "before" shape, the first
                 "But" lands by about 3 s.
LOOP x6-7        But [problem]. So [fix]. (This is [REAL TERM].)   Each problem and fix at its own spot on the set.
TWIST (~2/3)     One true story or surprise, in one or two sentences, with nobody shown hurt.
THAT'S WHY       "That's why [something the viewer can go and check]." Shown on the set.
JOKE             One small human moment (somebody's lost tennis ball, the crew's coffee thermos). Shown on the set.
ENDING           A three-beat imperative that loops into the first frame: "Bury the pipes, pave the road, and let it rain."
```
Never "Congratulations, you have built…" and never a spoken call to action. The comment question goes in the TikTok caption or a
pinned comment, never in the voice-over.

### 4.2 The opening rules (approved by the user on 18 Nov 2026; the evidence is 1.2)
1. **Frame 1 is the "before", or the event itself.** Never an establishing shot of a finished thing.
2. **The scene changes by 1.0 s**, not just the camera: something bursts, drops, lifts, ignites, floods or flies, big in the
   frame. A camera gliding over a still set does not count.
3. **The first line names what the picture is doing.** "This manhole cover just flew forty feet into the air." "If you cut a hole
   in your street, the rain has somewhere to go." Never "If you want…", never a remark ("Everyone's heard it…").
4. **The subject fills at least a third of the frame** in the first second, readable on a phone.
5. **A surprise by about 4 s:** in the "before" shape, the first "But" by about 3 s; in the cold-open shape, the line right
   after the event ("It wasn't sewer gas. It was road salt."), with the first "But" following within about 10 s.
6. **Two shapes that work:**
   - **The event first, then the why** (a cold open): the most dramatic moment plays in the first 1–2 s, then the story starts
     ("Never throw water on a grease fire. Here's what happens inside the pan.").
   - **The "before", then the first verb** (Hidden By Design's shape): an empty street, and the hole is cut as the narrator says
     "cut".
7. **It is checked twice:** at Gate A as a three-line plan (frame 0, what has changed by 1 s, the first line), and at Gate D on the
   hook pilot's frames at 0, 0.5, 1 and 2 s (6.2).

### 4.3 Writing rules (carried over from 7–16 Nov 2026, updated 18 Nov 2026)
- Second person, present tense: the viewer is the builder or the person it happens to.
- One action or one problem per sentence. Short, mostly one-syllable words; no filler, no hedging.
- Every "But" escalates: nuisance → weather or wear → a hidden danger → the worst case.
- Name the real term after the key fixes ("This is a trap."), spoken only; the look has no labels.
- At least one surprising number, fact-checked. Comparisons only if the set can show them (a gauge on the pipe, a tub beside the
  hydrant); cut any that would need a picture of something else.
- **Write for the set and the camera:** every line is something you can see happen on the one sliced-open set; most lines describe
  something moving; each problem and fix happens at its own spot, so the camera has somewhere to fly on every "But" and "So".
- **Length: about 220 words** (215–225), which is 62–64 s at our pace of about 3.5 words a second (18 Nov 2026). It is what the
  200-credit cap allows (6.1), and shorter videos finish more often. Never under 61 s: TikTok's Creator Rewards pays only on
  videos over a minute (for later). Videos 08–10 ran 75–80 s.
- Real people and deaths: one sentence each, nobody shown hurt, no faces of real people, no brand names, logos or team colours.
- Never reuse a reference account's wording; write every line fresh.

---

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

**The first video under the cap** (video 12, 18 Nov 2026): 186.50 for 63.7 s (stills 20.00, clips 144.00, two re-renders 22.50)
against a 194.64 quote: the standard plan below held.

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
**Start from video 12's set** (18 Nov 2026) and rename the prefix: `12-prompts.py` (STYLE, WIDE, SET, CAMERA, POS, LOCK, LOCKZ,
STREETZ and VAULTZ, REFS), `12-mk.py` (still requests), `12-clips.py` (clip requests; lengths read from `12-plan.json`; start-only
clips), `12-timing.py` (pause tightening, beats, clips rounded to the nearest second, OVERRIDE), `12-build.py` (the edit tools of
Step 9 plus vertical whips), `12-thumbnail.py`, `12-flightmap.py`, `12-post-copy.md`, and `12-beat-sheet.md` (the latest beat sheet
layout, with a production log). Whisper runs in the Higgsfield sandbox from a heredoc (the 10-whisper.py code with a new
`initial_prompt`), reading the ElevenLabs take URLs directly. The set before it, kept for reference: `10-prompts.py` (STYLE without water, WIDE, SET, CAMERA, POS, LOCK,
LOCKZ, INDOOR, REFS), `10-mk.py` (still requests), `10-clips.py` (clip requests, the floor line, middle keyframes), `10-whisper.py`,
`10-timing.py` (pause tightening, beats, the clip plan), `10-build.py` (all the edit tools of Step 9), `09-build.py` (pointers with
tracking), `10-thumbnail.py`, `10-flightmap.py`, `10-post-copy.md`; `pipeline/analysis/` (the checks) and `pipeline/youtube/`
(12.2). Video 11's `11-beat-sheet.md` is the latest beat sheet layout. Earlier per-video files stay in `pipeline/` for the record.

---

## 7. Production lessons that still apply (collected from videos 01–11; consolidated 18 Nov 2026)

### 7.1 Stills (seedream)
- **Stills take 1.6–1.8 tries each** in this look; budget for it. `seedream` takes about 8 jobs at once (more are refused with
  429, no charge). **Video 12 got all 16 on the first try** (18 Nov 2026): the wide made first as the set key, every other still an
  edit of it or of a neighbour, and a STREETZ or VAULTZ line on every close-up so no cut ground leaked in.
- **The set key can float** over a pale ground instead of reaching the bottom edge, whatever the deep-block line says (video 12):
  it leaves a calm lower area for the captions, so keep it.
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
- **A clip that has to get from the street into an underground room can invent its own route** (video 12, C12A): the road cracked
  open round the lid and the camera dived down a brick sewer shaft. Fix: a middle keyframe of the room's inside and "the camera
  never goes through the lid; the road never breaks; no bricks anywhere".
- **A start-only change clip can come back faint** (video 12, C6A: a thin thread of an arc). "On the first frame a big, bright arc
  bursts out … lighting the whole close-up" got bolts that read on a phone.
- Turning inside a cut-open room, Kling may glimpse the sky through the open front for half a second (video 12): accepted.

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
- **Round clip lengths to the nearest second, not up** (18 Nov 2026, `12-timing.py`): rounding up made 70 s of clips for a 65.6 s
  video; nearest-second rounding and one pinned clip gave 64 s for 63.7 s, all played at 0.88–1.26×.
- **Whips can be vertical** (`12-build.py`, WHIP takes an xfade direction): slideup for a dive down, slidedown for a flight up,
  with vertical motion blur.

### 7.5 Narration and sound
- Daniel's raw pace runs 2.9–3.3 words a second by take; pause tightening and `atempo` up to 1.1 bring it to ~3.5. Never speed it
  more than 1.1×; cut words instead.
- To fix a pronunciation, respell it in the text sent to the voice ("doo-er" for dewar); the captions keep the real word.
- Room-tone beds come back very quiet (mean −64 dB): set every level by measurement, never a fixed gain.
- Time each effect from its loud moment on the picture; cut a long effect short if the picture stops (the `FX` cut value).
- **Check the bed with `under_the_voice.py`, not by its setting** (18 Nov 2026): BED_UNDER 19 put a steady street bed 26 dB under
  the voice in the quiet moments; 14 brought it to 22 dB. Remix only the audio onto the finished picture (`mix()` and a stream copy).

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
  summaries and say so); on 18 Nov 2026 also `cbsnews.com`, `thecity.nyc`, `lincolnsquarebid.org`, `tdworld.com` and
  `lite.conedison.com`.
- **ElevenLabs `account_get_usage` needs the connector reconnected with more permissions** (18 Nov 2026); estimates and
  generations work, so the ElevenLabs balance can't be read from a session until then.
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

## 8. Posting and profile (approved by the user on 18 Nov 2026 unless marked)

### 8.1 TikTok, every video
- **Caption:** the question the video answers, with one emoji, then `#HowItWorks #Engineering #LearnOnTikTok #3DAnimation` and one or
  two topic tags.
- **The hashtags must turn into links.** From video 02 on, none of ours registered (TikTok saw plain text; 1.5, 9.1). Type each tag
  in the app, or tap it from the suggestion list after typing "#", and check that it shows as a link before posting. After
  posting, check from a session that `textExtra` is not empty (12.1).
- **AI label:** TikTok has added its own AI-generated label to our videos (9 of 10, seawater included), and it didn't stop seawater.
  Turn on "AI-generated content" when posting, as TikTok's rules ask for realistic AI scenes.
- **Cover:** TikTok Studio on desktop → Edit cover → upload the 1080×1440 crop (7.6); otherwise pick the most satisfying frame.
- **Pin a comment** with the comment question; reply to every comment in the first day.
- **When:** early evening, US Eastern (our two best went out at about 6–7 pm ET). At most one video a day; never two a few hours
  apart (videos 08 and 09 went out 2.4 h apart and split their first tests).
- Don't delete a video that stalls. For the re-cut test (2.2), set the old version to private when the new one goes up.

### 8.2 YouTube Shorts, every video
- **Title:** the question the video answers, under ~60 characters, no hashtags, no call to action.
- **Description:** two or three sentences that retell the premise with the named problems, one question for the comments, then at
  most three hashtags.
- **Audience:** "No, it's not made for kids" on the upload, and as the channel default (made-for-kids mode killed video 02 at
  7 views until it was fixed).
- **Altered or synthetic content: leave it unticked** for these cutaways. YouTube's own announcement exempts clearly unrealistic
  content such as animation, and a set sliced open like a cake can't be taken for footage; no source says the label changes reach
  (18 Nov 2026). Tick it only if a video ever shows a realistic scene that could pass for real footage of a real event or person.
- **Cover:** pick the frame yourself at upload (custom covers need the Partner Program): the most satisfying cutaway moment, with
  no stray caption word on it (ours have shown "WAY", "So", "COLORS").
- **Pin the comment question**; reply to every comment in the first day.
- Post the same day as TikTok.

### 8.3 Profile fixes (do these before the first of the ten)
- **Rename the TikTok account** to match the content and the YouTube channel: the handle @overthinkingyearly tells a visitor
  nothing (the display name changed from "OT" to "overthinkingyearly" on 18 Nov 2026; the handle hasn't). The natural pick is the
  YouTube name: check that `@letzbuildtogether` is free with `pipeline/youtube/handles.py <dir> tt letzbuildtogether`. TikTok
  allows a username change once every 30 days.
- **Bio on both platforms:** what you post and how often, in one line, e.g. "The hidden inside of everyday things, in 3D. New video
  every other day."
- **Pin the three best TikTok videos:** seawater, the hydrant, and the best of the new ones as it emerges.
- **The profile picture and the banner without the mascot** (18 Nov 2026, later; the user: "can you give me a eye catching
  profile and banner image for my TikTok and YouTube account. I don't want it to include the character"). Made from the videos'
  own stills, no credits, in `branding/`. The user hasn't said which goes live: check with `yt_snapshot.py` before saying which is up.
  - **Profile picture** (800×800, one file for TikTok and YouTube; a yellow ring round a circle-safe crop): **A, recommended:**
    `avatar-blast-800.png`, video 12's lid lifting off on a column of flame (one big shape that still reads at 24–32 px);
    **B:** `avatar-hydrant-800.png`, the hydrant cut open down to the main (video 03, the 196K Short); **C:**
    `avatar-portal-800.png`, the vented lid from below with daylight through its holes (striking, but grey at small sizes).
  - **YouTube banner** (2560×1440 JPG, about 0.35 MB): "3D CUTAWAY EXPLAINERS / EVERYDAY THINGS, CUT OPEN. / NEW VIDEO EVERY
    OTHER DAY", the second line sliced open with an orange core, beside three video cards (the hydrant, the manhole blast,
    seawater) inside the phone box, plus four cards that only computers show. **Yellow, recommended as the most eye-catching:**
    `banner-cutopen-yellow-2560x1440.jpg`; **ink** (navy, calmer): `banner-cutopen-ink-2560x1440.jpg`. TikTok has no banner.
  - How they look: `fit-check-banners.jpg` (YouTube on a computer and in the app, the full upload) and `fit-check-avatars.jpg`
    (sizes on light and dark, the TikTok profile and feed). Rebuild or change the words: `pipeline/branding/make_brand_v2.py
    <stills dir> <fonts dir> branding --fetch` (`--line1`, `--line2`, `--eyebrow`, `--pill`; change the pill if the posting
    rhythm changes). Older options, kept: the three mascot-free avatars made that morning (`avatar-cutaway-*.png`,
    `make_avatar_cutaway.py`) and the mascot set of 10 Nov 2026 (`avatar-800.png`, `banner-2560x1440.png`), which the new
    banner replaces.

### 8.4 After posting
- Read the views at about 24 h and 72 h on both platforms (12.1, 12.2) and add them to the video log (9.2).
- **The bars:** more than ~2K on TikTok within 72 h means it passed the first test (our failed ones stop at 330–454); more than ~1K
  on YouTube means it was tested normally; 10K+ is a breakout for us.

---

## 9. Channels, results and the video log

### 9.1 Snapshot (18 Nov 2026, about 00:20–01:00 UTC; read from public pages, 12)
TikTok @overthinkingyearly (display name "OT" until later that day): 54 followers (44 on 13 Nov), 679 likes, 10 videos, 46.4K views; it follows nobody.
YouTube @LetzBuildTogether: 310 subscribers (282 on 15 Nov), 10 Shorts, about 209K views.

| Video | Posted | TikTok views (likes · comments · shares · saves) | TikTok's category for it | YouTube views (likes) |
|---|---|---|---|---|
| 10 Cryonics | 16–17 Nov | 359 (12 · 2 · 0 · 1) | Science, Education | 11 (1) |
| 09 Lightning | 15 Nov | 340 (19 · 0 · 2 · 1) | none given | 17 (2) |
| 08 Sewer | 15 Nov | 354 (16 · 0 · 1 · 2) | Home & Garden, Daily Life, Lifestyle | 33 (3) |
| 07 1959 vs 2009 car | 14 Nov | 364 (24 · 0 · 0 · 2) | Cars, Auto & Vehicle | 42 (2) |
| 06 Petra | 12 Nov | 330 (14 · 0 · 0 · 4) | Anime & Comics, Entertainment | 64 (3) |
| 05 Aquarius | 11 Nov | 454 (25 · 1 · 0 · 3) | none given | 1,273 (67) |
| 04 Seawater | 10–11 Nov | 33,900 (381 · 10 · 38 · 63) | Science, Education | 8,802 (356) |
| 03 Fire hydrant | 9 Nov | 6,341 (117 · 0 · 3 · 8) | none given | 196,202 (about 6K) |
| 02 Canoe | 7 Nov | 1,873 (25 · 1 · 2 · 2) | Science, Education | 201 (11) |
| 01 Mud house | 6–7 Nov | 2,124 (46 · 1 · 2 · 5) | Humanities, Education | 2,106 (101) |

Also found on 18 Nov 2026 (12.1): from video 02 on, no caption hashtag registered on TikTok; TikTok added its own AI-generated
label to 9 of 10 videos; no video shows a penalty. The YouTube uploads carry no TikTok watermark and are not in made-for-kids mode.

### 9.2 Video log (condensed 18 Nov 2026; full notes for each video are in the repo history at commit `1174f29`)
| # | YouTube title | Made | Look | Higgsfield credits | Opening: does the scene change by 1–2 s? |
|---|---|---|---|---|---|
| 01 | How Mud Becomes a House in the Desert | 7 Nov | mascot, Lite | 106.25 | yes: rocks stacked into a wall |
| 02 | How a Fallen Tree Becomes a Canoe | 7 Nov | mascot, Full | 202.00 | yes: the log rolls into the river |
| 03 | Why Don't Fire Hydrants Freeze? | 8 Nov | cutaway, Lite | 123.25 | yes: water bursts from the pipe |
| 04 | How Seawater Becomes Drinking Water (Without Boiling It) | 10 Nov | cutaway, Lite | 111.75 | water flows from frame 1 |
| 05 | How a Steel Tank Becomes a House at the Bottom of the Sea | 11 Nov | mascot, Middle | 176.00 | no |
| 06 | How a Crack in a Cliff Becomes the Hidden City of Petra | 12 Nov | mascot, Middle | 158.75 | no |
| 07 | 1959 Car vs 2009 Car: Only One Driver Walks Away | 14 Nov | mascot, Middle | 157.25 | no (a frozen frame) |
| 08 | Why Your House Doesn't Smell Like the Sewer | 15 Nov | cutaway, one view | 203.50 | no |
| 09 | What Lightning Does Inside Your House | 15 Nov | cutaway, travelling camera | 264.25 | no (no bolt in 3 s) |
| 10 | Why These People Are Frozen Upside Down | 17 Nov | cutaway, travelling camera | 278.00 | no |
| 11 | Why This Castle Was Built Like a Maze (Himeji) | — | cutaway, travelling camera | quoted 271.69 | stopped by the user at Gate B, 18 Nov 2026 |
| 12 | Why Some Manhole Covers Are Full of Holes (V1) | 18 Nov | cutaway, travelling camera | 186.50 (quoted 194.64) | yes: the lid leaves the road on flame at ~0.6 s |

**Files kept for re-cuts** (Higgsfield storage, `https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.mp4`;
not reachable from a session, so give the links to the user or read them through the Higgsfield sandbox):
- 03 hydrant: final `cd23a38c-d887-48ff-8a32-df82dcb2a270`; clean master with narration, no captions `30f6f773-5ead-4cec-a367-bf6dd936839d`.
- 04 seawater: final `09f4ea3f-150f-4f02-a067-39b09fa5f366`; clean master `2bdc92ec-03d6-4c0e-a517-a72234807e71`.
- 07 car: final `35f8a478-c94f-4893-a326-552efd58100a`; clean master `f898830c-b0e8-4ebd-b3cd-a83ed0569f46`.
- 08 sewer: final `a970c674-b421-4a1e-ad15-152bab7b2815`; voice-only `b3435583-038b-454d-99de-f5867c24ac81`; clean master (full sound,
  no captions or pointers) `681cff41-db44-418c-83a3-b19f6eee19ad`; ElevenLabs flows: narration `VzHYC42k13jcCO777zar`, sound
  `jkPXm5LUPekg4BFsFLmm`.
- 09 lightning: final `d8e26fda-8fb2-4885-aa09-e2b5ebd37b00`; voice-only `ad92be18-b6a4-4257-bc6b-6ecfb8ba33d3`; clean master
  `bfe04732-841b-4595-8a7d-d81b150d8c3f`; flows: narration `0Udre8WpeBTl2gAnjT3Z`, sound `FSzLyvOaFzeFXRMh7RoX`; Higgsfield folder
  `783ef666-4a82-436a-90f9-36e3983264a4`; build `pipeline/09-build.py`, word timings `pipeline/09-words-takeA.json`.
- 10 cryonics: final `411ec54b-1d2d-4bcd-986a-ad5162a5d424`; voice-only `08f9539b-f60b-4c57-b18a-07b8ee5fdcc0`; clean master
  `92c26eb5-d5d7-46fb-b0da-d85613bda271`; flows: narration `veNoEzrTLWDaaHUTT1ie`, sound `shGklhH86OxmdJFiZJJ0`; Higgsfield folder
  `dc9cd687-a9ef-4334-a7db-29df6b684c68`; build `pipeline/10-build.py`, word timings `pipeline/10-words-takeA.json`.
- 12 manhole covers (18 Nov 2026; 63.7 s; picture 97% moving, camera 83% moving, parallax 0.88 px, bed 22 dB under the voice,
  -13.1 LUFS): final `4a06b2de-85f5-48ef-934c-127ab188feac`; voice-only `031bfa5e-7e50-4897-bf57-3de54b22f8fd`; clean master
  `f14e85d8-2eaa-47d0-868e-56e19a64c57f`; flows: narration `mGH44upt45AU8OjNz4mT`, sound `JjjBUf6oJu5ocLnAJd3K`; Higgsfield folder
  `25f62fea-3516-4722-a1d8-62520102b743`; build `pipeline/12-build.py`, word timings `pipeline/12-words-takeB.json`.
- Every video's script, beat sheet, prompts, job ids and build script are in `pipeline/NN-*`.

### 9.3 What the ten videos taught (18 Nov 2026)
- **Our two hits were our two cheapest videos** (hydrant 123.25, seawater 111.75, both Lite, about two thirds still pictures), and
  our three most expensive (203–278) stalled at ~350 on TikTok. Spending more on the middle didn't buy reach; the opening and the
  topic did (1.2, 1.3). Hence the 200-credit cap (6.1).
- **The topic:** everyday hidden workings won on both platforms; landmarks, a matchup and cryonics didn't (1.3).
- **The mascot videos did worst:** the two videos without it held 90% of the TikTok views and 98% of the YouTube views on 15 Nov
  2026, and TikTok filed one mascot video as "Anime & Comics". The topic and the look changed at the same time, so the mascot
  alone is not proven to be the cause.
- **The look got much better** (videos 09–10 meet every motion and camera target, 5), and it is ready for good openings.
- **Changing direction after almost every video** (three looks, five idea lists and four reference accounts in eleven days) left
  each video tested on a different audience (my read). The plan holds one lane for ten videos (2).

---

## 10. Money and monetisation (figures from web searches on 9–13 Nov 2026; re-check before quoting)

- **TikTok Shop affiliate** is a separate project with its own memory, `tiktokshop.md` (13 Nov 2026): 1,000 followers to apply in
  the US, a Pilot Program until 5,000, and why our animated videos can build followers but can't be the product videos. At about 2
  new followers a day (13–18 Nov 2026), 1,000 is far off; the plan in section 2 is the way there.
- **TikTok Creator Rewards:** 10K followers, 100K views in the last 30 days, 18+, a personal account, videos over 1 minute; quoted at
  about $0.40–1.00 per 1,000 qualified views (third-party figures). Our 62–64 s videos qualify on length.
- **YouTube Partner Program:** 1,000 subscribers plus 4,000 watch hours in a year or 10M Shorts views in 90 days. From 1 Feb 2027 new
  applicants need 8,000 hours or 20M Shorts views (announced 10 Aug 2026). Custom Shorts covers come with the program. Shorts pay
  about $0.03–0.07 per 1,000 views (more for US audiences); long videos about $1–10.
- **The answer given on 11 Nov 2026 to "$3,000 a month?":** not from Shorts ads alone (that is 43–100M views a month); realistic only
  as a mix led by TikTok Creator Rewards and longer videos, once one or two videos a month reach several million views.
- **YouTube's "inauthentic content" rule** (guidance of 16 Jul 2026): generic or template-based videos, unsatisfying content and AI
  personas giving advice are not eligible for ads, judged across the whole channel. Researched, original scripts and a single,
  consistent format are the defence.
- **Cost side (18 Nov 2026):** at most 200 Higgsfield credits a video (6.1) plus about 1,400–1,540 ElevenLabs credits a narration
  take and ~130 for the sound.

---

## 11. Paste-in prompts

### 11.1 Kickoff prompt (renewed 18/11/26 v2: the 10-video plan and the 200-credit cap)
Fill in the line in angle brackets and paste the whole block into a new session. The earlier versions are listed in 13.3.
```
KICKOFF PROMPT (renewed 18/11/26 v2)

Read CLAUDE.md in AliKandaz/short-form-video-memory (or the "Short-Form Video Memory"
artifact) first, all sections. Then make the video with the section 6 runbook.

IDEA:   <V1 ... V10 from section 3, or my own topic in the same lane>
SOUND:  bed and effects (unless I say voice only)

Budget (6.1): at most 200 Higgsfield credits for this video, the 15% reserve included.
Check the balance first. If the plan prices above 200, cut it (shorter script, fewer
camera positions, shorter clips) before you show me the quote. Clips at 720p.

The opening (Rule 0, section 4.2): frame 1 is the "before" or the event itself; the
scene changes, big in the frame, by 1.0 s; the first line says what the picture is
doing. Never an establishing shot, never "If you want...", never a remark. A
surprise by about 4 s (the first "But", or the line right after a cold open).

The look (section 5): Cutaway, no character; one place sliced open like a cake; a
travelling camera with 7-9 positions, each a real still; every line a clip; one-word
ALL CAPS captions about 57 px tall, 75% down; solid white pointers that ride with the
camera; a quiet bed and a few effects, no music; the last frame matches the first.
Narrator Daniel, video model kling4_0.

The script (section 4): about 220 words (62-64 s); a But/So chain with each problem
and fix at its own spot on the set; one true twist, one "that's why" and one small
joke, all shown on the set; a three-beat ending that loops into the first frame; never
"Congratulations..."; no spoken call to action. Fact-check every ⚠ before Gate A and
run the saturation check on the exact title (with "zack d films" + the topic).

Stop for my approval at:
- Gate A: titles, the script, the first second as three lines (frame 0 / what has
  changed by 1 s / the first line), the camera position on each line, the facts
  checked, the saturation numbers.
- Gate B: the quote at 720p, 200 or less with the reserve, and the balance after.
- Gate C: the stills as a flight map; the set matching from every angle; the first
  and last frames matching.
- Gate D: the hook pilot's frames at 0, 0.5, 1 and 2 s, and both pilots'
  camera_path.py and check_video.py numbers next to the reference.
Spend nothing before Gate B, and don't render the rest until the pilots pass.

When it's done, give me: the final MP4 link and the voice-only version; the motion
and camera numbers and the first-second check; credits quoted against spent; any line
that lost its clip; 3 covers (one a plain frame); TikTok copy (the question with one
emoji, and the hashtags for me to type in the app) and YouTube copy (a title under ~60
characters, a 2-3 sentence description, not made for kids, altered content
unticked). Then log the video in 9.2, add any new lessons to section 7, and update
both copies of the memory.
```

### 11.2 Re-cut prompt (18/11/26: the free opening test of section 2.2)
```
RE-CUT PROMPT (18/11/26)

Read CLAUDE.md in AliKandaz/short-form-video-memory (or the "Short-Form Video Memory"
artifact) first. Then re-cut video <09 | 10 | 07> with the new opening described for
it in section 2.2, spending no Higgsfield credits:
- Use the clips, word timings and build script that already exist (9.2 lists them).
- Only the opening changes: frame 1 shows the event and the scene changes by 1 s.
  Check the frames at 0, 0.5, 1 and 2 s.
- If the new opening needs a new first line, generate it in Daniel's voice with
  ElevenLabs (estimate first) and keep the rest of the narration.
- Show me a 5-second preview of the new opening before rendering the whole video.
Deliver the new final, a TikTok caption (hashtags for me to type in the app) and a
YouTube title. Log it in 9.2 as <NN>b and update both copies of the memory.
```

---

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
- **`yt_snapshot.py`'s save-to-playlist flag is unreliable** (18 Nov 2026): two runs minutes apart flipped it for two Shorts. Don't
  read a lone "save-to-playlist NO" as made-for-kids mode, which also turns comments off.
- **YouTube's search page now lists Shorts as plain video results that open in the Shorts player** (18 Nov 2026).
  `yt_saturation.py` counted them as long videos and reported "0 distinct Shorts" on pages that held a dozen; that is why V1's
  demand note said no Short used its title. Fixed (`bba4c0d`): it now counts them, with age and channel. Ideas checked before the
  fix may have missed Shorts, so rerun the check at each Gate A.
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

## 13. Parked ideas, topics to avoid, and history (18 Nov 2026)

### 13.1 Parked ideas (approved by the user on 16–18 Nov 2026; parked on 18 Nov 2026 for the one-lane plan)
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

### 13.2 Topics to avoid
- **Made by us:** the mud house, the canoe, the fire hydrant, seawater to tap water, the underwater habitat (Aquarius), Petra, the
  1959 vs 2009 crash, the sewer trap, lightning in a house, cryonics, the manhole covers (video 12).
- **Made by Hidden By Design:** the storm drain, the water well and water tower, a road tunnel under a river, a landfill into a
  park, a bridge foundation (cofferdam), the sewer and treatment works, power lines, the gas station, the roof, the beach.
- **Made by How Building Explained:** the nipa hut, an Amazon floating house, the igloo, the levee, a nuclear bunker, a nuclear
  plant (our cooling tower is the tower only, never a plant), Chernobyl, the White House, the Kremlin, a particle accelerator, an
  armored truck, the gas station, the car wash, an oil well, the septic tank, a drive-thru, a slot machine, a car engine,
  fire-, volcano- and earthquake-proof houses, a Halloween station.
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

### 13.3 History (one line a step; details at the commits named)
- **6–7 Nov 2026:** videos 01–02, How Building Explained's formula with a mascot.
- **8–10 Nov:** videos 03–04 in Hidden By Design's cutaway look (Lite). YouTube audit; branding made; the channel renamed
  LetZBuildTogether by the user between 10 and 15 Nov.
- **11 Nov:** back to the mascot look, Middle tier, famous places (ideas at `92a077a`); videos 05–06; the one-build shot rule; Ultra
  plan, 3,000 credits. **13 Nov:** TikTok Shop research (`tiktokshop.md`).
- **14 Nov:** "Who wins?" matchups (`c37181e`); video 07.
- **15 Nov:** the Cutaway look locked with no character; sound approved; Cutaway ideas C1–C5 (`45b7846`); video 08; the travelling
  camera approved; video 09.
- **16 Nov:** out-of-the-ordinary ideas X1–X5; video 10 (X5). **17–18 Nov:** NET FILES studied; fortress ideas F1–F3 (`b1656bb`);
  video 11 (F3) scripted and quoted.
- **18 Nov:** growth audit of both channels (`8a4a6da`, `1174f29`); profile pictures without the mascot (`13b080e`); the user
  approved the audit's recommendations, stopped video 11 and set the 200-credit cap; this file rewritten for the 10-video plan.
- **18 Nov (later):** video 12 (V1, the manhole covers) made under the 200 cap, retitled at Gate A; the saturation check's Shorts
  parser fixed (`bba4c0d`); the video's files from `679af8c` to the commit that logged it. Then an eye-catching profile picture
  and YouTube banner without the mascot, from the videos' stills (`make_brand_v2.py`, 8.3).
- Paste-in prompts before this one: 11/11/26 (`f8bf298`), 15/11/26 (`db03adc`), 15/11/26 v2 (`309d785`), 18/11/26 (`1174f29`).
