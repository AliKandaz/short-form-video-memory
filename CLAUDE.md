# Short-Form 3D Build Explainers: Project Memory

This project makes short vertical 3D-animated explainer videos in the style of the TikTok account
@howbuildingexplained ("How Building Explained By Zach"). Read this file before writing any script,
storyboard or animation brief.

Full visual reference (frames, beat sheet, both reconstructed scripts):
https://claude.ai/artifact/MPEu5jqcnUDLSsz3fiBc8N (private "How Building Explained Style Bible" artifact; open it with the Artifact tool's read action)

A second reference account, **@1hidden_by_design** ("Hidden By Design": the same narration formula, aimed at the hidden engineering
behind everyday things), was studied on 8 Nov 2026. Its learnings are in section 4. A third, **NET FILES** (TikTok @net.files6:
3D stories of ancient engineering, mostly Chinese fortresses, bridges and tombs), was studied on 17–18 Nov 2026 for the fortress
ideas F1–F3 (section 2); the record is in 7.9.

The user's own YouTube channel was audited on 9–10 Nov 2026. Section 6 has the audit, the YouTube channels that lead this
format (You Made It, You Built It), a topic-saturation check of the idea lists, and the YouTube upload checklist. Section 6.9
(11 Nov 2026) has what the views are worth in money on Shorts, TikTok and long videos.

**Direction from the user on the look (15 Nov 2026, current): Cutaway, no character.** The two videos made without the character
(03 fire hydrant, 04 seawater) hold 90% of our TikTok views and 98% of our YouTube views, so the user left the character look: "I
need to step away from the character figure animation and make similar ones to like the other two." The same day they approved six
refinements to that look: animate nearly all of it; one cutaway, changed in place; move the camera instead of fading between
pictures; hold the look steady; bigger captions on a quiet part of the frame; bolder pointers. The rules are in 3.4, the measurements
and reasons in 7.5. To make a video, paste the section 5 prompt (**renewed 18/11/26**, below). Later the same day they said "yes on the
sound": a quiet bed and a few effects under the voice, no music (3.4). The idea list was redone for the look that day as well
(five Cutaway ideas), and replaced on 16 Nov 2026 by five out-of-the-ordinary ideas with draft scripts (section 2), which three
fortress stories joined on 18 Nov 2026 (F1–F3).

**First Cutaway video (15 Nov 2026): 08, the sewer trap (idea C1).** Made the same day under the new rules, with the sound: 203.50
credits against a 219.65 quote, no clip redos (3.4b). Every line has a clip (93% of the running time), but `check_video.py` counts
only 20% of its seconds as moving, against the 80% target: what moves is small in the frame, and the camera moves were made from
crops of one still, which are zooms the checker takes out. Read 3.4k before the next video: plan a camera path with real close-up
stills, and make what moves big.

**First travelling-camera video (15 Nov 2026): 09, what lightning does inside your house (idea C3).** Made the same day under the
seven rules, opened on the cold claim. It met every Rule 1 and Rule 7 target: 84% of the seconds moving, the camera moving in 78%,
parallax 0.44 px, a big move in 23 of 76 seconds, no still-camera stretch over 3 s (3.4b). 10 camera positions on one storm house,
16 clips and no holds. 264.25 credits against a 242.65 quote (+8.9%): stills took 1.75 tries each, and three clips needed fixing
(one re-render each, one fixed in the edit). Read 3.4l before the next video.

**First video from the 16 Nov ideas (16–17 Nov 2026): 10, why these people are frozen upside down (idea X5).** Opened on "If
you…" (opening A, which the user picked at Gate A over the cold claim). It beat every Rule 1 and Rule 7 target: 90% of the seconds
moving, the camera moving in 92%, parallax 0.41 px, a big move in 35 of 77 seconds, no still-camera stretch over 2 s (3.4b). 9
camera positions on one sliced-open lab with no water in it, 19 clips and no holds. 278.00 credits against a 280.60 quote (244.00
before the reserve): stills took 1.6 tries each, three clips were rendered again because the cutaway opened a pit or a step in the
floor mid-move (one more was cut in the edit), and the edit added the drift to four still-camera clips and made the power cut.
Read 3.4m before the next video.

**Camera (approved by the user, 15 Nov 2026, after video 08): a travelling camera, like @1hidden_by_design's power-lines video.**
The user found the look good but "not enough movement. the camera should move in and away from the changes happening in the
videos", pointed to "How Do Those Giant Power Lines Get Electricity to Your House?", and approved seven changes "as long as it
accomplishes the same video as the one I referenced". The camera now flies around and into the one set, in to each change and away
again: Rules 2, 3, 5 and 6 of the look were rewritten and Rule 7 added, with targets measured by `pipeline/analysis/camera_path.py`
(3.4). The reference's camera path, the measurements and the record are in 7.7. The paste prompt was renewed for it (section 5,
**15/11/26 v2**).

**Earlier direction on the look (11 Nov 2026, replaced on 15 Nov 2026):** the look was Classic (the mascot look of videos 01–02 and
05–07). Section 7 has the details and the account the user likes (@thewhatifstudio). Video 05 (Aquarius) was made on 11 Nov 2026 in
the new **Middle** tier, which is still the default (3.1, 3.4). The ten ideas approved that day (famous real places and true extreme
stories) were replaced on 14 Nov 2026: see "Ideas" below.

**Shot rule (LOCKED by the user, 11 Nov 2026, after video 05): one build.** Its "one main view" part was replaced on 15 Nov 2026 by
the travelling camera (3.4 Rule 2, 7.7). The camera stays on the thing being explained, and every line of the script changes
something you can see on it. No shots of other things and no separate rooms. The rules are in 3.4 and the reasons in 7.2. Video 06 (Petra, 12 Nov 2026) was the first
made under it: 158.75 credits against a 186.30 quote, no clip redos (3.4b, 3.4h).

**Sister project (13 Nov 2026): TikTok Shop affiliate.** Its memory is `tiktokshop.md` in this repo, also attached to the memory
artifact as the file `tiktokshop.md`. Read it before any work on TikTok Shop, affiliate videos or TikTok monetisation. It holds the US
rules for joining (1,000 followers to apply), the plan to get @overthinkingyearly there, and how our videos are doing on TikTok. The
account is US-based (the user confirmed on 13 Nov 2026).

**Ideas (approved by the user, 16 Nov 2026): five out-of-the-ordinary ideas, each with a draft script.** X1 there are more people
under Paris than in it (the catacombs), X2 the town that's been on fire since 1962 (Centralia), X3 the car that split in half and
caught fire while its driver walked out (Grosjean and the halo), X4 the Alaska town that lives in one building (Whittier), and X5
why these people are frozen upside down (cryonics). The user asked for ideas with an opening that grabs, like "what happens when
you fall off a cruise ship", turned down a first five that were all about water, and approved these with their scripts. None is
about water, and none has been made by Zack D. Films, who owns the "what happens if you…" format on Shorts. They are section 2;
the brief and the research are in 7.8. The order is not set. **X5 was made as video 10 (16–17 Nov 2026); X1–X4 are still open.**

**Ideas added (18 Nov 2026): three fortress stories, F1–F3, beside X1–X4.** The user sent NET FILES' "How Ancient Engineers Built
An Almost Impossible To Conquer Mountain Fortress 😱" (TikTok @net.files6, 1.3M views in its first day and a half) and asked for "3
creative video ideas inspired by this … I want stories similar to this", then: "add these video ideas into claude.md without
removing the other ones in section 2. update the copy and paste prompt accordingly and label the new renewed date". F1 why this
rock has more tunnels than roads (Gibraltar), F2 the castle that beat an army and was then sold by its own guards (Malbork), F3
why this castle was built like a maze (Himeji). Each keeps the reference's three moves: a defense puzzle (every line answers how
an enemy could get in), the place named only at the end, and one line on what became of it. They are in section 2 after X5, with
an opening and the story as numbered beats instead of a full script; the reference study and the research are in 7.9. The order
is not set. The kickoff prompt was renewed for them (section 5, **18/11/26**).

**Growth audit of both channels (18 Nov 2026): why the views stall.** The user asked why their views are inconsistent and nothing
has gone viral. Read from public pages (6.10): on TikTok the six videos since seawater all stopped at 330–454 views, the size of
the first test; on YouTube the last five Shorts got 11–64 views, almost no test at all. In all six reference videos checked, the
scene itself changes in the first 0.5–2 s (a hole is cut, a roof is covered, sand is dumped); of ours only the mud house, the canoe
and the hydrant do, and those three all passed TikTok's first test. Videos 08–10 met every whole-video motion target and still
stopped at the same point. Recommended, not yet approved: an opening in which the first verb happens on screen within about a
second, one lane for the next 15–20 videos, two or three stalled videos re-cut with new openings as a free test, and TikTok
hashtags typed in the app (none has registered since video 02).

**Ideas before that (15 Nov 2026, removed 16 Nov 2026): five Cutaway ideas.** C1 (why your house doesn't smell like the sewer)
was made as video 08 and C3 (what lightning does inside your house) as video 09; their script facts are in 3.4b. C2 (the ice rink
under a basketball court), C4 (what's inside a nuclear cooling tower) and C5 (where your bowling ball goes) were not made; they are
in the repo history at commit `45b7846`, with that list's reserves. The brief and the research are in 7.6.

**Ideas before those (14 Nov 2026, removed 15 Nov 2026): four "Who wins?" matchups.** The user had found the earlier ideas and hooks
boring and asked for topics that hold viewers and start arguments in the comments (military, vehicles, engineering). One matchup
became video 07 the same day: 157.25 credits against a 177.68 quote, no clip redos, opened on a cold claim (3.4b, 3.4i). The other
three were written around the character and went with the list; they are in the repo history at commit `c37181e`. The brief is in
7.3 and the comment data in 7.4.

---

## 1. What we learned from the source video

**Source:** "How A Branch Of Bamboo Can Turn Into A Nipa Hut in the jungle"
(https://www.tiktok.com/@howbuildingexplained/video/7703769950413933854). 66.6 s, 7.2M views,
731K likes, 18.4K shares. It was cross-checked against the account's #2 video ("How A Hole In Your Yard Can Become A Levee",
100 s, 1.9M views). Both follow the identical formula.

### The niche
- 60–110 s fully 3D-animated vertical explainers. A humble starting thing becomes an impressive structure,
  one problem and one fix at a time, narrated in second person ("you").
- Title formula: `How [humble thing] Can Become [impressive / famous / survival structure] (in the [setting])`
  plus `#engineering #HowItWorks #Science #LearnOnTikTok` and 1–2 topic tags.
- What wins on the account: **primitive survival builds** (jungle nipa hut 7.2M, Amazon floating house 769K)
  and **famous or high-stakes structures** (levee 1.9M, White House 1.6M, nuclear bunker 1.4M, Kremlin 1.0M,
  nuclear plant 976K, particle accelerator 900K).
- What flops: mundane utilities (car wash 9.5K, slot machine 10K, septic 25K, drive-thru 30K, oil well 41K) and
  the "X-proof house" series (fireproof 131K, volcano 95K, earthquake 79K). The igloo also did poorly (38K).
- The hit is one of the shortest videos. Tight scripts with more danger per second do better.

### Script formula
```
HOOK (0-3s)  If [you're in situation], [do a naive thing] and you have a [crude version].
LOOP x6-8    But [specific problem].  ->  So you [concrete fix].  ->  (This is / These are [REAL TERM].)
TWIST        But the deadliest [X] here isn't [obvious thing]. It's [surprise]. + one shock stat
ASIDE        And [fun fact]  /  That's why [thing viewers have seen in real life].
CLIMAX       But then [worst-case disaster] hits. [Everything around you is destroyed.]
PAYOFF       But yours [stands / stays] [safe] while [disaster happens right next to you].
COZY         (You) add [prop 1], [prop 2] and [prop 3].
SIGN-OFF     Congratulations, you have built a [X].      <- their signature line; we never use it (our ending: section 5)
```

### Writing rules
- Second person, present tense. The viewer is always the builder ("you lift", "you drive", "you raise").
- One action or one problem per sentence. Short, mostly one-syllable words, no filler, no hedging.
- Every "But" escalates: nuisance -> weather -> hidden killer -> night threat -> catastrophe.
- After each fix, name the real-world term ("These are stilts." "This is thatch." "This is a rat guard.").
  The term also appears as an ALL-CAPS on-screen label. **Ours since 15 Nov 2026 (Cutaway look):** the term is spoken only; the
  look has no labels (3.4).
- Use everyday and body-scale comparisons: "to your shoulders", "as high as a basketball hoop",
  "knee-high by morning", "hard as rock". **Ours since 11 Nov 2026 (3.4 shot rule):** a comparison is shown only as a label or a
  measurement line on the build; cut any that would need a picture of something else. **Since 15 Nov 2026 (Cutaway look, no
  labels):** it is shown on the set itself (a gauge on the pipe, a tub beside the hydrant) or cut.
- At least one shock stat ("kills more people than snakes, sharks and lions combined", "84% fewer").
  **Fact-check every number before production.**
- One "that's why" tie-in ("That's why levees on the news are wrapped in plastic."). Ours: shown on the set (3.4).
- Pace: about 250 words per 66 s (~3.8 words/s, ~225 wpm). Long versions run ~100 s and ~350 words.

### Animation style
- **Look:** full 3D CG with a real-time, game-engine feel. Semi-realistic textures on simple models, soft shadows,
  mild depth of field. Not photoreal, not cartoon-shaded.
- **Set:** one small diorama (jungle clearing, suburban lawn) that stays the same location while the structure
  evolves on it.
- **Character:** one generic stock-rigged man (olive-green jumpsuit, no facial animation) for scale and
  simple poses: lying, standing, arms over head, waving. Machinery (excavator, backhoe, roller) can replace him.
  **Ours since 15 Nov 2026: no character** (3.4). Hands, small anonymous workers or machines do the work where someone must.
- **Mood through grading:** daylight for fixes, dark desaturated for night threats, blue-grey for storms, sunny
  for the ending.
- **Camera:** about one shot per sentence (2–5 s), hard cuts on "But" and "So", slow push-ins and orbits within shots,
  macro close-ups of key details and then a pull back to the wide shot. **We dropped the one-shot-per-sentence part on 11 Nov 2026:**
  our videos stay on one build (3.4 shot rule, 7.2). **Since 15 Nov 2026** the camera travels from one stage to the next inside a
  clip, never fading between different pictures, and flies around and into the set, in to each change and away again, like
  @1hidden_by_design's power-lines video (3.4 Rules 2, 3 and 7; 7.7).
- **Build moments:** parts appear, slide or grow into place exactly when the narrator names them.
- **Problems** are shown with environmental effects: rain particles, a rising water plane, critter models, swarm particles,
  darkness.
- **Explainer devices** for invisible mechanisms: cross-section cutaways, magnifying-glass macro, x-ray pipes, blue water
  particles, red and blue force arrows, a yellow highlight ring, dashed measurement lines ("10 FT").
- **Captions:** ONE word at a time, synced to the voice, centred at ~52% frame height. Title Case, heavy rounded sans
  (Fredoka-like), white fill, thin black outline, soft drop shadow. **Ours since 15 Nov 2026:** ALL CAPS, larger, about 75% down
  the frame: over plain ground in wide shots, over whatever is there in close-ups (3.4 rule 5).
- **Labels:** ALL CAPS bold white sans with shadow, placed by the object, for the term or stat
  (STILTS, THATCH, DEADLIEST ANIMAL, 84% FEWER, RAT GUARD). **Ours since 15 Nov 2026:** none; solid white arrows and one ring
  point at what matters (3.4 rule 6).
- **Format:** 9:16, 30 fps, 720×1280 or 1080×1920, 60–110 s.
- **End card:** final sunny hero wide shot, character waving, small in-scene signboard with social handles. Ours: the finished
  cutaway in the opening framing, with no character and no sign (3.4).

### Audio
Not analysed at first: the speech-to-text model was blocked in the analysis session, so the scripts were rebuilt from the
burned-in captions. The caption timing implies one continuous, fast narrator voice-over. Voice character and music still need a
listen.

**Measured on 15 Nov 2026, not listened to** (`pipeline/analysis/under_the_voice.py` on the nipa hut and the levee): there is no
steady bed under the voice. Short, quiet stereo sounds sit in the gaps between lines: non-voice sound is present about 34–39% of the
time, in 44 and 91 separate bursts, and the mix falls 28–33 dB below the voice in the quietest moments. TikTok lists both as
"original sound". What the sounds are (build sounds or whooshes) needs a listen. The comparison with the other accounts is in 7.5.

### Ground rules
- Copy the **formula**, never the content. Write new topics and new scripts. Don't reuse their wording,
  character design or "How Building Explained" branding.
- Pick topics with danger or fame built in. Avoid mundane utilities and "X-proof house" topics.
  Exception (section 4): an everyday thing works when its workings are hidden and it moves something the camera can follow
  (storm drain, 9.2M on @1hidden_by_design). Still avoid things whose workings are visible; the gas station flopped on both accounts.
  Since 15 Nov 2026 that exception is our main line: our two best videos and videos 08–09 are all of this kind. The 16 Nov list
  (section 2) adds strange real places and true stories, each still one place cut open (7.8), and the 18 Nov fortress stories
  (F1–F3) add real strongholds told as defense puzzles, with the place named at the end (7.9).
- Avoid topics the account has already done: nipa hut, Amazon floating house, igloo, levee, nuclear bunker,
  nuclear plant, Chernobyl, White House, Kremlin, particle accelerator, armored truck, gas station, car wash,
  oil well, septic, drive-thru, slot machine, car engine, fire/volcano/earthquake-proof house, Halloween station.
  The user's one exception, the nuclear cooling tower (chosen on 15 Nov 2026), left with that list on 16 Nov 2026. If it comes
  back, it is the tower only, never a plant build.

---

## 2. Video ideas: five out-of-the-ordinary ideas with draft scripts (approved 16 Nov 2026) and three fortress stories (added 18 Nov 2026)

**Added by the user on 18 Nov 2026:** three fortress stories, F1–F3, after X5 ("add these video ideas into claude.md without
removing the other ones in section 2"). Their brief, rules and notes are with them, below X5. Everything from here to X5 is the
16 Nov list as it was.

**Approved by the user on 16 Nov 2026:** "I approve these video Ideas, update the claude.md file, remove the other ideas. then
stop". X1–X5 below were the whole list until F1–F3 joined them on 18 Nov 2026. The Cutaway list of 15 Nov 2026 (C1–C5) was removed: C1 and C3 were made as videos 08 and
09, and their script facts moved to their entries in 3.4b; C2 (the ice rink under a basketball court), C4 (the nuclear cooling
tower) and C5 (where your bowling ball goes), with that list's reserves and checks, are in the repo history at commit `45b7846`.
The brief and the research are in 7.8.

- **The brief** (the user, 16 Nov 2026): "give me 5 creative out of the ordinary video ideas I can create videos about with an
  attention grabbing entrance or hook to keep users watching (for example what happens when you fall off a cruise ship)". The
  first five I gave were all about water, and the user said: "all these are water, sea, lake related. mix it up all the ideas
  don't need to be water related, im asking you to give me creative and attention grabbing scripts and video ideas. redo them
  then stop". These five are the redo (7.8).
- **What the five have in common:** an opening claim that sounds wrong and makes you need the answer; a strange real place or a
  true story; one place that can be cut open like a cake for the travelling camera (3.4); none is about water; none has been made
  by Zack D. Films, who owns the "what happens if you…" survival scenario on Shorts (7.8); and in each case the biggest videos
  are real footage, while nobody has animated what a camera can't film.
- **What the user saw and approved:** for each idea, the title, the cutaway line, the full draft script below (word for word),
  the comment question and the demand line. The draft camera positions, the sounds, the ⚠ items and the watch-outs are my notes
  for Gate A.
- **Rules for these ideas** (on top of sections 1 and 5):
  1. Each script opens on a cold claim and goes straight into "If you…", so its first "But" lands at about 5–8 s, later than
     section 5's ~3 s. At Gate A, show the script as approved next to a tightened opening that reaches the first "But" by ~3 s,
     and let the user pick (they chose the cold claim for videos 07 and 09, and the "If you…" opening for video 10, X5, although
     I recommended the cold claim there).
  2. One cutaway set per idea, seen by a travelling camera (3.4 Rules 2 and 3), with each problem and fix at its own spot. The
     camera positions listed are a first draft for the beat sheet (3.3 Step 2). None of these sets is a water set, so the STYLE
     line's translucent cyan water stays out of them (say "there is no water anywhere" in the prompts: 3.4l).
  3. Real people and real deaths: one sentence each, nobody shown hurt, no faces of real people, and no logos, team names or
     company names on screen.
  4. The comment question goes in the TikTok caption or a pinned comment, never in the voice-over (4.2).
  5. ✔ was checked by web search on 16 Nov 2026 (search summaries: reopen the page before quoting); ⚠ still needs checking
     before Gate A. Never plant a mistake to bait corrections.
  6. Before Gate A, run the saturation check on the exact title (6.7) and search "zack d films" with the topic: the numbers
     below come from topic searches.
- **Order:** not set by the user. The user picked X5 first (made as video 10, 16–17 Nov 2026); X1–X4 are open, and so are F1–F3
  (added 18 Nov 2026).
- **How we'll know** (from outside; the user does not want to be asked for retention figures, 7.5): the video gets past where most
  of ours stopped (under about 2K views, 6.1); comments per 1,000 views beat our 0.23; saves and shares per 1,000 views beat
  seawater's 1.9 and 1.1.

**X1. There Are More People Under Paris Than In It** (history, underground: the catacombs of Paris)
- **Set:** one Paris street cut open like a cake: houses and a cemetery on top, pale limestone below, the old quarry tunnels with
  their rock pillars, and the walls of bones. The camera drops from the street into the tunnels.
- **Script** (draft as approved; 248 words, ~71 s at 3.5 words/s):

  > There are more people under Paris than living in it. About six million of them.
  >
  > If you want stone to build a city, you dig it out of the ground right underneath. Paris does that for centuries. But every block you cut out leaves a hole, and the holes join up into tunnels under the streets. So you leave pillars of rock to hold up the roof. These are quarries. But nobody keeps a map, and the city keeps building on top. In 1774, a street called Rue d'Enfer, Hell Street, drops into the ground. So the king sends men down to map the tunnels and prop them up with stone walls. That's why Paris still has a team whose only job is checking under its streets.
  >
  > But there's a second problem up top. The cemeteries are full, and next to the biggest one, cellar walls start giving way. So you need room for the dead, and under the city there are over a hundred miles of empty tunnels. From 1786, carts covered in black cloth carry the bones across Paris at night, with priests walking behind. Down below, workers stack them into walls. Thigh bones in rows. Skulls in lines. This is an ossuary. In 1793, a man goes down alone and gets lost. He's found eleven years later. Above the way in, a sign still says: Stop. This is the empire of death.
  >
  > Dig out the stone, prop up the street, and move the dead in.

- **Comment question:** "Would you go down there? Yes or no."
- **Draft camera positions:** the street, wide → down a shaft into a quarry gallery → the rock pillars → the 1774 collapse seen
  from below → inspectors building stone walls → the cemetery wall from the cellar side → the carts at night, at street level →
  the shaft the bones go down → the walls of bones → the gallery where the man got lost → the sign over the entrance → back up
  to the street, wide.
- **Sounds:** the bed is a dripping stone tunnel; cart wheels on cobbles, creaking props, rubble falling for 1774, footsteps, a
  candle flame.
- **Demand** (16 Nov 2026): real footage leads: "we actually found the catacombs…" 22M on Shorts, then 2.4M (a facts iceberg
  Short), 2.1M and 1.8M; long videos 15.7M, 5.7M and 2.7M. No animated cutaway of the quarries or of how the bones got there.
  Zack D. Films: no catacombs Short found.
- **Checked ✔:** "more than six million" people's remains (other sources: "around six million"), against about 2.1 million living
  Parisians; limestone quarried under the city for centuries; in 1774 the ground under the rue d'Enfer gave way (sources give
  April or December 1774, one gives 1777); the quarry inspectorate founded in 1777 under Louis XVI; cellar walls collapsing
  around the Holy Innocents' Cemetery, the biggest source of bones, in 1774 (one source); transfers from April 1786 (some say
  1785), at night, in carts draped in black, escorted by priests; 200–300 km of tunnels in all; Philibert Aspairt, lost on 3 Nov
  1793 and found eleven years later (his tombstone); "Arrête! C'est ici l'empire de la mort" over the ossuary's entrance.
- **⚠ before Gate A:** that the inspectorate (the Inspection générale des carrières) still checks the tunnels today; the cellar
  collapses (one source says 1774, others 1780); the bone walls were arranged from about 1810, so "workers stack them into
  walls" compresses decades; "Hell Street" is the literal meaning of rue d'Enfer, though the name's origin is debated.
- **Watch out:** bones in walls only: no bodies, no gore. No tour company names.

**X2. The Town That's Been On Fire Since 1962** (disaster, ghost town: Centralia, Pennsylvania)
- **Set:** one small-town street cut open: houses, the gas station and the old dump on top; coal seams and old mine tunnels below,
  glowing orange under the houses. The camera dives through a steaming crack into the fire.
- **Script** (draft as approved; 251 words, ~72 s):

  > This town has been on fire since 1962. You can't see the flames. They're under the ground.
  >
  > If you want to get rid of a town dump, you burn it. Centralia, Pennsylvania, does that in May 1962. But the dump sits in an old mine pit, and under the pit is coal. The fire slips into the old tunnels and starts eating the coal. This is a mine fire. So you fight it. You dig trenches. You pump in water and crushed rock. But the rock down there is full of cracks. The water drains away, and the fire just goes around. Coal burns slowly underground, with almost no air, for years.
  >
  > So the ground starts to cook. In 1979, the mayor checks the tank under his gas station. The fuel inside is 172 degrees. Smoke rises through cracks in the road, and poison gas creeps into basements. In 1981, a 12-year-old boy is in his grandmother's yard when the ground opens under him. The hole is about 150 feet deep and full of gas. His cousin pulls him out. So the government pays 42 million dollars to move the town away. The houses come down. In 2002 it even loses its zip code. Five people still live there. That's why steam still rises out of the ground there in winter, and why a horror movie modeled its ghost town on it. The fire could burn for another 250 years.
  >
  > Light the dump, find the coal, and burn for 250 years.

- **Comment question:** "Would you live there for free? Yes or no."
- **Draft camera positions:** the town, wide → the dump in the old pit → down into the coal seam → the trenches → the cracked rock
  where the water drains → the tank under the gas station → steam through the road → the grandmother's yard as it opens → houses
  coming down → the few houses left → steam in winter → the town, wide.
- **Sounds:** the bed is wind along an empty street; a low roar under the ground, hissing steam, the ground giving way, a
  bulldozer.
- **Demand:** "The Town on Fire for 60 Years 🔥 Centralia 📍Pennsylvania" 20.9M (GeoGlobeTales, a facts Short), visits 2.9M, 737K
  and 208K; long videos 4.3M, 4.2M and 1.5M (Discovery UK, on the horror-film link). The fire is underground, so footage shows
  only smoke: the cutaway shows what no camera can. Zack D. Films: none found.
- **Checked ✔:** the fire traced to May 1962, when the town burned its dump in an abandoned strip-mine pit (historians disagree on
  the exact trigger, so the script tells the usual account); flushing with crushed rock and water, and digging the coal out,
  tried without success; the fractured rock lets water drain away; 1979, the mayor's gasoline at 172 °F; 14 Feb 1981, Todd
  Domboski, 12, fell into a hole about 150 ft deep (sources give 42 m to 150 ft) full of carbon monoxide, and his cousin pulled him
  out; more than $42 million approved by Congress to move the residents (1983 or 1984); the ZIP code discontinued in 2002
  (Pennsylvania's DEP says 2003); 5 residents in 2020; "could burn for another 250 years" is a projection; the 2006 horror film's
  town was inspired by Centralia (its screenwriter researched it).
- **⚠ before Gate A:** how the fire reached the coal (the usual account: an unsealed hole in the pit); gas in basements (carbon
  monoxide: find a source); that the houses were pulled down after the buyout.
- **Watch out:** "172 degrees" is Fahrenheit (our audience is in the US). The film is not named. The cracked "Graffiti Highway"
  was buried in 2020, so the "that's why" is the steam. The boy is not named, and nobody is shown hurt.

**X3. This Car Split in Half and Caught Fire. The Driver Walked Out.** (vehicles, true story: Romain Grosjean, Bahrain, 29 Nov
2020)
- **Set:** one corner of the track cut open: the triple steel barrier, the car's carbon tub with a small driver in a helmet (no
  face), the fuel cell behind him, the marshals and the medical car. The camera rides into the barrier with the car, then swings
  into the cockpit.
- **Script** (draft as approved; 248 words, ~71 s):

  > This car hit a steel barrier at 119 miles an hour, split in half and burst into flames. The driver walked out.
  >
  > If you want a driver to survive that, you put him in a carbon fiber tub. This is the survival cell. But in Bahrain in 2020, on the first lap, Romain Grosjean clips another car and spears into the barrier. The peak force is 67 times his own weight. The car punches through the steel. The back half, with the engine, tears away, and the fuel tank splits. So why is he alive? First, the tub holds. It jams between the rails of the barrier. Second, a bar over his head shoves the steel up and over his helmet. This is the halo. But now he's sitting in a fireball, and his left foot is stuck. So he pulls his foot free and leaves his boot behind. His fireproof suit buys him time. After about 27 seconds he climbs out, with burns on his hands. Marshals blast him with extinguishers, and the medical car is already there.
  >
  > Here's the twist. When the halo arrived two years earlier, people called it ugly. One team boss said that if you gave him a chainsaw, he'd take it off. Grosjean had doubts too. From his hospital bed, he called it the greatest thing Formula One ever brought in. That's the bar you see over every Formula One cockpit.
  >
  > Wrap the driver, shield the head, and let him walk out.

- **Comment question:** "Halo: ugly or genius?"
- **Draft camera positions:** the track, wide → behind the car through the corner → the barrier from the side → the impact → the
  back half tearing away → the tub jammed in the rails → the halo over the helmet → inside the cockpit, the foot stuck → the
  driver climbing out of the fire → the marshals and the medical car → the halo, close → the track, wide.
- **Sounds:** the bed is a race-track crowd with engines far off; the impact, tearing metal, the whoosh of fire, extinguishers,
  a siren.
- **Demand:** real footage leads: "Romain Grosjean - The Man That Walked Out of Fire🔥" 2.4M, then 965K, 497K and 216K on Shorts;
  long videos 9.7M (the drivers' radio reactions), 5.0M (his interview) and 2.5M. No animated cutaway; Zack D. Films: none found.
- **Checked ✔** (the FIA report of March 2021, via press coverage): impact at 192 km/h (119 mph) at 29°, peak 67 g; the survival
  cell, seat, headrest and halo all worked; the halo pushed the barrier up over his head, and the cell jammed between it and the
  bottom rail; the fire came from the power unit separating from the survival cell, and the FIA moved to stop fuel bladders
  splitting; his left foot was trapped and he pulled free, leaving his boot behind; 27 seconds to free himself (many outlets say
  28); the medical car on site within 11 seconds; burns on his hands; the halo arrived in 2018; Toto Wolff, Feb 2018: "if you give
  me a chainsaw I would take it off"; Grosjean had doubts about the halo at first and, from his hospital bed, called it the
  greatest thing brought to Formula One.
- **⚠ before Gate A:** many outlets give 137 mph (221 km/h): check whether that was his speed before the barrier (the script uses
  the FIA's 119 mph at impact); "the fuel tank splits" (implied by the FIA's change; confirm in the report).
- **Watch out:** a real, named person: helmet only, no face; no team colours, names or logos on the car, and no Formula One logo.
  A car on fire is shown: check TikTok's rules on fire before Gate B. The user turned down a race car on the ceiling on 14 Nov
  2026 (section 2, "Not in the list"); this is a true crash story, not a stunt.

**X4. The Alaska Town That Lives in One Building** (strange place: Whittier, Alaska)
- **Set:** one mountain valley cut open: the rail-and-road tunnel through the mountain, the 14-storey tower cut open floor by
  floor, the school across the street with a tunnel under it, and snow. The camera flies through the tunnel, up the tower and
  under the road.
- **Script** (draft as approved; 257 words, ~73 s):

  > Almost everyone in this town lives in the same building. And the only road out closes at night.
  >
  > If you need a port in Alaska during World War Two, you build one at Whittier. But there's no road in. Just a mountain. So the Army blasts a tunnel through it for trains. Two and a half miles of rock. But the people who work here need somewhere to live, through long, snowy winters. So the Army builds one giant tower. Fourteen floors, finished in 1957. Today it's called Begich Towers. About 270 people live in Whittier, and most of them live right here. Inside are the post office, the police, a store and a clinic. You can run most of your errands in slippers. But the school is across the street. So they dig a tunnel under it, and kids walk to class without ever going outside.
  >
  > For decades, the only way in is by train. Cars ride through on flat railcars. So in 2000 they lay a road over the tracks, inside the same tunnel. One lane. Cars and trains take turns. It's the longest highway tunnel in North America. But one lane can only go one way at a time, so the direction flips on a schedule. And at night it closes. In summer, the last car goes through at about quarter past eleven. Miss it, and you sleep in town. That's why, inside the tunnel, you drive right on top of the train tracks.
  >
  > Stack the homes, dig the tunnels, and never go outside.

- **Comment question:** "Could you live there? Yes or no."
- **Draft camera positions:** the valley, wide → the port → the mountain cut open as the tunnel is blasted → the tower going up →
  its floors (post office, police, store, clinic) → the street and the school → down into the school tunnel → a train carrying
  cars on railcars → the road laid over the rails → one lane, the direction flipping → night, the tunnel closing → the valley,
  wide.
- **Sounds:** the bed is wind and snow in a valley; a train horn in the tunnel, the tunnel's warning bell, an elevator, kids'
  footsteps in a tunnel.
- **Demand:** long videos lead: 13.8M (Peter Santenello's visit), 5.5M and 3.4M; the best Short 3.6M, then 81K, 75K and 72K. No
  animated cutaway; Zack D. Films: none found.
- **Checked ✔:** 272 residents in the 2020 census; Begich Towers, 14 storeys, completed in 1957 as a military building; most
  residents live there; a heated tunnel to the school; the US Army built the rail line and tunnel to Whittier in 1941–43; the
  tunnel is about 2.5 miles (13,300 ft), the longest highway tunnel in North America; open to cars since 2000; one lane, shared
  with trains at alternating times; summer hours 5:30 am to 11:15 pm (Whittier Chamber of Commerce); arrive after the last run and
  you stay the night.
- **⚠ before Gate A:** what is inside the tower (post office, police, store, clinic: widely reported, not yet in a checked
  source); that cars rode through on railcars before 2000; the current schedule (Alaska DOT); "long, snowy winters" is the only
  weather claim and has no number.
- **Watch out:** people live here, so small anonymous residents and kids belong in the set; no faces, no brand names. The sound
  in front of the town stays in the background: this is not a water video.

**X5. Why These People Are Frozen Upside Down** (science, the future: cryonics in Arizona) — **MADE as video 10 (16–17 Nov
2026).** The script as made, the facts checked at Gate A (the ⚠ items below are settled there), the saturation check and the
results are in its 3.4b entry; the notes below are the draft as approved.
- **Set:** one storage hall cut open: rows of tall steel tanks, one sliced open to show sealed bodies upside down in white nitrogen
  fog (no faces), and the room where they are cooled. The camera sinks into a tank through the fog.
- **Script** (draft as approved; 230 words, ~66 s: add a line or two at Gate A to reach ~75 s):

  > In Arizona, more than 200 people are stored upside down in steel tanks, waiting to be woken up.
  >
  > If you want to cheat death, a company there will freeze you after you die. But freezing wrecks you. The water in your cells turns to ice, and the crystals rip the cells apart. So they swap your blood for a kind of antifreeze. Then they cool you so far that you turn into something like glass instead of ice. This is vitrification. But glass can still warm up. So they keep you at minus 320 degrees, in liquid nitrogen. The tanks are giant steel thermoses. A vacuum in the walls keeps the heat out. They don't even plug in, so a power cut can't thaw anyone. But liquid nitrogen slowly boils away. So a crew tops it up. And if it ever ran low, the top of the tank would warm first. So you go in head down. Your brain stays cold the longest.
  >
  > It costs at least 220,000 dollars for your whole body, or 80,000 for just your head. That's why most members pay with life insurance. The first man was frozen in 1967. He's still in a tank today. Here's the catch. Nobody has ever been woken up. Not one. The plan is that doctors in the future will know how.
  >
  > Cool to glass, flip upside down, and wait.

- **Comment question:** "Would you do it? Yes or no."
- **Draft camera positions:** the hall, wide → the cooling room → a frosted vial next to a clear, glassy one (the lines about ice
  and glass inside your cells need a picture on the set like this, or a cut: 3.4 Rule 2) → the tank's double wall → nitrogen
  boiling off the top → a crew topping it up → inside a tank, the pods head down → the oldest tank → the hall, wide.
- **Sounds:** the bed is a quiet hall with the soft hiss of boiling nitrogen; a valve, nitrogen pouring, a tank lid, a truck.
- **Demand:** "LIFE AFTER DE@TH? THE CRYONICS HOPE" 6.6M (TrueUpdates, a facts Short), then 58K, 43K and 32K; long videos 1.3M,
  662K and 611K. Smaller than the other four, but open: Zack D. Films has freeze-dried pets (62M) and a morgue freezer (46M), not
  this.
- **Checked ✔:** Alcor in Scottsdale held 234 patients in Oct 2024 (another count says 248); they are stored head down, so the
  head is the last part to warm if the nitrogen runs low; liquid nitrogen at about −196 °C (−320 °F) boils off and the tanks are
  topped up; cryoprotectant and vitrification instead of ice; minimums of $220,000 for the whole body and $80,000 for the head
  alone (older figures: $200,000 and $80,000); most members pay through life insurance; James Bedford, frozen on 12 Jan 1967, is
  still at Alcor; nobody has been revived.
- **⚠ before Gate A:** "They don't even plug in" (one source says no electricity is involved: confirm on Alcor's own pages); the
  current prices and patient count.
- **Watch out:** death and bodies: sealed pods only, no faces; the first man is not named, and no company name or logo appears on
  screen. Keep it a bet, as the script does ("Nobody has ever been woken up").

**Fortress stories (added by the user on 18 Nov 2026): F1–F3**

- **The brief** (the user, 17 Nov 2026): "give me 3 creative video ideas inspired by this
  https://www.tiktok.com/@net.files6/video/7708777568689868064 … it doesn't have to match the length or animation style. I want
  stories similar to this". The reference is NET FILES' "How Ancient Engineers Built An Almost Impossible To Conquer Mountain
  Fortress 😱" (7.9). On 18 Nov 2026: "add these video ideas into claude.md without removing the other ones in section 2. update
  the copy and paste prompt accordingly and label the new renewed date".
- **What the three have in common** (the reference's three moves, 7.9): a defense puzzle, in which every "But" is a way an enemy
  (or thirst, cold or hunger) could beat the place and every "So" answers it; the place named only at the end ("This is ___."),
  with a title that hides it, as NET FILES' biggest fortress videos do; and one line on what became of it. Each is a real
  fortress with a twist at the end and one place that can be cut open, and no Short found tells its story (7.9). None is in NET
  FILES' 276 videos, and Zack D. Films has none of them.
- **What the user saw and added:** for each idea, the title, the place revealed at the end, the opening (a cold claim, then "If
  you…"), the story as numbered beats, the ending line, the set, the competition, the comment question and the ⚠ items, as
  written below. There is no full script yet: write it at Gate A from the opening, the beats and the ending (3.3 Step 1). The draft
  camera positions and the sounds are my notes for Gate A.
- **Rules for these ideas** (on top of sections 1 and 5, and rules 1 and 3–6 of the X list above):
  1. **Keep the name for the end.** The title, the TikTok caption and the narration don't name the place until the reveal line,
     just before the loop ending ("This is the Rock of Gibraltar. Dig in, aim down, and never leave."). People in the story can
     be named (Churchill, Fleming); the place can't. The cover can show the place, but not its name. NET FILES puts the name on
     screen as a big title card; our look has no labels (3.4), so the reveal is spoken and carried by the one-word captions. Ask
     at Gate A whether to allow one name card as an exception.
  2. **Every "But" is an attack, every "So" is a defense.** Write each problem as a way in (from above, through the gate, by sea,
     by thirst, by cold, by hunger) and each fix as the answer, at its own spot on the set, so the camera flies from the attackers
     to the fix and back (3.4 Rules 2 and 3).
  3. **The fate line is one sentence**, after the name: how it fell, or that it never did.
  4. **Armies are small and anonymous:** small soldier figures, ships, cannons and fire are fine; nobody is shown hurt; no faces
     of real people; no flags, coats of arms or wartime insignia on screen.
  5. **Time passes on the one set.** F1 and F3 span centuries (1779 to 1997; the 1600s to 1945): show the jump with the set
     changing (new tunnels, a new grade, the city around it), never a cut to another place.
  6. These sets have water in them (the sea, a river and moats; a moat at the foot of F3's hill), so the STYLE line's
     translucent cyan water stays, but keep it to the sea, the river and the moats, never inside walls or floors (3.4l, 3.4m).
  7. ✔ was checked by web search on 17–18 Nov 2026 (search summaries; en.wikipedia.org could not be opened in that session);
     ⚠ still needs checking before Gate A.

**F1. Why This Rock Has More Tunnels Than Roads** (a siege and a secret: the Rock of Gibraltar, 1779 to 1997; named at the end)
- **Set:** the Rock sliced open lengthwise like a cake: the cliff of the north face with cannon windows cut into it and the
  galleries behind them, the reservoirs and the WWII city (hospital, power station, bakery) inside, the hidden room near the top,
  the east slope covered in metal rain-catching sheets, the flat sand at its foot with the siege lines, and the sea with the
  floating gun platforms. The camera climbs from the siege lines up the cliff and flies through the rock.
- **Opening:** "This rock has nearly twice as many miles of tunnels inside it as roads outside. If you hold the rock at the gate to
  the Mediterranean, every navy in Europe wants it."
- **Story** (as shown to the user):
  1. In 1779 Spain and France surround you: 40,000 men against your 7,000, dug in on the flat sand below your cliff.
  2. But your cannons sit on top of the cliff and can't aim down at its foot. So you dig into the cliff by hand, and the hole you
     blast for air becomes a window for a cannon. These are the Great Siege Tunnels.
  3. But they come by sea, in floating gun platforms built to shrug off cannonballs, with water pumped through them to put out
     fires. So you heat your cannonballs in furnaces until they glow red, and the platforms burn.
  4. You hold out for 3 years and 7 months, the longest siege in British military history, and you never stop digging.
  5. But a rock has no rivers. So you cover a whole slope in metal sheets to catch the rain, and pipe it into reservoirs carved
     inside the rock.
  6. In World War II you dig a whole city in there: a hospital, a power station, a bakery, and food for 16,000 men for 16 months.
     The tunnels reach 34 miles.
  7. Twist: if the rock ever fell, six volunteers would be walled into a secret room near the top with supplies, to watch enemy
     ships for a year. Ian Fleming, who later wrote James Bond, helped plan it. Germany never came, the room was sealed, and
     cavers found it in 1997.
  8. That's why: legend says that if the monkeys leave, the British leave, so in 1944 Churchill ordered more monkeys. Europe's
     only wild monkeys still live on the rock.
- **Ending:** "This is the Rock of Gibraltar. Dig in, aim down, and never leave."
- **Comment question:** "Would you volunteer to be sealed in for a year? Yes or no."
- **Draft camera positions:** the rock and the sand, wide → down to the siege lines → the cannons on top, looking down the cliff
  → inside the cliff as the tunnel is cut and the air hole opens → out over the sea to the floating platforms → the furnaces and
  the red-hot shot → the platforms burning → the rain slope → the reservoirs inside → the WWII hospital and bakery → up to the
  hidden room and its slit → the monkeys on the summit → the rock, wide.
- **Sounds:** the bed is wind on a high rock with the sea far below; cannon fire, picks and a blast in the tunnel, a furnace roar,
  burning timber, rain on metal sheets, a heavy door sealing shut.
- **Demand** (17–18 Nov 2026): Shorts on Gibraltar's tunnels top out at 3K (one of them, "How a Rock Becomes Gibraltar", 2.7K, is
  a copy of our format); the secret room has Shorts of 60K, 23K, 7.7K and 6K; a long video on it, "Buried Alive: The Secret WWII
  Bunker Hidden Inside Gibraltar" (Calum), has 1.9M, and "Why Britain Built This Secret Underground City" 253K. Nobody has cut
  the rock open. Zack D. Films: nothing on Gibraltar or Operation Tracer.
- **Checked ✔:** about 34 miles (55 km) of tunnels, nearly twice the road network (29 km of roads in 2007); the Great Siege, 24
  Jun 1779 to 7 Feb 1783, three years and seven months, the longest in British military history (Gibraltar Museum), with 7,000
  defenders against 40,000 French and Spanish troops; the tunnel dug by hand from 25 May 1782 (Sergeant-Major Henry Ince's plan)
  to cover a blind angle the guns on top couldn't reach, an opening through the face turned into a gun window, and four guns in
  the Upper Gallery by the end of the siege; the floating batteries of 13 Sep 1782, with water piped through them against hot
  shot, set on fire by red-hot shot heated in furnaces; rain caught on corrugated iron sheets over the east-side sand slope and
  channelled to reservoirs cut inside the Rock from 1898 (5 million imperial gallons each), the catchments retired in the 1990s
  for desalination; the WWII tunnels held a hospital, a power station, a bakery, water distillation and a telephone exchange, room
  for the 16,000-strong garrison and food for 16 months; Operation Tracer: six men (a leader, two doctors and three wireless
  operators) to be sealed into a hidden chamber to report enemy shipping if the Germans took Gibraltar, expected to stay about a
  year with stores for seven, never used, the cave found by the Gibraltar Cave Group in 1997 and confirmed in 2008 by the last
  surviving member; the legend of the macaques, and Churchill's directive of 2 Sep 1944 to keep their number at 24.
- **⚠ before Gate A:** the order of events at the first gun window (sources differ on whether the opening was cut for air or for
  the gun); how many floating batteries burned, blew up or were scuttled; Ian Fleming's part (sources credit him with the
  stay-behind idea, and Admiral Godfrey is also named as its originator); that the hidden room is near the top and had a slit
  for watching ships; "Europe's only wild monkeys"; "at the gate to the Mediterranean" is our wording for the Strait.
- **Watch out:** WWII: no swastikas or German markings, and nobody shown hurt in the siege; the platforms burn, their crews are
  not shown. Churchill and Fleming are named, not shown.

**F2. This Castle Beat an Army. Then Its Own Guards Sold It.** (a medieval castle with a twist: Malbork, Poland, 1410 and 1457;
named at the end)
- **Set:** the red-brick castle on its river, cut open from the water to the tallest tower: the three castles in a row with the
  moats and gates between them, the cellar furnace under the palace with its chamber of stones and the hot-air ducts up to the
  floor vents, the summer hall with its single pillar and the stone ball in the wall above the fireplace, and the front gate. The
  camera dives from the moat into the cellar and rises through a floor vent into the hall.
- **Opening:** "This castle beat an entire army. Then its own guards sold it. If you need a fortress where there's no stone, you
  build it out of brick. Lots of brick."
- **Story** (as shown to the user):
  1. You build on a river, so water guards one side.
  2. But walls can be climbed. So you build three castles in a row, each behind its own moat and gate. If one falls, the next
     keeps fighting.
  3. But winter freezes a stone hall. So you hide a furnace in the cellar that heats a chamber of stones, and hot air rises through
     holes in the floor that open and close with lids. In an 1822 test it warmed a hall from 43 °F to 72 °F in 20 minutes.
  4. In 1410 the knights lose the Battle of Grunwald, one of the biggest battles of the Middle Ages, and the winners march straight
     to your walls.
  5. Your weak spot is the summer hall, whose whole roof stands on one pillar. Legend says the attackers fired a cannonball at it
     while the knights met inside, and missed. That's why a stone cannonball is still stuck in the wall above the fireplace.
  6. After two months, the army gives up and goes home.
  7. Twist: 47 years later the knights are broke and can't pay the hired soldiers guarding the castle. So the guards do what no
     army could: they sell it to the enemy king, who walks in through the front gate.
- **Ending:** "This is Malbork, the biggest castle on Earth. Stack the walls, warm the floors, and always pay your guards."
- **Comment question:** "Who's to blame: the knights or the guards?"
- **Draft camera positions:** the castle on the river, wide → the brick walls rising → along the three castles and their moats →
  down into the cellar furnace → up a hot-air duct and out of a floor vent → the summer hall and its pillar → out to the
  attackers' cannons in 1410 → the ball hitting the wall → the army marching away → the guards at the gate, counting money → the
  king riding in → the castle, wide.
- **Sounds:** the bed is a river and wind on brick; a furnace, a vent lid scraping open, cannon fire, a stone ball striking brick,
  marching feet, coins, a gate opening.
- **Demand** (17–18 Nov 2026): the best Malbork Short has 59K ("The Siege of Malbork Castle"), then 19K, 8.3K and 6.5K; searches
  for the sale ("castle sold by its own guards") and for the 1410 siege return no Shorts at all; long videos: "Malbork Castle: Why
  is it so massive?" 434K, its heating ("What's Below The World's Largest Castle?") 269K, the Battle of Grunwald 2.6M. Zack D.
  Films: nothing on Malbork.
- **Checked ✔:** widely described as the largest castle in the world by land area (Guinness lists it as the largest brick castle);
  the heat-storage hypocaust (a furnace in the cellar heats stones, and warm air rises through floor vents closed with covers),
  with an 1822 experiment in which a hall went from 6 °C to 22.5 °C in 20 minutes (one source); the Summer Refectory's single
  central pillar and, per the castle museum, a stone cannonball set into the east wall above the fireplace that legend says struck
  there in the 1410 bombardment; the 1410 siege, about two months, unsuccessful; the Teutonic Order's unpaid mercenaries (over
  400,000 florins owed by April 1455), who sold or handed the castle to King Casimir IV of Poland in 1457 (sources give 4–8 June
  for his entry); the Order then moved its seat to Königsberg.
- **⚠ before Gate A:** "the biggest castle on Earth" (say "the biggest castle in the world by area", or drop it); "where there's no
  stone"; the three castles in a row, each behind its own moat and gate; the price (190,000 Hungarian florins in one source); the
  1822 test (one source); the traitor in the cannonball legend (a travel blog only, so the story leaves the traitor out); whether
  it was a sale, a pledge or a seizure (sources differ, so "sell it" needs a check).
- **Watch out:** no flags, coats of arms or the Order's crosses painted large on screen; nobody shown hurt; the guards and the king
  are small and anonymous.

**F3. Why This Castle Was Built Like a Maze** (castle design and a survival story: Himeji Castle, Japan; named at the end)
- **Set:** the castle's hill cut open like a cake: the white main tower on top, sliced to show its floors and its two great
  pillars; the walls, gates and maze path spiralling up the slope, with gun holes, stone-drop chutes and dead ends; the town and
  the plain around it. The camera follows the maze up the hill, then rises through the floors of the tower.
- **Opening:** "To reach the top of this castle, you have to walk away from it. If you build your castle on a hill in the middle of
  a flat plain, every army can see it and march straight at it."
- **Story** (as shown to the user):
  1. So you turn the path into a maze. It winds and doubles back, so a 430-foot walk becomes more than 1,000 feet, and attackers
     heading for the tower get led away from it.
  2. But they'll rush the gates. So no gate opens straight in, and every one forces a turn right under your walls.
  3. The walls get holes shaped like circles, triangles and squares for guns and arrows, and chutes at the corners to drop stones
     on anyone climbing.
  4. From outside, the main tower looks like five floors. Inside there are seven.
  5. You build all this for a war that never comes, and no army ever lays siege to it.
  6. Twist 1: in 1871 the castle is auctioned for 23 yen to a man who plans to tear it down. Tearing it down costs too much, so it
     stays.
  7. Twist 2: in 1945 bombers burn most of the city around it. Workers cover the white tower in black nets so it won't shine at
     night, and locals say a firebomb landed on the top floor and never went off. That's why it's one of only twelve original
     castle towers left in Japan.
- **Ending:** "This is Himeji Castle. Bend the path, hide the floors, and let them get lost."
- **Comment question:** "Could you find your way to the top? Yes or no."
- **Draft camera positions:** the hill and the plain, wide → the first gate → along the maze path as it doubles back → a gate
  forcing a turn → a wall's gun holes from inside → a stone-drop chute at a corner → the tower from outside (five floors) → rising
  through it inside (seven) → the auction in the courtyard → night, 1945: the city burning, the black net → the dud on the top
  floor → the castle, wide, by day.
- **Sounds:** the bed is wind over a hill with birds; footsteps on gravel, a heavy gate, a stone sliding down a chute, an
  auctioneer's gavel, planes overhead, fire, a dull thud and then quiet.
- **Demand** (17–18 Nov 2026): Himeji Shorts are travel clips (best 39K, then 21K, 18K and 17K); the bomb story has four Shorts of
  about 1K ("A bomb hit this castle in 1945… and never exploded"); the defences have one long video, "What Made This Samurai
  Castle Impossible to Invade?" (BBC Timestamp) 53K; no Short found on the auction. Zack D. Films: nothing on Himeji.
- **Checked ✔:** the winding approach that doubles back, about 325 m of walking for about 130 m in a straight line from the Hishi
  Gate to the keep (MLIT, Japan's tourism texts); gates that don't open straight into the compounds; loopholes shaped as circles,
  triangles, squares and rectangles; chutes for dropping stones; the main keep looks like five storeys from outside and has six
  floors and a basement inside; auctioned for about 23 yen after the domains were abolished, to a Himeji man who meant to pull it
  down but found it too costly; a raid in July 1945 destroyed about 63% of the city's built-up area, and a black camouflage cover
  was put over the keep (MLIT); MLIT calls the firebomb that landed and didn't go off a local story.
- **⚠ before Gate A:** "no army ever lays siege to it": History Hit says it was never besieged, but MLIT says forces from Bizen
  stormed Himeji in 1868 and forced its surrender, and others say they surrounded it and fired warning or blank shots (if needed,
  say "it never fights a real siege"); the auction year (1869, 1871 or 1873 by source) and price (23 or 23.5 yen); "one of only
  twelve original castle towers"; the walk in feet (130 m is 427 ft, 325 m is 1,066 ft); the firebomb is told as a local story,
  as the story does ("locals say").
- **Watch out:** no Japanese or American flags or insignia on screen; the bombers are distant shapes, and nobody is shown hurt;
  the auction buyer is not named.

**Not in the list (16 Nov 2026, added to on 18 Nov 2026): topics not to propose again without a new reason**
- **Fortress stories already told on Shorts** (checked 17–18 Nov 2026 and dropped before the user saw the three; the user saw the
  first four named as dropped): Château Gaillard taken through its toilet ("The Castle That Fell Through Its Toilet" 124K,
  "Medieval Castle Toilets Became Secret Entrances" 144K, a 3D "ancient engineering" Short of it, and three more videos on it in
  the week before); Mont-Saint-Michel's siege ("Why England Couldn't Conquer This Island for 30 Years" 655K); Sigiriya's king who
  lost when his elephant turned ("A Palace 200 Meters Above the Ground—And a King's Fatal Mistake" 208K, with AI build Shorts at
  224K and 514K); Janjira, the sea fort nobody conquered (a Hindi 3D animation of the story 1.7M, "How Is There Sweet Water Inside
  Murud Janjira Fort?" 858K). Also checked, with small copies of our format already out: Krak des Chevaliers ("How to Build a
  Castle No Army Can Take 🏰 Krak des Chevaliers" 10K), Harlech ("You build Harlech 🏰 Wales, 1286" 9.7K), Kenilworth's siege
  lake (18K, 12K, 8.7K), Fort Jefferson ("…Built With 16 Million Bricks…" 10K); Suomenlinna's surrender of 1808 is open but has
  little demand (best Short 5.2K). The details are in 7.9.
- **Proposed the same day and turned down as a set (all water):** the pool on the edge of Victoria Falls (IShowSpeed's swim 58M,
  Jan 2026); the world's deepest pool, in Dubai (real dives 56M, 32M, 25M and 25M); the slot-canyon flash flood (5.5M); the
  Qiantang tidal bore (64M, 16M, 12M); and the hole in the lake at Monticello Dam (best Short 926K, with four small copies of the
  "fall in" hook). One of them could come back in a mixed list, never as a set. Their checked facts are in 7.8.
- **Already made by Zack D. Films** (checked 16 Nov 2026; his views): falling off a cruise ship (50M; the user's example),
  falling through ice (64M), a grain bin (57M), an avalanche (39M), a tar pit (7.9M), sinkholes (4.8M), a plane losing oxygen
  (25M) and its oxygen masks (21M), straightening the Leaning Tower of Pisa (18M), a power line on your car (56M), the woman hit
  by a meteorite (24M), the microwave's metal screen (10M) and ice in a microwave (16M), and the gold vault under Manhattan (17M).
  Taken by others: quicksand (29M, 20M), Niagara Falls in a barrel (18M), the Thai cave rescue (62M), opening a plane door in
  flight (30M), Lake Nyos (14M).
- **Weak on Shorts** (16 Nov 2026): Apollo 13's duct-tape filter (best 2.5K), stalling on a railroad crossing (91K), the salt
  mine under Detroit (188K), the deep mine cooled with ice (32K), why oxygen-mask bags don't inflate (34K). Coober Pedy's
  underground homes (494K; a long video 5.2M) is open but small.
- **Don't propose unless the user asks:** a race car driving on the ceiling ("I don't like p5", 14 Nov 2026); landing a jet on an
  aircraft carrier (swapped out on 15 Nov 2026).
- **Earlier lists** are in the repo history: the ten famous places of 11 Nov (commit `92a077a`), the matchups of 14 Nov
  (`c37181e`) and the Cutaway list of 15 Nov with its reserves (`45b7846`). Topics found crowded on Shorts before 16 Nov:
  escaping a sinking car (31M, 25M, 23M); undersea internet cables; train wheels as cones; airplane toilets; why McDonald's Coke
  tastes different; New York's street steam; Tokyo's flood tunnel; tsunami builds and how to survive a tsunami; the Fudai
  floodgate; oil-well fires; the Kola borehole; the Costa Concordia salvage; the Persian yakhchal; Biosphere 2; escaping a sunken
  submarine; Kansai airport; ice roads; Machu Picchu's underground; Cheyenne Mountain; the Chile miners; floating bridges; the
  Hanging Temple; Ski Dubai; Troll A; and, as builds, castles, the Panama Canal, wells, cave homes, lighthouses, the Hoover Dam,
  bank vaults, pyramids and cranes (6.3).

---

## 3. Production runbook (for Claude: follow this exactly when asked to make a video)

> Trigger phrases: "make video #N", "produce the [topic] video", "run the runbook on [topic]".
> **Never generate anything (images, clips, audio) before Gate B is approved.** Script and planning work is free.

### 3.0 Tools and verified prices (checked 7 Nov 2026 with `get_cost:true`; re-check, prices change)
| Job | Tool / model | Settings | Credits |
|---|---|---|---|
| Style key and stage stills (no character sheet since 15 Nov 2026) | Higgsfield `generate_image` / `generate_image_batch`, `seedream_v5_pro` | `resolution:"1k"`, `aspect_ratio:"9:16"` | **1.25 / image** |
| Cheap draft image (optional exploration only) | `gpt_image_2_6` | 9:16 | 0.25 / image |
| Animated shots (default since video 04) | `generate_video_batch`, **`kling4_0`** | `mode:"image-to-video"`, `resolution:"720p"` (it also offers `"1080p"`, which is its default: price both at Gate B, 3.3 Step 3), `aspect_ratio:"9:16"`, `duration` 3–30 s, `start_image` + `end_image` to travel from one picture to the next; ordered middle frames go in `image_references` (works: video 08, 3.4k) | **2.25 / second at 720p** (3 s = 6.75, 4 s = 9, 5 s = 11.25); **3.25 / second at 1080p** (checked 15 Nov 2026; not used yet) |
| Animated shots (optional) | `minimax_h3` | `resolution:"2K"`, `aspect_ratio:"9:16"`, `duration` 4–15 s | **2 / second** (4 s = 8, 5 s = 10); every queued job failed in videos 01–04 (3.4f) |
| Narration (preferred) | ElevenLabs connector `creative_generate_speech` | voice from `creative_list_voices` | ElevenLabs credits (0 Higgsfield) |
| Narration (fallback) | Higgsfield `generate_audio`, `text2speech_v2`, `variant:"elevenlabs"` | locked `voice_id` + `voice_type` | ~0.45 / line |
| Word timing, labels, captions, assembly | Higgsfield `sandbox_exec` (ffmpeg, faster-whisper, Pillow preinstalled; `$HF_WORKFLOWS/video-montage/scripts/audio_to_captions.py`) | — | no generation credits (confirm in `transactions` after the first run) |
| Sound bed and effects (approved 15 Nov 2026: 3.4, 3.3 Step 6b) | ElevenLabs connector: `creative_create_flow`, one `creative_add_flow_node` per sound (`node_type:"sfx"`, `model_id:"eleven_text_to_sound_v2"`, `model_parameters` `duration_seconds`, `loop`, `prompt_influence`), then one `creative_run_flow_nodes` for all of them | `estimate_only:true` first, then `generations_count:1` (the default is several and the cost scales). Recipe in 3.3 Step 6b | ElevenLabs credits: **about 3.33 per second of sound** (video 08: a 20 s bed 66.67, six effects of 1.5–4 s 5–13.33 each, 118.33 in all) |
| Checking a finished video | `pipeline/analysis/check_video.py` (share of seconds that move, caption size, sharpness), `camera_path.py` (how the camera moves: zoom, pan, 3D travel, big moves, still-camera stretches; 3.4 Rule 7), `under_the_voice.py`, `contact_sheet.py` | local, needs ffmpeg, numpy and opencv | free |
| Optional | `virality_predictor`, `tiktok_prepare_publish` (UPLOAD_TO_DRAFT) | — | ask before using |

Rejected alternatives at 10 s / 9:16: seedance_2_5 720p = 70, seedance_2_5 480p = 30, kling_4_0_flash = 30, kling4_0 720p = 22.5, seedance_2_0 720p = 45, grok_video_v15 = 45. `minimax_h3` is the cheapest and supports `start_image` + `end_image` keyframes, which is how we animate "the structure upgrades on screen".
Since video 04 the default is `kling4_0`: it also takes `start_image` + `end_image`, accepts 3 s clips, and has not failed a job, while every queued
minimax job has failed (3.4f). Prices re-checked 10 and 11 Nov 2026 with `get_cost`: unchanged.

Balance when this runbook was written: **604 credits (Plus plan)**. On 11 Nov 2026 the account moved to the **Ultra plan**: 3,000 subscription
credits (the 61.13 left were reset). 15 Nov 2026: 2,508 credits left before video 08, 2,304.50 after it, 2,040.25 after video 09.
17 Nov 2026: 1,762.25 after video 10. Always call `balance` at the start of a run.

### 3.1 Budget tiers (pick one at Gate B; default = Middle since video 05)
| Tier | What gets animated | Est. credits per 60–70 s video |
|---|---|---|
| **Lite** | 8 key beats animated with `kling4_0` (3–5 s each). Every other beat uses a still with a slow push-in/pan done free in the sandbox with ffmpeg. | **~105–125** (videos 01, 03, 04 cost 106, 123, 112) |
| **Middle** (default since video 05) | The whole opening, every build, the twist and the whole finale on `kling4_0` (~15 of ~25 beats, 3–5 s each). The other beats (terms, stats, label moments) hold on the build: the last frame of the clip before, or the current stage still, with a free push-in. | **~165–200** (video 05: 176 for 31 stills + 16 clips); **158.75** with the shot rule (video 06: 19 stills + 14 clips, 60 s); **157.25** for the first matchup (video 07: 16 stills + 11 clips, 61 s); **203.50** for the first Cutaway video (video 08: 26 stills + 11 clips, 76 s of clips in a 79.5 s video); **264.25** for the first travelling-camera video (video 09: 35 stills + 18 clip renders, 98 s of Kling for 81 s of clips in a 75 s video); **278.00** for video 10 (37 stills + 22 clip renders, 103 s of Kling for 86 s of clips in a 76 s video) |
| **Full** | Every beat animated (one clip per beat, duration = beat length rounded up, min 4 s) | **~180–210** (17 beats); ~270 quoted for 25 beats (incl. reserve); ~210–230 expected spend with the shot rule (estimate, 7.2) |
All include ~18–25 stills (~23–31 cr), narration (~0–7 cr) and a **15% retry reserve**. Stop and ask if a run will exceed its quoted total by more than 10%.

**Cutaway look (since 15 Nov 2026): Middle is the floor.** Rule 1 of the look (3.4) asks for animated clips over at least about 80%
of the running time: about 60 s of a 75 s video, which is what videos 06 and 07 had (60 s and 61 s of clips). Expect about 160
credits at 720p: the same clip seconds as those two (135–137 credits) plus 15–20 stills. **Measured on video 08:** 203.50, because
a 79.5 s script with clips over 93% of it needed 76 s of clips (171.00), and the stills took 26 tries (32.50). **With the travelling
camera (15 Nov 2026, 3.4 Rules 1–3)** quote ~215–225 at 720p for a ~78 s video: every line is a clip (about 78–80 s, ~175–180
credits), and the 8–12 camera positions need 20–24 stills on screen at ~1.8 tries each (~45 credits). **Measured on video 09:**
264.25 for a 75 s video: 35 still tries (43.75) and 98 s of Kling (220.50), because the clips are planned slightly longer than
their lines (81 s for 75 s) and three of 16 went wrong (17 s of re-renders, 3.4l). Quote ~235 + 15% (~270) for the next one.
**Measured on video 10:** 278.00 for a 76 s video, against a 280.60 quote: 37 still tries (46.25, 1.6 each) and 103 s of Kling
(231.75), because the clips were planned 86 s for 76 s and three of 19 were rendered again (18 s, the floor leak of 3.4m). Quote
~245 + 15% (~280) for the next one, and put the floor line in every indoor clip prompt from the start. Lite left two thirds of
videos 03 and 04 as still pictures (7.5), so offer it only when the balance cannot cover Middle, and name the lines that would be
stills. In this look a line without its own clip is only a fallback (3.2 rule 5): it holds the last frame of the clip before it, for
3 s at most, and never becomes a still of its own.

### 3.2 Credit rules (hard)
1. Script, beat sheet, prompts and the cost quote are free. Do them all first.
2. Before Gate B, add up the exact plan with `get_cost:true` (one call per distinct model/duration combo), multiply out, add 15% reserve, show the total, and wait for approval.
3. Images before video. Fix look, consistency and drift in stills (1.25 cr), never by re-rolling clips (8–20 cr).
4. Pilot first: render only 2 clips (the hook and one build beat) and show them before the batch.
5. `count: 1` always. No variants. Regenerate a failed or bad clip **once**, with a corrected prompt. If it fails again, fall back to the still with ffmpeg motion and say so. (Cutaway look: fall back to holding the last good frame, 3 s at most, and tell the user which line lost its clip; a still of something in motion is not a fallback.)
6. Clip `duration` = beat length rounded up to whole seconds (min 3 on kling4_0, 4 on minimax_h3). Never generate 10 s for a 4 s beat.
7. Never use `use_unlim` unless the user asks. Never auto-retry after a transport timeout; check the job id first.
8. After the run, call `transactions` and report the actual spend against the quote.

### 3.3 Step-by-step

**Step 1: Topic and script (free).**
- Take the idea the user names: X1–X4 or F1–F3 in section 2 (X5 was made as video 10), or their own topic. An X idea brings its
  set, a draft script the user approved with the idea (a cold claim, then "If you…"), the comment question, draft camera positions
  and the facts already checked (✔) or still to check (⚠); the script is a draft. An F idea (added 18 Nov 2026) brings the same,
  except that in place of a script it has an opening, the story as numbered beats and an ending line: write the script from them,
  keeping the place's name for the reveal line at the end (section 2, F rules 1–3). Write the script with the formula
  and writing rules in section 1 and the script rules in the section 5 prompt. Target ~75 s, ~260–280 words; never under 60 s.
- Write for the set (3.4 shot rule): every line must be something the viewer can see happen on the one cutaway set, and most lines
  should describe something moving, because every such line gets an animated clip (3.4 rule 1). Comparisons, stats and the "that's
  why" are shown on the set itself or cut; the Cutaway look has no labels. Cut any line that would need a picture of another place.
  At Gate A, list the lines that were cut and the lines that were moved onto the set.
- **Write for the camera** (3.4 Rules 2 and 3, 7.7): put each problem and each fix at its own spot on the set, so the camera has
  somewhere to fly on every "But" and "So" (the power-lines video reaches a new spot every 5–10 s). Two lines at one spot are fine;
  three in a row read as a still shot. At Gate A, show where the camera is on each line next to the script.
- Run the saturation check on the title (`pipeline/youtube/yt_saturation.py`, 6.7) and report near-identical Shorts and the best views.
  Search the exact title, "how a [thing] becomes [place]" and "[place] how it was built": in video 06 only the second found the 27K
  near-identical build (3.4h).
- Fact-check every ⚠ claim with web search before locking. Remove anything unverifiable.
- Show the script. **GATE A: user approves the script.**

**Step 2: Beat sheet (free).**
- Split the script into beats, one sentence or one "But/So" unit each (usually 14–18 beats).
- For each beat, write: `beat_id | VO text | est. seconds (words ÷ 3.5) | shot type (problem / build / twist / aside / climax / payoff / end) | camera (its position, and the move to the next) | start picture → end picture | what moves | pointer (arrows or ring, if any) | sound effect (if any) | clip`. In the Cutaway look every beat is a clip; plan no holds (a hold is only the fallback for a lost clip, 3.2 rule 5; 3.4 rule 1). A beat in which nothing can move is a sign that the line should be cut or merged with its neighbour.
- Define the **stage ladder**: an ordered list of how the structure looks after each fix (Stage 0 = bare ground → Stage N = finished build). Each build beat moves from stage k to k+1.
- **Every beat shows the build** (3.4 shot rule): one of its camera positions, at the current stage. Problems hit the build where the
  camera sees them up close (the storm over it, the water pouring in). If the build itself has to move to a new setting, give that
  setting its own wide view and continue the ladder there.
- **Plan the camera path** (3.4 Rules 2, 3 and 7; 7.7), like the power-lines video:
  - **8–12 camera positions on the one set:** the wide view to open, to close (the loop) and to step back once or twice; the rest
    close, low, from the side or looking up, each where a problem or a fix happens. Each position is a real still (Step 5), never a
    crop of another still: a crop makes Kling zoom across a flat picture, which `check_video.py` and `camera_path.py` read as still
    (3.4k).
  - **The rhythm:** on "But" the camera pushes in or swoops to where the problem happens; the problem and the fix play out close,
    with the camera still drifting (a slow push, slide or turn of a few percent a second); on "So", or once the fix is done, it pulls
    away or flies on to the next position. Plan a big move (a quarter of the frame or more in a second) at least every 8 s on
    average and never more than 15 s apart, and never a still camera for more than 5 s (3.4 Rule 7).
  - **Name each move** in the camera column: swoop down, rise, push in, pull away, fly along, orbit, drift, whip. A whip is a fast
    swing with motion blur for a far jump on a "So" line (the power-lines video has one at 0:17): ask Kling for it in the travel
    clip, or make it in the edit between two clips. No fades, and a hard cut only where the setting truly changes.
  - **Make what moves big:** frame each change so it fills a good part of the picture (the haze filling the room, the water rushing
    through a pipe that is big on screen).

**Step 3: Cost quote. GATE B.**
- `balance`, then `get_cost:true` per model/duration combo, then the total plus reserve.
- Price Kling at 720p and at 1080p (`get_cost:true` for each) and show both totals; the user picks. Our 720p clips carry about half
  the fine detail of the stills they sit between (7.5).
- Price the sound bed and the effects as well: add their nodes to the flow and run `creative_run_flow_nodes` with
  `estimate_only:true` and `generations_count:1` (Step 6b; about 3.33 ElevenLabs credits per second of sound).
- Price the narration too: `creative_generate_speech` with `estimate_only:true` shows the ElevenLabs cost and any quota block. In video 05 one
  take of a 272-word script cost 1,368 ElevenLabs credits, the plan had 354 left, and the first try failed until the user upgraded.
- Present: tier, number of camera positions and stills, number and length of clips, total credits, remaining balance after.
- **Wait for approval.** Nothing below this line runs without it.

**Step 4: Project and style lock.**
- `get_preferences`; if asked or preferred, `create_project` named after the video and reuse its `folder_id` on every generation.
- Write the **STYLE FORMULA** once and paste it byte-identical into every image and video prompt. **Cutaway default (video 08 used it with the composition sentence inside; since the travelling camera, 15 Nov 2026, that sentence is the separate WIDE line below):**
  > "Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent cyan water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark."
- **WIDE**, only in the prompts of wide shots (the opening, the ending and the step-backs): "Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail ground." Close-ups and low angles leave it out (3.4 Rule 5). The STYLE says "Bright soft daylight", so night edits need `NIGHT` from `08-prompts.py` (3.4k).
- **The shared line names no objects and no place** (3.4 rule 4). In video 04 the words "blue-painted pumps" in it put pumps under the kitchen sink, under three glasses and on the seabed. One SET line per video carries the place and its colours (name colours, not objects: 3.4g). A prop goes in the prompt of the shot that needs it.
- **No character** (3.4). Hands, small anonymous workers or machines appear only in the shots that need them and are described in that shot's prompt. Every other still and clip prompt ends "No people, no characters" (Kling invents figures otherwise: 3.4d).
- Generate the style key: the wide opening view of the set at Stage 0, 9:16. `jobs_wait`, then `show_generation_by_ids`. If off-style, regenerate once.
- (Classic look, videos 01–02 and 05–07, for the record: the game-engine STYLE string in `pipeline/02-prompts.py`, the locked mascot as a second reference image, and a 2:3 mascot sheet generated with the style key.)

**Step 5: Stage stills (~1.25 cr each).**
- **Camera positions** (3.4 Rules 2 to 4): for each position in the camera column, one 9:16 still of the SAME set from that position, made by editing the wide still (or a neighbouring position already made; pass it as `medias` role `image_references`). Name the new camera position and hold everything in view: `[STYLE FORMULA] The same [set] as the reference, with the same parts, colours and materials. New camera position: [where the camera is, how high, which way it looks, what fills the frame, e.g. low and close at the kitchen sink, looking at the U-bend from the front; the U-bend fills the middle third of the frame]. Nothing in view changes.` "Extreme close-up: the [part] fills most of the frame" works where "close-up of" alone gives a wide shot (3.4f). Video 08's flap close-up was made this way and was the one position that made the camera fly in depth.
- **Stages at each position:** a change that happens at a position gets its before and after as edits of that position's still, with the framing lock, so the clip that plays the change starts and ends in the same place. Prompt pattern: `[STYLE FORMULA] Same scene and camera as reference. Now [exact change for this stage]. Everything else identical.`
- Night or storm grades are re-grades of the same picture (say "the same water colour as the reference; nothing glows"), made by
  editing the still they grade ("Keep exactly the same camera position, zoom and framing as the reference image"; "Change only
  this: …"; 3.4f, 3.4g). Never make a still of something away from the build. Before Gate C, check that every still is a camera
  position on the one set and that the set matches from position to position: the same parts in the same places, the same colours
  (an AI set drifts more seen from many angles; regenerate the still that drifted). The first and last stills match part for part
  (in video 03 the last frame lost its see-through barrel), and the wide stills keep the subject in the upper 60% of the frame with
  plain ground below it (3.4 Rule 5).
- Submit in batches of ≤12, `jobs_wait` (≤12 per call), one `show_generation_by_ids`. Regenerate drifted stills once. **GATE C: show the stills as a flight map (the camera positions in order, the move between each pair, and the stages at each position); user approves.**

**Step 6: Narration.**
- Preferred: ElevenLabs connector. `creative_list_voices`, pick a calm, confident male or female explainer voice (or the voice locked in 3.4), and generate the **whole script as ONE continuous take** (sounds like the source: fast, even, no pauses). Two takes come back by default; pick one.
- Fallback: Higgsfield `text2speech_v2` + `variant:"elevenlabs"` with the locked voice pair. Never mix voices within a video.
- Pace target: ~3.5–3.8 words/s. If the take is much slower, tighten the script. Never speed-shift audio more than 1.1×.
- Get word timestamps in the Higgsfield sandbox: download the audio with curl, then run faster-whisper (or `audio_to_captions.py --script <manifest> --max-words 1`) so the authored words supply the text and Whisper only supplies the timing. Derive each beat's real start and end. **These timings replace the estimates from Step 2.**

**Step 6b: Sound bed and effects (approved 15 Nov 2026; never before Gate B).**
- What it is (3.4): one quiet, steady bed that fits the place, with no tune, and four to eight short effects on the moments where
  something visibly happens. No music.
- **Working recipe (video 08, 15 Nov 2026), all on one ElevenLabs flow:**
  1. `creative_create_flow` with a name ("HBX 08 sewer trap: sound bed and effects").
  2. One `creative_add_flow_node` per sound: `node_type:"sfx"`, `model_id:"eleven_text_to_sound_v2"`, a `label`, the `prompt`, and
     `model_parameters` `{"duration_seconds": N, "loop": false, "prompt_influence": 0.5}` (`loop: true` for the bed).
  3. `creative_run_flow_nodes` with every node id, `generations_count:1` and `estimate_only:true`; show the price; then the same call
     without `estimate_only`.
  4. Poll `creative_get_flow_run_status` until all are done, then download each result. Never call run again to retry: that
     starts and bills a second generation.
- **Prompts:** short and concrete, naming the sound, its texture and the space; no visual words (the model guide). Video 08's, all
  usable first time: bed "Quiet house interior room tone, soft steady air with a faint distant refrigerator hum, calm and even, no
  music, no voices" (20 s, loop); "Kitchen tap running into a steel sink, water gurgling down a drain pipe, close, clean" (3 s);
  "Toilet flush, close, water rushing down a pipe inside a wall" (3 s); "Sink drain gurgling as the water is sucked out of the
  pipe, hollow glug, close" (2 s); "Small bathroom exhaust fan switching on and whirring steadily, close" (4 s); "Small splash of
  water inside a pipe and a rat squeaking twice, hollow pipe echo, close" (2 s); "Small metal flap swinging shut inside a plastic
  pipe, short hollow clank" (1.5 s).
- **Cost:** about 3.33 ElevenLabs credits per second of sound, so set `duration_seconds` to what the moment needs: the seven above
  cost 118.33, against 350 estimated at the default length.
- **The bed:** one clip of the place's air, looped under the whole video in ffmpeg (`-stream_loop -1`), with a short fade in and
  out. The 20 s room tone came back very quiet (mean −64 dB), so set every level from measured loudness, never a fixed gain:
  `rms_db()` in `08-build.py` takes the RMS of the loud frames of the voice, the bed and each effect on the mono fold-down
  ((L+R)/2, what one phone speaker plays), and the gain puts the bed 19 dB and each effect 11 dB under the voice.
- **Mix in stereo:** the sounds come as stereo files and the voice is mono. Copy the voice to both channels
  (`pan=stereo|c0=c0|c1=c0`) and give every sound `aformat=channel_layouts=stereo` before `amix`, or the mix folds to mono.
- **The effects:** take them from the beat sheet's sound column and place each on the word that triggers it (`at(beat, word,
  offset)` in `08-build.py`, from the Step 6 word timings): the flush 0.25 s before "flushes", the clank just after "drops".
- Check: `under_the_voice.py` on the final; video 08 measured its quietest moments 21 dB under the voice with a steady stereo bed
  (the target 18–22; the reference 19–20).

**Step 7: Pilot clips. GATE D.**
- Render 2 clips with the default video model (3.0; `kling4_0` since video 04): **the hook**, flying from the wide opening view down
  to the first change, and **one travel clip** between two camera positions on a "But" or a "So" (3.4 Rules 2 and 3).
- A middle keyframe (a third picture in `image_references`, between `start_image` and `end_image`) lets one clip pass through three stages: it held the set's shape in video 08 (the 12 s hook went S0 → S0H → S1, and the last clip passed the rat at the flap before pulling back to the house). Use it where one line has three states, or to push in to a change and pull away again in one clip (wide → close → wide).
- **Measure the pilots against the reference** (3.4 Rule 7, 7.7): show each with its `camera_path.py` and `check_video.py` numbers next to the power-lines video's (camera moving in 66% of the seconds, parallax 0.46 px, a big move in one second in four). A pilot that zooms across a flat picture (parallax near 0) fails however it looks: video 08's hook looked right and measured as still. Fix the stills (a real camera position, not a crop) or the move, render it once more, and don't batch the rest until the pilots move like the reference.
- **Travel clip:** `start_image` = the still at position A, `end_image` = the still at position B (different camera positions, not only a different zoom). Prompt: `[STYLE FORMULA] [the move, in the words of the camera column, e.g. The camera swoops down and forward from high above the house to a low, close view of the kitchen sink, passing close to the wall, and slows as it arrives]. [what happens on the way]. Motion starts on frame 1. No people, no characters. No text, no captions.`
- **Change clip** (a problem or a fix at one position): `start_image` = the position's before still, `end_image` = its after still. The camera keeps drifting (a slow push, slide or turn of a few percent a second), never `FIXED`. The prompt describes the change (water rising, a pipe bending, a flap swinging) and the drift. (Classic look, for the record: `The character only gestures and does not talk.` in place of `No people, no characters.`)
- The camera travels around and into the build, never to another place (3.4 shot rule).
- `duration` = the beat's measured length rounded up (min 3 on `kling4_0`); a move between two far positions needs 3–6 s. Show both pilots. If the look fails, fix the stills or prompt, not by re-rolling.

**Step 8: Remaining clips.**
- Batch the rest (every beat marked as a clip in Step 2) in `generate_video_batch` chunks of ≤12, `jobs_wait`, then one `show_generation_by_ids`.
- Check each clip: right stage, no drift, no text artefacts, motion from frame 1, the thing the line describes really moves, and the camera makes its planned move (run `camera_path.py` on the clip: a travel clip with parallax near 0 only zoomed). One corrected regeneration max per clip.

**Step 9: Assembly (Higgsfield sandbox, free).**
- Download all clips, stills and narration into one working folder in a single `sandbox_exec` (use `background:true` for long renders, `size:"xl"` only for the final encode).
- For each beat in order: fit its clip to the beat's measured length (from the Step 6 timestamps; `08-build.py` plays a clip at 0.8–1.15×, and a 3 s clip over a ~2 s line whole at up to 1.7×, `FULLFIT`). Only a line that lost its clip holds the last frame of the clip before it with a slow push-in, for 3 s at most, and the clip after a hold eases out of its zoom (`EASE_AFTER`). Never turn a still of something in motion (a pour, a splash, smoke, a gauge needle) into a shot: it reads as frozen (3.4 rule 1). No cross-fades between different pictures; a whip only for a far jump; a hard cut only where the setting truly changes (3.4 rule 3).
- If the clips are 720p, add a light sharpen after the upscale (start from `unsharp=5:5:0.6` and judge it on a frame) so they sit closer to the stills (7.5).
- Lay the narration on top at full volume, then mix the sound under it (3.4, Step 6b): the bed about 18–20 dB below the voice, with a short fade in and out, and each effect starting about 10–12 dB below the voice. Never copyrighted music. Check the mix with `pipeline/analysis/under_the_voice.py`: the quietest moments should sit about 18–22 dB below the voice (the reference: 19–20 dB; our voice-only videos: 37–42 dB). Keep the voice-only mix as a second master.
- Output 1080×1920, 30 fps, H.264 + AAC. Keep this as the **clean master** (no text).
- Run `pipeline/analysis/check_video.py` and `camera_path.py` on the master, and report both against the targets (3.4 Rules 1 and 7). Inside the picture: 80% or more of the seconds moving (the reference's storm drain and roof score 84% and 87%, the power-lines video 70%; our videos 03, 04 and 08 scored 33%, 33% and 20%). The camera: moving in 65% or more of the seconds, median parallax 0.3 px or more, big moves in at least one second in eight with no gap over 15 s, and no still-camera stretch over 5 s (the power-lines video: 66%, 0.46 px, 22 in 88 s with a longest gap of 15 s, 5 s; video 08: 45%, 0.03 px, 7 in 80 s, 13 s).

**Step 10: Pointers and captions (sandbox, free).**
- **Cutaway look (since 15 Nov 2026): no term labels.** The term is spoken. Nothing is written on the picture except the captions.
- **Pointers** (3.4 rule 6): solid white arrows with a soft dark shadow, about three times the size of the old chevrons (about 200 px long at 1080×1920; the chevron in `04-build.py` is 68 px), three or four at a time, sliding along the flow. One ring where a small part must be found: a stroke of about 16 px (it was 7), fading in. One device per beat, only where it explains the mechanism, and never under a caption. A pointer appears when the camera arrives at a detail and slows (the 1–2 s drift at the end of a move) and stays pinned to the detail: track the picture with the point tracker of `camera_path.py` and move the arrow or ring with it (written for video 09: `POINTERS` and `track()` in `09-build.py`, positions measured on a gridded frame of the rendered segment; 3.4l). The camera never stops for a pointer (3.4 Rule 6).
- **Captions** (3.4 rule 5): one word per cue, timed from the Whisper word timestamps, text from the authored script. ALL CAPS, Montserrat ExtraBold, white fill, 7 px black stroke, soft shadow. Letters about 57 px tall: ASS `Fontsize` 114 with our "HBX Caption" font (Montserrat 800 from fontsource; `CAP_FS` in `08-build.py`). The 130 first written here, scaled from the 44 px letters of videos 03–04 at 100, measured 65 px in video 08, so measure the letters with `check_video.py` whenever the font file changes. Centred at about 75% of the frame height (`CAPY` ≈ 1440): over plain ground in wide shots and over whatever is there in close-ups, where the stroke and the shadow keep it readable, as in the power-lines video (3.4 Rule 5). Long words are fitted to 900 px (`MAXW`). Take the cue timing from `07-build.py`: a short word pushes the next one back, so two words are never on screen together (the 03–04 scripts drew one word half-clipped for two frames).
- Render with an ASS subtitle file through ffmpeg/libass (the bundled `subtitle_paper_burn.py` only places captions at the bottom). Use the bundled scripts for transcription only.
- Verify: duration matches the master within 0.2 s, every script word appears exactly once, and 3 spot frames (start, middle, end) show the right word, readable over the picture. Inspect them with `image_paths`. `check_video.py` also prints the caption letter height and position.
- **Fallback:** if the caption burn fails, deliver the clean master plus an `.srt` of one-word cues, and the user captions it in CapCut (one-word preset).
- (Classic look, videos 01–02 and 05–07, for the record: ALL CAPS term labels near the subject, dashed dimension lines, and Title Case captions in Fredoka Bold centred at ~52% of the frame height, 64–72 px at 1080 wide.)

**Step 11: End card and delivery.**
- Final beat: the finished cutaway in the framing of the first frame, so the last line loops into the hook. No character and no sign (3.4).
- Upload the final MP4 to Higgsfield storage (`media_upload` → PUT in the same `sandbox_exec` → `media_confirm`) and give the user the link.
- Report: final length, credits quoted vs spent (`transactions`), the share of seconds that move and the camera numbers (Step 9), and any line that lost its clip.
- On the first video with sound, deliver the voice-only version too, so the user can compare the two by ear (3.4).
- Only if asked: `virality_predictor` (ask about cost first), then `tiktok_prepare_publish` with `mode:"UPLOAD_TO_DRAFT"` (the user always reviews and submits).

**Step 12: Post copy (free).**
- TikTok: the idea's title or a hook question with one emoji, then `#HowItWorks #Engineering #LearnOnTikTok #3DAnimation` and 1–2 topic
  tags (video 04's pattern, 3.4f). The `social-media-skills:caption-writer` and `hook-writer` skills can help with alternates.
- **TikTok hashtags must register as hashtags** (18 Nov 2026): from video 02 on, none of the tags in our captions did (6.10), most
  likely because the caption was pasted. Tell the user to type each tag in the app, or pick it from the suggestion list, and check
  that it shows as a link before posting.
- **YouTube Shorts gets its own copy:** follow the upload checklist in 6.4 (a title in the idea's form: the question the video
  answers, `How a ___ Becomes ___` or `If You…`, with no hashtags or call to action; a written description; audience set to "not
  made for kids").

### 3.4 Locked choices (fill in after the first video and keep them for every video)
- Narration voice (LOCKED): ElevenLabs connector, model `eleven_v4`, voice "Daniel's Voice - Warm, Low, Confident" voice_id `rFhx8PVgXxOyaeAGq9fq`. Raw take runs ~3.2 words/s; tighten pauses to 0.15 s (timing.py) to reach ~3.5 words/s. The user upgraded the ElevenLabs plan on
  11 Nov 2026 after the 10,000-credit quota ran out mid-run.
- **Mascot (retired from the videos on 15 Nov 2026; kept for the channel artwork and for the record):** "a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, brown work boots, short dark beard, simple friendly face, game-character proportions". Higgsfield reference image: job_id `f97004b9-f63f-4971-ab16-e0519314a404` (seedream_v5_pro, 2:3). He is in videos 01–02 and 05–07. Don't put him in a new video unless the user asks.
- End card: no sign (the user chose none). End on the finished cutaway in the framing of the first frame. (Classic look: the mascot waving at the finished build.)
- Default tier: **Middle** (the user, 11 Nov 2026: "lite isn't enough animation and full is too much"; they picked Middle B, 15 clips,
  ~170–200 credits). In the Cutaway look Middle is the floor (Rule 1 below, 3.1); offer Full when the beat count calls for it.
- **Look (LOCKED by the user, 15 Nov 2026): Cutaway, no character, with a travelling camera.** It is the look of videos 03–04
  (then called Hidden By Design) with the six refinements the user approved on 15 Nov 2026 ("all 6 refinements are approved"; the
  measurements and the reasons are in 7.5). After video 08 the same day, the user asked for the camera to move in and away from the
  changes like @1hidden_by_design's power-lines video and approved seven changes "as long as it accomplishes the same video as the
  one I referenced": Rules 2, 3, 5 and 6 were rewritten and Rule 7 was added (the record is 7.7). Elsewhere in this file "3.4 rule
  N" means the rules below.
  - **What it is:** a bright, clean, photoreal-leaning 3D render of one place sliced open like a cake, in soft daylight, with
    translucent cyan water, seen by a camera that flies around and into it. "You" is the viewer and nobody stands in for them:
    hands, small anonymous workers or machines appear only where the work needs them. One small living thing per video is welcome
    (the yellow fish, the dog). No on-screen term labels. One-word captions, the loop ending and no spoken call to action stay as
    they were.
  - **Rule 1. Animate nearly all of it.** Animated clips cover at least about 80% of the running time; plan every line as a clip,
    with no holds. Every line in which something flows, turns, pours, fills, breaks or freezes gets a clip. A hold is only the
    fallback for a lost clip (3.2 rule 5): the last frame of the clip before it, with a slow push-in, for 3 s at most. Never show a
    frozen splash, pour, plume of smoke or gauge needle. `pipeline/analysis/check_video.py` measures it on the finished video.
  - **Rule 2. One set, a travelling camera** (replaced "one cutaway from one main view" on 15 Nov 2026). The video stays on one
    sliced-open set, and each fix is added to it (the shot rule below), but the camera flies around and into it like the
    power-lines video: 8–12 camera positions, the wide view only to open, to close (the loop) and to step back once or twice, and
    every problem and every fix seen up close from its own position. Anything that needs another place is shown on the set or cut.
  - **Rule 3. Every clip flies the camera.** Each clip starts at one camera position and ends at another (a change clip at one
    position still drifts), and each position is a real still of the set from there, never a crop of another still: a crop makes
    Kling zoom across a flat picture, which reads as still (3.4k). On "But" the camera pushes in or swoops to where the problem
    happens; the change plays out close while the camera keeps drifting; on "So" it pulls away or flies on to the next position. No
    still-camera clips. A middle keyframe can carry one clip in to a change and back out. No cross-fades between different pictures;
    a whip (a fast swing with motion blur) only for a far jump; a hard cut only where the setting truly changes.
  - **Rule 4. Hold the look steady.** Every still is an edit of the wide still or of a neighbouring camera position, so the set
    keeps its parts, colours and materials from every angle; the versions at one position keep the framing lock. The shared style
    line names no objects and no place. Night and storm are a re-grade of the same picture: the same water colour, and nothing
    glows. The first and last frames match part for part. All of it is checked at Gate C.
  - **Rule 5. Bigger captions, readable anywhere.** Wide shots are composed with the subject in the upper 60% and plain, calm
    ground below it (the WIDE line, 3.3 Step 4). In close-ups the caption sits over whatever is there, as in the power-lines video;
    the stroke and the shadow keep it readable. Captions are ALL CAPS, with letters about 57 px tall at 1080×1920 (30% larger than
    in videos 03–04), centred about 75% down the frame (3.3 Step 10).
  - **Rule 6. Bolder pointers that ride with the camera.** Solid white arrows about three times the size of the old chevrons, with
    a soft shadow, moving along the flow, three or four at a time, and a thicker ring that fades in. One device per beat. A pointer
    appears when the camera arrives at a detail and slows, and stays pinned to the detail while the camera drifts (tracked in the
    edit); the camera never stops for a pointer (3.3 Step 10).
  - **Rule 7. Measure the camera** (added 15 Nov 2026). `pipeline/analysis/camera_path.py` on the pilots, the clips and the final:
    the camera moving in 65% or more of the seconds; median parallax 0.3 px or more (it flies through the set rather than zooming
    across a picture); big moves (a quarter of the frame or more in a second) in at least one second in eight on average, with no
    gap over 15 s; and no still-camera stretch over 5 s. The power-lines video scores 66%, 0.46 px, 22 big-move seconds in 88 s
    (longest gap 15 s) and 5 s; video 08 scored 45%, 0.03 px, 7 in 80 s (42 s) and 13 s (7.7).
  - **Agreed the same day, not rules:** price Kling's 1080p at the next Gate B, because our 720p clips carry about half the fine
    detail of the stills, and add a light sharpen otherwise (3.3 Steps 3 and 9); take the caption timing from `07-build.py`.
- **Sound under the voice (APPROVED by the user, 15 Nov 2026: "yes on the sound").** The user asked what the competition does and
  what I recommend, then said yes to the recommendation. What was approved:
  - A quiet, steady bed that fits the place (street air, the sea, a plant hall humming), with no tune, about 18–20 dB under the
    voice, running the whole video.
  - Four to eight short effects on the moments where something visibly happens (water rushing, a valve closing, ice cracking),
    starting about 10–12 dB under the voice. The effect levels are my starting point, not measured from anyone.
  - No melodic music, and never a copyrighted or trending track.
  - The voice-only mix is kept as a second master. On the first video with sound the user gets both, to compare by ear.
  - How: the ElevenLabs Sound Effects node, mixed in ffmpeg (3.3 Steps 3, 6b and 9). It costs ElevenLabs credits: about 3.33 a
    second of sound (video 08: 118.33 for a 20 s bed and six effects).
  - Why (7.5): measured on 15 Nov 2026, not listened to. @1hidden_by_design runs a quiet steady bed under the whole video, about
    19–20 dB below the voice in the quietest moments, with almost no separate effects; @howbuildingexplained has no bed, only short
    quiet sounds in the gaps between lines; @thewhatifstudio has full sound design, loud in the mix. Ours was the only voice-only
    track.
  - The section 5 prompt's SOUND line now defaults to "bed and effects".
- Earlier look (**Classic**, locked by the user on 11 Nov 2026 and replaced on 15 Nov 2026), for the record: the look of videos
  01–02 and 05–07. The locked mascot stands in a small sunny 3D diorama: a stylised, toy-like game-engine render with soft daylight
  and mild depth of field, seen from a slightly raised three-quarter view. Base STYLE string in `pipeline/02-prompts.py` plus one
  palette line per setting. Captions centred, one word at a time, in Title Case, with ALL CAPS term labels (`pipeline/02-build.py`).
- **Shot rule (LOCKED by the user, 11 Nov 2026, after video 05): one build.** Its "one main view" part was replaced on 15 Nov 2026
  by the travelling camera (Rule 2 above, 7.7). The reasons for the rule and its credit effect are in 7.2.
  1. The camera stays on the thing being explained. Every line of the script changes something you can see on it: a part grows in,
     a problem hits it, something inside starts working. (Classic look: the mascot is in the scene doing the work. Cutaway look:
     nobody is, unless the work needs hands or a small worker.)
  2. Close-ups show only the build, as it is at that moment. In the Cutaway look each close-up is a camera position with its own
     still (Rule 3), and the camera flies on from it rather than cutting back. (Classic look, for the record: close-ups were
     push-ins on the same picture, and the next shot went back to the main view.)
  3. To show how it works inside, slice the wall open from the same view. Never cut to a separate room. (In the Cutaway look the
     set is already sliced open.)
  4. Comparisons and asides stay on the build. Classic look: only as labels ("17 HOURS", a dashed "60 FT" line). Cutaway look, which
     has no labels: on the set itself (a gauge on the pipe, a tub beside the hydrant). Cut any that would need a picture of
     something else (like video 05's cup in a bath, kitchen sponge, airliner and space capsule, or video 04's coal heap, three
     glasses and Perth).
  5. Problems (storms, floods, threats) hit the build where the camera sees them up close.
  6. The setting changes only when the build itself has to move (a tow-out, a launch, a flight); the new setting gets its own wide
     view. A journey topic (water from the sea to a tap, power from the plant to a house) is one long section through the whole
     system that the camera flies along, stopping wherever something changes (the power-lines video stops about ten times in 88 s).
- Higgsfield project / folder naming: `HBX – [video title]`
- Channels: YouTube **LetZBuildTogether**, handle **@LetzBuildTogether** (channel id `UCNaqNT-R3K2GmISUfLdfBzA`, created Sep 2025). The
  user renamed it from @overthinkingyearly some time between 10 and 15 Nov 2026; the old handle still redirected on 15 Nov 2026.
  TikTok is still **@overthinkingyearly** (nickname "OT"). The 6.5 shortlist was not used.
- Channel branding (made 10 Nov 2026, details in 6.8): profile picture = the mascot's head and shoulders on blueprint blue; banner =
  blueprint grid, "ONE PROBLEM / AT A TIME", tiles of the finished builds. Files in `branding/`. Brand colours: blueprint blue `#1F4E8C`,
  hard-hat yellow `#FFC83D`; type: Barlow Condensed. Both were live on the YouTube channel on 15 Nov 2026. The mascot is retired from
  the videos only: the user has not asked to change the artwork, so leave it unless they do. `branding/mascot-cutout.png` was made
  for covers and thumbnails; Cutaway videos use a frame of the cutaway instead.

### 3.4b Video log
YouTube ids, view counts and comments for the posted videos are in 6.1.
- **01 Desert Adobe** (Lite) — DELIVERED v1, 7 Nov 2026. 74.3 s, 1080×1920, 24 fps. Higgsfield spend **106.25 cr** (quote 122): 19 stills 23.75 + clips 82.5 (net of refunds). ElevenLabs ≈ $0.13.
  Final in Higgsfield storage: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/11972224-4d3b-45ee-947f-b84b88b1f651.mp4 (media_id 11972224-4d3b-45ee-947f-b84b88b1f651).
  Known edit candidates: ending blanket floats above the roof; bricks clip pushes in tight; "cutaway" is a heat-glow view; thick-walls and lime beats are free wipes.
- **02 Fallen Tree → Outrigger Canoe** (Full, idea #2) — DELIVERED v1, 7 Nov 2026. 67.96 s, 1080×1920, 24 fps, −15 LUFS, 17 beats, 235 words.
  Higgsfield spend **202.00 cr** (quote 214.5): 20 stills 25.00 (18 + 2 redos) + clips 177.00 net (8 minimax_h3 clips 96; 9 kling4_0 retries 81;
  72 cr of failed minimax jobs refunded). ElevenLabs ≈ $0.25 (2 takes; take A used at 1.07×).
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/7adc5a84-79d3-41f5-9ca0-d19b7e607510.mp4 (media_id 7adc5a84-79d3-41f5-9ca0-d19b7e607510);
  clean master without text: media_id 5d3de2af-12f7-43d4-adc2-2c2e8f14d4ea. Higgsfield project "HBX – Outrigger Canoe" (folder 6f533c69-8a0f-4734-8c9d-cb3f40f12e49).
  Fell back to a still: B9 (lake-bed aside; the kling clip invented a mannequin swimmer). Known edit candidates: B9 still push-in; B10 hard hat
  blurs for a moment; the outrigger float sits on the sand side; LAKEBED is tropical shallows rather than a murky lake.
  Covers (1080×1920, free, `pipeline/02-thumbnail.py`): **A "LOG → CANOE" split (recommended)** media_id f3fd1ad4-eae4-4908-b2c7-c8bd27ba7699;
  B "NOT THE CROC" curiosity c10b2919-3e9c-4f9d-bd51-12da30eb996a; C storm hero + log inset bebf2e3d-db45-4501-8f84-b7427180b965
  (each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.png).

- **03 Fire Hydrant** (Lite, idea H1, Hidden By Design look, loop ending) — DELIVERED v1, 8 Nov 2026. 77.88 s, 1080×1920, 24 fps, −15.3 LUFS, 24 beats, 269 words.
  Higgsfield spend **123.25 cr** (quote 119.0, +3.6%): 24 stills 30.00 (22 + 2 redos) + clips 93.25 net (1 minimax_h3 clip 10; 8 kling4_0 clips 83.25,
  including one fire-clip redo; 2 failed minimax jobs refunded). ElevenLabs: 2 takes × 1,451 credits (≈ $0.29); take A used at 1.07×.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/cd23a38c-d887-48ff-8a32-df82dcb2a270.mp4 (media_id cd23a38c-d887-48ff-8a32-df82dcb2a270);
  clean master with narration and no captions: media_id 30f6f773-5ead-4cec-a367-bf6dd936839d. Higgsfield project "HBX – Fire Hydrant" (folder d37f9156-5d12-45fc-941c-157590560a13).
  Covers (`pipeline/03-thumbnail.py`): **D "IT'S EMPTY" (final, recommended for both TikTok and YouTube Shorts, made 9 Nov 2026)**: the B21 night-fire
  still (the house burns while the barrel is still dry). YouTube Shorts 1080×1920 media_id 011c136f-9f03-4f42-b77c-bc17b9d52981; TikTok 3:4 upload
  1080×1440 f154d4f5-2e07-4ba0-8817-4031a6aac368 (each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg).
  Earlier options (each <media_id>.png at the same path): A "FREEZES / DOESN'T" split b4c1143d-538b-4533-8e6b-9688d81df52a (the hydrant itself is out
  of frame); B "MOVIES LIED" curiosity bd99655f-79e3-42f4-83e1-8506bb8b0c2b; C plain mid-video cutaway, no text ace9d4c0-c734-4945-a6e9-f281d544f02c.
  Known edit candidates: B15 shows only the first 1.35 s of the crash clip, then dissolves into the SNAP still (Kling puffed water at the valve later);
  in END the underground barrel is a solid red pipe rather than a see-through one; the movie geyser comes from an intact hydrant (letterboxed in post).

- **04 Seawater to Tap Water** (Lite, idea H15, Hidden By Design look, loop ending) — DELIVERED v1, 10 Nov 2026. 78.67 s, 1080×1920, 24 fps, −15.4 LUFS, 27 beats, 271 words.
  Higgsfield spend **111.75 cr** (quote 121.3, −8%): 30 stills 37.50 (25 on screen + 1 base kitchen + 4 rejected) + 8 kling4_0 clips 74.25 (the one
  minimax_h3 pilot sat queued and failed, refunded). ElevenLabs: 2 takes × 1,475 credits (≈ $0.30); take B used at 1.09×.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/09f4ea3f-150f-4f02-a067-39b09fa5f366.mp4 (media_id 09f4ea3f-150f-4f02-a067-39b09fa5f366);
  clean master with narration and no captions: media_id 2bdc92ec-03d6-4c0e-a517-a72234807e71; Gate D preview (B1–B4): d311f93c-8955-4497-a467-e67c327ab78e.
  Higgsfield project "HBX – Seawater to Tap Water" (folder 95b78d03-a34b-4999-b679-1c8f5371f9de).
  Final packaging (11 Nov 2026, the user asked for "high converting"): YouTube title "How Seawater Becomes Drinking Water (Without Boiling It)";
  TikTok caption "How do you turn seawater into drinking water without boiling it? 🌊" + #HowItWorks #Engineering #LearnOnTikTok #3DAnimation
  #Desalination. (First drafts: TikTok "How Do You Turn Seawater Into Drinking Water? 🌊"; YouTube "How the Ocean Becomes Your Tap Water".)
  Covers (`pipeline/04-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg): **D "THIS WAS THE
  OCEAN" (final, both platforms)**: the payoff glass of clear tap water with the plant and the sea in the window. 1080×1920 022bdfce-42de-4a40-a43b-3b94f97817e4,
  TikTok 3:4 upload 1080×1440 31722592-1c35-4179-936f-de976c0bac41. Earlier options: B "THEY ADD ROCKS" 1080×1920 d5310788-302e-4054-a10f-56456f6e1629
  (3:4 5f543776-e159-44bd-afe9-efc54646e480); A "SEA / TAP" split dfdb17dd-a334-4778-99c9-be0e6d525952; C plain cutaway of the finished plant, no text
  b222091e-36dd-4898-a032-af879b37616f (the frame to pick on YouTube until the channel can upload covers).
  Known edit candidates: the intake clip ends with the yellow hero fish sucked into the pipe (it reappears at the cap); clips play 1.12–1.17× faster to
  fit their beats; stray blue valves from the cutaway style sit under the GLASSES counter and beside the intake pipe.

- **05 Steel Tank → House at the Bottom of the Sea** (Middle, idea #1 Aquarius, Classic look, loop ending) — DELIVERED v1, 11 Nov 2026. 78.83 s,
  1080×1920, 24 fps, −15.2 LUFS, 26 shots (25 beats), 272 words. Higgsfield spend **176.00 cr** (quote 196.4, −10%): 31 seedream stills 38.75
  (24 on screen + the DIVER reference + 6 redos) + 16 kling4_0 clips 137.25 (15 planned 130.50 + one storm redo 6.75). ElevenLabs: 2 takes × 1,368
  credits (after the plan upgrade); take A used at 1.00× (no speed-up needed).
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/bb9b3915-8070-4405-bb10-ad4f2ad8be39.mp4 (media_id bb9b3915-8070-4405-bb10-ad4f2ad8be39);
  clean master with narration and no captions: media_id b061a807-0316-43e6-9fac-8f31374a03fa. Higgsfield project "HBX – House at the Bottom of the Sea"
  (folder 696a691c-e24b-415f-96a3-427d896b05e2). ElevenLabs flow zkTwApM30LKPD4O79xg2. Gate D preview (B1–B5) was sent as a file, not uploaded.
  Post copy: YouTube "How a Steel Tank Becomes a House at the Bottom of the Sea"; TikTok "Why does it take 17 hours to leave a house 60 feet
  underwater? 🌊" + #HowItWorks #Engineering #LearnOnTikTok #3DAnimation #Underwater #ScubaDiving.
  Covers (`pipeline/05-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg): **A "17 HOURS /
  TO LEAVE" (recommended)** over the finished house with the buoy above: 1080×1920 b27d1a52-48ea-4d87-97bd-ea161787c859, TikTok 3:4
  47ac6544-ee17-42bd-a8be-cb2fc8e0a038; B "DON'T SWIM UP" on the bends rush 2e733e44-722d-4b41-8683-7d097cd86aec; C plain storm frame, no text
  1cce6c8d-5506-4d0e-a54f-db2c4bfb5268.
  Fell back to a still: B21 (the storm; both Kling versions crashed the breakers onto the deep tank and calmed the sea). Trimmed clips: B4 keeps the
  first 2.0 s (later the foam pours out of the cutaway), B15 the first 2.9 s (later he breaks the surface and flies at the sun), then a held frame.
  Known edit candidates: the tank is ~2.5× the mascot's length (not bus-sized); a toy island under the plane; the payoff sky is lighter than the
  storm's; the door shot shows the tank floating without legs; during "This is the bends" he is half out of the water.

- **06 Crack in a Cliff → the Hidden City of Petra** (Middle, idea #9, Classic look, first under the 3.4 shot rule, loop ending) — DELIVERED v1,
  12 Nov 2026. 76.42 s, 1080×1920, 24 fps, −15.6 LUFS, 24 beats, 263 words. Higgsfield spend **158.75 cr** (quote 186.30, −15%): 19 seedream
  stills 23.75 (18 used + the S3 redo) + 14 kling4_0 clips 135.00 (60 s, no redos). ElevenLabs: 2 takes × 1,409 credits; take A at 1.06×.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/9c3ccf8e-cf8f-43ee-bd71-3cec6ac41aeb.mp4 (media_id 9c3ccf8e-cf8f-43ee-bd71-3cec6ac41aeb);
  clean master with narration and no captions: media_id 7915ceaa-682a-4760-ae5e-63219d0b551a. Higgsfield project "HBX – Hidden City of Petra"
  (folder 452e85a7-bd8f-4644-bdab-cb74b076b356). ElevenLabs flow MJ96Xe95SwRqRmdOFjcK. Gate D preview (B1–B3) was sent as a file, not uploaded.
  Post copy: YouTube title "How a Crack in a Cliff Becomes the Hidden City of Petra", description "A crack in a desert cliff, almost no rain,
  storms that dump it all at once, and a 39-meter tomb carved from the top down. Here's how Petra was built one problem at a time, and why
  the urn on its famous Treasury is full of bullet holes. Which lost city should we build next? #Petra #HowItWorks #3DAnimation"; TikTok
  "How do you carve a 39-meter tomb straight out of a cliff? 🏜️" + #HowItWorks #Engineering #LearnOnTikTok #3DAnimation #Petra #Jordan.
  Covers (`pipeline/06-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg): **A "CARVED /
  TOP DOWN" (recommended)** on the half-carved facade with a down arrow: 1080×1920 6a96ed0c-8f31-4cc9-91c6-3367317bf007, TikTok 3:4
  01e2573a-58d9-44b1-afde-e32fd0e7f8bf; B "WHY THE / BULLET HOLES?" on the pockmarked urn 37d96132-abc0-4c97-b29b-7aee70a47e3e; C plain END
  frame, no text 27847837-eda0-4035-b67c-5f75d3a26547.
  Known edit candidates: the hook pushes in to a close-up of the mascot (Kling read "slow push-in" as a dolly-in); in C5 he leaps up the cliff
  to the ledge; INSIDE drops the lower storey to show the room; URNSLICE cuts the dome, not the urn on top; the mascot is large next to the facade.

- **07 1959 Car vs 2009 Car: One Driver Walks Away** (Middle; P4 of the "Who wins?" matchup list of 14 Nov 2026, which was removed on
  15 Nov 2026; Classic look, one arena in one main view, loop ending) — DELIVERED v1, 14 Nov 2026. 77.00 s, 1080×1920, 24 fps,
  −15.2 LUFS, 23 beats, 270 words (272 spoken). Higgsfield spend
  **157.25 cr** (quote 177.68, −11.5%): 16 seedream stills 20.00 (10 used + the S0T base + 5 tries and fixes) + 11 kling4_0 clips 137.25
  (61 s, no redos). ElevenLabs: 2 takes × 1,387 credits; take A at 1.03×.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/35f8a478-c94f-4893-a326-552efd58100a.mp4 (media_id 35f8a478-c94f-4893-a326-552efd58100a);
  clean master with narration and no captions: media_id f898830c-b0e8-4ebd-b3cd-a83ed0569f46. Higgsfield project "HBX – 1959 Car vs 2009 Car"
  (folder f5ea6596-e005-46f2-a7b0-cd016a6cf293). ElevenLabs flow kOKX6WGXJo1KWbsqBlsK. Gate D preview (B1–B4) was sent as a file, not uploaded.
  Post copy: YouTube title "1959 Car vs 2009 Car: Only One Driver Walks Away", description "In 2009, crash testers at the Insurance
  Institute for Highway Safety drove a 1959 Chevrolet Bel Air into a 2009 Chevrolet Malibu, both at 40 mph. Here is that crash slowed
  right down: the crumple zone, the safety cage, the belt, the airbag and the steering column, and why the old car's footwell was
  shoved in two feet while the new one moved about three inches. Which car would you rather be sitting in? #CrashTest #CarSafety
  #HowItWorks"; TikTok "Only one of these drivers walks away. Which car are you picking? 🚗" + #HowItWorks #Engineering #LearnOnTikTok
  #3DAnimation #CrashTest #CarSafety.
  Covers (`pipeline/07-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg): **A "PICK YOUR /
  CAR" (recommended)** on the mid-crash frame with 2009 and 1959 tags: 1080×1920 b671811c-ae4c-48d0-8c8a-c1534e476dfb, TikTok 3:4
  2472c704-09df-4665-b931-b25d77d5252f; B "BUILT LIKE / A TANK?" on the old car coming apart cca50859-44fe-413f-9ca3-6f6f57fc9383; C plain
  airbag frame, no text 59c90763-3435-4474-a227-6cf4d2037fea.
  Known edit candidates: the hook is frozen at the moment of contact (seedream would not leave a gap); a small generic emblem on the red
  car's grille; the belt clip (C6) barely moves, so the hold after it pushes in on him; the old car is open from above, so line 11's
  "the roof" has no roof to hit; C3 plays at 1.25× and C11 at 1.19× to fit their lines.
  Script facts (moved here on 15 Nov 2026, when the matchup list left section 2). The test: the IIHS crash of 9 Sep 2009, a 40 mph
  offset frontal test; the Bel Air's cabin collapsed and the Malibu's stayed intact; 62 cm against 7 cm at the footrest; rated Poor
  against Good; the Malibu's worst score was the left leg and foot. As made: opening A (the cold claim), script in
  `pipeline/07-script.txt`; the arena seen from high above with the 1959 car at the bottom (a plain dummy, no belt) and the 2009 car
  at the top (the mascot, belted, seen through the windshield); FOOTWELL PUSHED IN 24 IN against 3 IN as the scoreboard; verdict
  label "STILL THINK THEY DON'T BUILD THEM LIKE THEY USED TO?". Cut from the draft chain: "nearly two tons" (the Bel Air weighed
  about 3,600 lb, about the same as the Malibu's 3,400–3,650), "steel that doesn't bend" (the old car did bend, into its cabin), "30
  thousandths of a second" (sources give 20–50 ms, so "faster than you can blink"), and the per-mile death rate (5.06 per 100M miles
  in 1960, 1.26 in 2023: true, but nothing on the cars shows it and belt laws, roads and drunk-driving laws share the credit).
  Verified for the script: no belts or airbags in the test Bel Air; its dummy's head hit the wheel, the roof and the metal dash; the
  wheel moved up and back; the windshield came out, the driver's door opened and the bench seat tore loose; the Malibu had front
  belt pretensioners and front airbags as standard; GM brought in collapsible columns for 1967 and every US car needed one from 1
  Jan 1968; crumple zones (the Mercedes W111) and the three-point belt (the Volvo PV544) both went on sale in 1959 (the twist).
  Reply-video answers: the Bel Air had its engine (a straight six; Jalopnik, Sep 2009) and was in good condition with a little
  engine rust (its former owner, via The Truth About Cars); the two cars weighed about the same. Saturation check of the title: at
  least 7 near-identical Shorts, best 926K ("What Happens When a 1959 Chevy Hits a Modern Car?", 4 weeks old), the rest 29K–64K, all
  re-posting the crash footage.

- **08 Why Your House Doesn't Smell Like the Sewer** (Middle; idea C1; the first Cutaway video and the first with sound; one set
  from one main view; loop ending) — DELIVERED v1, 15 Nov 2026. 79.53 s, 1080×1920, 30 fps, −13.8 LUFS, 24 beats in 14 segments
  (11 clips, 3 holds), 274 words. Higgsfield spend **203.50 cr** (quote 219.65 with the 15% reserve, 191.00 without it): 26
  seedream stills 32.50 (14 on screen, 12 drafts and redos) + 11 kling4_0 clips at 720p 171.00 (76 s, no redos). ElevenLabs: 2
  takes × 1,399 credits (take B used at 1.00×) + 118.33 for the bed and six effects.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/a970c674-b421-4a1e-ad15-152bab7b2815.mp4 (media_id a970c674-b421-4a1e-ad15-152bab7b2815);
  the same video with the voice only: b3435583-038b-454d-99de-f5867c24ac81; clean master with the full sound and no captions or
  pointers: 681cff41-db44-418c-83a3-b19f6eee19ad. Higgsfield project "HBX – Why Your House Doesn't Smell Like the Sewer" (folder
  69c0772c-01fe-4bd4-a2cc-54828fa84bca). ElevenLabs flows: narration VzHYC42k13jcCO777zar, sound jkPXm5LUPekg4BFsFLmm. The Gate D
  preview (P1, H1, C11, H3) was sent as a file, not uploaded.
  Measured: clips over 93% of the running time, holds 5.8 s; `check_video.py` 20% of the seconds moving (16% without the pointer
  arrows), longest still stretch 29 s (0:28–0:57), against the 80% target (3.4k); captions 57 px at 75%; the quietest moments 21 dB
  under the voice with a steady stereo bed (the voice-only version: 48 dB).
  Post copy (`pipeline/08-post-copy.md`): YouTube title "Why Your House Doesn't Smell Like the Sewer", description "There's an open
  pipe between your kitchen and the sewer, and the water sitting in one bend is all that keeps the stink out. Here's how the
  U-bend, the pipe on your roof and a little flap under the lawn keep sewer gas (and rats) out of your house, and why dried-out
  floor drains helped spread SARS through a Hong Kong apartment complex in 2003. Which drain in your house smells? #Plumbing
  #HowItWorks #3DAnimation";
  TikTok "Why doesn't your house smell like the sewer it's connected to? 🚽" + #HowItWorks #Engineering #LearnOnTikTok
  #3DAnimation #Plumbing #HomeTips; pinned comment "Which drain in your house smells?".
  Covers (`pipeline/08-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg):
  **B "SWAM UP / THE TOILET" (recommended)** on the rat in the toilet at night: 1080×1920 47c73657-39fa-486d-ab66-c2cc5a4dd9af,
  TikTok 3:4 e3d74c2e-3aaf-434a-b699-6d81fed31a36. A "ONE CUP / OF WATER" with an arrow to the kitchen U-bend:
  3554fa95-5666-47e1-82ae-dae0cca7cadb, 3:4 b785c72f-7bef-4c75-b8ef-b599eec76575 ("one cup" is my estimate from the pipe size,
  roughly 1–1.5 cups for a 1½-inch kitchen trap; no published figure was found). C plain frame of the fan pulling the haze out of
  the floor drain, no text: 3486a068-4f88-4f12-b58c-f4758330ab99.
  Known edit candidates: the hook (12 s) and the Hong Kong stretch (12 s) keep a still camera and read as still (3.4k; the user
  kept the hook at Gate D); in the hook the draining water falls beside the main pipe instead of out of the kitchen sink, and the
  sloping pipe under the lawn wiggles for about a second at 0:08; the vent sticks out of the roof about a metre (a short stub was
  invisible at phone size); the narration says the rat climbs the main pipe, but it is only seen swimming in the sewer window and
  then in the toilet; in the zoomed bathroom framing (0:38–0:51) the captions sit on the lawn edge, not on plain soil; C6 plays at
  1.46× and C10 at 1.69× to fit their lines.
  Script facts (moved here on 16 Nov 2026, when the Cutaway list left section 2; sources in 7.6): opening A ("If you pipe your sink
  straight into the sewer, it drains."; the cold claim shown to the user was "There's an open pipe from the sewer to your kitchen.
  One cup of water is in the way."); five problems and five fixes (trap, vent, running the water, trap primer, rat blocker); the
  Hong Kong story told over our own bathroom; the ending "Bend the pipe, let it breathe, and keep it wet."; comment question
  "Which drain in your house smells?". Checked at Gate A: induced siphonage and the roof vent (plumbing code guides); the toilet
  bowl's water as its own trap; trap primers (California's plumbing code requires them on floor drains that are rarely used); rats
  swimming the sewer, climbing a 3-inch pipe and swimming through a toilet's bend (National Geographic, video, 2015); a rat blocker
  as a one-way flap where the house drain meets the sewer; the WHO findings at Amoy Gardens (dried-out floor-drain traps, and
  bathroom fans drawing contaminated droplets into the flats) and 321 cases by 15 April 2003; traps dry out in two weeks to several
  months, typically three to four weeks. Cut: the washer gurgle, the backwater valve, how long a rat holds its breath (sources
  give 30 s to 15 minutes) and the SARS death toll (35 to 42 by source). Saturation on the exact title: no Short used it; about
  eight animated U-bend explainers (best 211K), none with the vent, Hong Kong or rats; rat-in-toilet Shorts reach 15M and plumbers
  on camera 21M, 2.6M and 2.2M; the reference account's sewer video (309K) covers the street sewer and treatment works.

- **09 What Lightning Does Inside Your House** (Middle; idea C3; the first video with the travelling camera; opening B, the cold
  claim; one storm house seen from 10 camera positions; loop ending) — DELIVERED v1, 15 Nov 2026. 75.21 s, 1080×1920, 30 fps,
  −13.2 LUFS, 24 beats in 16 clips (no holds), 270 words. Higgsfield spend **264.25 cr** (quote 242.65 with the 15% reserve, 211.00
  without it; +8.9%): 35 seedream stills 43.75 (20 on screen, 3 bases, 12 drafts and redos) + 18 kling4_0 renders at 720p 220.50
  (98 s: the 16 clips, 81 s, plus the first C15 pilot and the first C8 and C11). ElevenLabs: 2 takes × 1,395 credits (take A used
  at 1.00×) + 131.67 for the rain bed and six effects.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/d8e26fda-8fb2-4885-aa09-e2b5ebd37b00.mp4 (media_id d8e26fda-8fb2-4885-aa09-e2b5ebd37b00);
  the same video with the voice only: ad92be18-b6a4-4257-bc6b-6ecfb8ba33d3; clean master with the full sound and no captions or
  pointers: bfe04732-841b-4595-8a7d-d81b150d8c3f. Higgsfield project "HBX – What Lightning Does Inside Your House" (folder
  783ef666-4a82-436a-90f9-36e3983264a4). ElevenLabs flows: narration 0Udre8WpeBTl2gAnjT3Z, sound FSzLyvOaFzeFXRMh7RoX. The Gate C
  flight map is `pipeline/09-flightmap.jpg`; the Gate D preview (C1, C15) was sent as a file, not uploaded.
  Measured: `check_video.py` 84% of the seconds moving, longest still stretch 2 s (79% and 5 s before the push-in added to C7);
  captions 57 px at 75%; `camera_path.py` camera moving 78%, parallax 0.44 px, 23 big-move seconds (longest gap 9 s), longest
  still camera 3 s, 26 s in / 27 s out / 13 turns (the power-lines video: 66%, 0.46 px, 22 in 88 s, 5 s); the quietest moments
  21 dB under the voice with a steady stereo bed (the voice-only version: 51 dB). No line lost its clip.
  Post copy (`pipeline/09-post-copy.md`): YouTube title "What Lightning Does Inside Your House", description "A lightning bolt
  that hits your roof is hunting for the ground, and the wires in your walls and the copper pipe to your shower can be its way
  down. Here's how a lightning rod, bonding and a surge protector give it a safer road, and why about a third of lightning
  injuries happen indoors. Do you shower during a storm? #Lightning #HowItWorks #3DAnimation"; TikTok "What does lightning
  actually do inside your house? ⚡" + #HowItWorks #Engineering #LearnOnTikTok #3DAnimation #Lightning #Thunderstorm; pinned
  comment "Do you shower during a storm? Yes or no."
  Covers (`pipeline/09-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg):
  **A "SHOWER IN / A STORM?" (recommended)** on a frame of the video (0:09: the current glowing down the wall beside the running
  shower): 1080×1920 99a396c6-5ede-4294-bd75-55895a3d1af6, TikTok 3:4 13309e11-4eb6-4f15-80de-037b1ddbcc1b. B "IT JUMPS / TO YOUR
  PIPES" on the side flash: a3693c33-f023-48d4-8bc0-8e220abb31eb, 3:4 7f338e1a-6c20-4091-99b6-818eafd1abab. C plain frame of the
  bolt on the rod, no text: dd749b3b-7fc4-47e6-b2df-df79b4ad7842.
  Known edit candidates: at 0:33–0:35 (C8) the middle ~2 s of both renders scrolled a second copy of the house up from under the
  ground, so the edit joins the clean start and end with a 0.3 s whip down, both parts at 0.66×; C7 came back with a dead-still
  camera, so the edit pushes in to 1.18× and C8 eases back out; the big flash at 1:05 whites out most of the frame for ~0.2 s; the
  panel close-ups (0:45–0:52) read as a real room more than a cutaway; the bathroom gains a window on its right wall in C14; the
  attic keyframe was dropped, so C2 dives from the ridge to the bathroom in one move.
  Script facts (moved here on 16 Nov 2026, when the Cutaway list left section 2; sources in 7.6): opening B, the cold claim
  ("Everyone's heard it: don't shower in a thunderstorm. Here's what the bolt actually does."), chosen at Gate A over "If lightning
  hits your house, it has to reach the ground. The easiest way down might be your shower."; four fixes (a lightning rod with its
  cable and ground rod, bonding, a surge protector at the panel, waiting out the storm to shower); the twist is the CDC's third of
  lightning injuries indoors; the ending "Catch it high, carry it down, and bury it deep."; comment question "Do you shower during
  a storm? Yes or no.". Checked at Gate A: wiring, plumbing and phone lines as paths (NWS); rods catch strikes already coming and
  do not attract them (NOAA, LPI); ground rods at least 8 ft, often 10 ft deep (said as "deep"); side flash and bonding (LPI, NFPA
  780 via trade sources); surges in on the power line (State Farm, Exponent); the surge protector at the panel (NEC 2020 230.67,
  not said); about 30,000 amps (NWS); the CDC's advice not to shower, bathe or wash dishes in a storm. Cut: the Empire State
  Building's 23 strikes a year, "300 million volts" and "hotter than the sun" (other pictures), the NWS expert's no-deaths remark
  (not found on an official page), the plastic-pipe nuance (kept for replies), rods every 20 ft and two down conductors (secondary
  sources only), corded phones. Saturation on the exact title: about 8 near-identical Shorts, best 15K (a builder on camera);
  animated ones 1K or less; the topic's biggest Shorts are "Should You Shower During A Thunderstorm?" 20M and 4.8M; two rivals in
  our format had the rod basics that autumn (7.9K and 1.7K), so the script led with the shower, the side flash and the pole.

- **10 Why These People Are Frozen Upside Down** (Middle; idea X5, the first of the 16 Nov ideas; opening A, "If you…"; one
  sliced-open lab seen from 9 camera positions, with no water in it; loop ending) — DELIVERED v1, 17 Nov 2026. 76.21 s, 1080×1920,
  30 fps, −13.7 LUFS, 24 beats in 19 clips (no holds), 269 words. Higgsfield spend **278.00 cr** (quote 280.60 with the 15%
  reserve, 244.00 without it): 37 seedream stills 46.25 (23 keyframes used, L1 unused, 13 drafts and redos) + 22 kling4_0 renders
  at 720p 231.75 (103 s: the 19 clips, 86 s, plus C4A, C6A and C7A, thrown away for a pit or a step in the floor). ElevenLabs: 2
  takes × 1,417 credits (take A used at 1.06×) + 128.33 for the lab bed and seven effects.
  Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/411ec54b-1d2d-4bcd-986a-ad5162a5d424.mp4 (media_id 411ec54b-1d2d-4bcd-986a-ad5162a5d424);
  the same video with the voice only: 08f9539b-f60b-4c57-b18a-07b8ee5fdcc0; clean master with the full sound and no captions or
  pointers: 92c26eb5-d5d7-46fb-b0da-d85613bda271. Higgsfield project "HBX – Why These People Are Frozen Upside Down" (folder
  dc9cd687-a9ef-4334-a7db-29df6b684c68). ElevenLabs flows: narration veNoEzrTLWDaaHUTT1ie, sound shGklhH86OxmdJFiZJJ0. The Gate C
  flight map is `pipeline/10-flightmap.jpg`, with `10-keyframes.jpg` and `10-first-last.jpg`.
  Measured: `check_video.py` 90% of the seconds moving, longest still stretch 3 s; captions 57 px at 75%; `camera_path.py` camera
  moving 91%, parallax 0.40 px, 35 big-move seconds (longest gap 9 s; two of them are the power-cut dip at 0:37–0:38), longest
  still camera 2 s, 38 s in / 25 s out / 17 turns (the power-lines video: 66%, 0.46 px, 22 in 88 s, 5 s); the quietest moments
  21 dB under the voice with a steady stereo bed (the voice-only version: 48 dB). No line lost its clip.
  Post copy (`pipeline/10-post-copy.md`): YouTube title "Why These People Are Frozen Upside Down", description "In Arizona,
  people who paid to cheat death wait in steel tanks of liquid nitrogen, head down. Here's how they're turned to glass instead of
  ice, why the tanks don't even plug in, and why the brain goes at the bottom. Would you do it? #Cryonics #HowItWorks
  #3DAnimation"; TikTok "Why are these people frozen upside down? 🧊" + #HowItWorks #Engineering #LearnOnTikTok #3DAnimation
  #Cryonics #Science; pinned comment "Would you do it? Yes or no."; altered content: yes.
  Covers (`pipeline/10-thumbnail.py`, each at https://d2ol7oe51mr4n9.cloudfront.net/user_3F8W7HJSSs1Z3chuyNCs9igUdIk/<media_id>.jpg):
  **A "WHY UPSIDE / DOWN?" (recommended)** on the tank window with the four pods head down (I0), an arrow to a pod's rounded head
  end: 1080×1920 5eb2324b-d3b7-4ebd-b3c8-58f9a7947011, TikTok 3:4 603577b1-e7ee-42d8-b8da-e483e0080f68. B "$80,000 / JUST THE
  HEAD" on the stack of head canisters (I3): 425e50d9-22bc-4a04-b9ab-6a5ba6c8a4c1, 3:4 807db354-8d0f-4db1-a27a-f6017b2848a2. C
  plain frame of the nitrogen at halfway with the pods head down (I1), no text: ce44d072-b356-4c97-952b-5e236afdc506.
  Known edit candidates: soil shows as the camera leaves the building past the cut edge of its block (0:28, 0:40–0:45,
  0:60–0:61), and at 0:42–0:44 the catwalk seems to stand on soil; C3 (the ice, 0:06–0:09) is two clean parts of its render
  joined by a 0.25 s dissolve at 0.73×; the power cut (0:37–0:38) is made in the edit; the ice pours from above the tub, not from
  a bucket; the arrows planned for B7, B14 and B18 were not drawn (three rings only).
  Script facts (Gate A, 16 Nov 2026; search summaries: Bloomberg, Quartz, Alcor's storage, protocol and cooling procedures and
  its fee schedule via cryonicsarchive.org, Merkle on the tank layout, CMAJ, Gray TV Nov 2026, CB Insights, a strawberry-thawing
  page, NYU on brain cell death): opening A ("If you want to cheat death, get frozen when you die."), chosen over the tightened
  cold claim I recommended ("In Arizona, people are stored upside down in steel tanks, waiting to be woken up. If you want to
  cheat death, they'll freeze you here after you die."); the script as made is `pipeline/10-script.txt` (7 "But"s, 5 "So"s; the
  terms vitrification and dewar, spoken only); the "that's why" is the frozen strawberry and the joke the crew's coffee thermos;
  the ending "Cool to glass, flip upside down, and wait."; comment question "Would you do it? Yes or no.". Checked at Gate A: the
  tanks need no power (Bloomberg, Quartz, Alcor's storage procedures); $220,000 for a whole body (2026 coverage) and $80,000 for a
  head (Alcor's fee schedule; one Nov 2026 report says $80,000–90,000); about 250 patients in 2026 coverage and 225 at the end of
  2023 by Alcor's count (said as "more than two hundred"); after death a team cools the body in ice water and a machine keeps the
  blood moving (Alcor's protocol; sources disagree on how many minutes the brain has, so no number is said); one tank holds four
  bodies, with heads in its middle column (five or six by source, so no count is said); no known cooling method avoids all
  cracking at liquid-nitrogen temperature (Alcor's procedures); ice crystals pierce a strawberry's cells, so it collapses when it
  thaws; from the section 2 checks: stored head down so the head warms last, −320 °F, the first man frozen in 1967 and still in
  storage, nobody revived. Changed from the draft: "That's why most members pay with life insurance" cut (nothing on the set
  shows it); "a company there" became "they'll freeze you here" (Alcor is a nonprofit); the opening's "more than 200 people are
  stored upside down" moved to line 20 (more than half the patients are heads only, and nothing found says the heads are stored
  upside down). Saturation on the exact title: no Short uses it; three small Shorts take the upside-down angle (best 1.6K); the
  closest in format is a 3D explainer of 8 Nov (1.4K) with a body standing upright in a tube; the topic's biggest Shorts are "Why
  Don't We Have Cryosleep Yet?" 6.2M, "The Science of Immortality: Cryonics and James Bedford" 4.3M, "Human Bodies Can NOT be
  Cryogenically Frozen" 3.2M and "Cryonics 101" 2.0M; Zack D. Films has no cryonics Short.

### 3.4c Lessons from video 01 (apply next time)
- **minimax_h3 failed 6 of 9 clip jobs** (all refunded; long-queued jobs fail most). The retry on **kling4_0** (`mode:"image-to-video"`, 720p, start_image only, 2.25 cr/s) succeeded 4 of 4 (one took ~15 min). Next time: submit on minimax_h3; retry failures once on kling4_0 instead of minimax.
- Kling returns 724×1284; it upscales to 1080×1920 fine. Minimax returns 1440×2560, 24 fps, ~0.17 s longer than asked.
- Still-to-still **wipes** (ffmpeg xfade wipeup/wiperight + push-in) are a good free substitute for build beats.
- ElevenLabs free tier is sometimes "busy": it may start only 1 of 2 takes. One take is enough.
- Word timings: local Whisper download is blocked; run faster-whisper `small.en` inside Higgsfield `sandbox_exec` on the ElevenLabs content URL, then map the times through the pause-tightening (timing.py).
- Fonts: `npm pack @fontsource/fredoka @fontsource/montserrat`, convert woff2 to TTF with fontTools, rename families to "HBX Caption" / "HBX Label". libass sizes at 1080×1920: caption 116 (y=1000), label 104 (y=560), labels start at "This is…" and stay ≥1.6 s.
- Loudness: loudnorm −14 + 2.6 dB + limiter gives about −15 LUFS.
- **Reusable scripts** are attached to the memory artifact as files (`pipeline/prompts.py`, `mk.py`, `fetch.py`, `timing.py`, `build.py`). Read them with Artifact `read` + `path`, copy them into the new video folder, and edit the beat list, labels and prompts.

### 3.4d Lessons from video 02 (apply next time)
- **minimax_h3 queue:** the account accepts about 11 active video jobs; more submissions are refused with `429 rate_limit_reached` (no job, no charge).
  Only ~3 run at once, and **every job left queued failed** (9 of 9, all refunded), while every job that started right away succeeded (8 of 8,
  pilots included). Next time: submit minimax in groups of **≤3**, wait until they finish, then send the next group. Kling has the same 429
  behaviour, so feed retries in groups of 2–4.
- **kling4_0 retries** (image-to-video, 720p, start frame only, 9 cr per 4 s) worked 9 of 9, but one (B9, a scenery-only underwater shot) invented a
  faceless mannequin swimmer. For shots with no mascot, put "No people, no swimmers, no characters" in the motion prompt, and drop the
  "The character only gestures" tail.
- **Still drift fixes:** a boat came out tub-shaped until the prompt said "seen side-on so the whole canoe is visible from end to end"; a single
  outrigger came out double until it said "ONE float … nothing on the other side". A big change in a ladder still (log → dugout) can reframe the
  camera slightly; later stills inherit it, which is fine.
- **This session could not reach the Higgsfield CDN** (`*.cloudfront.net` blocked by the network policy). Inspect stills and clips inside
  `sandbox_exec` with `image_paths`; build contact sheets locally from the tool-result preview JPEGs; give the user CDN links (their browser can open them).
- **pip in the Higgsfield sandbox fails** (`PermissionError: '/root'`). Get fontTools by curling its `py3-none-any` wheel from the PyPI JSON API,
  unzip into `/home/user/pylib`, run with `PYTHONPATH=/home/user/pylib`, and convert the fontsource **.woff** (WOFF1) files; WOFF2 needs brotli.
- **Narration pace varies by take:** this time 3.02 w/s raw (3.28 after pause tightening). Picked the faster of 2 takes and applied a pitch-preserving
  `atempo` 1.07 (limit 1.1) to reach 3.50 w/s, matching video 01. `02-timing.py` takes the speed as its 2nd argument. Whisper `initial_prompt` with the
  script's rare words, plus proportional alignment for "10,000"/"800", matched 235/235 words.
- **Gate D preview:** `02-build.py B1,B2,B3` renders the first beats with narration and captions; upload it (`media_upload`, PUT with headers
  `Content-Type: video/mp4` and `If-None-Match: *`, then `media_confirm`) so the user can watch the pilot in context.
- **Cover / thumbnail (Step 13, free, after delivery):** build it in the sandbox from the video's own frames (2K minimax frames are sharpest) with
  `02-thumbnail.py`: 0–4 words in Montserrat ExtraBold, yellow + white with a black stroke and drop shadow, one yellow arrow. Keep words and the
  subject inside the 3:4 profile-grid crop (y 240–1680 of 1920), clear of TikTok's right-hand buttons (x > 940 below y ≈ 950) and the caption
  zone (y > 1560). Make 3 concepts that each test a different reason to click (transformation split, the twist as curiosity, single action hero),
  check them as a 3:4 grid tile and at feed size. Covers must show what the video shows. Video 03 replaced the split with a stakes cover in two
  upload sizes; see "Covers for TikTok and YouTube Shorts" in 3.4e.
- **Scripts for video 02** (in the repo's `pipeline/` and attached to the memory artifact under `pipeline/`): `02-thumbnail.py` (covers), `02-prompts.py` (stills), `02-clips.py` (motion prompts + request builder), `02-whisper.py`, `02-timing.py`,
  `02-build.py` (assembly; preview mode), `02-jobs.tsv` (all job ids). Copy these as the starting point for video 03.

### 3.4e Lessons from video 03 (apply next time)
- **minimax_h3 ran only one job at a time today**, and 2 of its 3 jobs sat "queued" and failed (refunded). **kling4_0 ran up to 6 jobs at once with
  no failures (9 of 9) and accepts `start_image` + `end_image` keyframes** (`models_explore` get kling4_0), so it handles build beats too. Next time: send
  one minimax job; if it is still "queued" on its first poll, expect it to fail and put the remaining clips on kling4_0 (720p, 9 cr per 4 s, 11.25 per 5 s).
  Kling instead of minimax cost +4.25 cr over the quote.
- **Kling leaks state between beats.** In the fire shot it filled the hydrant barrel with water before the valve opened; in the crash shot it puffed
  water at the valve. Say what must NOT change ("the barrel stays dark, dry and empty with no water inside it, and the valve stays closed"); that fixed
  the fire redo. Free fix in the edit: `CUT` in `03-build.py` keeps only the first N s of a clip, then dissolves into the beat's still.
- **Still drift fixes:** a "buried" hydrant stayed visible until the prompt said "completely buried: above the surface there is only smooth white snow,
  no red visible at all"; a night still came out in daylight until it said "IT IS NIGHT, exactly like the reference ... no daylight at all".
- **Hidden By Design assembly (`03-build.py`):** 0.3 s xfade dissolves between beats; one-word captions in ALL CAPS Montserrat ExtraBold (preinstalled at
  `/usr/share/fonts/truetype/higgsfield/`), white with a 7 px black stroke and shadow, at y=1300 (~68%) instead of 75% so the cutaway's valve stays
  visible; long words auto-fit to 840 px; white rings, flow chevrons and movie letterbox bars are drawn as ASS shapes. **Draw ASS vector shapes from a
  top-left origin with `\an7`**: libass misplaces shapes drawn around negative coordinates.
- **Stills:** 22 stills in 5 rounds (S0 → S1 → the rest), each referencing the hydrant still so its design stays locked. seedream refused 1 of 9 in one
  batch with `429` (no job, no charge); resubmit it with the next round.
- **This environment reaches the Higgsfield generation CDN** (`d8j0ntlcm91z4.cloudfront.net`), so stills and clips can be downloaded and inspected
  locally. `media_upload` links (`d2ol7oe51mr4n9.cloudfront.net`) still can't be opened here; give those to the user.
- **Narration:** take A 3.04 w/s raw → 3.27 after pause tightening → `atempo` 1.07 → 3.49 w/s, the same as video 02. Whisper matched 269/269 words with
  the `initial_prompt`.
- **Covers for TikTok and YouTube Shorts (9 Nov 2026).** One design, two upload files (`03-thumbnail.py D`):
  - **Upload paths** (from third-party guides, not the platforms' own help pages; re-check): TikTok Studio on desktop → Edit cover → Upload cover,
    which crops the image to 3:4, so upload the 1080×1440 crop (y 240–1680 of the 9:16 master); the phone app may only let you pick a frame.
    YouTube Shorts custom thumbnails reached Partner Program channels in 2026 and are uploaded in YouTube Studio on desktop (the phone app may only
    offer a frame, during upload); Test & Compare does not cover Shorts. Upload the 1080×1920 JPG, kept under 2 MB.
  - **Overlays on a cover** (not on the playing video): TikTok's grid shows the 3:4 centre with the view count bottom-left; the YouTube app's Shorts
    shelf lays the title and view count over the bottom ~25% of the card, with a ⋮ menu top-right. Keep the headline between y ≈ 300 and 1440.
    TikTok's right-hand buttons and caption zone only cover the video while it plays.
  - **What goes on it:** the hero object, recognisable at tile size (cover A had no hydrant in frame), plus stakes the video pays off. Cover D uses
    the frame that sets up the climax (house on fire, barrel still dry) with two words: "IT'S EMPTY". It is the default now but unmeasured: compare
    profile taps and Shorts click-through with earlier videos once there is data.
  - **Typesetting:** one line, "IT'S" white + "EMPTY" yellow, Montserrat ExtraBold 165 px (~995 px wide) with a 16 px black stroke and shadow, a soft
    dark backdrop behind it on busy soil, and one curved yellow arrow to the detail.
  - **Check the claim against the pixels:** a cyan glint at the foot of the dry barrel read as water at thumbnail size; `neutralise()` greys it out
    so the picture matches the narration ("the empty barrel").
  - The script also writes phone-size mock-ups of the TikTok grid and the YouTube Shorts shelf (`thumb/mock_*.jpg`); look at both before delivering.
    Upload with `media_upload`, PUT (`Content-Type: image/jpeg`, `If-None-Match: *`), then `media_confirm`.
- **Scripts for video 03** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `03-script.txt`, `03-beat-sheet.md`, `03-whisper.py`,
  `03-timing.py`, `03-build.py` (Hidden By Design look, `CUT`, preview mode), `03-thumbnail.py` (covers A–D; `D` also writes both upload sizes and the
  platform mock-ups), `03-jobs.tsv` (all job ids). Copy these as the starting point for the next Hidden By Design video.

### 3.4f Lessons from video 04 (apply next time)
- **kling4_0 is now the default video model** (3.0). The single minimax_h3 pilot sat queued and failed again: every queued minimax job in videos 01–04
  has failed. Kling ran 6 jobs at once, 8 of 8 succeeded in about 4–6 minutes, and it now takes **3 s** clips (3–30 s), so a beat of 2.7 s or less costs
  6.75 instead of 9. Quote clips on Kling prices.
- **seedream_v5_pro accepts about 8 jobs at once**; the rest of a batch is refused with `429 rate_limit_reached` (no job, no charge). Send stills in
  groups of 8 and resend the refused ones when slots free up.
- **The cutaway STYLE formula leaks into every shot:** seedream sliced open a water bottle (granules and a filter inside), added a pool with a tap to a
  drought street, and put blue pumps under a kitchen counter. For shots that must look ordinary, say "NOT cut open", "an ordinary street view, not a
  cutaway", "no water anywhere". If the stray thing survives, **edit it out**: pass the still as the reference with "Change only this: remove …
  Everything else identical" (worked first time for the drought pool).
- **References copy the layout:** passing the hero wide (S0) as a reference for a different location (the drought street) reproduced the whole S0 scene.
  Use a reference only for "same scene, change X" edits or the same location; describe a new location in text only.
- **Make matching shots by editing one base still:** a fresh "salt-crusted tap" came out with no salt; editing a clean kitchen still into a salty one
  worked, and the same base gave the payoff shot (clean tap, drought hills outside the window). Two matching shots for 2.5 cr.
- **Close-ups:** "close-up of a gauge" gave a wide pump shot with a tiny gauge; "Extreme close-up: the gauge fills most of the frame" worked.
- **Journey ideas need more stills:** 27 beats and 25 distinct stills (30 generated) cost 37.5 cr; a single-set ladder idea needs fewer.
- **Narration:** Daniel's eleven_v4 takes ran slower this time (2.89–2.92 w/s raw, 3.20 after pause tightening), so the faster take needed `atempo`
  1.09 to reach 3.49 w/s. Whisper with the `initial_prompt` matched 271/271 words ("sixty" came back as "60" and was aligned by length).
- **`sandbox_exec` foreground calls time out at about 60 s in the MCP layer**, whatever `timeout_seconds` says. Keep foreground commands under ~50 s
  (no long `sleep`); run Whisper and renders with `background:true`. The full 27-beat render on `size:"xl"` took about 4 minutes.
- **Overlays on stills:** measure positions on a 100 px grid drawn over the still scaled to 1080×1920. `04-build.py` reads ring and chevron positions
  from `overlays.json` (each chevron path takes a `rot`; the stock chevron points up, so `rot -113` points it down-right along a rotor).
- **Saturation check before Gate A (6.3) changed the idea:** H13 (crane) was dropped for H15 after the search found 20+ near-identical Shorts.
- **Packaging pattern for the final cover and title (my read, unmeasured):** the cover puts a claim that sounds wrong on the payoff object ("THIS WAS
  THE OCEAN" over a glass of tap water) and keeps the context that makes it believable in frame (the plant and the sea through the window); the
  title front-loads the search words the topic's biggest Shorts use ("seawater", "drinking water") and adds a second hook the video pays off early
  ("(Without Boiling It)") instead of repeating the cover. I judged the curiosity cover with no topic cue (B "THEY ADD ROCKS") weaker at tile size,
  because nothing in it says "ocean". Compare D's click-through with video 03's "IT'S EMPTY" once there is data.
- **Network:** this session reached the generation CDN (`d8j0ntlcm91z4.cloudfront.net`), `upload.higgsfield.ai` from the sandbox and `www.youtube.com`,
  but not `pw-cdn.watercorporation.com.au` or `www.wa.gov.au`; search-result summaries were used for the Perth figure instead.
- **Scripts for video 04** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `04-script.txt`, `04-beat-sheet.md`,
  `04-prompts.py` (stills + `REFS`), `04-mk.py` (still requests), `04-clips.py` (motion prompts + request builder), `04-whisper.py`, `04-timing.py`,
  `04-build.py` (reads `overlays.json` and `cut.json`), `04-thumbnail.py` (covers A–C, upload sizes, mock-ups), `04-jobs.tsv`. Copy these for the next video.

### 3.4g Lessons from video 05 (apply next time)
- **Middle tier is the new default** (3.1): the user found Lite too still and Full too much. Animate the opening (first ~20 s), every build, the
  twist and the finale; keep analogies, asides and stat inserts as stills.
- **Saturation check: search the exact title first.** The 11 Nov idea check searched topic words (Aquarius, moon pool) and missed three
  near-identical "X Becomes an Underwater House/Base" Shorts from the previous two weeks (best 339K) that `yt_saturation.py` found at once on the
  exact title. The script then spent its first ~27 s on the shared basics and the rest on what they lacked (saturation, the bends, the 17-hour
  exit, NASA, real hurricanes).
- **ElevenLabs quota:** price the narration with `estimate_only:true` at Gate B (3.3 Step 3). eleven_v4 costs about 1 credit per character:
  1,368 per take of a 272-word script.
- **Daniel ran faster this time:** 3.16 w/s raw, 3.49 after pause tightening, so no `atempo` was needed (videos 02–04 needed 1.07–1.09×). Whisper
  matched 268/268 words; it splits hyphenated words ("forty -seven -ton") and the aligner spreads them.
- **Local assembly works in this environment:** the container has ffmpeg with libass, zoompan and xfade, plus Python, npm and pip. Fonts:
  `npm pack @fontsource/fredoka@5.1.0 @fontsource/montserrat@5.1.0`, then fontTools (`pip install --target <dir> fonttools brotli`) converts the
  700/800 woff2 files to TTF named "HBX Caption" / "HBX Label". The 26-shot render took under 2 minutes on 4 cores, with no 60 s tool limit.
  Reachable from here: the generation CDN, `upload.higgsfield.ai` (PUT with `Content-Type` and `If-None-Match: *`, then `media_confirm`) and
  `elevenlabsusercontent.com`. Not reachable: `huggingface.co`, so Whisper still runs in the Higgsfield sandbox (background job, ~1 min a take).
- **Stills:**
  - The Classic STYLE says "small diorama-like outdoor set" and "bright blue sky", so interior cutaways came out above water on a beach. For
    interiors and underwater shots add one line: "The tank is deep underwater: everything seen outside it is deep blue sea ...; no sky, no clouds,
    no beach and no waterline anywhere in the frame." (`UNDER` in `05-prompts.py`).
  - Name colours, not objects, in the palette line. Even so it added a toy island under the plane and a beach outside the kitchen window.
  - Stage edits can zoom in: adding the buoy reframed the shot until the prompt said "Keep exactly the same camera position, zoom and framing as
    the reference image ... stay exactly where they are and the same size" and sized the new part ("small in the frame, about the size the barge was").
  - "A towering wall of hurricane clouds" came out as a black smoke column rising off an island (a volcano). Write "the whole sky is dark grey with
    low, heavy storm clouds, and grey curtains of rain ...; no island, no land, no smoke, no volcano, no fire".
  - A dive-gear version of the mascot works: a 2:3 reference (`DIVER`) made from the locked reference keeps the yellow hard hat with a mask,
    regulator, tank and fins. Pass it on every underwater still.
  - "Edit it out" (3.4f) worked again: the sky at the end of a corridor became a closed hatch.
- **Clips:**
  - Kling accepted 13 jobs at once on Ultra (two batch calls of 8 and 5, no 429) and finished them in ~7–9 minutes.
  - Kling reads a diorama with the habitat close under the waterline as shallow water: in both storm versions the breakers crashed onto the tank
    and the sea calmed by the end, even with "no wave ever reaches the tank". Next time frame storm shots with much more water between the surface
    and the structure, or show the surface storm and the calm structure as separate shots.
  - Kling runs past the action: the door flood ended with foam pouring out of the cutaway, and the rush ended with the mascot flying out of the water
    at the sun. `CLIPWIN` in `05-build.py` keeps a window of a source clip (retimed 0.8–1.25×, then a held last frame with a push-in).
  - Start and end keyframe builds worked well (legs rising out of the sand; barge out, buoy in).
  - Clip lengths from the real timings: `ceil(len − 0.06)`, so a 3.02 s beat gets a 3 s clip played 1% slow (58 s of clips instead of 62 quoted).
- **Captions:** `02-build.py`'s 0.12 s minimum let short words overlap the next word for a frame ("Rush" + "Up" read as "RUph"). `05-build.py`
  pushes the next word back instead (no overlaps; at most 0.10 s behind the voice).
- **Composite story beats:** the user approved telling two real storms as one in the "you" story (the Rina early exit in 2011 and the Irma buoy loss
  in 2017). Flag composites like this at Gate A.
- **Network:** WebFetch could not reach `en.wikipedia.org` or `environment.fiu.edu`; WebSearch summaries were used for the fact-check.
- **Scripts for video 05** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `05-script.txt`, `05-beat-sheet.md` (with "As
  made"), `05-prompts.py` (STYLE, DIVER, UNDER, REFS, AR), `05-mk.py`, `05-clips.py`, `05-jobs.tsv` (all job and media ids), `05-whisper.py`,
  `05-timing.py` (sub-beat split B16b), `05-timeline.json`, `05-build.py` (camera move per still, WIPE fallback, CLIPWIN, label heights, depth line
  from `05-overlays.json`), `05-thumbnail.py`. Copy these for the next Classic video.

### 3.4h Lessons from video 06 (apply next time)
- **The shot rule held and cost less** (7.2): one main view, every still an edit of the one before it with the framing lock; 19 stills for
  18 used, 14 clips with no redos, 158.75 credits (video 05: 31 stills, 176). Beats without a clip stay in the view for free: `HOLD` repeats
  the last frame of the clip before with a slow push-in, and `WIPE` from `PREV` wipes or fades from that frame into the next still
  (`06-build.py`).
- **Saturation: search the place in the format too.** The exact-title search found nothing close, but "how a crack becomes petra" found
  "How a Cliff Becomes Petra" (27K, 29 Oct) with nearly our whole chain. Search the exact title, "how a [thing] becomes [place]" and
  "[place] how it was built" (Step 1). The script then spent ~15 s on the shared water basics and the rest on what it lacked.
- **Edits that move the mascot copy him:** S3 kept the man in the plaza and added one on the ledge. Add "he is the only person in the whole
  scene" (or "the ledge is empty") to every edit where he moves; S3b removed the copy with an edit-out (3.4f).
- **Kling camera words:** "Slow push-in" on the hook became a dolly-in to a close-up of the mascot. Put "The camera stays in the same place
  looking at the same cliff" (`FIXED` in `06-clips.py`) on every clip that must hold the main view, and always on a clip under an overlay
  (C8 carried the 39 M line).
- **Kling on Ultra took 12 jobs at once** (batches of 8 and 4, no 429); the first finished in ~4 minutes, the slowest in ~17.
- **Labels with the build in frame:** TikTok's top bar covers y < ~200 and the facade fills the upper middle, so labels sat in the clear band
  above the pool (y 1345) or below the basin (1440), measured on a 100 px grid (`06-labels.json`); two-line labels at 62–80 px.
- **"Slice the wall open" in seedream:** asked to cut away the rock beside the facade, it replaced the lower storey with the open room; a
  wipe from the finished facade sells it as a slice. Asked to slice the urn, it sliced the dome and turned the base to sand; a 1.2× crop
  anchored at the top (`top` move) hid it.
- **Narration:** Daniel ran slower again (2.95 w/s raw, 3.30 tightened), so atempo 1.06 reached 3.48 w/s. eleven_v4 billed 1,409 ElevenLabs
  credits per take of 263 words.
- **Network:** `huggingface.co` is still blocked (403), so Whisper ran in the Higgsfield sandbox (~1 min); one download from the generation
  CDN reset and worked on retry.
- **Scripts for video 06** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `06-script.txt`, `06-beat-sheet.md`
  (with "As made"), `06-prompts.py` (STYLE, SET, CAMERA, LOCK, OUTLINE, REFS), `06-mk.py`, `06-clips.py` (FIXED), `06-jobs.tsv` (all job and
  media ids), `06-whisper.py`, `06-timing.py`, `06-timeline.json`, `06-build.py` (HOLD, WIPE from PREV, one clip over two beats, labels,
  height line), `06-labels.json`, `06-overlays.json`, `06-thumbnail.py`. Copy these for the next one-view Classic video.

### 3.4i Lessons from video 07 (apply next time)
- **A two-sided arena in a vertical frame:** two cars side by side come out tiny in 9:16; stacked top to bottom and seen from high above
  they fill it (the user approved the steeper view at Gate A). The car facing the camera keeps its roof and we see the mascot through
  its windshield; the car facing away is opened from above so its cabin shows.
- **S0 took three fresh tries and one edit:** seedream drew the cars touching every time ("about two metres apart; they are not
  touching" was ignored), so the video opens frozen at the moment of contact. The diorama look needed video 06's wording ("a square
  block of ground … the front edge cut straight down like a slice of cake … a cross-section of … soil"); without it the pad came out like
  a photo of a car park. The 1959 batwing fins came only with "seen from above, its back end spreads into two wide, flat, wing-like tail
  fins that stick out past the sides of the car". In a top view, check which way each figure faces: the base still had the dummy facing
  backwards, and one edit turned it around.
- **Edits fixed pose and placement first time:** "no longer waves: grips the steering wheel and braces" (S1b); a crush that was too mild
  became one that reads when the edit named the distance and its effect ("about two feet back into the cabin, so the dashboard now
  presses against the dummy's knees", S2b); an airbag drawn beside him moved in front of him ("bursting out of the steering wheel he is
  holding … covers his chest and the lower half of his face", S4b). Pass the mascot reference again on stills that show him whole (his
  beard faded in S6).
- **A glowing part as free motion:** an edit of the same frame with one part glowing (the cage orange, the steering columns red), faded
  in over the last frame of the clip before, reads as an x-ray reveal at no clip cost.
- **Kling handled a slow-motion crash between keyframes:** 11 of 11 clips usable as rendered (61 s), including 9 s and 7 s clips that
  crush the cars from one still to the next. All nine clips of the second batch were accepted at once on Ultra and finished in ~7–17
  minutes (the 3 s belt clip was the slowest). A small motion (a belt pulling tight) does not read from high above; a free push-in on
  the hold after it sells the line (`('focus', fx, fy, zoom)` in `07-build.py`).
- **Text when the subject fills the middle:** the impact point sat at mid-frame, so captions moved to the old car's trunk (y 1330) and
  labels went into one left-hand column (TikTok's buttons are on the right); long labels sit on the red car's roof. Scoreboard counters
  roll the number up (`count` in `07-labels.json`); the final question has its own boxed style (`Verdict`).
- **Narration in parallel:** the voice script is fixed at Gate A, so the two takes can start as soon as Gate B is approved. Pick the take
  from Whisper's punctuation and pauses: take B read "The question is where?" as a question and ran "holds. Worst case" together. Take A:
  88.72 s raw (3.07 w/s), 78.44 s with tightened pauses (3.44), atempo 1.03 → 76.16 s (3.55 w/s); Whisper matched 270/270 words.
- **One clip can carry two lines:** `07-build.py` builds segments of several beats (C2 B2–B3, C4 B6–B7, C5 B10–B11, C7 B14–B15). A clip
  up to ~4% short of its lines plays slightly slower instead of buying another second.
- **Fact-check network:** classroom.iihs.org and the blog that reviews the IIHS report are outside the network policy; WebSearch
  summaries were used for the figures.
- **Scripts for video 07** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `07-script.txt`, `07-beat-sheet.md`
  (with the changes after Gate B), `07-prompts.py` (STYLE with the steep view, SET as a cut diorama block, OLD, NEW, DUMMY, CUTAWAY, LOCK,
  REFS), `07-mk.py`, `07-clips.py` (FIXED, SLOW), `07-jobs.tsv` (all job and media ids), `07-whisper.py`, `07-timing.py`, `07-timeline.json`,
  `07-build.py` (multi-beat segments, focus moves, counters, the Verdict style), `07-labels.json`, `07-thumbnail.py`, `07-ladder.jpg`.
  Copy these for the next matchup.

### 3.4j Starting point for the first Cutaway video (15 Nov 2026; video 08 was made from it the same day, and its lessons are in 3.4k)
- **What changed and why:** the look and its six rules are in 3.4, the measurements behind them in 7.5. Read both before the beat sheet.
- **Scripts to start from** (repo `pipeline/`): the build from `07-build.py` (segments of several beats, holds on a clip's last
  frame, focus push-ins, cue timing without overlaps); the caption and shape drawing from `04-build.py` (ALL CAPS Montserrat
  ExtraBold; the ring and the chevron as ASS shapes drawn from a top-left origin), with `PF` and `Fontsize` 130, `CAPY` 1440 and
  `MAXW` 900; the still chain from `06-prompts.py` (`LOCK`, `CAMERA`: every still an edit of the one before); the clip wording from
  `06-clips.py` (`FIXED`) and `07-clips.py` (`SLOW`); the cutaway wording from `04-prompts.py` and `03-beat-sheet.md`, without the
  object words (3.3 Step 4).
- **Take out of the 03–04 build:** the 0.3 s `xfade` between beats (Rule 3); the shots made from a still with a push-in (`zoompan`
  is now only for a hold on a clip's last frame, 3 s at most); and the 0.12 s minimum cue that let two words overlap.
- **New drawing to write:** a solid arrow in place of the chevron path (`m 0 34 l 34 0 l 68 34 l 68 48 l 34 14 l 0 48`): about
  200 px long, white fill, a soft shadow (`\shad`), three or four sliding along the flow 0.3 s apart. The ring with `\bord16`.
- **What the pilot must answer** (Gate D): does a start-and-end-frame clip carry the camera from one stage to the next without the
  set changing shape? Does a middle keyframe let one clip pass through three stages? Is 1080p worth its price next to 720p with a
  sharpen? **Answered by video 08 (3.4k):** yes to both (all 11 clips held the set's shape, including a glide from the house down
  into the ground); 1080p was not tested (the user chose 720p at Gate B).
- **Check before delivery:** `python3 pipeline/analysis/check_video.py final.mp4` (`pip install numpy opencv-python-headless` first).
  Targets: 80% or more of the seconds moving, no stretch without movement longer than about 6 s, caption letters about 57 px at
  about 75% down, and moving and still seconds about equally sharp. `contact_sheet.py` makes one-frame-a-second sheets for reading
  a video shot by shot; `under_the_voice.py` shows what sits under a narration (target for our mix: the quietest moments 18–22 dB
  below the voice).
- **Reading TikTok from a session** (a correction to the note at the top of section 4): the `-0` and `-1` format suffixes do not map
  to fixed hosts. On 15 Nov 2026 the allowed host (`v16-webapp-prime.us.tiktok.com`) carried `-0` for some videos and `-1` for
  others, and the mapping changed between two calls. Read the format list with `yt-dlp -J`, pick a format whose URL is on the v16
  host, and if the download is refused try the other suffix. The profile page (`https://www.tiktok.com/@handle`, fetched with a
  browser user agent) carries `followerCount`, `heartCount` and `videoCount` in its embedded JSON.

### 3.4k Lessons from video 08, the first Cutaway video (15 Nov 2026; apply next time)
- **The motion check failed although every line has a clip.** Clips cover 74 s of 79.5 s (93%) and no line lost its clip, yet
  `check_video.py` counts only 20% of the seconds as moving (16% without the pointer arrows), against the 80% target. The checker
  takes the camera move out, then counts a second only when the average change over the whole frame passes 0.8 grey levels.
  - **What moves is too small in the frame.** The main view is the whole house, and the motion is water inside a pipe a few pixels
    wide, faint see-through haze and a rat the size of a fingernail. The still-camera clips (the 12 s hook, the flush, the 12 s
    Hong Kong stretch) scored 0.07–0.34 a second, below our holds (a still under a slow zoom: 0.42–0.54).
  - **Camera moves made from crops of one still don't count.** After Gate D the main-view clips got moves between the approved
    still and a crop of it (free). Kling then zooms or pans across a flat picture, which the checker removes exactly: those clips
    scored 0.4–0.8. I told the user at Gate D that camera moves would lift the score; moves made from crops cannot.
  - **What counted:** a move to a different still with its own perspective (the glide from the night house into the ground to the
    flap close-up, 3.4–8.1 a second, and the pull back from it, 7.9), the light changing (dusk 1.3–3.2, dawn 1.1–1.4) and the
    pointer arrows (0.6–0.9).
  - **Next time** (made into rules the same day: 3.4 Rules 2, 3 and 7; 7.7): plan a camera path with a real still for each camera
    position (3.3 Steps 2 and 5), frame each problem so what moves fills a good part of the picture, and show the pilots'
    `camera_path.py` and `check_video.py` numbers at Gate D (3.3 Step 7). Whether the measure tracks how people watch is open:
    compare video 08's views with videos 03 and 04 (7.5).
- **Stills (26 tries for 14 on screen, 32.50 credits against 20 quoted; budget ~1.8 tries a still in this look):**
  - The first S0 put the sewer pipe 75% down the frame, under the captions. Shrinking the picture to 76%, lifting it, extending the
    edges and one seedream clean-up edit fixed it (the house in the top ~63%). Next time give the layout in the S0 prompt ("the roof
    peak about 10% from the top, the sewer pipe about 60% down, plain soil below").
  - Seedream would not put a small thing inside a pipe in the wide view: three flap tries and two rat tries put them outside or on
    top of the pipes. What worked: a see-through window in the pipe (the rat swims in it) and a separate close-up still (the flap).
  - Grain grows with every edit of an edit (high-pass noise on a plain wall 8.3 → 16.3 over four edits). Denoise a still before it
    goes to Kling (`cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 7, 21)`), or branch edits from an earlier, cleaner still.
  - The STYLE line says "Bright soft daylight", so a night edit needs "IT IS NIGHT, with no daylight at all (the daylight described
    above does not apply to this picture)" (`NIGHT` in `08-prompts.py`).
- **Clips:** all 11 held the set's shape at the first try, so nothing was redone. Kling took the batch of 9 at once on Ultra and
  finished it in about 4 minutes. A middle keyframe works (3.3 Step 7).
- **Assembly (`08-build.py`):**
  - The clip after a hold starts at the hold's zoom and eases back over 0.8 s (`EASE_AFTER`); the first cut snapped back to the
    wider framing at each of the three holds.
  - A 3 s clip over a ~2 s line plays whole and faster, up to 1.7× (`FULLFIT`); trimming its start made a jump from the clip before.
  - Measure arrow paths on a frame of the clip they sit on, with a 100 px grid, not on the still: Kling's framing drifts a little
    from the keyframe.
  - Captions: `Fontsize` 114 gives the 57 px letters (3.3 Step 10).
- **Sound (the first video with it; recipe and prices in 3.3 Step 6b):** the bed and effects come as stereo files and the voice is
  mono. Copy the voice to both channels (`pan=stereo|c0=c0|c1=c0`), or `amix` follows the voice and folds the whole mix to mono
  (the first cut's side channel was −68 dB). Set the levels on the mono fold-down (`rms_db()`), which is what one phone speaker
  plays and what `under_the_voice.py` measures: set that way, the stereo mix's quietest moments measured 21 dB under the voice
  (inside the 18–22 target); set from ffmpeg's own mono downmix of each file, the same mix measured 24 dB.
- **Narration:** take B, 3.17 words/s raw, 3.48 after pause tightening, so no `atempo`. 2 takes × 1,399 ElevenLabs credits.
- **Scripts for video 08** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `08-script.txt`,
  `08-beat-sheet.md` (with "As made"), `08-prompts.py` (STYLE, SET, CAMERA, HOUSE, LOCK, HAZE, NIGHT, RAT, REFS), `08-mk.py`,
  `08-clips.py` (FIXED, the crop-keyframe moves), `08-jobs.tsv` (all job and media ids), `08-timing.py` (pause tightening, beats and
  the clip plan), `08-plan.json`, `08-timeline.json`, `08-words-takeB.json`, `08-build.py` (segments, holds, `EASE_AFTER`,
  `FULLFIT`, the stereo mix, captions and arrows), `08-thumbnail.py`, `08-post-copy.md`, `08-ladder.jpg`. Copy these for the next
  Cutaway video.

### 3.4l Lessons from video 09, the first travelling-camera video (15 Nov 2026; apply next time)
- **The travelling camera works with our tools.** Ten real camera positions on one set, every clip flying between two of them, met
  every Rule 1 and Rule 7 target (3.4b), against video 08's 20% and 45%. Kling flies between two stills of the same set from
  different angles with real parallax (the hook: 1.11 px, more than twice the reference), and a middle keyframe carried one 6 s clip
  through three positions (the climax: bathroom, wide, ground). Electricity animated well: bolts, a glow racing along cables and
  pipes, an arc, roots of light in the soil.
- **Stills (35 tries for 20 on screen, 1.75 each, as budgeted):**
  - Camera positions are edits of the wide with `POS` ("The same house, set and storm as the reference image, with the same parts,
    colours and materials. New camera position: …"); changes at a position use `LOCK` (wide) or `LOCKZ` (close-ups: "everything in
    view stays exactly where it is", which names nothing out of frame). "Extreme close-up" was again needed for a part to fill the
    frame.
  - The style key came out as a thin slab on a dirt plain until it said "the block of ground is deep: below the lawn its front is
    cut straight down all the way to the bottom edge of the frame … there is no ground in front of the block".
  - Describe parts as the camera sees them: "the right end of the ridge" on a front-gable house put the rod on the slope; "the peak
    of the roof, at the front end of the ridge" worked.
  - Seedream joins new parts to old ones: the lightning cable was clamped to the water pipe until the prompt said "stands a little
    to the right of the water pipe and does not touch it". It drops parts too: the bonding clamp lost the cable until the prompt
    named it as staying.
  - The STYLE line's cutaway and cyan water leak into close-ups: upstairs rooms got soil under them ("nothing below the bathroom
    floor is in view: no soil, no lawn, no pipes") and the living room got a cut floor over water ("the floor is solid wood and
    nothing is cut open; there is no water anywhere"). Kling needs the same words: C11's first render flooded the room.
  - A position that fails twice is dropped rather than forced: the attic close-up mixed attic and soil both times, so C2 lost its
    middle keyframe and flew without it.
  - Grain stayed low (no edit chain longer than three), so nothing was denoised.
- **Clips (18 renders for 16 clips):**
  - Every keyframe of a clip must agree on the state of things. C15 started on a drained tub and passed through a wide still with a
    full one, and Kling refilled the tub on screen; Bo was remade with the water kept (the line only needs the shower off).
  - A move of one storey down a wall (C8, from the bathroom floor to the foundation) scrolled a second copy of the house up from
    under the ground, in both renders. Fixed in the edit (`SPLICE` in `09-build.py`: the clean start and end at 0.66×, joined by a
    0.3 s whip with vertical motion blur). Next time give such a move a middle keyframe, or end it at a position that shows the same
    storey.
  - A change clip at one position can come back with a dead-still camera although the prompt asks for a drift (C7, 5 s). Check
    each with `camera_path.py`; a push-in of 3% a second or more in the edit fixes it (`PUSH`), and the clip after eases back out
    (`EASE_AFTER`).
  - Kling took 12 clips at once on Ultra and finished them in about 9 minutes; the pilots took about 13.
  - Plan clips about a second longer than their lines in total (81 s for 75 s); the build fits them at 0.94–1.15× (3 s clips over
    ~2 s lines play whole at up to 1.38×).
- **Pointers pinned to the picture** (Rule 6) are in `09-build.py` (`POINTERS`, `track()`): Lucas–Kanade points near the pointer
  give a similarity transform from the anchor frame to every frame, and the arrows and the ring are drawn per frame in ASS, scaled
  with the zoom. Measure positions on a gridded frame of the rendered segment (`seg/<clip>.mp4`), at the moment the camera arrives.
- **Sound:** the ElevenLabs sound estimate prices each effect at its default length (395) while the run billed 131.67 for 39.5 s
  (3.33 a second): budget from the durations. Put each effect's loud moment on its picture: measure the flash frame (brightest
  frame of the clip) rather than trusting the word. An effect can be cut short (`FX` third value: fx5 cut at 2.9 s so the tub does
  not drain by ear when it stays full on screen).
- **Narration:** take A ran 3.34 words/s raw and 3.63 after pause tightening, faster than any earlier take, so the video is 75 s for
  270 words. Pick the take that reads "So you…" straight through (take B paused after each "So").
- **Covers:** when no still holds the moment, build the cover from a frame of the clean master (cover A, 0:09).
- **Network:** weather.gov and cdc.gov were blocked for WebFetch in this session; the fact-check used search summaries.
- **Scripts for video 09** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `09-script.txt`,
  `09-beat-sheet.md` (with "As made"), `09-prompts.py` (STYLE, WIDE, SET, CAMERA, HOUSE, STORM, LOCK, LOCKZ, POS, REFS, and the
  redo notes), `09-mk.py`, `09-clips.py` (STORMV, ONE, one clip per segment with optional middle keyframes), `09-jobs.tsv` (all job
  and media ids), `09-whisper.py`, `09-timing.py`, `09-plan.json`, `09-timeline.json`, `09-words-takeA.json`, `09-build.py`
  (`POINTERS` with tracking, `SPLICE`, `PUSH`, `EASE_AFTER`, `FULLFIT`, effects with cuts), `09-thumbnail.py`, `09-post-copy.md`,
  `09-flightmap.py`, `09-flightmap.jpg`, `09-ladder.jpg`, and `analysis/pilot_measure.py` (Gate D numbers next to the reference).
  Copy these for the next video.

### 3.4m Lessons from video 10, cryonics (16–17 Nov 2026; apply next time)
- **The travelling camera held up on an indoor set.** Nine positions in one sliced-open lab, every clip flying between two real
  stills, beat every Rule 1 and Rule 7 target (3.4b), better than video 09. The hook and the climax pilots passed Gate D first
  time (parallax 0.40 and 1.46 px).
- **A set with no water:** the Cutaway STYLE without "translucent cyan water" (section 2 rule 2), plus NITRO in every tank prompt
  ("looks exactly as in the reference: clear and very pale … it is not water and it never glows"). The style key still drew the
  liquid nitrogen pale blue-white; matching the reference rather than fighting it kept every later still the same colour.
- **The style key decides the layout; fit the plan to it.** Seedream gave a three-quarter view and a tank with a big see-through
  window instead of a removed front half. Rewriting the position prompts to the picture's real layout (the hook over the middle
  tank, the oldest tank at the right end) worked first time; asking for the planned layout would have fought every edit.
- **The STYLE line's "sliced open … what is buried" leaks into indoor stills and clips.**
  - Stills: soil grew under the hall floor (two tank close-ups) and a jar was buried under the lab counter. One line fixed all
    three: INDOOR ("This is an indoor close-up: nothing is cut open, and there is no soil, no ground, no pit and nothing buried
    anywhere in the frame").
  - Clips, in the middle of a move: a pit with roots and stones opened in the floor (C4A), a pit of rubble under the table
    (C6A), the floor turned into a raised wooden step with layered sides for about 3 s (C7A), and the cabinet behind the ice tub
    turned to soil for about 1 s (C3). Both stills at each end were clean, so only the clip shows it. The re-renders with "The
    floor is solid grey and nothing is cut open: no soil, no pit, no steps, no wooden layers" came back clean (C4, C6, C7).
  - **Next time put that floor line in every clip prompt of an indoor set from the start**, and check each clip at about five
    frames a second (a sheet at 0.2 s): the one-frame-a-second sheet of the final caught C3 and C7 only after the build.
  - When the camera is still, cut the bad stretch out instead (free): `SPLICE` in `10-build.py` now takes `"fade"`, a 0.25 s
    dissolve between the clean start and end of the same shot (C3, at 0.73×), which reads as the fog clearing.
  - Kept: soil seen as the camera leaves the building past the cut edge of its block of ground (C8, C11, C12, C16). It reads as
    the edge of the diorama.
- **ffmpeg's xfade slide transitions write junk on their first frame.** The whip (`slideleft`) drew a bright green strip down the
  left 34 columns for one frame. `fillborders=…:mode=smear` during the whip hides it (`whip_join` and `seg_splice` in
  `10-build.py`). Check the first frame of every whip; video 09's `slideup` splice may have had the same on its top rows.
- **Kling held the camera still in four clips** (C3 the ice, C5 the strawberry, C17 the crack: changes at one position; C19 the
  closing drift). The edit adds the move: `PUSH` (a push-in of 12–15% toward the change), the clip after easing back out
  (`EASE_AFTER`), and `PULL` on C19, which starts zoomed in and pulls back to exactly the first frame's framing, so the loop lands.
- **Neighbouring positions in one room are best made from each other.** The table and the tray made from the wide lost the
  room's ceiling (open sky) or landed in the wrong room; made from the door close-up (D0) they kept the room.
- **A detail the wide drew wrong carries into every edit of it:** the wide's four short capsules came back twice in the tank
  close-up. A LOCKZ edit of the near-miss that names the swap ("the four short capsules are gone; in their place stand four long
  pods… like the pod in the second reference image", the hoist still as the second reference) fixed it in one try.
- **"Extreme close-up … almost touching the window … the frame is not in view"** got the stack of canisters; "close on the
  middle column" gave back the same framing as the tank view, which would have left C14/C15 without a real move.
- **A lights-off re-grade did nothing** (the still came back almost as bright). Lighting changes are cheaper and surer in the
  edit: `LIGHTS` in `10-build.py` dips brightness, saturation and gamma between two times and flickers back on. The dip fools
  `camera_path.py` into two big-move seconds (0:37–0:38); read around it.
- **Effects:** time each from its measured loud moment (fx5's clunk is its first 0.5 s; fx1 is a steady tone, cut to 1.8 s).
- **Narration:** Daniel ran 3.04 words/s raw (the slowest yet), 3.37 after pause tightening; atempo 1.06 gave 3.53 w/s and a
  76.2 s video for 269 words. Writing "dewar" as "doo-er" in the text sent to the voice gave "DOO-er"; the captions keep DEWAR.
  1,417 ElevenLabs credits per take; the bed and 7 effects cost 128.33 for 38.5 s (the estimate said 385).
- **Covers:** check that the arrow lands on the thing the words name. The first draft of cover A pointed at the middle of a pod;
  the head end is its rounded bottom (`HEAD_A` in `10-thumbnail.py`).
- **Session restarts:** the scratchpad path changed after a restart, and the MCP tools reconnect. Keep job ids in `10-jobs.tsv`
  and commit often; the Higgsfield sandbox keeps Whisper output for 24 hours. huggingface.co and the upload CDN are blocked
  here, so the word timings were copied out of the sandbox's output.
- **Scripts for video 10** (repo `pipeline/` and attached to the memory artifact under `pipeline/`): `10-script.txt`,
  `10-beat-sheet.md` (with "As made"), `10-prompts.py` (STYLE without water, WIDE, SET, CAMERA, BUILDING, NITRO, NOWATER, FLOORS,
  POD, POS, LOCK, LOCKZ, INDOOR, REFS, and the redo notes), `10-mk.py`, `10-clips.py` (LIGHT, ONE, the floor line in C4, C6 and
  C7), `10-jobs.tsv` (all job ids), `10-whisper.py`, `10-timing.py`, `10-plan.json`, `10-timeline.json`, `10-words-takeA.json`,
  `10-build.py` (`WHIP` with `fillborders`, `SPLICE` with `fade`, `LIGHTS`, `PUSH`, `PULL`, `EASE_AFTER`, `POINTERS`),
  `10-thumbnail.py`, `10-post-copy.md`, `10-flightmap.py`, `10-flightmap.jpg`, `10-keyframes.jpg`, `10-first-last.jpg`. Copy
  these for the next video.

### 3.5 Things that will go wrong, and the fix
- **Structure drifts between stages:** always pass the previous stage still as a reference and say "everything else identical". Regenerate the still, not the clip.
- **Video model adds text or subtitles:** add "no text, no captions, no letters" to the prompt and regenerate once.
- **Clip starts frozen:** add "motion starts on frame 1" and regenerate once.
- **Character lip-syncs:** add "the character does not talk; mouth closed".
- **Narration runs long:** cut words from the script; don't speed it up.
- **Balance too low for the quoted tier:** offer Lite, or fewer animated beats. Never start a run you can't finish. (Cutaway look: name the lines that would become holds; 3.1.)
- **A still of something in motion looks frozen** (a pour, a splash, smoke, a gauge needle; videos 03–04 had many): give the line a clip, or hold the frame before it. Never cut to a new still (3.4 Rule 1).
- **The same stray object turns up in every shot:** an object word in the shared style line. Move it to the prompt of the shot that needs it (3.4 Rule 4).
- **The last frame doesn't match the first:** make the END still by editing the last stage still, and compare it with Stage 0 at Gate C.
- **A night or storm shot changes the render** (glowing water, redrawn pipes; video 03's fire shot): make it by editing the day still and say "the same water colour as the reference; nothing glows; only the light changes".
- **The sound competes with the voice:** lower the bed until `under_the_voice.py` reports the quietest moments 18–22 dB below the voice, and drop any effect that lands on a stressed word. If in doubt, deliver the voice-only master and say so.
- **Every line has a clip, and `check_video.py` still says the video is mostly still** (video 08: 93% clips, 15% moving): the motion is small in the frame (water inside a pipe, faint haze, a small animal in a wide view) and the camera moves are zooms across a flat face, which the checker takes out. Frame closer on what moves, make it bigger, and fly the camera through the set between real camera positions rather than zooming toward it (3.4 Rules 2, 3 and 7; 3.4k).
- **A jump where a clip meets a hold or a trimmed clip:** the clip after a hold should start at the hold's zoom and ease back (`EASE_AFTER` in `08-build.py`), and a 3 s clip over a 2 s line should play whole and faster (`FULLFIT`), never lose its first frames.
- **The set changes from one camera position to the next** (pipes move, colours shift): make each position by editing the wide still with "The same [set] as the reference, with the same parts, colours and materials … Nothing in view changes", compare the positions side by side at Gate C, and regenerate the one that drifted.
- **A travel clip only zooms** (`camera_path.py` shows parallax near 0): its two stills are the same view at two sizes. Make the end still a real camera position (lower, closer, from the side) and render it once more.
- **Something changes back during a clip** (video 09: a drained tub refilled as the camera pulled back): a keyframe of the same clip shows the old state. Make every keyframe of one clip agree on the state of things, or drop the change from the line.
- **A move of one storey up or down a wall stacks a second copy of the house** (video 09, C8, both renders): give the move a middle keyframe, or join the clean start and end with a whip in the edit (`SPLICE` in `09-build.py`).
- **A change clip comes back with a dead-still camera** (video 09, C7): add the drift in the edit, a push-in of 3% a second or more toward the change, with the next clip easing back out (`PUSH`, `EASE_AFTER` in `09-build.py`).
- **Close-ups grow soil, cut floors or cyan water** (the STYLE line leaking): say in the still and the clip prompt "nothing below the floor is in view", "the floor is solid wood and nothing is cut open; there is no water anywhere".
- **A pit, a step or soil opens in an indoor floor in the middle of a clip, though both stills are clean** (video 10: C4A, C6A, C7A and C3): put "The floor is solid grey and nothing is cut open: no soil, no pit, no steps, no wooden layers" in every clip prompt of an indoor set, check each clip at about five frames a second, and render a bad one again once with that line. Where the camera is still, cut the stretch out and join the clean parts with a short dissolve (`SPLICE` with `"fade"` in `10-build.py`).
- **A one-frame coloured strip at the edge of a whip** (video 10: bright green down the left edge): ffmpeg's xfade slide transitions write junk on their first frame. Smear the edge columns during the whip (`fillborders` in `whip_join`, `10-build.py`) and check the whip's first frame.
- **A lights-off or night still comes back almost as bright as the day still** (video 10, L1): make the change in the edit instead (`LIGHTS` in `10-build.py`: a dip of brightness, saturation and gamma that flickers back on).

---

## 4. Second reference account: @1hidden_by_design ("Hidden By Design")

Studied 8 Nov 2026 (https://www.tiktok.com/@1hidden_by_design). All 9 videos were downloaded with yt-dlp (pin a format ending in `-0`,
served from the allowed `v16-webapp-prime.us.tiktok.com`; the `-1` mirror on v19 is blocked), transcribed with faster-whisper in the
Higgsfield sandbox, and sampled as contact sheets. The comment sections and the bio's Payhip guide (payhip.com is outside the network
policy) could not be read. (15 Nov 2026: the suffix does not map to a fixed host; see 3.4j.)

**This is the account our look comes from.** Since 15 Nov 2026 our videos are made in its look, without a character (3.4). That day
its storm drain, roof and landfill videos were downloaded again and measured against our two best (4.4, 4.5, 7.5).

### 4.1 The account
- 9 videos, 25 Oct to 8 Nov 2026, now 2 a day. 33.9K followers, 509K likes. The profile was created in May 2025, but these are its only posts.
- Bio: "Learn how I create these animations 🎬 Get the step-by-step guide below ↓", linking to a paid Payhip guide. 4 of the last 5 videos end
  with "If you wanna make videos like this, check out the link in my bio." The channel's business is selling the method.
- Same narration formula as @howbuildingexplained (and our videos), aimed at a different subject: **the hidden engineering behind everyday
  things you use or walk past.** The cutaway is the brand.

| Video (title as posted, abridged) | Posted (UTC) | Length | Views | Likes | Shares | Saves |
|---|---|---|---|---|---|---|
| Where Does the Water Go When Your Street Floods? 🌧️ | 25 Oct | 74.7 s | **9.2M** | 402.8K | 16.7K | 32.8K |
| You Drill a Hole… Now the Whole Neighborhood Has Water 💧 | 30 Oct | 75.9 s | 926K | 43.5K | 2,903 | 8,165 |
| How do you dig under a river without letting the water in? 🌊 | 6 Nov | 74.2 s | 494K | 13.7K | 319 | 1,187 |
| How Do You Turn a Garbage Dump Into a Park? 🗑️ | 8 Nov | 78.2 s | 431K **in 4 h** | 11.7K | 561 | 1,011 |
| How Do You Build a Bridge When the Foundation Is Underwater? 🌉 | 26 Oct | 64.6 s | 380K | 14.4K | 681 | 1,343 |
| You flush. It disappears. Here's where it actually goes. 🚽 | 28 Oct | 68.2 s | 236K | 11.0K | 864 | 1,470 |
| How Do Those Giant Power Lines Get Electricity to Your House? ⚡ | 7 Nov | 87.7 s | 159K in 23 h | 10.0K | 471 | 1,611 |
| You Fill Up Here Every Week… But How Does It Work? ⛽ | 7 Nov | 87.9 s | 37K in 25 h | 1,553 | 48 | 223 |
| Why Doesn't Rain Leak Through Your Roof? 🌧️🏠 | 8 Nov | 77.2 s | 19K in 1.5 h (too new) | 579 | 23 | 34 |

Snapshot 8 Nov 2026, 21:30 UTC. Hashtags on every post: #HowItWorks #Engineering #LearnOnTikTok, often #3DAnimation, plus 1–2 topic tags.

**15 Nov 2026:** 10 videos, 21.1M views. Storm drain 9.9M, roof 4.2M, landfill 3.9M, water well 991K, river tunnel 900K, bridge
foundation 423K, power lines 347K, sewer 303K, gas station 112K, beach 44K.

### 4.2 Why it works
1. **Universal, hidden, and moving.** Everyone sees a storm drain, a tap or a manhole; nobody sees what's underneath. Each topic moves
   something (water, sewage, power, trash) along a path the camera can follow, so the title can ask "where does it go?" or "how does it get here?"
2. **Water is the star.** The five best mature videos all have water as the payload or the enemy (drain, well and tower, under-river tunnel,
   underwater foundation, sewer). Translucent water in a cutaway is satisfying to watch, and it hands the script its problems (floods, leaks,
   seepage, backflow).
3. **This refines our "avoid mundane utilities" rule.** Mundane works when the workings are hidden (storm drain, 9.2M). It still flops when
   the workings are already visible: the gas station flopped on both accounts (37K here, 41K on HBE).
4. **Titles name one concrete mystery the viewer owns:** "your street", "your house"; a paradox ("dig under a river without letting the
   water in"); or a transformation ("turn a garbage dump into a park"). The flop had the vaguest title ("...But How Does It Work?").
5. **Fast first problem.** The first "But" lands at 2.5–3.5 s on the top videos and at 4.6–6.5 s on the weaker ones.
6. **The top three end on a loop.** All three close on a three-beat imperative that flows back into the hook, with no "Congratulations" and
   no CTA: "...Bury the pipes, pave the road, and let it rain." → "If you cut a hole in your street, the rain has somewhere to go."
   So far every video that ends on "Congratulations" or the creator CTA has fewer views than these three (small sample; the landfill
   video has the CTA and is climbing fast).
7. **One continuous camera.** 8 of 9 videos have 0–2 hard cuts in ~75 s. The gas station had 27 cuts and close-up montages, and it flopped.
8. **Length.** The three best run 74–76 s; both 88 s videos underperformed. All run over 60 s (TikTok's Creator Rewards only pays on
   videos over a minute, which may be why).
9. **One small human joke per video:** "somebody's missing tennis ball", "your street becomes a swimming pool", "your drain becomes a
   fountain", "stroll over the same trash they left at the curb".
10. **A "that's why" viewers can check on their next walk:** "Those are the manholes you drive over every day." "That's why the handle
    clicks when your tank is full."

### 4.3 Script formula as they use it
```
HOOK (0-3s)  If you [naive action], [it sort of works].
             "If you cut a hole in your street, the rain has somewhere to go."
             (or a question: "You flush your toilet, and everything disappears. But where does it actually go?")
LOOP x7-8    But [problem]. So [fix]. (This is a [TERM].)        first "But" by ~3 s
THAT'S WHY   "Those are the manholes you drive over every day."
END          three-beat imperative that loops into the hook: "Bury the pipes, pave the road, and let it rain."
             (weaker variant: "Congratulations, you've built a [X]." + "If you wanna make videos like this, check out the link in my bio.")
```
- 235–326 words in 64–88 s, 3.4–4.0 words/s (top three: 269–302 words in ~75 s).
- Fixes are often bare imperatives ("So line the hole with compacted clay...", "Push a giant steel shield into the ground").
- Real terms are named only 0–4 times per video ("This is a catch basin."), and never shown as on-screen labels.
- Stakes are everyday disasters (flooding, sewage in the yard, collapse, fire, contamination, blackout), not the HBE "deadliest X" twist.

### 4.4 Animation style
- **Look:** bright, clean, photoreal-leaning 3D render: soft sunny daylight, warm tones, soft shadows, mild depth of field, clean materials
  (concrete, grey PVC, steel, terracotta roof tiles) and translucent cyan water. Almost certainly AI image-to-video, not hand animation
  (two long videos a day, morphing details, and they sell a "how I make these" guide). The landfill, roof and gas videos switch to an
  overcast, drone-documentary look with real-looking workers.
- **The cutaway is the signature:** the ground is sliced like a cake to show soil layers (topsoil, gravel, sand, clay, a blue groundwater
  band) with the pipes, chambers and tanks inside. Machines and fittings get see-through housings (check valve, fuel nozzle, transformer coils).
- **The world:** the same idyllic suburb every time (cream houses, terracotta roofs, blue shutters, lawns, a curving road, a creek), with a
  yellow excavator, a blue drill truck, and white or blue sedans.
- **No mascot.** "You" is the viewer. People appear only as hands at a tap, a woman flipping a light switch, small figures walking, or workers.
- **Camera:** one continuous, slowly moving camera. Transitions are fly-throughs that follow the flow: down the grate into the pipe, up the
  well to the kitchen tap, along the wires from the plant to the house. The camera path is the story. **Measured on the power-lines
  video (15 Nov 2026, 7.7):** the camera reaches about 11 positions in 88 s, moves in 66% of the seconds and is never still for more
  than 5 s; it has been our model since then (3.4 Rules 2, 3 and 7).
- **Build moments:** each fix appears on the same cutaway set (pipe slides in, chamber grows, tank fills). This is our stage-ladder method.
- **Explainer devices:** small flat white arrows for flow and force, a white highlight circle, and a final labelled cutaway "summary
  diagram" (landfill: Cap, Gas Wells, Subsurface Waste, Bottom Liner System).
- **Captions:** one word at a time at ~72–78% of frame height (just above TikTok's caption area). Video 1 used lowercase white rounded sans
  with a soft shadow; from video 2 on, ALL CAPS heavy sans, white with a black stroke and drop shadow. No other on-screen text.
- **Covers:** a mid-video frame showing the most satisfying cutaway (the catch basin with grit, leaves and the tennis ball). No headline text.
- **End overlays:** an animated TikTok "FOLLOW" button with a cursor click, or a red YouTube "SUBSCRIBE 🔔" button, in the last ~3 s
  (they probably cross-post to YouTube Shorts).
- **Format:** 9:16, 30 fps, uploaded at 1080×1920.
- **Measured on 15 Nov 2026** (the storm drain and the roof, with `pipeline/analysis/check_video.py`; 7.5):
  - Something in the picture moves in 84% and 87% of the seconds. The longest stretch without movement is 6 s and 4 s.
  - No hard cuts and no cross-fades were found: the camera travels from one detail to the next.
  - Each stays in one place from start to finish: one street, one house. The roof video shows small workers and gloved hands
    doing the work.
  - Caption letters are about 62 px tall (storm drain, lowercase) and 54 px (roof, ALL CAPS), at 75% and 77% of the frame height.
    In the storm drain the lower ~40% of most frames is plain dark soil, and the captions sit on it.
  - Pointers are small solid white arrows with a shadow, three or four at a time (storm drain), or long thin white arrows (roof).

### 4.5 Audio (measured, not listened to)
- The same narrator in all nine: fast, even and lively, almost certainly an AI voice. Median pitch ~150 Hz with a wide 118–239 Hz range,
  which suggests a male voice with lively intonation.
- A quiet, low, non-melodic stereo bed (ambient or cinematic pad) under the mono voice: pauses sit only 12–14 dB below speech. Integrated
  loudness about −23 LUFS. The gas station had a steadier, more tonal bed.
- **Re-measured on 15 Nov 2026** (storm drain, roof and landfill, with `pipeline/analysis/under_the_voice.py`): the bed is there
  71–93% of the time, the mix falls only 19–20 dB below the voice in its quietest moments, and the side channel sits 21–22 dB below
  the whole mix. There are few separate bursts, so no event sound effects to speak of. TikTok lists every video as "original sound".
  (The 12–14 dB above came from a different window; both measures say the bed is always there.) How this compares with the other
  accounts, and the recommendation for our videos, is in 7.5.

### 4.6 Topics @1hidden_by_design has already done (avoid)
Storm drain, water well and water tower, road tunnel under a river, landfill into a park, bridge foundation in a river (cofferdam), sewer
and wastewater treatment, power grid, gas station, roof.

### 4.7 Production notes for this look (retired 11 Nov 2026; current again since 15 Nov 2026)
- **15 Nov 2026:** this look is ours again, as the Cutaway look. 3.4 has the rules; where a note below disagrees with 3.4 (the split
  cover of 3.4d shows the mascot, for one), 3.4 wins.
- The stage ladder fits this look: one cutaway set, one hero angle, one fix added per stage. Add a cutaway line to the STYLE FORMULA, e.g.
  "photoreal 3D cutaway cross-section, the ground sliced open to show soil layers and the pipes inside, bright sunny daylight, clean
  materials, translucent cyan water".
- Link stage stills with continuous camera moves (start and end keyframes on neighbouring stages) instead of hard-cut close-up montages.
- End on a three-beat imperative that loops into the hook. Put any CTA after it, or leave it out.
- Cover: a mid-video cutaway frame, or the split cover from 3.4d.

---

## 5. Kickoff prompt, renewed 18/11/26 (paste this to make a video)
**Renewed 18/11/26:** this is the current version. On 18 Nov 2026 the user added three fortress stories, F1–F3, to section 2 and
asked for this prompt to be updated to match, with the new date. The IDEA line now names the open ideas (X1–X4 and F1–F3; X5 was
made as video 10), the first script rule says how to start from an F idea (it has an opening and numbered story beats, not a
script), and a new rule carries the F ideas' structure: the place named only at the end, and every "But" a way an enemy could get
in. Nothing else changed. The 15/11/26 v2 version (the travelling camera the user approved after video 08: 3.4 Rules 2, 3, 5, 6
and 7; 7.7) is in the repo history at commit `309d785`; the first 15/11/26 version (the Cutaway look with one main view) is at
`db03adc`, and the 11/11/26 version, for the character look, at `f8bf298`. Fill in the three lines in angle brackets and paste the
whole block into a new session. SOUND defaults to "bed and effects" (3.4).
```
KICKOFF PROMPT (renewed 18/11/26)

Read CLAUDE.md in AliKandaz/short-form-video-memory (or the "Short-Form Video Memory"
artifact) first, all sections. Then make a video with the section 3 runbook.

IDEA:   <X1, X2, X3 or X4, or F1, F2 or F3, from section 2, or your own topic>
TIER:   <Middle | Full>   (Middle unless I say otherwise)
SOUND:  <bed and effects | voice only>   (bed and effects unless I say otherwise)

Fixed choices (3.4):
- Look: Cutaway, no character. One place sliced open like a cake, bright and clean,
  with translucent cyan water. "You" is the viewer. Hands, small workers or machines
  appear only where the work needs them. No labels on the picture.
- Camera: move it like @1hidden_by_design's power-lines video ("How Do Those Giant
  Power Lines Get Electricity to Your House?", section 7.7). The camera flies around
  and into the set, in to each change and away again, and is almost never still.
- The seven rules of the look:
  1. Animate nearly all of it. Every line is a clip; plan no holds. A hold is only
     the fallback for a lost clip: the last frame of the clip before, 3 s at most.
     Never show a frozen splash, pour, smoke or gauge needle.
  2. One set, a travelling camera. Stay on the one sliced-open set and add each fix
     to it, but give it 8-12 camera positions: the wide view only to open, to close
     and to step back once or twice, and every problem and every fix seen up close
     from its own position. Anything that needs another place is shown on the set
     or cut.
  3. Every clip flies the camera from one position to another, and each position is
     a real still of the set from there, never a crop of another still. On "But"
     push in or swoop to where the problem happens; let the change play out close
     while the camera keeps drifting; on "So" pull away or fly on. No still-camera
     clips and no cross-fades; a whip only for a far jump; a cut only where the
     setting truly changes.
  4. Hold the look steady. Make every still by editing the wide still or a
     neighbouring position, so the set keeps its parts and colours from every
     angle. Keep objects out of the shared style line. Night and storm are a
     re-grade of the same picture. The first and last frames match part for part.
  5. Captions: one word at a time, ALL CAPS, about 57 px tall, about 75% down the
     frame. Wide shots keep the subject in the upper 60% with plain ground below; in
     close-ups the caption sits over whatever is there, with its stroke and shadow.
  6. Pointers: solid white arrows about three times the old size, moving along the
     flow, and a thicker ring. One device per beat. They appear when the camera
     arrives at a detail and stay pinned to it while the camera drifts; the camera
     never stops for a pointer.
  7. Measure the camera with pipeline/analysis/camera_path.py: moving in 65% or more
     of the seconds, median parallax 0.3 px or more, big moves in at least one second
     in eight with no gap over 15 s, and never still for more than 5 s.
- Narrator: Daniel (3.4). Video model: kling4_0 (3.0).
- Sound: a quiet, steady bed that fits the place and four to eight short effects where
  something visibly happens, all well under the voice. No music. Keep a voice-only
  version too.

Script rules, on top of section 1:
- For an idea from section 2, start from its set and its draft script there.
  The script is a draft. An F idea has an opening, numbered story beats and an
  ending line instead of a script: write the script from them.
- For an F idea (a fortress story), keep the place's name out of the title, the
  caption and the narration until the reveal line just before the ending
  ("This is ___."), then give one line on what became of it. Every "But" is a
  way an enemy (or thirst, cold or hunger) could beat the place, and every "So"
  answers it at its own spot on the set.
- Open with "If you..." and land the first "But" by ~3 s. If the idea also has a
  cold-claim opening in section 2, show me both at Gate A.
- Aim for ~75 s: ~260-280 words at our 3.5 words/s. Never under 60 s.
- 7-8 But/So beats that escalate. Name the real term after the key fixes (spoken only).
- Write for the set and the camera: every line must be something we can show happening
  on the one cutaway, most lines should describe something moving, and each problem
  and fix should happen at its own spot on the set so the camera has somewhere to fly.
  Show comparisons and stats on the set itself or cut them. Cut any line that would
  need a picture of another place, and tell me at Gate A which lines you cut or moved
  onto the set.
- Build in one "that's why" viewers can check in real life and one small human joke,
  both shown on the set.
- End on our own line: a three-beat imperative that loops back into the hook (4.3).
  Never "Congratulations, you have built..." (How Building Explained's signature line).
- Fact-check every ⚠ claim before Gate A and cut anything unverifiable. Never reuse any
  reference account's wording.
- Before Gate A, run pipeline/youtube/yt_saturation.py on the title and tell me how many
  near-identical Shorts exist and the best view count.

Credits: check the balance first. If it's below the quote, offer a smaller plan and tell
me which lines would lose their clip, instead of starting. In the quote, price the clips
at 720p and at 1080p and show both totals, and price the sound (ElevenLabs credits).

Stop for my approval at Gate A (script and title, with where the camera is on each
line), Gate B (credit quote), Gate C (stills: the camera positions on one set as a
flight map, the set matching from every angle, the first and last frames matching)
and Gate D (pilot clips: the hook flying down to the first change, and one clip that
flies between two camera positions, each with its camera_path.py and check_video.py
numbers next to the power-lines video's). Spend no credits before I approve Gate B,
and don't render the rest until the pilots move like the reference.

When the video is done, give me:
- the final MP4 link, and the voice-only version of the same video so I can compare
  the two by ear
- the share of the running time that moves (check_video.py; target 80% or more), the
  camera numbers (camera_path.py; the Rule 7 targets) and any line that lost its clip
- 3 cover options (3.4d), one of them a plain mid-video cutaway frame with no text
- TikTok post copy: the title or a hook question with one emoji, then #HowItWorks
  #Engineering #LearnOnTikTok #3DAnimation and 1-2 topic tags
- YouTube post copy per 6.4: a title under ~60 characters (the question the video
  answers, or "How a ___ Becomes ___"), no hashtags in it; a 2-3 sentence description
  with one question and at most 3 hashtags; audience "not made for kids"
Then log the video in 3.4b (and mark the idea used in section 2 if it came from there),
add any new lessons, and update both copies of the memory.
```

---

## 6. YouTube channel audit and the format on YouTube (9–10 Nov 2026)

The user asked for a channel review ("username? profile pic? what can I do better to blow the channel up"). The channel was read from
public pages with `pipeline/youtube/yt_snapshot.py` (how-to in 6.7). The audit was delivered in chat on 10 Nov 2026. **Whether the user
applied the fixes in 6.2 is unknown: re-run the snapshot before relying on 6.1.** Conclusions marked "my read" are Claude's
interpretation of the data, not measured facts. **15 Nov 2026:** the snapshot was re-run and most of the fixes are in: see the end
of 6.1.

### 6.1 Channel snapshot (10 Nov 2026, 08:54 UTC)
- **@overthinkingyearly**: 13 subscribers (9 the evening before), 6 Shorts, about 4.3K total views, only a Shorts tab.
- Bio left over from an older concept: "Welcome to The Empire Outpost — where history meets fun for an educational and entertaining
  journey." No channel keywords, country or links.
- Avatar: a cartoon portrait (curly-haired person, teal hoodie, orange-purple background) with no link to the videos. Banner: the same
  picture, so the desktop banner shows a strip of forehead and eyes.
- TikTok @overthinkingyearly: 7 followers, 6 videos, 65 likes.
- **TikTok on 13 Nov 2026 (22:30 UTC):** 44 followers, 485 likes, 6 videos, 34.7K views: seawater 25.5K, hydrant 6.1K, canoe 1.5K,
  mud house 990, Aquarius 376 (2 days old), Petra 291 (1 day old). About 1.3 followers per 1,000 views. So far the everyday "how does
  it work" questions beat the famous places on TikTok (small sample, and the last two are young). The bio now reads "Start with
  something simple. Add problems, A few fixes later it's a project." The plan to reach 1,000 followers is in `tiktokshop.md` section 4.

| Short | YouTube id | Posted | Views | Likes | Notes |
|---|---|---|---|---|---|
| 03 Fire hydrant | `CHSiOhYhCx0` | 9 Nov | 1,857 after 9.5 h | 143 | 2 comments: a hydrant installer agreeing about the movie myth; "Not true on paint" (the NFPA 291 cap colours are a recommendation that many towns don't follow) |
| 02 Canoe | `VFxSJ_sCHEg` | 7 Nov | 7 | 1 | **served in made-for-kids mode** (6.2) |
| 01 Mud house | `FRwZoiwTwJY` | 6 Nov | 1,795 | 86 | 1 hostile comment about bricks drying "for weeks" (NMSU: adobe bricks cure 3–4 weeks, so the script is right) |
| ASMR marble run | `PnFGPBCMRKc` | 5 Nov | 5 | 0 | off-niche AI clip |
| bubble wrap ×2 | `1C52H0poplc`, `Ly1sETBBq34` | 3 Nov | 1,356 / 1,249 | 3 / 9 | off-niche AI clips; one viewer commented "Ai!!!!!" |

- Titles as posted: "How Mud Can Become A House In The Desert | comment below what you would like next"; "How A Fallen Tree Can Become A
  Canoe In The Jungle #engineering #HowItWorks #Science #learnonyoutube"; "Why Don't Fire Hydrants Freeze? ❄️🚗 #HowItWorks #Engineering
  #Learn #3DAnimation". Every description is empty.
- Covers are mid-video frames carrying one caption word ("Dry", "The", "COLORS"). The channel is not in the Partner Program, so the
  designed covers (3.4d, 3.4e) can't be uploaded on YouTube yet; only a frame can be picked.

**Snapshot on 15 Nov 2026 (03:10 UTC), both platforms.** This is the data behind the move to the Cutaway look (7.5).

| Video | Character | TikTok views (likes · comments · shares · saves) | YouTube views (likes) |
|---|---|---|---|
| 04 Seawater | no | 28.7K (314 · 6 · 32 · 54) | 8,217 (339) |
| 03 Fire hydrant | no | 6,213 (115 · 0 · 3 · 6) | 166,949 (5.2K) |
| 02 Canoe | yes | 1,664 (23 · 1 · 2 · 2) | 169 (11) |
| 01 Mud house | yes | 1,448 (42 · 1 · 2 · 5) | 2,072 (100) |
| 05 Aquarius | yes | 385 (19 · 1 · 0 · 1) | 1,244 (66) |
| 06 Petra | yes | 302 (13 · 0 · 0 · 4) | 34 (3) |
| 07 1959 vs 2009 car (8 hours old) | yes | 162 (4 · 0 · 0 · 1) | 5 (1) |

- The two videos without the character hold 90% of the TikTok views (34.9K of 38.9K) and 98% of the YouTube views (175.2K of 178.7K).
- **YouTube:** the channel is now **LetZBuildTogether** (@LetzBuildTogether), with 282 subscribers (13 on 10 Nov) and 7 Shorts. The
  three off-niche clips are gone. Description: "Start with something simple. Add problems. A few fixes later it's a project. Animated
  build explainers, one problem at a time. Every script is researched and fact-checked." The mascot profile picture and the "ONE
  PROBLEM AT A TIME" banner (6.8) are live. Video 02 is out of made-for-kids mode (comments on). Videos 01 and 02 carry the 6.2
  retitles; video 03 still has its first title, with four hashtags and an empty description.
- **The hydrant Short went from 1,857 views to 166,949 in five days**, our first video to leave the test batch on YouTube. Sixteen
  comments were read: several local corrections (cap colours mean different things in different towns; a hit hydrant does spray in
  Los Angeles and Baton Rouge), praise for the dog line, a UK and an Australian viewer describing underground hydrants, and two
  "AI" remarks ("🤖 ai 🤖", "AI SLOP").
- **TikTok:** 48 followers, 530 likes, 7 videos, 38.9K views.
- **A caution on 6.3 and 6.4 (my read, from one video):** our best YouTube result has a "why" title, hashtags in the title and an
  empty description, all things 6.4 advises against. The packaging advice is unproven, and "becomes beats why" (6.3) did not hold
  for us. The video had to do the work.

### 6.2 Problems found, and the fix recommended to the user
1. **Video 02 is served in made-for-kids mode**, which is why it has 7 views: comments are off, "Save to playlist" is missing, there is
   no "Original Sound" pivot, and the hashtags in its title are not links. The other five Shorts have none of this. Fix: Studio →
   Content → the video → Details → Audience → "No, it's not made for kids", and set the channel default (Settings → Channel → Advanced
   settings). Only Studio shows whether the user picked it or YouTube's classifier set it. If the video stays flat after the fix,
   re-upload it with the 6.4 title and delete the old copy.
2. **Three channels in one:** a handle that reads like a journaling channel, a history-channel bio, AI ASMR clips, and build explainers.
   Fix: make the three ASMR Shorts private, rewrite the bio, rename (6.5), replace the avatar with the locked mascot and make a real
   banner. The avatar and banner were made on 10 Nov 2026 from existing renders at no credit cost (6.8). (The audit message gave the
   banner's text area as 1235×338; that is the area for the 2048×1152 minimum upload. On a 2560×1440 upload it is 1546×423.)
3. **Packaging:** calls to action and four hashtags inside titles, empty descriptions. Fix: the 6.4 checklist. Suggested retitles:
   "How Mud Becomes a House in the Desert", "How a Fallen Tree Becomes a Canoe", "How a Pipe in the Street Becomes a Fire Hydrant".
4. **Three videos, two looks:** videos 01–02 use the centred Title Case caption and the "Congratulations, you have built…" sign-off,
   which are How Building Explained's look and signature line; video 03 uses ALL CAPS captions, no mascot and a loop ending. Fix: one
   caption style, the mascot in the first and last shot of every video, and our own closing line. **Settled the other way on 15 Nov
   2026:** one look, the Cutaway look of video 03, with no mascot (3.4).
5. **Comments:** reply to all of them in the first day and pin a question. The hydrant comments are worth answering with facts.

### 6.3 The format on YouTube Shorts (benchmarks, 9–10 Nov 2026)
"How a ___ Becomes ___" took off on YouTube around mid-October 2026 and is now copied by hundreds of channels.

| Channel | Subscribers | Videos | Best Shorts | Notes |
|---|---|---|---|---|
| **You Made It** (@youmadeit3d) | 128K | 13 | Jungle Hole → Cu Chi Tunnels 36M (24 Oct), Cave → Home 23.5M (23 Oct), Crate → Plane 12M, Hole in Your Yard → Basement 8.8M, Spoon → Escape from Alcatraz 4.8M, Log → Raft 3.7M (21 Oct), Bunker 2.8M, Rented House → $70 Million Bank Heist 2.1M, Coffin → Your Way Out of the Grave 1.6M; lowest 94K | bio: two creators, real 3D scenes, about 12 hours a video, "new videos every week", "no reused clips" |
| **You Built It** (@youbuilt_it) | 64.7K | 60 | Hole in Your Yard → Swimming Pool 8.3M (11 Oct), Strip of Dirt → Road 5.6M, Stack of Boards → Roof 3.4M, Hole in Your Roof → Fireplace 3M, Septic Tank 2.7M, Fallen Tree → Log Cabin 2M, Running Water 1.7M, Field → Colosseum 1.1M; recent ones 6.5K–422K | a small in-scene "YOU BUILT IT" yard sign |
| How Building Explained (@HowBuildingExplained) | 31.8K | 24 | Nipa Hut 7.4M, Levee 5.3M, White House 5.1M, Nuclear Power Plant 1.4M | description is "4665465", no banner |
| Mildly Elsewhere (@MildlyElsewhere) | 31.2K | 137 | Why Guardrail Ends Peel Away 9.4M (mostly crash mechanics); Hole Under Your House → Basement 1.2M, Hole in the Desert → House 868K (7 Nov) | phrase captions, corner watermark |
| How Things Were Built (@HowThingsWereBuilt) | 12.3K | 118 | Canoe → Submarine 1.9M, Sign on a Stick → Traffic Light 590K, Hole in the Ground → Well 199K; recent ones 2K–31K | |
| Low Poly Films (@LowPolyFilmss) | 11K | 28 | Big Hole in the Backyard → Swimming Pool 6.4M, Nuclear Test Shaft 1.3M; most 20K–50K | |
| Jeff (@Jeff-Labs) | 953 | 180 | Why Wipers Used to Stop at Full Throttle 990K, Ship's Anchor 354K; most 1K–2K | daily "why" mechanics |
| How Things Hold Up / But Then, So | 68 / 17 | 11 / 20 | best 2.3K / every video about 1.2K | "why" cutaways with tidy branding |

What it shows:
- **About 1–2K views is the default test batch** for a new channel (ours: 1.8K and 1.9K; But Then, So: twenty videos at ~1.2K). Branding
  doesn't move it: How Building Explained has three 5M+ Shorts with a junk description and no banner. The video has to hold viewers.
- **Quality beats volume.** The biggest channel has 13 videos; the daily one has 180 videos and 953 subscribers.
- **"Becomes" beats "why" on YouTube right now** (my read; channel size confounds it). Same topics, both framings: Sign on a Stick →
  Traffic Light 590K vs "The Hidden Wire That Turns Your Red Light Green" 1.3K; Garden Hose on the Ceiling → Fire Sprinkler 61K vs
  fifteen-plus "Why Fire Hydrants Don't Freeze" Shorts in a month whose best is 14.5K.
- **What the multi-million titles promise:** something you'd want in *your yard* (pool, basement, bunker, running water), survival (cave,
  raft, log cabin), or a true escape, heist or war story (Cu Chi, Alcatraz, the bank heist). Landmarks do less (Colosseum 1.1M,
  Hoover Dam 171K, pyramid 82K, castle 56K).
- **Our old idea lists were everyone's idea lists** (both removed 11 Nov 2026). Searched 9 Nov: castle 14 near-identical Shorts (best 56K), Panama Canal 10+ (43K),
  well 14 (1.7M), cave home 14 (23.5M), lighthouse 9 (127K), Hoover Dam 8+ (171K), bank vault 8 (29K), pyramid 9 (82K), Antarctic
  base 1 (26K in two days). "How a Ditch Becomes the Panama Canal" and "How a Wooden Box Becomes a Bank Vault" exist word for word.
  From section 4: crane (Jeff, 74K), elevator, traffic light, P-trap, sprinkler and water tower are all done. A search for an Alaska
  log cabin found no Short under that title (You Built It has Fallen Tree → Log Cabin, 2M). Not searched: the underground town
  (You Made It did Derinkuyu, 1.1M), the Alps tunnel, the space station (Mildly Elsewhere has "Turn Your House Into a Space Station", 71K).
  Searched 10 Nov: H13 crane, 20+ near-identical Shorts (best "How Do They Get Cranes Down From Skyscrapers?" 932K, "How cranes get on top of the
  building" 892K, "How Tower Cranes Build Themselves Taller!" 747K in 8 days), so it was dropped. H15 seawater: survival distillation Shorts are huge
  (Zack D Films' Roman sailors 13.5M, real-footage distillation clips 3.5M and 1.1M, a cartoon 1.0M), while city-plant explainers stay small (Sydney Water 139K,
  Nexus Digest 52K, recent 3D ones 1.2–1.5K); the exact title "How Seawater Becomes Drinking Water" is taken.
  **Before Gate A, run `pipeline/youtube/yt_search.py "<title>"` and report how many near-identical Shorts exist and the best view
  count.** A crowded topic can still win in the Shorts feed, but bring something the others lack: a true story, a named place, "your yard".
- **Look (my read from four frames per video):** the leaders render real 3D scenes as a block of ground sliced open, usually from one
  camera angle, and the build changes in place. Our videos 01–02 cut between separate, better-looking shots with no sliced ground.
  Their first frames are calm and use the same one-word "If" caption as ours, so our opening words and caption style are not the
  problem. The 23.5M cave video does move between views, so the single angle is a tendency, not a rule.
- **Like rates:** ours are 4.8% and 7.7% of views at test-batch scale; the leaders sit at 2–3% at millions of views. Viewers who stay
  like the videos. What we can't see from outside is how many swipe away. **Ask the user for "Viewed vs swiped away" and average
  percentage viewed from Studio for videos 01 and 03** before changing the script formula. (15 Nov 2026: the user said "forget
  about the retention graphs". Don't ask for these; use them only if the user offers them. 7.5.)

### 6.4 YouTube upload checklist (apply from video 04)
1. Audience: "No, it's not made for kids", on the upload and as the channel default. After publishing, run `yt_snapshot.py`; it flags
   made-for-kids mode.
2. Title: `How a [humble thing] Becomes [Y]` (or the idea's `If You…` form), under about 60 characters. No hashtags, no call to
   action, no "| …" suffix.
3. Description: two or three sentences that retell the premise with the named problems, one question for the comments, then at most
   three hashtags.
4. Pin a comment that asks what to build next. Reply to every comment in the first day.
5. "Altered content" disclosure: tick it when the scenes look photoreal (the Hidden By Design look). Re-check YouTube's help page for
   the current rule. **18 Nov 2026:** YouTube's own announcement exempts clearly unrealistic content such as animation, and a set
   sliced open like a cake can't be taken for footage, so I recommended that the user stop ticking it for the Cutaway videos. No
   source says the label changes reach, and the collapse of 6.10 began with Petra, which was not photoreal. The user's decision
   is open (6.10).
6. Cover: pick the frame of the finished build or the most dramatic beat. Uploading a designed cover needs the Partner Program.
7. Raise at Gate A and Gate C: the Cutaway look (locked by the user on 15 Nov 2026, see 3.4): no character, one set seen by a
   travelling camera (7.7), wide shots with the subject in the upper 60% of the frame, one caption style, and a closing line that is
   ours rather than "Congratulations, you have built…". (History: the audit's single-angle, build-in-place suggestion became the user's shot rule on 11 Nov 2026, first
   inside the Classic look, and carried over to the Cutaway look on 15 Nov 2026: 3.4, 7.2 and 7.5.)

### 6.5 Rename shortlist (not used: the user renamed the YouTube channel themselves)
**15 Nov 2026:** the YouTube channel is now **LetZBuildTogether** (@LetzBuildTogether); the user chose their own name some time after
10 Nov. TikTok is still @overthinkingyearly. The shortlist below is kept for the record.

Free on both YouTube and TikTok on 9 Nov 2026, by handle lookup (`pipeline/youtube/handles.py`); YouTube can still refuse a handle
for its own reasons.
- **Seven Problems Later** (@sevenproblemslater): recommended. It describes the format, could become the closing line ("Seven problems
  later, you have a…") and an on-screen problem counter. **Just Add Problems** (@justaddproblems), **A Few Problems Later**
  (@afewproblemslater), **First You Dig** (@firstyoudig), **Starts With Mud** (@startswithmud).
- Taken, or too close to an existing channel: You Built It, You Made It, But Then So, How Things Hold Up, Fix By Fix, Built That Way,
  Looks Simple, OverBuilt, One Fix Later, Problem Fix Repeat (TikTok, same niche), Sounds Simple, Minute Builds, Pocket Engineering.

### 6.6 Platform facts (from web searches on 9 Nov 2026; re-check before quoting)
- **Partner Program:** 1,000 subscribers plus 4,000 watch hours in a year or 10M Shorts views in 90 days. From **1 Feb 2027** new
  applicants need 8,000 hours or 20M Shorts views (announced 10 Aug 2026). The fan-funding tier stays at 500 subscribers plus 3,000
  hours or 3M Shorts views.
  Also from 1 Feb 2027 (YouTube's Shorts monetisation policy page as summarised by web search, 11 Nov 2026): Shorts ad money is paid
  only for months in which the channel has 10M qualified Shorts views in the 90 days ending on the 15th of the month before. Sources
  disagree on whether channels already in the program are exempt.
- **Inauthentic content** (the monetisation rule, renamed in July 2025): guidance of 16 Jul 2026 lists generic or template-based
  videos, unsatisfying content, and AI personas giving advice as not eligible for ads. YouTube reviews whole channels. This is one
  more reason to keep the AI ASMR clips off the channel and to keep scripts researched and original.
- **Custom Shorts covers:** since July 2026 for Partner Program channels, in Studio on desktop. Everyone else picks a frame.
- **Made for kids** turns off comments, the notification bell, and saving to playlists or Watch Later.
- **Handles:** two changes per 14 days; the old handle is held for 14 days.
- **Banner:** upload 2560×1440 (minimum 2048×1152, 16:9, at most 6 MB). TVs show all of it; desktop shows the full-width strip
  y 508–931 (desktop serves the banner with crop parameters for the middle 29.4% of the height, read from the channel page); phones show
  the centre 1546×423 (x 507–2053), which is the 1235×338 text-and-logo area YouTube publishes for the minimum size, scaled up.
  Third-party guides, 9–10 Nov 2026. **Profile picture:** square, 800×800 is the usual recommendation, shown as a circle as small as
  ~24 px (not verified on YouTube's help pages).

### 6.7 Reading YouTube from a session
- The Default environment allows `www.youtube.com`, `i.ytimg.com`, `yt3.ggpht.com` and `yt3.googleusercontent.com` (added 9 Nov 2026).
- `/watch?v=<id>` redirects cloud IPs to a Google bot check on a blocked host; `/shorts/<id>` and channel pages work. The player
  response is bot-gated, so there are no captions, storyboards, durations or downloads. Views, likes, dates and comments come from
  `ytInitialData` and the `youtubei/v1/browse` continuation.
- Frames without downloading video: `https://i.ytimg.com/vi/<id>/frame0.jpg` (first frame) and `oar1.jpg`, `oar2.jpg`, `oar3.jpg`
  (about 25%, 50% and 75%; `oar2` is the default cover).
- Pace requests about 2–3 s apart. Scripts in `pipeline/youtube/` (exact usage is in each docstring; all but the first take a work
  directory as their first argument): `yt_snapshot.py @handle` (channel facts, per-Short stats, comments, made-for-kids check),
  `yt_channels.py <dir> handle:@name shorts:<id>` (a channel's latest and most popular Shorts; who posted a given Short),
  `yt_search.py <dir> "<query>"` (saturation check), `yt_saturation.py <dir> "<query>"…` (the same check, summarised to the top
  Shorts and long videos per query, for vetting many topics at once), `handles.py <dir> yt|tt <handle>…` (is a handle in use).

### 6.8 Channel branding (made 10 Nov 2026, no credits)
The user asked for "an updated profile picture and something I can put in my banner that will fit". Delivered on 10 Nov 2026.
**Both were live on the YouTube channel on 15 Nov 2026** (`yt_snapshot.py` prints the avatar and banner URLs). The mascot was retired
from the videos that day; the user has not asked for new artwork, so don't change it unless they do.
- **Files** (repo `branding/`): `avatar-800.png` (800×800), `banner-2560x1440.png` (1.6 MB), `fit-check.png` (TV, desktop and phone
  mock-ups, the avatar at 160–24 px), `mascot-cutout.png` (the locked mascot as a transparent PNG, 424×858).
- **Profile picture:** head and shoulders from the mascot reference (job f97004b9-…), scaled 1.95×, hat top at 11.5% of the height;
  background a radial glow `#3870B6` → `#133463` with a faint 8×8 grid and a soft shadow. Hat yellow on blue stays readable at 24 px.
- **Banner:** blueprint blue `#1F4E8C` with a 32/160 px grid. Phone box: eyebrow "3D BUILD EXPLAINERS" (Barlow Semi Condensed 600,
  `#C9DAF0`), headline "ONE PROBLEM" white / "AT A TIME" yellow `#FFC83D` (Barlow Condensed 800, fitted to the space), and three 3:4
  tiles of the finished builds (the END stills of videos 01–03) captioned MUD → HOUSE, LOG → CANOE, PIPE → HYDRANT. Desktop-only
  wings: the full-body mascot on the left, a dashed "NEXT BUILD?" tile on the right. The channel name is left off on purpose
  (YouTube prints it under the banner, and the rename is undecided).
- **Rebuild** (free, ~1 min): `pipeline/branding/cutout.py` (mascot cutout: OpenCV GrabCut, then edge pixels that match the
  backdrop right beside them are dropped; `pip install opencv-python-headless`), `make_brand.py <src> <fonts> <out>`
  (`--eyebrow/--line1/--line2`; the tiles are the `TILES` list) and `render.js` (Playwright Chromium screenshot). Fonts: `npm pack
  @fontsource/barlow-condensed@5.1.0 @fontsource/barlow-semi-condensed@5.1.0`. Stills: `jobs_wait` with `timeout_seconds: 0` on
  the job ids returns their CDN URLs. Swap in new END stills as the channel grows (keep 3 tiles; the phone box has no room for 4).
- `remove_background` and `upscale_image` were not used: `remove_background` has no cost preflight, so it would need a quote.

### 6.9 What the views are worth (11 Nov 2026)
The user asked whether $3,000 a month is realistic from faceless AI Shorts "once I'm monetized". Answer given: not from Shorts ads
alone (that is the top channel of this format, every month); realistic only as a mix led by TikTok Creator Rewards and longer
videos, at the stage where one or two videos a month reach several million views. The figures below are creator-blog and
calculator numbers from web-search summaries, not the platforms' own pages: **re-check before quoting.**
- **Shorts pay:** usually quoted at $0.03–0.07 per 1,000 views; mostly-US audiences more (reports of $0.10–0.30). YouTube pools the
  Shorts feed's ad money per country and splits it by engaged views (the creator keeps 45% of their share, per secondary sources).
  Studio's Shorts RPM is per 1,000 engaged views, which run below the public view counter.
- **$3,000 a month from Shorts ads** = about 43–100M views a month (60M at $0.05). Scale check with the 6.3 snapshot: You Made It's
  nine best Shorts total ~95M views (about $2.9–6.7K) and You Built It's eight best ~28M (about $0.8–1.9K). The Partner Program's
  entry pace, 10M views per 90 days, is worth about $100–230 a month.
- **TikTok Creator Rewards:** 10K followers, 100K views in the last 30 days, age 18+, an eligible country, videos of 60 s or more,
  and only posts made after joining earn. Quoted at about $0.40–1.00 per 1,000 qualified views (some US figures up to $2), roughly
  ten times Shorts, so $3,000 = about 3–7.5M qualified views a month. Our ~75 s videos already qualify on length. **The account
  is US-based** (the user confirmed on 13 Nov 2026), and the US is an eligible country. TikTok's support page gives the same thresholds
  and adds that the account must be a personal one, not a Business account (search summary, 13 Nov 2026).
- **Long videos on YouTube:** quoted at $1–10 per 1,000 views, so $3,000 = about 0.3–3M views a month.
- **Cost side:** third-party pricing pages put Higgsfield at about $5 per 100 top-up credits (Plus $49–59 a month for 1,000–1,200
  credits; not checked against the user's own plan), so a Lite video costs roughly $5–7 and needs about 80–190K Shorts views to pay
  for itself from Shorts ads alone.
- **Reading the sources:** www.tubefilter.com, ppc.land and searchenginejournal.com are outside the Default environment's network
  policy (WebFetch can't resolve them); WebSearch summaries were used instead.

### 6.10 Growth audit of both channels (18 Nov 2026)
The user: "take a look at my TikTok and YouTube pages, why are my views not consistent and why have I not had a video that's gone
viral yet. I want to increase my followers and viewership for both accounts what am I doing wrong?" Read from public pages on 18
Nov 2026 (about 00:20–01:00 UTC) and answered in chat. Nothing here has been approved: the recommendations at the end are open
decisions for the user. Conclusions marked "my read" are interpretation, not measurement.

**Snapshot.** TikTok @overthinkingyearly ("OT"): 54 followers (44 on 13 Nov), 679 likes, 10 videos, 46.4K views; it follows
nobody. YouTube @LetzBuildTogether: 310 subscribers (282 on 15 Nov), 10 Shorts, about 209K views.

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

**The reference accounts the same day.** @1hidden_by_design: 57.5K followers, 10 videos, 22.0M views (median 689K, lowest 49K),
no post since 9 Nov. @howbuildingexplained: 31.4K followers, 22 videos, 23.3M views (median 308K, lowest 10.8K), no post since 3
Nov, and its bio now reads "It was a good run, Zach was here". NET FILES (7.9): 276 videos, most recent ones at 5K–15K. Followers
per 1,000 views: ours 1.2, How Building Explained 1.3, Hidden By Design 2.6, so turning viewers into followers is not the main
problem; reach is.

**What was found.**
1. **Views are pass or fail at the first test.** On TikTok the six videos since seawater all stopped at 330–454 views, whatever
   the topic or the look; three earlier ones passed one round (1.9K–6.3K) and seawater went further (33.9K). On YouTube the
   first Shorts got 1.2K–9K each (the canoe was in made-for-kids mode), the hydrant 196K, and the last five 11–64. Different
   videos broke out on each platform (the hydrant 196K on YouTube against 6.3K on TikTok; seawater 33.9K on TikTok against 8.8K
   on YouTube), so a video that fails one test is not proven bad.
2. **The opening (the biggest finding).** Frames at 0, 0.5, 1, 2 and 3 s, ours against six reference videos (Hidden By Design's
   storm drain 10.1M, roof 4.5M, landfill 4.2M and beach 49K; How Building Explained's nipa hut 12M and car wash 10.8K). In every
   reference video the scene itself changes in the first 0.5–2 s, on the first verb: a hole is cut in the street and fills with
   rain, plywood covers the roof, a trench is dug and a truck dumps trash, a truck dumps sand, a bamboo raft appears, a hole is dug
   and soap poured in. Frame 1 is the "before". Of ours, only the mud house (rocks stacked into a wall), the canoe (the log pushed
   into the river) and the hydrant (water bursting out of the pipe at about 1.5–2 s) change in the first 3 s, and those three all
   passed TikTok's first test. Six of the seven that open on a finished scene stopped at 330–454; the exception is seawater, with
   water flowing from frame 1. The lightning video shows no bolt in its first 3 s, the car video is a frozen frame for 3 s, the
   sewer video doesn't change for 3 s, and the cryonics video glides over a finished lab, then cuts to a covered body on a gurney.
   The first lines drifted from a verb the picture shows ("If you stick a pipe on the water main…") to wishes and talk ("If you
   want to cheat death…", "If you want a hidden city…", "Everyone's heard it…"). `check_video.py` on the first 3 s does not
   separate these, because a camera travelling over a finished set counts as movement: judge openings from the frames. Videos
   08–10 met every whole-video target (84–90% moving) and stopped at the same ~350 as 05–07, so the gains went into the middle,
   past where most viewers decide (my read).
3. **The direction changed after almost every video.** In 11 days: three looks (Classic mascot, Hidden By Design, Cutaway with a
   travelling camera), idea lists replaced on 11, 14, 15 and 16 Nov and a fortress list added on 18 Nov, and four reference
   accounts. TikTok filed the ten videos under five different sets of categories (Petra as Anime & Comics, because of the cartoon
   mascot), so each new video is tested on a different first audience, and a profile visitor sees a mascot survival channel, a
   cutaway channel and a history channel at once (my read).
4. **TikTok hashtags don't register.** From video 02 on, every caption's hashtags are plain text: TikTok's `textExtra` and
   `challenges` are empty, so they are not links and add no hashtag signal. Only video 01's three tags registered. The likely
   cause is pasting the caption (3.3 Step 12).
5. **What it isn't** (ruled out from outside): a penalty (every TikTok video shows `display_penalty_type` 0, not prohibited, not
   under review); TikTok's AI label (TikTok applied it itself to 9 of 10 videos, seawater included: `moderationAigcLabelType` 1,
   `ShowAIGC` true, `IsAigc` false); the follow rate (normal for the format); a TikTok watermark on the YouTube uploads (none in
   the cover frames).
6. **YouTube's collapse began with Petra (12 Nov), while the hydrant was going viral.** No public marker separates the dead Shorts
   from the others (comments on, so not made for kids). My read, from creator reports rather than anything official: after a
   breakout, a channel's next Shorts are tested first on viewers like the breakout's audience, and these came for hydrants; Petra,
   a 1959 car and cryonics are off that topic, and none of the five opens with something happening. The post copy for videos
   08–10 said to tick "altered or synthetic content"; YouTube's policy exempts clearly unrealistic content such as animation, and
   no source says the label changes reach (6.4 item 5). The YouTube covers are auto-picked mid-video frames carrying a random
   caption word ("WAY", "So", "COLORS").
7. **Credits:** 1,762.25 left after video 10. At 265–280 a video, that is about six more videos at the current cost.

**Recommended to the user (open, not approved).**
1. Fix the first two seconds: frame 1 is the "before", and the first verb happens on screen within about a second; or open on
   the most dramatic moment and explain backwards. The first line is a physical action the picture shows, never "If you want…" or
   a remark. Proposed check at Gate A and Gate D: what happens on screen in the first second?
2. A free test first: re-cut two or three stalled videos (lightning opening on the bolt hitting the house; cryonics on the pods
   head down in the tank; the car on the impact) with one new first line from Daniel, post them as new videos and make the old
   ones private. A normal first test on YouTube and more than about 2K on TikTok would show the opening was the block.
3. One lane for the next 15–20 videos, judged after ten, not after one. The data favours the hidden inside of things everyone
   walks past (the hydrant and seawater here; the storm drain, roof and landfill on Hidden By Design); the X and F ideas can come
   back as single tests later. On YouTube that is also what the 300 subscribers came for.
4. Small fixes: type the TikTok hashtags in the app; stop ticking "altered content" for clearly animated cutaways; pick a cover
   frame at upload; rename TikTok @overthinkingyearly ("OT") to match the content and the YouTube name, with a bio that says what
   you post; pin the three best videos.

**How it was measured (to repeat it).** TikTok: `yt-dlp --flat-playlist -J https://www.tiktok.com/@overthinkingyearly` for
views, likes, comments, shares and saves; each video page (`https://www.tiktok.com/@overthinkingyearly/video/<id>`, fetched with
a browser user agent) carries `itemStruct` under `webapp.video-detail` in `__UNIVERSAL_DATA_FOR_REHYDRATION__`, with
`diversificationLabels` (TikTok's category), `textExtra` and `challenges` (empty means the hashtags are not links),
`moderationAigcLabelType`, `ShowAIGC` and `IsAigc` (the AI labels) and `penaltyContext`. The profile page gives followers and
likes. YouTube: `yt_snapshot.py @LetzBuildTogether` and the `oar2.jpg` cover frames (6.7). Videos were downloaded with yt-dlp
(formats on `v16-webapp-prime.us.tiktok.com`; one reference came from v19 this time) and cut into frames with ffmpeg.

---

## 7. User direction and the account the user likes (11–18 Nov 2026)
- **Look:** Cutaway with no character since 15 Nov 2026 (locked in 3.4; the record is 7.5). Before that, Classic: on 11 Nov the user
  asked to go back to the mascot look of videos 01–02 after video 04 was made in the Hidden By Design look, and videos 05–07 were
  made in it.
- **Format and ideas:** on 11 Nov the user asked for second-person "how to" / "if you…" videos about famous real places and true
  extreme stories, nothing boring. **Replaced on 14 Nov 2026** by four "Who wins?" matchups (7.3), one of which became video 07.
  **Replaced again on 15 Nov 2026** by five Cutaway ideas (7.6): things with hidden workings, each one place sliced open with
  something moving through it. **Replaced again on 16 Nov 2026** by five out-of-the-ordinary ideas with draft scripts, none
  about water (section 2, 7.8). **Joined on 18 Nov 2026** by three fortress stories, F1–F3, inspired by a NET FILES video
  (section 2, 7.9).
- **Credits:** Ultra plan since 11 Nov 2026 (3,000 credits); 2,824 left after video 05, which cost 176; 2,665.25 left after video 06,
  which cost 158.75; 2,508 left after video 07, which cost 157.25 (confirmed by `balance` on 15 Nov 2026; the look review spent
  nothing); 2,304.50 left after video 08, which cost 203.50 (confirmed by `balance` the same day); 2,040.25 left after video 09,
  which cost 264.25 (confirmed by `balance` the same day); 1,762.25 left after video 10, which cost 278.00 (confirmed by
  `balance` on 17 Nov 2026).
- **Shots:** one build (locked in 3.4 after video 05; the agreement and the reasons are in 7.2). Its "one main view" part was
  replaced on 15 Nov 2026 by the travelling camera.
- **Camera:** approved on 15 Nov 2026 after video 08: move like @1hidden_by_design's power-lines video, "as long as it
  accomplishes the same video as the one I referenced" (3.4 Rules 2, 3, 5, 6 and 7; 7.7).
- **Sound:** approved on 15 Nov 2026 ("yes on the sound"): a quiet bed and a few effects under the voice, no music (3.4, 7.5).
- **Analytics:** on 15 Nov 2026 the user said "forget about the retention graphs". Don't ask them for retention or watch-time
  figures; work from what can be seen from outside (7.5).

### 7.1 @thewhatifstudio (TikTok), checked 11 Nov 2026
- 60.9K followers, 38 videos, 1.4M likes; bio sells a "learn how we make them" guide. The linked video is "How a hole under your house becomes
  the underground city of Derinkuyu" (70 s, 1.2M plays, 133K likes; You Made It did the same topic on YouTube, 1.1M).
- Their winners are "what if every human… at the same time" and "what if X disappeared for 5 seconds" simulations (clapped 2.5M, tsunamis
  gone 2.1M, jumped 2.0M, deep breath 1.6M, friction 1.1M), disaster POVs (sea pulls back 1.7M, Krakatoa 935K) and the Derinkuyu build.
  Their builds of ordinary things stall: bamboo jungle house 28K, closet → panic room 15K, backyard → stadium 13K, tornado shelter 143K.
- My read: what wins in this format is a famous real place or a true extreme story with jaw-dropping numbers, not an everyday object.
  That was the filter for the ten ideas of 11 Nov (removed on 14 Nov 2026). `yt-dlp --flat-playlist -J https://www.tiktok.com/@<handle>` lists a TikTok account with stats.

### 7.2 One build, one main view (agreed with the user, 11 Nov 2026, after video 05)
The user, after video 05: "I like the animation visuals and use of the character, but it seems inconsistent at times. too many shots
of different things in the video. I would like to keep the visuals consistent on the main topic and make changes to the animation as
the script describes how the topic we are building works." The agreed rules are the 3.4 shot rule; this is the record behind them.
- **What was wrong in video 05** (counted from `pipeline/05-beat-sheet.md`): 26 shots made from 24 different pictures. Only 7 shots,
  about a third of the running time by the beat sheet's estimates, showed the house from the main view. 5 shots were not the house at
  all (a cup in a bath, a kitchen sponge, a dive boat, an airliner and a space capsule); each came from a comparison or side note in
  the script. The other shots were separate rooms and angles, each a fresh picture, so details drifted: the door shot shows the tank
  without the legs it got one shot earlier, and the payoff sky is lighter than the storm's a few shots before. The cause was our own
  rules: about one shot per sentence plus close-ups and inserts (section 1, Step 5), and a script formula that asks for comparisons.
- **It fits what we saw in the format** (my read, not measured): the leading channels mostly keep one view and change the build in
  place (6.3).
- **The user's answers (11 Nov 2026):** close-ups yes ("camera can move close on detail"), with the conditions in rule 2 of the 3.4
  shot rule; slice the wall open from the same view instead of cutting to a separate room, yes; comparisons only as labels and the
  rest cut, "I agree completely"; "if the build requires to move the setting can change". They like the visuals and the mascot: keep
  both.
- **Credit effect** (my estimate, 11 Nov 2026, from the 3.0 prices; check it against the next video's spend): clips are paid per
  animated second (kling4_0 2.25 cr/s), and stills are the cheap part (1.25 each). With the same amount of animation as video 05
  (Middle), a video should cost about 150–165 credits instead of 176, because it needs about 20 stills instead of 31. Animating nearly
  every second would cost about 210–230. Moments that only add a label hold on the last frame of the clip before, which is free and
  matches because it is the same view. Problems that hit the build in the main view are harder for Kling (video 05's storm clip came
  out wrong twice), so expect the odd redo at 7–11 credits; the 15% reserve covers it. At the 2,824 credits left after video 05, that
  is about 12–17 videos. **Measured on video 06 (12 Nov 2026): 158.75 credits** (19 stills 23.75 + 60 s of clips 135.00), inside the
  estimate, with no clip redos.
- **How to make it hold together:** make each stage still by editing the one before it, with the framing lock from 3.4g ("Keep exactly
  the same camera position, zoom and framing as the reference image"). Animate build beats from stage k to k+1 with start and end
  keyframes, which worked well in video 05 (the legs rising out of the sand; the barge out and the buoy in).
- **15 Nov 2026:** the "one main view" part of this rule was replaced by the travelling camera (7.7); "one build" stays.

### 7.3 New brief: ideas that start arguments (the user, 14 Nov 2026)
The user: "I feel like the video ideas aren't good enough the hooks don't keep people watching the ideas are boring. I need ideas that
are creative that will keep people watching and switch to followers, topics that will get engagement where people will comment there
opinions on the topic and debate. the video ideas don't necessarily need to be just about building. topics like military, vehicles,
engineering, etc I feel like are good topics what do you think? if you have better options use those." They asked for five ideas and
to stop and wait for approval.
- **Delivered:** five "Who wins?" matchups (P1–P5), each with hooks, a chain, a verdict question and a Shorts check.
- **The user's decision (14 Nov 2026):** "I like p1-4 I don't like p5, update claude.md file remove the old video ideas replace with
  these 4 for now". P1–P4 became section 2. P5 (a race car on the ceiling) and the ten older ideas were removed; they are in the
  repo history at commit `92a077a`.
- **Answered at video 07's Gate A:** the cold claim, for P4. Whether "Who wins?" would become the running series was never
  answered, and the question went with the list.
- **Locked at the time:** the Classic look, the mascot as "you", the 3.4 shot rule (as "one arena, one main view"), the loop ending.
- **What became of it (15 Nov 2026):** P4 was made as video 07 (3.4b). The user then left the character look (7.5) and replaced the
  list with five Cutaway ideas (7.6). P1–P3, with their chains and checked facts, are in the repo history at commit `c37181e`.

### 7.4 What gets comments in this format (TikTok, read 14 Nov 2026)
Read with `yt-dlp --flat-playlist -J https://www.tiktok.com/@<handle>`; each entry carries `view_count` and `comment_count`.

| Account | Videos | Views | Comments | Comments per 1,000 views |
|---|---|---|---|---|
| @thewhatifstudio (what-ifs, then builds) | 38 | 21.5M | 14,105 | 0.66 |
| @howbuildingexplained (builds) | 22 | 20.9M | 6,534 | 0.31 |
| @1hidden_by_design (how it works) | 10 | 20.7M | 3,670 | 0.18 |
| Ours | 6 | 34.7K | 9 | 0.26 |

- **Most comments per 1,000 views** (videos over 20K views): "What if all wood disappeared for 5 seconds?" 1.7; "every human on Earth
  sneezed" 1.5; "What if everything went wrong today?" 1.4; "glucose disappeared… What would you lose first?" 1.3; "every man on
  Earth disappeared" 1.3; How Building Explained's nuclear power plant 1.0 (its Kremlin got 0.1); "a penny doubled every day…
  Would you take the penny?" 0.8.
- **My read:** comments come from a choice put to the viewer, from a subject people already argue about (nuclear power, men and
  women), and from requests (@thewhatifstudio's captions say "You asked for it"). Views and comments are different things:
  @1hidden_by_design has the steadiest views and the fewest comments per view.
- **The same account, two formats:** @thewhatifstudio's 28 what-ifs have a median of 457K views (41K to 2.6M) and 0.70 comments per
  1,000 views. Its 8 builds have a median of 35K (14K to 1.4M, the top one being Derinkuyu) and 0.30. The builds came later (from
  late October), so timing may play a part. Its copy of the bamboo jungle house got 31K against How Building Explained's 9.7M.
- **Updates to section 4.1:** @1hidden_by_design now has 10 videos and 20.7M views: storm drain 9.8M, roof 4.1M (it had 19K after
  1.5 hours on 8 Nov), landfill 3.7M, water well 979K, river tunnel 878K, power lines 339K, gas station 108K, and a new one, "Building
  a beach is easy… until the ocean takes it back", 42K after five days.

### 7.5 The Cutaway look, refined (agreed with the user, 15 Nov 2026)
The rules that came out of this are in 3.4. This is the record behind them.

**What the user said.** "look at my TikTok page … the videos without the character figure have performed the best (fire extinguisher,
sea water to drinking) I need to step away from the character figure animation and make similar ones to like the other two. look at
the two videos with the highest engagement, makes some refinement suggestions to the animation style to improve it." ("Fire
extinguisher" is video 03, the fire hydrant.) After reading the suggestions: "all 6 refinements are approved". On sound: "I don't
know, what is the competition doing? what do you recommend?" On ideas: "we will do the video ideas later". Later the same day,
after the sound comparison below: "forget about the retention graphs, yes on the sound."

**The numbers** (15 Nov 2026; the table is at the end of 6.1). The two videos without the character hold 90% of the TikTok views
and 98% of the YouTube views. They lead on both platforms, in opposite order: seawater on TikTok (28.7K), the hydrant on YouTube
(167K).

**A caution given to the user.** Those two videos differ from the other five in three ways at once: no character, an everyday thing
with hidden workings as the topic, and the bright cutaway look. The character alone is not proven to be the cause. The whole package
is what @1hidden_by_design uses (21.1M views on ten videos), so the move is to the package. When the ideas were redone later that
day, they were that kind of topic (section 2, 7.6).

**How the two videos were studied.** Both were downloaded from TikTok and set beside @1hidden_by_design's two biggest (storm drain
9.9M, roof 4.2M): contact sheets at one frame a second, then `pipeline/analysis/check_video.py` and `under_the_voice.py`. Nothing
was listened to, and retention cannot be seen from outside.

| | 03 hydrant | 04 seawater | Storm drain | Roof |
|---|---|---|---|---|
| Seconds in which something moves | 33% | 33% | 84% | 87% |
| Longest stretch without movement | 20 s | 26 s | 6 s | 4 s |
| Different pictures | 22 | 25, in about a dozen places | one street | one house |
| Changes of shot | 23 cross-fades or wipes | 26 cross-fades | no cuts, no fades | no cuts, no fades |
| Caption letters | 44 px at 68% | 44 px at 73% | about 62 px at 75% | 54 px at 77% |
| Sharpness, moving / still seconds | 43 / 85 | 14 / 81 | 54 / 68 | 37 / 44 |
| Under the voice | nothing | nothing | a steady bed | a steady bed |

About the measure: a still picture under a zoom counts as not moving, and so does movement in a small part of the frame (video 03's
creeping frost and its drain-hole trickle are real clips that count as still). By the beat sheets, 35–40% of each of our two videos
is a generated clip. Seawater's sharpness figure is pulled down by hazy underwater clips.

**What was found, and the rule each finding became (3.4):**
1. **Two thirds of each video is a still picture with a slow zoom.** Seawater has 26 s of stills in a row (0:33–0:59: the clogged
   sheet, the sand filter, the pump, the pressure exchanger, the rusty pipe, the limestone, the pebble, the bottle, the glasses) and
   the hydrant video has 17 s (0:47–1:04: the movie geyser, the fallen top, the snow drift, the flag, the dog). It shows most where
   the line describes motion: the bathtub pour, the pebble splash and the geyser are frozen, the gauge needle never moves on "sixty
   times normal air pressure", and the wrench never turns on "twenty slow turns". Both videos were Lite. This became Rule 1.
2. **The best stretch in either video is the first 18 s of the hydrant video:** one sliced-open sidewalk from one angle, four clips
   in a row, and the pipe freezes, splits, becomes a hydrant and drains. After it the video moves through about ten other framings,
   and seawater never has a home view. This became Rule 2 (the shot rule of 11 Nov, carried over).
3. **Every change of shot is a 0.3 s cross-fade between two unrelated pictures,** and mid-fade both are on screen (0:19, 0:25,
   0:49, 0:59 and 1:13 in seawater). The reference has none: its camera travels. This became Rule 3.
4. **The look drifts.** Video 03's night fire shot has glowing neon water and a redrawn valve, its last frame shows a solid red pipe
   where the see-through empty barrel was, and the frost band is missing from some shots. In video 04 blue pumps sit under the
   kitchen sink, under the three glasses and on the seabed, because the STYLE line listed "blue-painted pumps". This became Rule 4.
5. **The captions are smaller than the reference's and sit on the subject** (video 03's had to move up to 68% to clear the valve).
   The storm drain keeps the lower ~40% of most frames as plain soil, with the captions on it. This became Rule 5.
6. **The pointers are thin:** chevrons 68 px wide with a 14 px stroke, and a ring with a 7 px stroke. The reference's arrows are
   solid. This became Rule 6.

**Smaller findings.** Our clips are softer than our stills (720p enlarged to 1080p), so the picture softens and sharpens as shots
alternate; Kling 4.0 offers 1080p, not yet priced. A caption glitch at 1:16 in video 03: "LET" is drawn half-clipped for two frames
and "AND" is on screen for one, the overlap bug that `05-build.py` fixed later. Two of the sixteen YouTube comments read on the
hydrant video call it AI; frozen stills and cross-fades are the usual tells (my read).

**What to keep** (told to the user): hands and small living things instead of a character (a YouTube commenter singled out the dog
line); the cyan water; the loop ending; one-word captions.

**Sound.** The user asked what the competition does. Measured with `under_the_voice.py`; nothing was listened to.

| Account (videos measured) | What sits under the voice |
|---|---|
| @1hidden_by_design (storm drain, roof, landfill) | A quiet steady bed through the whole video: present 71–93% of the time, the quietest moments only 19–20 dB below the voice, few separate bursts |
| @howbuildingexplained (nipa hut, levee) | No bed. Short quiet sounds in the gaps between lines: present 34–39% of the time, in 44 and 91 bursts |
| @thewhatifstudio (clap, tsunami) | Full sound design: music or drones and effects, loud (the side channel is only 11 dB below the whole mix) |
| Ours (03, 04) | Voice only: mono, near silence between words |

The YouTube leaders (You Made It, You Built It) could not be checked: YouTube blocks downloads from a session (6.7). The
recommendation was to do it the way @1hidden_by_design does: a quiet steady bed, a few effects, no music. **The user approved it
the same day ("yes on the sound");** what was approved is in 3.4 ("Sound under the voice"). The reasons given: all three accounts
put something under the voice and ours is the only dry one; once nearly everything on screen moves, water that pours in silence
feels unfinished; it costs ElevenLabs credits, not Higgsfield credits; and keeping the voice-only mix makes it reversible. The
ElevenLabs credit balance could not be read from the session (`account_get_usage` needs the connector reconnected with more
access), so price the sound with `estimate_only` at Gate B.

**Credit effect.** Rule 1 needs the Middle tier's clip seconds: about 160 credits a video at 720p (videos 06 and 07 cost 158.75 and
157.25 with 60 s and 61 s of clips) against 111.75 and 123.25 for the two Lite videos. With 2,508 credits that is about 15 videos.
1080p would cost more; price it at the next Gate B.

**Open after this session:**
- The idea list: closed later the same day (7.6, section 2).
- The first video under the new rules: made the same day as video 08 (3.4b). Start-and-end-frame clips do carry the camera from
  stage to stage, and the sound recipe is in 3.3 Step 6b. But by `check_video.py` only 20% of its seconds move (16% without the
  arrows), against the 80% target, although clips cover 93% of it: what moves is small in the frame, and zooms made from crops of
  one still are taken out by the checker (3.4k). Whether that measure tracks how viewers watch is still open: compare video 08's
  views from outside with videos 03 and 04.

**Closed by the user:** I asked for TikTok's retention graphs for videos 03 and 04 and YouTube's for video 03, to see whether
viewers leave during the still stretches. The user: "forget about the retention graphs". Don't ask again. (My reading: this covers
the older ask for watch-time figures in 6.3 as well, which carries the same note. The one in the matchup list went with that
list.)

**Files.** The scripts are in `pipeline/analysis/`. The two pictures shown to the user (the motion timeline, and captions and
pointers side by side) were not kept.

### 7.6 Five ideas for the Cutaway look (the user, 15 Nov 2026)
The list that came out of this was section 2 until 16 Nov 2026, when it was replaced (section 2, 7.8); the whole list is in
the repo history at commit `45b7846`. This is the record behind it.

**The brief.** After the look and the sound were settled (7.5), the user: "give me 5 creative and engaging video ideas following
the new animation style. the video ideas need to be different something that will keep people watching. before replacing the
current video selections wait for my approval".

**Delivered:** five ideas, C1–C5, each with an opening line, the cutaway, what changes on it, why people stay, a comment question
and the rivals; one line of reserves (a nuclear cooling tower, a kitchen grease fire, a wave pool, the Netherlands below sea level,
how fish get past a dam); and a recommendation to start with C1.

**The user's decision:** "update claude.md file, remove old video ideas and replace them with the new 5. replace c4 with nuclear
cooling tower". C4 had been landing a jet on an aircraft carrier. The cooling tower was in the reserve line with the note "72M, but
close to a topic How Building Explained has done". The matchup list that the five replace is in the repo history at commit
`c37181e`.

**How the ideas were found.**
- The filter: what our two best videos and @1hidden_by_design's best share (4.2, 7.5). One place that can be sliced open, hidden
  workings, and something moving along a path the camera can follow. Then a reason to keep watching (a claim that sounds wrong, a
  true story, an answer that comes late) and a question people can answer in two words (7.4).
- About thirty topics were put through `pipeline/youtube/yt_saturation.py` as topic searches. Each result is in section 2, under
  the idea or under "Not in the list".
- The pattern in the results (my read): on the topics with the biggest Shorts, the leaders are real footage or a person on camera
  (a plumber, a time-lapse of an arena, a pinsetter filmed from behind, the echo inside a cooling tower), and animated cutaways of
  the same thing are small or missing. Topics that explainer channels have already animated many times were left out (train
  wheels, airplane toilets, undersea cables).
- Facts were checked by web search and marked ✔ or ⚠ in section 2. The cooling tower was searched after the user's message, so
  the user has seen none of its entry.

**Open after this** (closed on 16 Nov 2026, when the list was replaced):
- The order. C1 was recommended first; the user has not chosen.
- C4's title, hook and chain, which the user sees for the first time at Gate A.
- Every ⚠ in section 2, and the saturation check on each exact title (the searches so far were by topic).
- Whether C1 overlaps the reference account's sewer video: read its transcript before Gate A.

**Sources for the checked facts** (15 Nov 2026; search summaries, so re-open the page before quoting a number):
- C1: the Hong Kong Health Bureau on the WHO findings at Amoy Gardens
  (https://www.healthbureau.gov.hk/en/press_and_publications/press/2003/press030516.htm); This Old House on how a trap loses its
  water (https://www.thisoldhouse.com/plumbing/how-a-trap-can-lose-water).
- C2: NBA.com on the postponed game (https://www.nba.com/news/kings-76ers-postponed-court-condensation); the Philadelphia Inquirer
  on the Wells Fargo Center changeover (https://www.inquirer.com/flyers/wells-fargo-center-changeover-flyers-sixers-20220406.html);
  NBC Chicago on the United Center's 2,000 pieces.
- C3: the CDC's lightning safety page (https://cdc.gov/lightning/safety/index.html); NWS New York
  (https://www.weather.gov/okx/LightningSafetyAwarenessWeek).
- C4: Historic England and Grace's Guide on Ferrybridge
  (https://historicengland.org.uk/services-skills/education/educational-images/ferrybridge-c-power-station-3277,
  https://www.gracesguide.co.uk/Ferrybridge_C_Power_Station); a USGS report for the 32% efficiency and the tower's water use
  (https://pubs.usgs.gov/wri/1975/0043/report.pdf); an EPA document for 420 gallons per MWh
  (https://www3.epa.gov/region1/npdes/schillerstation/pdfs/AR-343.pdf); WISE for the share of US reactors with towers
  (https://wiseinternational.org/labels/nei). How the tower works came from vendor and trade pages, and the shell thickness from
  an engineering paper the search did not name: both need a better source before Gate A.
- C5: Wikipedia's Pinsetter article (https://en.wikipedia.org/wiki/Pinsetter); the USBC on string pinsetters
  (https://bowl.com/news/usbc-certifies-string-pin-bowling-as-independent-competition-effective-august-1,-2023).
- The carrier idea: HowStuffWorks (https://science.howstuffworks.com/aircraft-carrier4.htm) and Wikipedia's Arresting gear article.

### 7.7 The travelling camera (agreed with the user, 15 Nov 2026, after video 08)
The rules that came out of this are 3.4 Rules 2, 3, 5, 6 and 7, with the runbook steps that carry them out (3.3 Steps 1, 2, 4, 5 and
7–11). This is the record behind them.

**What the user said.** After video 08: "the animation style is good but its not enough movement. the camera should move in and away
from the changes happening in the videos. currently its just a majority of a single shot with minor changes as the script goes on
visually. watch this video, I want the camera movement similar to this. tell me what changes can be made to achieve this." After
the proposal: "I approve all changes as long as it accomplishes the same video as the one I referenced. make the necessary changes
to the claude.md file. make sure to update the copy and paste prompt accordingly and labeled the new renewed date at the top".

**The reference.** @1hidden_by_design, "How Do Those Giant Power Lines Get Electricity to Your House? ⚡"
(https://www.tiktok.com/@1hidden_by_design/video/7705562191029636383), posted 7 Nov 2026, 87.7 s. On 15 Nov 2026: 353.7K views,
24.6K likes, 192 comments, 1,247 shares, 3,808 saves. A journey topic: power from the plant along the lines to a house. Downloaded
at 720p (format `h264_720p_1346671-0`, on the v16 host) and measured with `check_video.py` and `camera_path.py`; not listened to.

**Its camera path** (from one-frame-a-second sheets; the caption words show where the narration is):

| Time | Where the camera is and what it does |
|---|---|
| 0:00–0:04 | High aerial over the plant and the road to town; it pulls back and swings round to show the town |
| 0:05–0:09 | Swoops down to road level beside the wires; a car drives over them by the camera (arrow); the wires rise onto poles (arrow up) |
| 0:10–0:17 | Flies forward along the road beside the poles as the wires glow orange (pushing in 7–26% a second), then whips across the grass with motion blur on "So" |
| 0:18–0:23 | Lands on the transformer at the plant and drifts in 2–4% a second while its case cuts open to show the coils |
| 0:24–0:30 | Pulls up and away to an aerial of the road on "But", then swoops to the foot of a tower being built (+74% in one second) |
| 0:31–0:39 | Looks up the tower, drifting and turning slowly, while an orange line shows the current in the steel and glass insulators appear |
| 0:40–0:43 | Pushes in on the insulator string (10–15% a second), with a ring on it |
| 0:44–0:48 | Pulls back and flies over the fields toward the town (−15%, −58% and −30% a second) |
| 0:49–0:55 | Dips into the substation and back out, then glides along the line toward the houses |
| 0:56–1:00 | Swoops down the street to the pole by a house (+29%, +69%, +46%) and settles on its transformer |
| 1:01–1:06 | Pulls back to the street as a tree falls on the line; holds still for 3 s with a ring on the spark |
| 1:06–1:12 | Pulls out, then pushes into a roadside switch cabinet that opens (arrow on a switch), then pulls back |
| 1:13–1:19 | The street with one house cut open; a slow drift while its lights go out and come back |
| 1:20–1:22 | Pushes into the house's cut-open room (+72%): a woman flips the switch and the lamp lights |
| 1:22–1:27 | Pulls out to a huge aerial of the whole town and grid (its "Congratulations" line and the creator's call to action play here; we use neither) |

**What it shows:**
- About 11 camera positions in 88 s, each where something changes; the camera goes to the change and away again.
- It pushes in for 31 seconds and pulls out for 17, turning between the two 14 times. 22 seconds hold a big move (a quarter of the
  frame or more), one every 4 s on average and never more than 15 s apart.
- The moves are 3D: near things slide past faster than far things (median parallax 0.46 px), so it feels like a drone in the scene.
- The camera slows only on arrival: it drifts for 1–3 s while the change happens and the pointer appears. The longest still-camera
  stretch is 5 s (the tree falling).
- The cutaways open on arrival: the transformer, the switch cabinet and the house open in front of the camera.
- Captions (about 50 px, 77% down) sit over whatever is there, busy close-ups included.

**Measured against video 08** (15 Nov 2026):

| | Power lines | Video 08 |
|---|---|---|
| Seconds moving inside the picture (`check_video.py`) | 70% | 20% |
| Longest stretch without movement | 5 s | 29 s |
| Camera moving (`camera_path.py`) | 66% of the seconds | 45% |
| Median zoom and pan speed | 5.5% and 4.1% a second | 0.9% and 0.7% |
| Median parallax (3D travel) | 0.46 px | 0.03 px |
| Big-move seconds (longest gap) | 22 in 88 s (15 s) | 7 in 80 s (42 s) |
| Longest still-camera stretch | 5 s | 13 s |
| Camera positions | about 11 | about 3 (wide, roof, flap close-up) |

Video 08's one move like the reference's was the glide from the night house into the ground to the flap close-up, between two
different stills: 3.4–8.1 a second by `check_video.py`, and 50–66% zoom a second with 6–14 px of parallax by `camera_path.py`.

**The seven changes approved:** (1) Rule 2, one set seen by a travelling camera with 8–12 positions; (2) Rule 3, every clip flies
between two camera positions, each a real still, with no still-camera clips and a whip allowed for a far jump; (3) Rule 7, camera
targets measured with `pipeline/analysis/camera_path.py` (written for this comparison), beside the 80% motion target; (4) Rule 6,
pointers that appear on arrival and stay pinned to the picture; (5) Rule 5, plain ground only in wide shots, captions over whatever
is there in close-ups; (6) the camera column in the beat sheet (Step 2), the camera-position stills and the flight map at Gate C
(Step 5), and pilots measured against the reference at Gate D (Step 7); (7) the paste prompt renewed (section 5, 15/11/26 v2). Two
follow-ons serve the same goal: no planned holds, so every line is a clip (Rule 1), and the composition sentence moved out of the
shared style line into a WIDE line for wide shots only (3.3 Step 4).

**The user's condition:** "as long as it accomplishes the same video as the one I referenced". Our tools (seedream stills and Kling
between keyframes) approximate its camera, so the check is at Gate D: the pilots' `camera_path.py` and `check_video.py` numbers next
to the reference's, and no batch until they match.

**Cost and risk** (my estimate): about 78–80 s of clips (every line is a clip), ~175–180 credits at 720p; 20–24 stills on screen
from ~35–40 tries, ~45 credits; so ~215–225 a video against 203.50 for video 08. An AI set drifts more seen from many angles (pipes
move, colours shift), so each position is checked at Gate C, and each move runs 3–6 s between two stills so it does not warp.

**Files.** `pipeline/analysis/camera_path.py`, and `pipeline/analysis/camera-compare-powerlines-vs-08.jpg` (where the camera is every
few seconds in both videos, as shown to the user).

**The first video under it: 09, lightning (15 Nov 2026).** The pilots passed Gate D next to the reference (the hook: camera moving
80%, parallax 1.11 px; the climax: 67%, 0.40 px, 3 big-move seconds in 6), and the final met every target:

| | Power lines | Video 09 |
|---|---|---|
| Seconds moving inside the picture (`check_video.py`) | 70% | 84% |
| Longest stretch without movement | 5 s | 2 s |
| Camera moving (`camera_path.py`) | 66% of the seconds | 78% |
| Median zoom and pan speed | 5.5% and 4.1% a second | 6.4% and 6.5% |
| Median parallax (3D travel) | 0.46 px | 0.44 px |
| Big-move seconds (longest gap) | 22 in 88 s (15 s) | 23 in 76 s (9 s) |
| Longest still-camera stretch | 5 s | 3 s |
| Camera positions | about 11 | 10 (wide, ridge, bath, wall, ground, gap, foot, pole, panel, and the tub close-up) |

Two numbers came from the edit, not from Kling: C7 (the side flash) came back with a dead-still camera, so the edit pushes in toward
the arc; before that the final measured 79% and a 6 s still-camera stretch. The cost was 264.25 against the ~215–225 estimated
above: the stills matched the estimate (43.75), and the clips ran 220.50 because of 17 s of re-renders and clips planned slightly
longer than their lines (3.4l).

### 7.8 Ideas that grab from the first second (the user, 16 Nov 2026)
The list that came out of this is section 2. This is the record behind it.

**What the user asked.** "give me 5 creative out of the ordinary video ideas I can create videos about with an attention grabbing
entrance or hook to keep users watching (for example what happens when you fall off a cruise ship) only give the ideas don't
change anything on the claude.md file". The memory was read and nothing was changed until the approval below.

**First answer: five water ideas, turned down.** Each was a "what happens if you…" scenario in one place cut open, with proven
demand and no Zack D. Films Short (topic searches, 16 Nov 2026):
- **The pool on the edge of Victoria Falls** (Devil's Pool): a rock barrier at the lip makes a pool with almost no current when
  the river is low, so it opens only in the dry season (sources give August–January); the drop is about 108 m; about 500 million
  litres a minute go over in April and about a tenth of that in November. IShowSpeed's swim there 58M (Jan 2026); National
  Geographic's 360° video 6.6M.
- **The world's deepest pool, in Dubai:** 60.02 m (Guinness), 14 million litres kept at 30 °C and filtered every six hours (the
  operator's FAQ), a sunken city with pinball and foosball 38 m down; the no-flying rule after a dive is given as 12, 18 or 24
  hours by different sources. Real dives 56M, 32M, 25M and 25M; no animated cutaway. It touches the bends, which video 05 covered.
- **The slot-canyon flash flood:** Lower Antelope Canyon, 12 Aug 1997, 11 dead on a day with very little rain at the canyon (the
  storm was 3 to 30 miles upstream by source); the walls were carved mainly by flash floods; ladders are bolted down and nets hang
  at the top now. "Hikers vs Flash Flood" 5.5M, then 1.8M, 1.7M and 1.5M.
- **The Qiantang tidal bore:** up to about 9 m high and 40 km/h; the bay narrows from about 60 miles to 13 at the river; reflected
  waves off the seawall break over the banks; a typhoon-boosted bore injured about 30 watchers in Aug 2013; the biggest bores come
  around the 18th day of the 8th lunar month. Real footage 64M, 16M and 12M; the best explainer 2.1M.
- **The hole in the lake at Monticello Dam:** a spillway 72 ft across that drops about 200 ft and turns 90° into Putah Creek; it
  starts to take water when the lake reaches 440 ft, up to about 48,800 cubic feet a second; skateboarders ride the dry outlet;
  a duck was filmed going in in Feb 2017, and nobody agrees whether it survived. Best Short 926K, with four small copies of the
  "fall in" hook at 331K–833K; the 1997 drowning there has a single source.

The user: "all these are water, sea, lake related. mix it up all the ideas don't need to be water related, im asking you to give
me creative and attention grabbing scripts and video ideas. redo them then stop".

**Second answer: the five in section 2, each with a full draft script** (66–73 s at our pace), the cutaway, a comment question and
a demand line. Approved the same day: "I approve these video Ideas, update the claude.md file, remove the other ideas. then stop".

**What was learned.**
- **Zack D. Films owns the "what happens if you…" survival scenario on Shorts.** The user's own example is his ("Surviving A Fall
  Off A Cruise Ship 😨", 50M, Jul 2024), and so are most classic survival topics (the list under "Not in the list" in section 2).
  A scenario idea has to be one he hasn't done, or show what his person-centred style doesn't: the hidden place or system, cut
  open. To check, search "zack d films" with the topic (`yt_saturation.py`), then run `yt_channels.py <dir> shorts:<id>` on the
  biggest Shorts to see who posted them. The ids are in the saved results page: each `shortsLockupViewModel` carries
  `onTap.innertubeCommand.reelWatchEndpoint.videoId`. His titles end in one emoji (😨, 🤔, 😮, 🤯).
- **Mix the subjects.** Five ideas on one theme (water) read as one idea to the user, however different the places are.
- **"Scripts" meant full draft scripts**, not hooks alone: give each idea its script in our formula when the user asks for scripts.
- **Where the openings are** (the same pattern as 7.6): real footage of a strange place or a true story leads with millions
  (IShowSpeed 58M at the edge of Victoria Falls, a facts Short 20.9M on Centralia, a 13.8M visit to Whittier), while nobody has
  animated what a camera can't film (the fire under Centralia, the quarries under Paris, the inside of a cryonics tank).

**Not yet seen by the user:** the camera positions, the sounds, the ⚠ lists and the watch-outs in section 2 (my notes for Gate A).
X5's were shown at its Gate A, when it was made as video 10.

**Open after this:** the order of X1–X4 (the user picked X5 first: video 10, 16–17 Nov 2026); the exact-title saturation checks
and every ⚠ for X1–X4 (X5's were done at its Gate A, 3.4b). X5's draft ran short (230 words); the script as made has 269.

**Sources for the checked facts** (16 Nov 2026; search summaries, so reopen the page before quoting a number):
- X1: Wikipedia, Catacombs of Paris (https://en.wikipedia.org/wiki/Catacombs_of_Paris); Smithsonian
  (https://www.smithsonianmag.com/travel/what-lies-beneath-the-catacombs-of-paris-180950160/); Atlas Obscura on Aspairt's grave
  (https://www.atlasobscura.com/places/grave-of-philibert-aspairt); Part-Time Parisian on the 1774 collapse
  (https://www.parttimeparisian.com/p/when-rue-denfer-collapsed-and-paris); Paris Tickets' timeline
  (https://www.paristickets.com/fr/catacombs/history/).
- X2: Wikipedia, Centralia (https://en.wikipedia.org/wiki/Centralia,_Pennsylvania); Slate and Atlas Obscura
  (https://www.slate.com/blogs/atlas_obscura/2014/06/04/centralia_a_town_in_pennsylvania_destroyed_by_a_mine_fire.html); Science
  News on why water fails (https://sciencenews.org/?p=28468); the Bureau of Mines report RI 8799
  (https://onemine.org/documents/ri-8799-problems-in-the-control-of-anthracite-mine-fires-a-case-study-of-the-centralia-mine-fire-august-1980-);
  Pennsylvania DEP's FAQ
  (https://crawler.dep.state.pa.us/Mining/Abandoned%20Mine%20Reclamation/AbandonedMinePortalFiles/Centralia/BookmarkTest.pdf).
- X3: The Drive on the FIA report
  (https://www.thedrive.com/accelerator/39630/grosjeans-horrific-f1-crash-at-bahrain-registered-67-gs-investigation); Gulf News
  (https://gulfnews.com/sport/motorsport/formula-one-romain-grosjean-hit-barrier-at-192kph-with-67g-force-in-fireball-crash-1.77647856);
  ESPN on the chainsaw remark (https://africa.espn.com/f1/story/_/id/22542522/mercedes-boss-toto-wolff-remove-halo-chainsaw);
  Autosport (https://www.autosport.com/f1/news/grosjean-pays-tribute-to-f1-halo-after-surviving-137mph-bahrain-gp-crash-4976770/4976770/).
- X4: Alaska Beacon
  (https://alaskabeacon.com/2025/07/22/quirky-once-isolated-alaska-town-is-eyeing-a-transportation-system-upgrade/); the Whittier
  Chamber of Commerce on the tunnel (https://www.whittieralaskachamber.org/info/whittier-alaska-tunnel/); Alaska DOT
  (https://dot.alaska.gov/creg/whittiertunnel/); Atlas Obscura on the tunnel
  (https://atlasobscura.com/places/anton-anderson-memorial-tunnel); Wikipedia, Whittier (https://en.wikipedia.org/wiki/Whittier,_Alaska).
- X5: Smithsonian
  (https://www.smithsonianmag.com/smart-news/200-frozen-heads-and-bodies-await-revival-at-this-arizona-cryonics-facility-180980981/);
  Decrypt on the prices (https://decrypt.co/243997/cryonics-alcor-hal-finney-bitcoin); Guinness on Bedford
  (https://guinnessworldrecords.com/world-records/452742-first-person-to-be-cryonically-suspended); Wikipedia, James Bedford
  (https://en.wikipedia.org/wiki/James_Bedford); Superlative on the upside-down storage (https://superlative.substack.com/p/cryonics).
- The water five: Atlas Obscura on Devil's Pool (https://atlasobscura.com/places/devil-s-swimming-pool); Deep Dive Dubai's FAQ
  (https://www.deepdivedubai.com/faqs); Wikipedia, Antelope Canyon (https://en.wikipedia.org/wiki/Antelope_Canyon); NTSLF on the
  bore (https://ntslf.org/node/8); the Bureau of Reclamation on Monticello Dam (https://www.usbr.gov/projects/index.php?id=186).

### 7.9 Fortress stories from a NET FILES video (the user, 17–18 Nov 2026)
The ideas that came out of this are F1–F3 in section 2. This is the record behind them.

**What the user asked.** "give me 3 creative video ideas inspired by this
https://www.tiktok.com/@net.files6/video/7708777568689868064?… it doesn't have to match the length or animation style. I want
stories similar to this". After the answer: "add these video ideas into claude.md without removing the other ones in section 2.
update the copy and paste prompt accordingly and label the new renewed date". The prompt was renewed as 18/11/26 (section 5).

**The reference.** NET FILES (TikTok @net.files6), "How Ancient Engineers Built An Almost Impossible To Conquer Mountain
Fortress 😱", posted 16 Nov 2026 (about 14:30 UTC), 125.9 s. On 17 Nov 2026, about 33 hours old: 1.3M views, 71.3K likes, 383
comments (0.29 per 1,000 views) and 868 shares. Not listened to.
- **How it was read:** yt-dlp, with `bytevc1_1080p_2261105-0` for the picture and `h264_540p_1937509-0` for the sound (both on the
  v16 host; the bytevc1 formats carry no sound); one frame every two seconds as contact sheets; the sound sent to Higgsfield storage
  (`media_upload`, a PUT, `media_confirm`) and transcribed with faster-whisper `small.en` in the Higgsfield sandbox (about a minute,
  no credits; the audio file stays in the user's Higgsfield uploads).
- **The story** (in my words; never reuse theirs): a city built in a valley between two mountains, which the narrator calls a
  big mistake, because enemies on the ridges can shoot fire arrows down into it (0–10 s); so walls 4–5 m high and watchtowers
  along both ridges, which also take away the blind spots (12–26 s); that leaves two ways in, the valleys at each end (26–32 s);
  the north one is a steep, narrow stone path that siege engines and ladders can't use (32–51 s); a turn to the place's weak
  point, the flat south gate (51–63 s), answered by a fort inside and a fort outside the gate, a trench 7–8 m wide and a
  drawbridge (63–84 s); then the objection a viewer would raise, what if the enemy just surrounds it and waits (84–90 s),
  answered by a spring that never stops and fields inside the walls, enough for years (90–109 s); the payoff (110–116 s); the
  name, Wugucheng, a fortress of the Korean kingdom of Goguryeo, at 116 s, with a big title card in Chinese characters and
  pinyin; and its fate in two lines: it came under the Tang dynasty when Goguryeo was defeated (117–126 s).
- **Their wording, never to use:** "congratulations buddy", at the start and at the payoff ("Congratulations" is also How Building
  Explained's sign-off, section 1); "even the strongest defenses have weaknesses"; "some people might ask".
- **The look:** a game-engine landscape (Unreal-like), not a cutaway; small soldier figures, catapults, ladders and fire on the
  town; a drone-like camera; small one-word white captions low in the frame; the name on a big title card.
- **Why it works** (my read): (1) it is a defense puzzle: every line answers "how would an enemy get in?", and the objection
  beat answers the comment before anyone writes it; (2) the place is named only at the end, so the viewer stays for the answer;
  (3) one line on what became of it closes the story.

**The account** (read on 17 Nov 2026 with `yt-dlp --flat-playlist -J`): 276 videos, 72.2M views. Ancient engineering, mostly
Chinese (fortresses, passes, bridges, tombs, cliff temples, water machines), with a few modern builds. The biggest: a tomb
defended with quicksand (Guozhuang) 10.2M; a bridge over a 70 m canyon 6.8M; London's Tower Bridge 5.8M; Vietnam's 100 km of war
tunnels 3.4M; "How This Fortress Outmastered Entire Armies" (the Changba octagonal fortress) 2.9M; a tower over a subway 2.7M;
"How Ancient Engineers Defended This Mountain Pass" (Niangziguan) 2.4M; the Great Wall into the sea 2.0M; Tibet's Bori bridge
2.0M; "How Geography Made This City Impossible To Conquer" (a Chinese city that held off the Mongols) 654K; "How Ancient Engineers
Built The Perfect Fortress" (a cross-shaped fortress in Gansu) 603K. The places behind the titles that hide them were read from
the videos' last 24 seconds.
- **Titles** (my read): their five biggest fortress videos (603K–2.9M) all keep the place out of the title. Fortress titles that
  name the place or say "Ancient China" sit at 10K–83K, apart from Diaoyu Fortress (513K and 176K). Hidden titles flop too (four
  of them at 15K–35K), so the title alone doesn't do it.
- Most of their recent videos get 5K–15K: the account's views come from a few hits.

**How the ideas were found.**
- The filter: a real fortress with a defense puzzle, a twist at the end, one place that can be cut open, and no Short found that
  already tells its story; not in NET FILES' list (its fortresses are Chinese, plus one general star-fort video) and not by Zack D.
  Films (searched "zack d films" with each topic: nothing).
- About thirty searches with `pipeline/youtube/yt_saturation.py`. Kept: Gibraltar (F1), Malbork (F2), Himeji (F3); their numbers
  are in section 2. The dropped topics and their numbers are under "Not in the list" in section 2.
- The pattern (my read): the fortress twists everyone knows are already Shorts, some animated (the toilet at Château Gaillard,
  the elephant at Sigiriya, the 30-year siege of Mont-Saint-Michel, Janjira's sweet water); the open ones are told only in long
  videos or travel clips (Gibraltar's sealed room 1.9M long, Malbork's heating 269K long, Himeji's defences 53K long).
- A caution: castles as builds were found crowded on 9 Nov 2026 (14 near-identical Shorts, best 56K; 6.3), and landmarks did less
  than survival or "your yard" topics on YouTube. F2 and F3 are real castles told as stories with a twist, not "How a ___ Becomes
  a Castle" builds; keep the twist and the hidden name up front at Gate A.
- Facts were checked by web search and marked ✔ or ⚠ in section 2. WebFetch could not open en.wikipedia.org in this session (it
  is outside the network policy), so the checks used search summaries; a request to probe other hosts was refused by the session's
  auto-mode check.

**What the user saw:** the three moves above, then the three ideas as written in section 2 (title, the place named at the end,
opening, numbered story, ending, set, competition, comment question, ⚠), and the four dropped topics (Château Gaillard,
Mont-Saint-Michel, Sigiriya, Janjira) with the Shorts that already tell them. The sources were listed under the answer.

**Open after this:** the order of X1–X4 and F1–F3; full scripts for F1–F3 (at Gate A); every ⚠; the exact-title saturation check
before Gate A (the searches so far were by topic and angle); whether to allow one name card for the reveal (section 2, F rule 1).

**Sources for the checked facts** (17–18 Nov 2026; search summaries, so reopen the page before quoting a number):
- F1: Wikipedia, Great Siege Tunnels (https://en.wikipedia.org/wiki/Great_Siege_Tunnels); the Gibraltar Museum on the Great Siege
  (https://www.gibmuseum.gi/our-history/military-history/great-siege-of-gibraltar); Wikipedia, The Defeat of the Floating
  Batteries (https://en.wikipedia.org/wiki/The_Defeat_of_the_Floating_Batteries_at_Gibraltar,_September_1782); AquaGib on the
  water supply (https://www.aquagib.gi/history/); gibraltar.com on the WWII tunnels
  (https://gibraltar.com/en/travel/see-and-do/history-and-heritage/world-war-2-tunnels.php); War History Online on the 34 miles
  (https://www.warhistoryonline.com/world-war-ii/rock-of-gibraltar-tunnels.html); Wikipedia, Operation Tracer
  (https://en.wikipedia.org/wiki/Operation_Tracer); the Ministry for Heritage on the Stay Behind Cave
  (https://www.ministryforheritage.gi/heritage-and-antiquities/stay-behind-cave-complex-1072); History Hit on Fleming
  (https://www.historyhit.com/for-your-eyes-only-the-secret-gibraltar-hideout-built-by-bond-author-ian-fleming-in-world-war-two/);
  Finest Hour on Churchill and the macaques
  (https://winstonchurchill.org/publications/finest-hour/finest-hour-161/curiosities-churchill-and-the-barbary-macaques-a-visit-to-gibraltars-fabled-rock/).
- F2: the Malbork Castle Museum on the Summer Refectory (https://zamek.malbork.pl/?p=3621); Low-tech Magazine, via Resilience, on
  the heat-storage hypocaust (https://www.resilience.org/stories/2017-03-22/heat-storage-hypocausts-air-heating-middle-ages/); the
  1410 siege (https://military-history.fandom.com/wiki/Siege_of_Marienburg_(1410)); Wikipedia, Siege of Marienburg (1457–1460)
  (https://en.wikipedia.org/wiki/Siege_of_Marienburg_(1457%E2%80%931460)) and Malbork treaty
  (https://en.wikipedia.org/wiki/Malbork_treaty); Islands on the largest castle by land area
  (https://www.islands.com/1704197/world-largest-castle-poland-malbork-land-area-vibrant-impressive-beauty-europe).
- F3: MLIT's tourism texts on Himeji's defences (https://www.mlit.go.jp/tagengo-db/en/R1-00693.html) and on Himeji in the modern
  age (https://www.mlit.go.jp/tagengo-db/en/R1-00692.html); Wikipedia, Himeji Castle (https://en.wikipedia.org/wiki/Himeji_Castle);
  History Hit (https://www.historyhit.com/locations/himeji-castle/); Muza-chan on the main keep's floors
  (https://muza-chan.net/japan/index.php/blog/himeji-castle-main-keep).
