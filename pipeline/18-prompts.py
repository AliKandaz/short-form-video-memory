# Video 18 (B20, "How to Launch a Ship From Your Back Yard"): picture and clip requests for Higgsfield.
#   python3 18-prompts.py still KEY [KEY ...]   -> requests for generate_image_batch (seedream_v5_pro, 1k, 9:16)
#   python3 18-prompts.py clip  KEY [KEY ...]   -> requests for generate_video_batch (wan2_7, 720p, 9:16)
# Gate A and Gate B approved by the user on 25 Nov 2026 (quote 190.66). The plan is 18-beat-sheet.md. Job ids are read from
# 18-jobs.tsv (key <tab> job id; a key with a try suffix, S1_2.B, replaces S1_2 when it is listed later). Lines here are
# CLAUDE.md 6.3's, with this set's own words. Every picture after the base is an edit of the one before it (LOCK); the
# boat key (KH) is a second reference wherever the boat is in the picture.
#
# THE BASE (K0S): the set key K0 (try A) cropped to 8%..92% of its width and stretched back to full width on this machine
# (free), so that the lawn and the lake run off both sides of the frame: the truck, the small boats and the hoist come and
# go at the frame's edges, never across the bare ground beside the block. Uploaded to Higgsfield; its media id is K0S in
# 18-jobs.tsv. K0 try B (a deeper lake) came back corner-on and is not used.
#
# THE LAYOUT, in % of the frame (measured on K0S): house 0-10 down; lawn 10-54; bank 54; lake 55-69.5; the cut face
# 69.5-88.5 (water in section to 79.5, sand and earth under it); pale ground below. The barbecue 67.5 across, 47 down. The
# dock's root at the bank 87-92 across; its T-shaped end 59-87 across, 62.5-67 down.
# THE STAGING: the boat lies ACROSS the lawn, parallel to the water's edge, bow to the right, and is launched sideways,
# toward the camera (the lake is 15% of the frame deep: a boat end-on would not fit in it, and would be half as wide on
# screen). Boat 27.5-74 across (as S0 came). Rails at 24 and 76 across, 30-60 down. Cradle 21-79 across. Chain heaps at
# 8-14 and 81-86 across (the hoist rolls down straddling the left ones). The hoist's piers at 1-6 and 16-21 across, 54-66 down.
import json, sys

STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent "
"cyan water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
BOATW = ("a stubby steel workboat with a dark navy-blue hull, a red band along its bottom, a thin white stripe at the deck "
"edge, a small white wheelhouse at its bow end, one big open rectangular hatch in the middle of its grey deck and a flat "
"empty stern deck")
BOAT2 = "The boat is the same boat as in the second reference image: " + BOATW
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"house, the porch, the lawn, the bank, the lake, the wooden dock, the cut face of the block and everything already standing "
"on the lawn or in the water stay exactly where they are, the same size and the same shape.")
BOATSTAY = "The boat stays exactly where it is, in exactly the same position, the same size and the same shape."
GREEN = "The lawn keeps exactly the same bright green."
WHOLE = ("The lawn stays whole: no hole, pit or trench is dug anywhere, and the cut face at the front does not change.")
KEEP = "Everything else identical."
PASTE = ("Same picture as the reference image: keep exactly the same camera position, zoom and framing, and keep every object "
"exactly where it is in that image, at the same size and the same angle: the house, the porch, the lawn, the boat, the bank, "
"the lake, the cut face of the block and everything standing on the lawn or in the water. The reference is a rough paste-up: "
"render it as one clean photoreal picture with the same layout.")
CLOSE = ("Same picture as the reference image, which is a soft, blurry enlargement: keep exactly the same framing, and keep "
"every object exactly where it is in that image, at the same size and the same angle. Render it sharp and richly detailed, "
"as one clean photoreal close view.")
LOCKC = ("Same scene as the reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in it stays exactly where it is, the same size and the same shape.")
BOATIS = ("The boat is " + BOATW + "; it is exactly broadside to the camera, its keel level across the picture, its pointed "
"bow at the right.")
NOPIT = "No hole, pit or trench is dug anywhere: the lawn stays whole, and the cut face at the front does not change."
NOONE = "No people. No animals."

P = {
 # ---- keys (as run) ----
 "K0": (
        "Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers "
        "and what is buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean "
        "realistic materials, translucent cyan water, tidy and uncluttered. No text, no letters, no numbers, no "
        "captions, no logos, no watermark. Scene: a suburban back yard that runs down to a lake, on a bright summer "
        "afternoon, shown as a cutaway model. Across the back stands the rear of a one-storey house with pale "
        "grey-blue horizontal siding, white window frames, a wide back door and a covered wooden porch. In front of "
        "it a large, freshly mown green lawn with faint mowing stripes slopes gently down to a low grassy bank at "
        "the water's edge. Near the bottom of the lawn, right of centre, stands a small black kettle barbecue on "
        "three legs. Beyond the bank lies the lake: calm, translucent cyan water. From the right, a narrow wooden "
        "dock on posts comes out over the water and ends in a wider T-shaped platform. The yard and the lake stand "
        "on a deep block cut straight down like a slice of cake toward the camera, so the cut face shows the lake in "
        "section, like the glass side of an aquarium: translucent cyan water over a bed of pale sand and even layers "
        "of brown earth. Camera: from the front and high up, as if from a drone at the height of the house's roof "
        "edge, looking down at about 45 degrees over the cut face, across the lake and up the lawn toward the back "
        "of the house. The house's roof is cut off by the top of the frame: only its ground floor, the back door and "
        "the porch show, in the top tenth of the frame. The lawn is seen from above and fills the frame from about "
        "10% to 52% down, from the left edge to the right edge: wide, open and empty but for the barbecue, which "
        "stands about 66% across and 48% down. The grassy bank and the water's edge run straight across the frame "
        "about 52% down. The lake fills the frame from about 52% to 76% down, from edge to edge. The neighbor's "
        "wooden dock comes in from the right edge about 64% down; its T-shaped end is about 58% to 74% across and "
        "61% to 68% down. The front edge of the water runs straight across the frame about 76% down; below it the "
        "cut face of the block runs down to about 88%: the translucent cyan water in section with the dock's posts "
        "standing in it, and the pale lake bed and earth layers under it. Under the block is plain, pale, calm "
        "ground to the bottom of the frame. There is no ground in front of the block. The lawn is empty but for the "
        "barbecue: no boat, no vehicle, no people, no animals, no tools, no furniture."),
 "K0.B": (
        "Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers "
        "and what is buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean "
        "realistic materials, translucent cyan water, tidy and uncluttered. No text, no letters, no numbers, no "
        "captions, no logos, no watermark. Scene: a suburban back yard that runs down to a lake, on a bright summer "
        "afternoon, shown as a cutaway model. Across the back stands the rear of a one-storey house with pale "
        "grey-blue horizontal siding, white window frames, a wide back door and a covered wooden porch. In front of "
        "it a large, freshly mown green lawn with faint mowing stripes slopes gently down to a low grassy bank at "
        "the water's edge. Near the bottom of the lawn, right of centre, stands a small black kettle barbecue on "
        "three legs. Beyond the bank lies the lake: calm, shallow, translucent cyan water, wide open. From the "
        "right-hand end of the bank a narrow wooden dock on posts runs out over the water and ends in a wider "
        "T-shaped platform. The yard and the lake stand on a block cut straight down like a slice of cake toward the "
        "camera, so the cut face shows the lake in section, like the glass side of an aquarium: a low band of "
        "translucent cyan water over a thin bed of pale sand and brown earth. Camera: from the front and high up, as "
        "if from a drone above the house's roof edge, looking steeply down at about 55 degrees over the cut face, "
        "across the lake and up the lawn toward the back of the house. The house's roof is cut off by the top of the "
        "frame: only its ground floor, the back door and the porch show, in the top tenth of the frame. The lawn is "
        "seen from above and fills the frame from about 10% to 46% down, from the left edge to the right edge: wide, "
        "open and empty but for the barbecue, which stands about 64% across and 41% down. The grassy bank and the "
        "water's edge run straight across the frame about 46% down. The lake is big: seen from above, its surface "
        "fills the frame from about 46% to 78% down, from edge to edge, almost as long from the bank to its front "
        "edge as the lawn is from the house to the bank. The wooden dock starts at the right-hand end of the bank "
        "and runs out over the water down the right-hand side of the lake; near the front of the lake it ends in its "
        "wider T-shaped platform, which is about 62% to 82% across and 66% to 71% down. The front edge of the water "
        "runs straight across the frame about 78% down; below it the cut face of the block is a low band that runs "
        "down only to about 88%: the shallow translucent cyan water in section with the dock's posts standing in it, "
        "and a thin layer of pale lake bed and brown earth under it. Under the block is plain, pale, calm ground to "
        "the bottom of the frame. There is no ground in front of the block. The lawn is empty but for the barbecue: "
        "no boat, no vehicle, no people, no animals, no tools, no furniture."),      # not used: came back corner-on
 "KH": (
        "Photoreal 3D render of a stubby steel workboat sitting on plain, pale, flat ground in bright soft daylight "
        "with soft shadows, seen from its side and from above at about 45 degrees, like a reference picture: the "
        "boat lies across the frame with its pointed bow to the right and its flat stern to the left, the whole boat "
        "in frame. It is about three times as long as it is wide, with high sides. Its steel hull is dark navy blue "
        "with a red band along the bottom and a thin white stripe at the deck edge. At the bow end stands a small "
        "white wheelhouse with square windows, taking up the front third of the deck. Behind the wheelhouse, in the "
        "middle of the boat, is one big rectangular open hatch in the grey steel deck: through it the empty inside "
        "of the hull shows, its bare steel bottom far below. The stern end of the deck is flat, grey and empty. A "
        "low steel rail runs round the deck edge. No mast, no crane, no name, no flag, no numbers, no ropes. Nothing "
        "else is in the frame: no water, no plants, no props, no people, no animals. Clean realistic materials, mild "
        "depth of field. No text, no letters, no numbers, no captions, no logos, no watermark."),
 # ---- the hook ----
 # try A (refs BASE, KH) put the boat at the key's three-quarter angle, 61% wide and low on the lawn, with a toy-sized truck.
 # try B: no boat key (it pulls the pose), the pose spelled out, the truck bigger. The boat of the accepted S0 is the key
 # from here on (KB: a crop of it, uploaded).
 "S0.A": (f"{STYLE} {LOCK} Change only this: a boat now sits on the lawn near the house, on a row of short wooden blocks, "
        f"lying across the lawn, parallel to the water's edge: its pointed bow to the right, its flat stern to the left. "
        f"{BOAT2}. It is big: from the camera it runs from about 33% to 75% across the frame and from about 12% to 26% "
        f"down; we see its lake-side flank and, from above, its deck. A thick pale tow rope runs tight and straight from "
        f"the middle of the boat's near side down the lawn to the back of a red pickup truck with dark windows, which "
        f"stands on the grass below the boat with its nose pointing at the lake, about 49% to 59% across and 31% to 43% "
        f"down. The barbecue stays where it is. {WHOLE} {GREEN} {KEEP} {NOONE}"),
 "S0.B": (f"{STYLE} {LOCK} Change only this: a boat now sits on the lawn close to the house, on a row of short wooden "
        f"blocks. It is {BOATW}; it is about three times as long as it is wide, with high sides. It lies exactly "
        f"broadside to the camera: its keel runs level, straight across the picture from left to right, parallel to the "
        f"house wall behind it and to the water's edge in front of it. Its pointed bow is at the right and its flat stern "
        f"at the left, both at the same height in the picture: the boat is not turned or angled. We look square at its "
        f"long lake-side flank and down onto its deck. From the camera the boat runs from about 31% to 75% across the "
        f"frame; the top of its wheelhouse is about 12% down the frame and the wooden blocks under its keel about 27% "
        f"down. A thick pale tow rope runs tight and straight down the lawn from the middle of the boat's near side to "
        f"the back of a big plain red pickup truck with dark windows, which stands on the grass below the boat, facing "
        f"the lake: its tailgate toward the boat, its nose toward the camera. The truck is large in the picture: about "
        f"46% to 60% across the frame and 30% to 44% down. The barbecue stays where it is, right of the truck and "
        f"clear of it. {WHOLE} {GREEN} {KEEP} {NOONE}"),
 # tries C and D: the boat and the truck of try B cut out on this machine, the boat levelled (a shear) and both laid on the
 # base at their places (the paste-ups S0C, then S0D with the boat 25-75% across and 1.25x taller: uploaded); this pass
 # renders the paste-up clean. S0 is try D.
 "S0": (f"{STYLE} Same picture as the reference image: keep exactly the same camera position, zoom and framing, and keep "
        f"every object exactly where it is in that image, at the same size and the same angle: the house, the porch, the "
        f"lawn, the boat, the pickup truck, the barbecue, the bank, the lake, the wooden dock and the cut face of the "
        f"block. The reference is a rough paste-up: render it as one clean photoreal picture with the same layout. The "
        f"boat is {BOATW}; it sits on a row of short wooden blocks on the lawn, exactly broadside to the camera, its keel "
        f"level across the picture, its pointed bow at the right. It casts a soft shadow on the grass to its right, like "
        f"the barbecue's. A thick pale tow rope runs tight and straight down the lawn from the middle of the boat's near "
        f"side to the tow hitch at the back of the red pickup truck, which stands on the grass below the boat, facing the "
        f"lake, its nose toward the camera; it casts a soft shadow to its right. {WHOLE} {GREEN} {NOONE}"),
 # ---- the hook's end, and failure 1 ----
 "H": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: the red pickup truck has dug itself in. Its rear wheels have torn "
       f"two short, shallow brown ruts of bare earth in the grass under and behind them, and a fan of loose brown earth "
       f"and torn turf is sprayed over the grass behind the truck, between the truck and the boat. The truck has slewed "
       f"a quarter turn to its left: it now stands at an angle, its nose pointing at the lower left corner of the picture "
       f"and lifted a little off the ground, its rear wheels sunk in the ruts. The tow rope is still tight between the "
       f"boat and the back of the truck. The barbecue stays where it is. The cut face at the front does not change. "
       f"{GREEN} {KEEP} {NOONE}"),
 "F1": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: the red pickup truck and the tow rope are gone: the grass where the "
        f"truck stood is empty. The two short brown ruts and the loose earth sprayed on the grass stay exactly as they "
        f"are. The barbecue stays where it is. The cut face at the front does not change. {GREEN} {KEEP} {NOONE}"),
 # ---- loop 1: the slipway ----
 "S1_1": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: twelve steel piles now stand in two straight rows of six, running "
          f"from the lawn just below the boat straight down into the lake. Each pile is a thick round grey steel pipe, as "
          f"thick as a tree trunk, driven into the ground and standing waist-high. The left row is about 24% across the "
          f"frame and the right row about 76% across; in each row the piles stand about 31%, 36%, 42% and 48% down the "
          f"frame on the lawn, and about 55% and 59% down in the lake, where they stand in the water with their tops above "
          f"the surface and show through the water in the cut face. There are no rails yet. The barbecue stays where it "
          f"is, between the two rows. {NOPIT} {GREEN} {KEEP} {NOONE}"),
 "S1_2": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: two long, heavy steel rails now lie on top of the pile heads, one "
          f"along each row of piles: two straight dark steel beams, parallel, each running from the top pile of its row, "
          f"about 30% down the frame, down the lawn, over the bank and under the water to the last pile, about 60% down, "
          f"where its lower end is under the surface. Each rail rests on the tops of its six piles. Nothing sits on the "
          f"rails yet. The barbecue stays where it is, between the rails. {NOPIT} {GREEN} {KEEP} {NOONE}"),
 "S1_3": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: a long timber cradle now sits across the top end of the two rails, "
          f"just below the boat: a sturdy, flat, open frame of heavy brown timbers, a little longer than the boat, with "
          f"steel wheels at each end that rest on the two rails. It spans from about 21% to 76% across the frame and from "
          f"about 30% to 37% down. It is empty: the boat still sits on its wooden blocks behind it. The barbecue stays "
          f"where it is. {NOPIT} {GREEN} {KEEP} {NOONE}"),
 "S1_4": (f"{STYLE} {PASTE} {BOATIS} It now sits on the long timber cradle, its keel resting in the cradle's timbers; the "
          f"cradle's steel wheels rest on the two steel rails. The row of short wooden blocks the boat used to stand on "
          f"stays on the lawn behind it, empty. The boat casts a soft shadow on the grass to its right. The two steel "
          f"rails run on down the lawn on their piles and into the lake, as in the reference. The barbecue stays where "
          f"it is, between the rails. {NOPIT} {GREEN} {NOONE}"),
 # ---- loop 2: the launching trigger ----
 "F2": (f"{STYLE} {PASTE} {BOATIS} The boat sits on the long timber cradle, which has rolled a little way down the two "
        f"steel rails toward the lake and stopped: the cradle's front timber has run over the kettle barbecue, which now "
        f"lies crushed flat on the grass under it, its black bowl dented, its legs splayed and its lid lying beside it. "
        f"The upper ends of the two rails, behind the cradle, are bare again. The row of short wooden blocks stays on the "
        f"lawn near the house. The boat casts a soft shadow on the grass to its right. {NOPIT} {GREEN} {NOONE}"),
 "CV2_0": (f"{STYLE} {CLOSE} It shows the left end of the long timber cradle on the lawn: heavy brown timbers bolted "
           f"together, with steel wheels resting on the left steel rail, which runs straight down the lawn on its row of "
           f"round steel piles. On the cradle sits the stern end of the boat: a dark navy-blue steel hull with a red band "
           f"along its bottom and a thin white stripe at the deck edge, at the right-hand side of the picture. The lawn "
           f"around is plain mown grass. No hole, pit or trench anywhere. {NOONE}"),
 "CV2_1": (f"{STYLE} {LOCKC} Change only this: one thick round grey steel pile now stands in the lawn just behind the "
           f"cradle's back timber, beside the steel rail: driven into the ground and standing chest-high, as thick as a "
           f"tree trunk. Nothing is attached to it yet. The lawn stays whole around it: no hole, pit or trench. {KEEP} "
           f"{NOONE}"),
 "CV2_2": (f"{STYLE} {LOCKC} Change only this: a heavy black iron hook, as long as an arm, is now hinged on the head of "
           f"the steel pile and clamped down over the cradle's back timber, gripping it. {KEEP} {NOONE}"),
 "CV2_3": (f"{STYLE} {LOCKC} Change only this: a tall steel release lever with a red handle now stands beside the steel "
           f"pile, linked to the hook at the pile's head: a straight steel bar, half as tall again as the pile. {KEEP} "
           f"{NOONE}"),
 "S2_T": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: a launching trigger now holds the cradle. Just behind the cradle's "
          f"back timber at its left end, beside the left rail, stands a thick round grey steel pile, chest-high; a heavy "
          f"black iron hook hinged on the pile's head is clamped down over the cradle's back timber; and beside the pile "
          f"stands a tall steel release lever with a red handle. The cradle stays exactly where it is. {NOPIT} {GREEN} "
          f"{KEEP} {NOONE}"),
 # ---- loop 3: the drag chains ----
 "S3_1": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: the wooden dock is wrecked. Its wide T-shaped end platform is "
          f"smashed away and gone, posts and all: only the first short stretch of the dock is left, running from the bank "
          f"at the right-hand side out to a broken, splintered end about 84% across the frame and 58% down. A few broken "
          f"planks float on the water close to the right-hand edge of the frame. The water in the middle of the lake is "
          f"open and clear. The cradle, the trigger and everything on the lawn stay exactly as they are. {GREEN} {KEEP} "
          f"{NOONE}"),
 "F3": (f"{STYLE} {PASTE} {BOATIS} The boat has just slid into the lake and floats there, close to the camera, low in the "
        f"water: only the upper part of its navy hull shows above the surface. It has smashed through the end of the "
        f"wooden dock: white foam and spray surge all round its hull, rings of waves spread across the lake, and broken "
        f"planks float against its right-hand end; the stub of the dock at the right ends in splintered wood. On the lawn "
        f"the two steel rails are empty: the cradle has gone down the rails with the boat and is under the water, out of "
        f"sight. The trigger's steel pile stands beside the left rail with its hook thrown open. The crushed barbecue "
        f"lies on the grass between the rails. {GREEN} {NOONE}"),
 "S3_2": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: two heaps of heavy, rusty anchor chain now lie on the lawn, one "
          f"beyond each end of the cradle. Each heap is a knee-high pile of big dark chain links. The left heap is about "
          f"8% to 14% across the frame and the right heap about 81% to 86% across; both are about 42% to 46% down. From "
          f"each heap a steel wire rope runs along the grass to the nearest end of the boat's hull, where it is shackled "
          f"to the hull. {NOPIT} {GREEN} {KEEP} {NOONE}"),
 "S3_3": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: two more heaps of the same heavy, rusty anchor chain now lie on "
          f"the lawn further down the slope, straight below the first two and just above the bank: the left one about 8% "
          f"to 14% across the frame and the right one about 81% to 86% across, both about 48% to 52% down. From each new "
          f"heap a steel wire rope also runs along the grass to the nearest end of the boat's hull. The first two heaps "
          f"and their wire ropes stay exactly as they are. {NOPIT} {GREEN} {KEEP} {NOONE}"),
 "S3_L": (f"{STYLE} {PASTE} {BOATIS} The boat floats quietly in the lake just off the bank, low in the water, at rest: the "
          f"water round it is calm, with only a few soft ripples. On the lawn the two steel rails are empty: the cradle "
          f"is under the water at the foot of the rails, out of sight. The four heaps of anchor chain have been dragged "
          f"down the lawn and lie at the top of the bank, two at each side, each at the end of a brown drag mark scraped "
          f"through the grass; from each heap a steel wire rope runs tight over the bank to the nearest end of the boat. "
          f"The trigger's steel pile stands beside the left rail with its hook open. The crushed barbecue lies on the "
          f"grass between the rails. The dock is wrecked, as in the reference. {GREEN} {NOONE}"),
 # ---- loop 4: the ballast (a closer view of the boat afloat) ----
 "CV4_u": (f"{STYLE} {CLOSE} It shows the boat afloat in the lake, seen from above and from its side: {BOATW}. It floats "
           f"level and low in the calm translucent cyan water, exactly broadside to the camera, bow at the right. Through "
           f"the big open hatch the empty steel floor of its hold shows, far below. Behind it are the grassy bank and the "
           f"lower edge of the lawn; in front of it the front edge of the water and the cut face of the block. {NOONE}"),
 "CV4_0": (f"{STYLE} {LOCKC} Change only this: the boat is heeling over toward the camera. It has rolled about 20 degrees "
           f"onto its near side: its near deck edge and rail are under water and water washes across the deck toward the "
           f"open hatch; its far side is lifted, and the wheelhouse leans toward the camera. It floats in the same place "
           f"and is the same size. {KEEP} {NOONE}"),
 "CV4_1": (f"{STYLE} {LOCKC} The boat stays heeled over exactly as it is. Change only this: a row of four black cast-iron "
           f"ballast blocks now sits on the floor of the hold, seen through the open hatch, in the right-hand half of the "
           f"hatch opening, the half nearer the wheelhouse: four identical dark iron blocks, each the size of a suitcase, "
           f"side by side. {KEEP} {NOONE}"),
 "CV4_2": (f"{STYLE} {LOCKC} The boat stays heeled over exactly as it is. Change only this: a second row of four identical "
           f"black cast-iron blocks now sits on the floor of the hold in the left-hand half of the hatch opening, behind "
           f"the first row, the half nearer the stern. The first row stays exactly as it is. {KEEP} {NOONE}"),
 "CV4_3": (f"{STYLE} {LOCKC} Change only this: the hatch in the boat's deck is now closed by a flat grey steel hatch cover "
           f"with a raised rim: the opening is covered and the hold can no longer be seen. The boat floats level, exactly "
           f"as it is. {KEEP} {NOONE}"),
 "S4_T": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: the hatch in the middle of the boat's deck is now closed by a flat "
          f"grey steel hatch cover. {GREEN} {KEEP} {NOONE}"),
 # ---- loop 5: the boat hoist ----
 "F5": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: small boats have crowded into the lake round the big boat, waiting. "
        f"A small white sailboat with a bare mast floats alone at the left, about 7% to 15% across the frame and 57% to "
        f"64% down; a white rowing boat floats between it and the big boat's stern, about 21% to 26% across; and at the "
        f"right, between the big boat's bow and the stub of the dock, float a little red motorboat and a yellow kayak, "
        f"about 76% to 85% across. All are far smaller than the big boat. Nobody is in them. {GREEN} {KEEP} {NOONE}"),
 "S5_1": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: two long concrete piers now stand in the lake at the left, side by "
          f"side, each running straight out from the bank toward the camera: flat grey concrete decks standing just above "
          f"the water on thick round concrete piles. The left pier is about 1% to 6% across the frame and the right pier "
          f"about 16% to 21% across; both run from the bank, about 54% down the frame, out to about 66% down. The small "
          f"white sailboat floats in the slot of water between them. The piers' piles show through the water in the cut "
          f"face at the front. The small boats stay where they are. {GREEN} {KEEP} {NOONE}"),
 "S5_2": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: a tall yellow boat hoist now stands on the two concrete piers, "
          f"straddling the slot of water between them: an open gantry of bright yellow steel, with four tall legs on big "
          f"black rubber tires, two tires on each pier, joined at the top by two long yellow beams and two cross beams. "
          f"Nothing hangs from it yet. It is about 1% to 21% across the frame; its tires stand on the piers and its top "
          f"beams are about 38% down the frame, high above the small white sailboat that floats between its legs. "
          f"{GREEN} {KEEP} {NOONE}"),
 "S5_3": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: two wide black slings now hang from the hoist's top beams "
          f"straight down into the water between the piers, one near each end of the small white sailboat, passing under "
          f"its hull. The hoist and the sailboat stay exactly where they are. {GREEN} {KEEP} {NOONE}"),
 "S5_U": (f"{STYLE} {LOCK} {BOATSTAY} Change only this: the hoist has lifted the small white sailboat out of the water. "
          f"It now hangs in the two black slings between the hoist's legs, its keel well clear of the water, with water "
          f"dripping from its hull. The hoist stays exactly where it is. {GREEN} {KEEP} {NOONE}"),
}
REFS = {
 "K0": [], "KH": [],
 "S0.A": ["BASE", "KH"], "S0.B": ["BASE"], "S0.C": ["S0C"], "S0": ["S0D"],
 "H": ["S0"], "F1": ["H"],
 "S1_1": ["F1"], "S1_2": ["S1_1"], "S1_3": ["S1_2"], "S1_4": ["S1_4P"],
 "F2": ["F2P"], "CV2_0": ["CV2P"], "CV2_1": ["CV2_0"], "CV2_2": ["CV2_1"], "CV2_3": ["CV2_2"], "S2_T": ["F2"],
 "S3_1": ["S2_T"], "F3": ["F3P"], "S3_2": ["S3_1"], "S3_3": ["S3_2"], "S3_L": ["S3LP"],
 "CV4_u": ["CV4P"], "CV4_0": ["CV4_u"], "CV4_1": ["CV4_0"], "CV4_2": ["CV4_1"], "CV4_3": ["CV4_u"],
 "S4_T": ["S3_L"], "F5": ["S4_T"], "S5_1": ["F5"], "S5_2": ["S5_1"], "S5_3": ["S5_2"], "S5_U": ["S5_3"],
}
# ---- 25 Nov, later: text edits could not place a dozen small parts (S1_1.T came back with piles as tall as the boat, in
# clumps, and the ruts erased). From here a step is laid out on this machine (pipeline/18-stage.py: drawn or pasted at its
# exact place on the picture before), the paste-up is uploaded (key + "P") and one pass renders it clean.
for k in ("S1_1", "S1_2", "S1_3"): P[k + ".T"] = P[k]; REFS[k + ".T"] = REFS[k]
P.update({
 "S1_1": (f"{STYLE} {PASTE} {BOATIS} Twelve round grey steel piles stand in two straight rows of six, running from the lawn "
          f"below the boat down into the lake, exactly where the reference shows them: thick steel pipes driven into the "
          f"ground, standing waist-high, each casting a short soft shadow on the grass to its right; the lowest two of "
          f"each row stand in the water. There are no rails on them. The two brown ruts in the grass stay as they are. "
          f"The barbecue stays where it is. {NOPIT} {GREEN} {NOONE}"),
 "S1_2": (f"{STYLE} {PASTE} {BOATIS} Two long, heavy steel rails lie on the heads of the two rows of steel piles, exactly "
          f"where the reference shows them: two straight, dark steel I-beams, each resting on the tops of its six piles, "
          f"running from just below the boat down the lawn and over the bank, where their lower ends slope under the "
          f"water. Each rail casts a soft shadow on the grass to its right. Nothing sits on the rails. The ruts and the "
          f"barbecue stay as they are. {NOPIT} {GREEN} {NOONE}"),
 "S1_3": (f"{STYLE} {PASTE} {BOATIS} A long timber cradle sits across the top end of the two steel rails, just below the "
          f"boat, exactly where the reference shows it: a sturdy, flat, open frame of heavy brown timbers bolted "
          f"together, with steel wheels at each end resting on the rails. It is empty: the boat still sits on its wooden "
          f"blocks behind it. The rails, their piles, the ruts and the barbecue stay as they are. {NOPIT} {GREEN} "
          f"{NOONE}"),
})
REFS.update({"S1_1": ["S1_1P"], "S1_2": ["S1_2P"], "S1_3": ["S1_3P"]})
# ---- the plate (PLATE: the yard with rails, ruts and empty blocks, no boat, no cradle; made on this machine) and what is
# drawn on it once: the crushed barbecue. The boat and the cradle are then laid on it at each position (18-stage.py).
P["BBQ"] = (f"{STYLE} {LOCK} Change only this: the black kettle barbecue has been run over and crushed flat. It lies squashed "
            f"on the grass in exactly the same spot: its black bowl flattened and dented, its three legs splayed out flat on "
            f"the grass, its domed lid lying beside it. Nothing else changes: the two steel rails, their piles, the wooden "
            f"blocks, the brown ruts and the dock stay exactly as they are. {GREEN} {KEEP} {NOONE}")
REFS["BBQ"] = ["PLATE"]
ASPECT = {"KH": "16:9"}

# ---- clips (wan2_7, 720p, 9:16): from the stage before to the stage after (CLAUDE.md 6.3); written at Step 7 ----
CLOCK = "The camera is locked and never moves."
SELF = "Nobody is there: the parts move by themselves."
C = {}

def jobs():
    J = {}
    try:
        for l in open(__file__.replace("18-prompts.py", "18-jobs.tsv")):
            if l.startswith("# Higgsfield folder "): J["FOLDER"] = l.split()[3]
            if l.strip() and not l.startswith("#") and not l.startswith("key"):
                k, j = l.split("\t")[:2]; J[k.split(".")[0]] = j.strip()
    except FileNotFoundError:
        pass
    J.setdefault("BASE", J.get("K0S", J.get("K0")))   # the stage base: the widened set key
    return J

if __name__ == "__main__":
    kind, keys = sys.argv[1], [a for a in sys.argv[2:] if not a.startswith("--")]; J = jobs(); out = []
    for i, key in enumerate(keys):
        k = key.split(".")[0]
        if kind == "still":
            prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": ASPECT.get(k, "9:16"),
                   "prompt": P[key] if key in P else P[k]}
            refs = REFS[key] if key in REFS else REFS[k]
            if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
        else:
            a, b, secs = C[k][0], C[k][1], C[k][2]
            prm = {"model": "wan2_7", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs,
                   "medias": [{"role": "start_image", "value": J[a]}, {"role": "end_image", "value": J[b]}],
                   "prompt": C[k][3]}
        if "FOLDER" in J: prm["folder_id"] = J["FOLDER"]
        out.append({"index": i, "params": prm})
    wrap = "--wrap" in sys.argv
    print(json.dumps({"requests": out} if wrap else out, ensure_ascii=False))
