# 08 Sewer Trap: beat sheet (Middle tier, Cutaway look, first video under the 15 Nov 2026 rules)

Idea C1 (section 2), "Why Your House Doesn't Smell Like the Sewer It's Connected To". Script approved at Gate A on 15 Nov 2026 with
opening A ("If you…", first "But" at ~3 s): 274 words, est. ~78 s at 3.5 words/s, loop ending. Titles proposed: YouTube "Why Your
House Doesn't Smell Like the Sewer"; TikTok "Why doesn't your house smell like the sewer it's connected to? 🚽".

Est. seconds = words / 3.5. Real timings come from the narration (Step 6) and replace these; clip lengths are set from them.
Look (3.4): one sliced-open set from one main view, changed in place; animated clips over ~90% of the running time; holds only on
the last frame of the clip before, 3 s at most; no cross-fades between different pictures; every still an edit of the one before;
night is a re-grade of the same picture; captions ALL CAPS ~57 px at ~75% down; solid white arrows and one thick ring; no labels.

## Set and main view
- **Place:** a two-storey suburban house sliced open like a dollhouse (front wall removed) on a block of ground that is cut
  straight down like a cake. Cream walls, a terracotta roof, pale wood floors, white tiles, grey pipes; translucent cyan water.
- **Upstairs:** a bathroom with a toilet (its curved water seal visible in the cut-open bowl), a small sink with its U-bend,
  a round floor drain in the tiled floor with its own trap below, and a ceiling exhaust fan.
- **Downstairs:** a kitchen sink with the cabinet doors open, so the drain under it shows.
- **The main pipe:** one grey pipe inside the cut side wall, from the upstairs floor down to the foundation; every fixture joins it.
- **Below ground:** the house pipe slopes from the foundation to a big sewer pipe running left to right under the street strip at
  the front edge of the block, about 55–60% down the frame. Below that, plain dark soil down to the bottom of the frame.
- **Main view (S0, END):** straight-on, slightly raised, the whole house and the sewer in the upper ~60%, plain soil below for the
  captions. The roof's top sits below TikTok's top bar (y > ~200 of 1920).
- **Gas:** a faint, translucent yellow-green haze, the only thing drawn to be seen that is not really visible. It must never read as
  smoke or fire.
- **The small living thing:** one brown rat (night beats only).
- **Nobody in the house.** One hand appears in B13 (turning on the bathroom tap).

## Stage ladder and stills (each an edit of the one named; framing lock on every edit)
| Still | Made from | What changes |
|---|---|---|
| S0 | (style key) | The house as above; the kitchen sink drains through a straight pipe (no U); the main pipe stops below the roof (no vent) |
| S0H | S0 | Haze rising out of the kitchen sink |
| S1 | S0 | The kitchen pipe has a U-bend holding cyan water; no haze |
| S1D | S1 | The kitchen U is empty; haze rising out of the kitchen sink; a column of water falling inside the main pipe |
| S2 | S1 | A vent pipe continues from the top of the main pipe up through the attic and out through the roof; kitchen U full |
| S2X | S2 | A month later: the bathroom sink's U and the floor drain's trap are dry, the toilet water is low; haze in the bathroom |
| S2R | S2X | The bathroom sink's U is full again; the floor drain is still dry with a thin wisp of haze; the rest of the haze is gone |
| S2HK | S2R | Haze streaming up out of the floor drain toward the ceiling fan, filling the bathroom |
| S3 | S2 | A thin copper pipe from the bathroom sink's water supply down to the floor drain; floor drain full; no haze |
| S3N | S3 | Night re-grade: the same picture in cool moonlight, the same water colour, nothing glows |
| S3NS | S3N | The rat swimming inside the big sewer pipe, in its left see-through window |
| S3NT | S3N | The rat's head poking up through the water in the toilet bowl |
| S4NZ | S3N | Night close-up of the junction under the lawn: the steel flap hangs inside the house pipe where it meets the sewer |
| S4NZR | S4NZ | The same close-up with the rat in the sewer below the junction, facing the closed flap |
| END = S3 | — | The finished house in daylight, same framing as S0 (the flap is only seen in the close-up) |

**As made (Gate C, 15 Nov 2026):** 26 seedream jobs (32.50 credits) for 14 stills on screen; every job id is in `08-jobs.tsv`.
- S0 was reframed: the first generation (S0A) had the sewer pipe ~75% down the frame, under the captions. It was shrunk to 76% and
  lifted locally (roof peak at 10%, clear of TikTok's top bar; sewer pipe at ~63%), the edges were extended, and one seedream edit
  cleaned them (S0).
- Seedream would not put a small thing inside a pipe in the wide view: three flap tries hung a plate or disc outside the pipes, and
  two climbing-rat tries sat the rat on the pipe. The rat now swims in the sewer pipe's see-through window (S3NS), and the flap got
  its own close-up (S4NZ), which the camera pushes in to and pulls back from (Rule 3).
- Other redos: S1D (a waterfall outside the pipe), S2 (the vent rose far above the roof; the second try is a pipe about a metre
  tall), S2R (a white wisp removed), S2HK (two edits: haze in the kitchen), S4NZR (the rat was on the house side of the flap).
- Framing check: every edit sits within 0.2 px of S0 (phase correlation) and keeps 91–100% of its edges. END (S3) matches S0 part
  for part.
- Grain grows with each edit of an edit (high-pass noise on a plain wall: S0 8.3, S2 9.9, S2X 11.1, S2R 13.9, S2HK 16.3). Denoise
  S2X, S2R and S2HK locally before they go to Kling as keyframes.

## Beats
| # | VO | ~s | Type | Start → end picture | What moves | Pointer | Sound | Clip / hold |
|---|---|---|---|---|---|---|---|---|
| B1 | If you pipe your sink straight into the sewer, it drains. | 3.1 | hook | S0 → (S0H) | Tap runs; water drops straight down the plain pipe to the sewer | — | tap + drain | P1 (12 s, B1–B4) |
| B2 | But the sewer's stink comes right back up the pipe. | 2.9 | problem | (S0H) | Haze rises up the pipe and out of the sink | — | — | P1 |
| B3 | So you bend the pipe into a U. Water sits in the bottom and blocks the gas. | 4.9 | build | S0H → S1 | The pipe bends into a U, water settles in it, the haze stops below it | — | — | P1 |
| B4 | This is a trap. | 1.1 | term | S1 | Water in the U settles; slow push-in | — | — | P1 |
| B5 | The water in your toilet bowl is one too. | 2.6 | that's why | S1 (last frame of P1) | Push-in toward the upstairs toilet | ring on the bowl water | — | hold 2.6 s |
| B6 | But upstairs, someone flushes. | 1.1 | problem | S1 → S1D | The toilet flushes | — | flush | C3 (6 s, B6–B7) |
| B7 | Water falling down the main pipe drags the air behind it, and sucks your trap dry. | 4.6 | problem | (S1D) | Water falls down the main pipe; the kitchen U is pulled empty; haze comes up | arrows down the main pipe | gurgle | C3 (fixed camera) |
| B8 | So you run a pipe up through the roof to let air in. This is a vent. | 4.9 | build | S1D → S2 | A pipe grows up through the attic and roof; the kitchen U refills | — | — | C4 (5 s) |
| B9 | That's the pipe sticking out of your roof. | 2.3 | that's why | S2 (last frame of C4) | Push-in toward the roof | — | — | hold 2.3 s |
| B10 | But then nobody uses the bathroom for a month. | 2.6 | problem | S2 → S2X | Time-lapse: light sweeps across the house | — | — | C5 (9 s, B10–B12) |
| B11 | The water in its drains dries up, and the stink creeps back. | 3.4 | problem | (S2X) | Water sinks out of the bathroom traps; haze creeps in | — | — | C5 |
| B12 | That's why guest bathrooms smell. It was never the guests. | 2.9 | joke | S2X | Haze curls through the empty bathroom | — | — | C5 |
| B13 | So now and then, you run the water. | 2.3 | fix | S2X → S2R | A hand turns on the bathroom tap; the sink's U refills; most haze clears | — | tap | C6 (3 s) |
| B14 | But the worst thing a dry drain lets in isn't the smell. | 3.4 | twist | S2R → S2HK | A wisp of haze curls out of the dry floor drain | — | — | C7 (12 s, B14–B16) |
| B15 | In two thousand three, at a Hong Kong apartment complex, bathroom floor drains had dried out. | 4.6 | twist | (S2HK) | More haze rises from the floor drain (our bathroom; no other building, no people) | — | — | C7 |
| B16 | Fans pulled sewer air up through them, and more than three hundred people caught SARS. | 4.3 | twist | S2HK | The ceiling fan spins and pulls the haze up across the room | arrows from the drain to the fan | fan whir | C7 (fixed camera) |
| B17 | So some floor drains refill themselves from a water pipe. This is a trap primer. | 4.3 | build | S2HK → S3 | A thin pipe reaches the floor drain; a trickle refills it; the haze clears | — | trickle (in the bed) | C8 (5 s) |
| B18 | But water stops gas. It doesn't stop rats. | 2.3 | problem | S3 → S3NS | Dusk falls to night; a rat swims along inside the sewer pipe | — | — | C9 (8 s, B18–B19) |
| B19 | At night, one swims up from the street, climbs the main pipe, and holds its breath through the bend. | 5.4 | climax | (S3NS) | The rat swims along the sewer toward the house pipe | — | splash, squeak | C9 |
| B20 | Then it pops up in your toilet. | 2.0 | climax | S3NS → S3NT | The rat slips into the house pipe; its head comes up through the toilet water | — | splash | C10 (3 s) |
| B21 | So you fit a flap where your pipe meets the sewer. It opens for everything going out, and drops shut behind it. | 6.3 | build | S3NT → S4NZ | The rat ducks back down; the camera glides down to the junction; outgoing water swings the flap open and it drops shut | — | flap clank | C11 (7 s, camera travel) |
| B22 | This is a rat blocker. | 1.4 | term | S4NZ (last frame of C11) | Slow push-in on the flap | ring on the flap | — | hold 1.4 s |
| B23 | Next time, the rat hits the flap and turns back. | 2.9 | payoff | S4NZ → S4NZR (middle) → S3 | The rat swims up, bumps the flap, turns back | — | flap clank | C12 (6 s, B23–B24, middle keyframe) |
| B24 | Bend the pipe, let it breathe, and keep it wet. | 2.9 | end / loop | → S3 (END) | The camera pulls back up to the house as dawn turns to morning; the finished house in the S0 framing | — | — | C12 |

Clips: 11 (P1 12 s, C3 6, C4 5, C5 9, C6 3, C7 12, C8 5, C9 8, C10 3, C11 7, C12 6) = 76 s. Holds: B5, B9, B22 = 6.3 s (8%).
Clip coverage ≈ 92% of the running time. No cuts: dusk happens inside C9, the push-in to the flap inside C11, and the pull-back
and dawn inside C12.

## Pilot (Gate D)
- **P1, the hook and the first travel in one clip, with a middle keyframe** (3.3 Step 7, 3.4j): start S0, middle S0H
  (`image_references`), end S1, 12 s. If the set holds its shape, keep it. If it does not, render it as two 6 s clips (S0 → S0H,
  S0H → S1).
- **C11, the push-in to the close-up** (S3NT → S4NZ, 7 s): the second pilot, because it tests the camera travelling from the main
  view to a close-up inside one clip (Rule 3) and the flap.
- The user chose 720p at Gate B without the 1080p test.

## Sound (Step 6b; ElevenLabs Sound Effects, one generation each)
- Bed: quiet house interior, soft steady room tone with a faint distant fridge hum; looped under the whole video, ~18–20 dB under
  the voice.
- Effects: tap running and draining (B1, B13); toilet flush (B6); drain gurgle as a trap is sucked dry (B7); bathroom fan whirring
  on (B16); small splash and a rat squeak in a pipe (B19–B20); metal flap clanking shut in a hollow pipe (B21, B23).

## Quote (Gate B, 15 Nov 2026; prices checked with get_cost)
- kling4_0 image-to-video: 2.25 credits/s at 720p, 3.25/s at 1080p (3, 5, 6, 7, 8, 9 and 12 s checked at both). seedream_v5_pro
  1k 9:16: 1.25 per still.
- 16 stills 20.00 + 76 s of clips: **720p 171.00 → 191.00, +15% = 219.65**; **1080p 247.00 → 267.00, +15% = 307.05**.
- Resolution test at Gate D: one extra 6 s clip, 19.50 (1080p) or 13.50 (720p).
- ElevenLabs: narration, 2 takes of eleven_v4 with Daniel, 2,798 credits; sound, 7 generations at 50 each = 350 at the default length.
- Balance before: 2,508 Higgsfield credits (Ultra).
