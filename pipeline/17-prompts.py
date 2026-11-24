# Video 17 (B12, "How to Keep a T-Rex in Your Back Yard"): picture and clip requests for Higgsfield.
#   python3 17-prompts.py still KEY [KEY ...]   -> requests for generate_image_batch (seedream_v5_pro, 1k, 9:16)
#   python3 17-prompts.py clip  KEY [KEY ...]   -> requests for generate_video_batch (wan2_7, 720p, 9:16)
# Gate A and Gate B approved by the user on 23 Nov 2026 (quote 188.40). The plan is 17-beat-sheet.md (the stage ladder and
# the step sheet). Job ids are read from 17-jobs.tsv (key <tab> job id; a key with a try suffix, S1_2.B, replaces S1_2
# when it is listed later). Lines here are CLAUDE.md 6.3's, with this set's own SET, CAMERA, the T-rex's words and the dog's.
# Every picture after the set key is an edit of the one before it (LOCKG), so the set keeps its parts, colours and light;
# the T-rex key (KT) is a second reference wherever he is in the picture, and the dog key (DOG, video 16's) wherever the dog is.
import json, sys

STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent "
"cyan water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
SET = ("a big suburban back yard on a bright summer afternoon, shown as a cutaway model. Across the back stands the rear of a "
"one-storey house with pale grey-blue horizontal siding, white window frames, a wide back door and a covered wooden porch with "
"two chairs. In front of it lies a large, flat, freshly mown green lawn with faint mowing stripes. At the back left corner of "
"the lawn stands a small garden shed of pale timber with a grey shingle roof. Near the front of the lawn, right of centre, a "
"small grey robot lawn mower sits on its charging dock. Down the right side of the lawn runs a plain wooden board fence about "
"as tall as a person, and beyond it, in the neighbor's yard, is a small rectangular swimming pool of translucent cyan water "
"with a white stone edge, at the front. The yard stands on a deep block of ground cut straight down like a slice of cake "
"toward the camera, so the cut face shows dark topsoil over even layers of brown earth")
CAMERA = ("Camera: from the front and high up, as if from a drone at the height of the house's roof edge, looking down at about 45 "
"degrees over the cut face and across the lawn toward the back of the house. The house's roof is cut off by the top of the "
"frame: only its ground floor, the back door and the porch show, in the top fifth of the frame. The lawn is seen from above "
"and fills the frame from about 20% to 64% down and from the left edge to about 72% across: wide, open and empty, with the "
"shed in its back left corner and the mower's dock near its front, about 50% to 57% across. The neighbor's fence runs from "
"the back to the front about 73% across, and the neighbor's pool fills the front right corner, from about 76% to 100% across "
"and 44% to 64% down. The lawn's front edge runs straight across the frame about 64% down; below it the cut face of the block "
"of ground runs down to about 84%: dark topsoil over even layers of brown earth, and at the front right the neighbor's pool "
"is cut through too, its translucent cyan water showing in section inside its concrete shell. Under the block is plain, "
"pale, calm ground to the bottom of the frame. There is no ground in front of the block")
EMPTY = "The lawn is empty: no animals, no people, no tools and no furniture on the grass."
# the stage view, if the set key comes back from head height (CLAUDE.md 7.1): a POS edit that raises the camera
POS = ("The same back yard, house, porch, lawn, shed, mower, fence, neighbor's pool and block of ground as the reference image, "
"with the same parts, colours, materials and light.")
STAGE = ("New camera position: much higher and a little closer, as if from a drone at the height of the house's roof edge, "
"looking down at about 45 degrees. The house's roof is cut off by the top of the frame: only its ground floor, the back door "
"and the porch show, in the top fifth of the frame. The lawn is seen from above and fills the frame from about 20% to 64% "
"down, wide and open. Its front edge runs straight across the frame about 64% down; below it the cut face of the block of "
"ground runs down to about 84%, and under that is plain pale ground. Nothing in view changes: the lawn is empty.")

TREXW = ("The T-rex is the same animal as in the T-rex reference image: a Tyrannosaurus rex with scaly, pebbly skin, moss-green "
"on his back fading to grey on his flanks, a pale cream belly and throat, small two-fingered arms, no stripes and no feathers")
DOGW = ("the same dog as in the dog reference image: a small scruffy tan terrier with a cream chest and muzzle, soft folded ears "
"and a red collar")
LOCKG = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"house, the porch, the lawn, the fences, the neighbor's pool, the cut face of the ground and everything already standing on "
"the lawn stay exactly where they are and the same size.")
REXSTAY = "The T-rex stays exactly where he is, in exactly the same pose."
GREEN = "The lawn keeps exactly the same bright green."
WHOLE = ("The lawn stays whole around it: no hole, pit or trench is dug anywhere, and the cut face of the ground at the front "
"does not change.")
KEEP = "Everything else identical."
ONLYREX = "No people; the only animal is the T-rex."
REXDOG = "No people; the only animals are the T-rex and the dog."
NOANIMAL = "No people. No animals."
NONEW = ("No other holes, pits or trenches are dug anywhere, and the rest of the cut face of the ground does not change.")

P = {
 # ---- keys ----
 "K0": f"{STYLE} Scene: {SET}. {CAMERA}. {EMPTY}",
 "KV": f"{STYLE} {POS} {STAGE}",
 "KT": ("Photoreal 3D render of a Tyrannosaurus rex standing on plain, pale, flat ground in bright soft daylight with soft "
        "shadows, seen exactly side-on from his left, facing right, the whole animal in frame from the tip of his tail to his "
        "snout, like a museum reference picture. He is heavily built: a huge deep head, a closed mouth with a few teeth showing, "
        "small two-fingered arms, thick muscular legs with three-toed feet, and a long tail held level off the ground. His skin "
        "is scaly and pebbly, moss-green on his back fading to grey on his flanks, with a pale cream belly and throat; no "
        "stripes, no spots and no feathers. His eye is calm and alert. Nothing else is in the frame: no plants, no props, no "
        "people, no other animals. Clean realistic materials, mild depth of field. No text, no letters, no numbers, no "
        "captions, no logos, no watermark."),
 # ---- the hook ----
 "S0a": (f"{STYLE} {LOCKG} Change only this: a Tyrannosaurus rex now stands on the lawn, side-on, facing right. {TREXW}. He "
         f"is as tall as the house's roof edge: his feet stand on the grass in the middle of the lawn, about 40% down from the "
         f"top; his body runs from about 8% to 55% across the frame, his tail to the left and his head to the right, about 22% "
         f"down. The mower and its dock stay where they are, in front of him. {WHOLE} {GREEN} "
         f"{KEEP} {ONLYREX}"),
 "S0": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: a few short sections of white wooden picket fence, as high as the "
        f"T-rex's ankles, already stand on the grass in an arc round the left side of his feet: the start of a ring round him. "
        f"And on the porch at the back, small in the frame, stands {DOGW}, barking toward the T-rex. {WHOLE} {GREEN} {KEEP} "
        f"{REXDOG}"),
 "H": (f"{STYLE} {LOCKG} The T-rex and the dog stay exactly where they are, in exactly the same poses. Change only this: the "
       f"white picket fence now runs all the way round the T-rex's feet in a closed oval ring on the grass, about 40% of the "
       f"frame wide, its pickets as high as his ankles. {WHOLE} {GREEN} {KEEP} {REXDOG}"),
 # ---- loop 1: the cable fence ----
 "F1": (f"{STYLE} {LOCKG} Change only this: the T-rex has stepped right over his picket fence: the right side of the ring "
        f"is trampled flat, and one of his feet now stands on the flattened pickets there while the other is still inside the "
        f"ring; his body and head are where they were, a little further right. {TREXW}. The porch is empty now: the dog has gone inside. {WHOLE} {GREEN} "
        f"{KEEP} {ONLYREX}"),
 "S1_1": (f"{STYLE} {LOCKG} {REXSTAY} The flattened picket ring stays as it is. Change only this: round dark holes, "
          f"each as wide as a person and with a small ring of fresh soil round it, are now dug along three sides of the "
          f"lawn only: one row along the back edge of the lawn, in front of the porch and the house; one row down the left "
          f"edge of the frame; and one row down the right side, just inside the neighbor's wooden fence. There are no holes "
          f"along the front edge of the lawn: the front of the lawn, toward the camera, stays open and whole. Only the two "
          f"front corner holes reach the cut face, where each shows as one deep round shaft going straight down through the "
          f"soil layers; the rest of the cut face does not change. The rest of the lawn stays whole. And the house's back "
          f"door is now shut. {GREEN} {KEEP} {ONLYREX}"),
 "S1_2": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: a tall round grey steel pole now stands straight up in every "
          f"one of the holes, as thick as a man and much taller than a man: each pole rises about 12% of the frame's height "
          f"above the grass, so the poles along the back of the lawn reach up past the porch roof, the poles down the left "
          f"side reach as high as the T-rex's back, and the two poles at the front rise out of their shafts in the cut face to "
          f"as high as the T-rex's hips. No hole is left empty. {NONEW} {GREEN} {KEEP} {ONLYREX}"),
 "S1_3": (f"{STYLE} {LOCKG} {REXSTAY} The poles stay exactly where they are. Change only this: smooth grey concrete "
          f"now fills the top of every hole that has a pole in it, round the pole's foot, flush with the grass; the two "
          f"shafts in the cut face are filled with grey concrete round their poles: deep footings. And the row of empty holes "
          f"beside the neighbor's fence and pool is filled back in: the grass there is whole again. {NONEW} {GREEN} {KEEP} "
          f"{ONLYREX}"),
 "S1_4": (f"{STYLE} {LOCKG} {REXSTAY} The poles and their concrete stay exactly where they are, and so does the white "
          f"picket ring round the T-rex's feet with its trampled pickets. Change only this: six "
          f"thick steel cables now run level from pole to pole, evenly spaced from near the ground to the top of the poles, "
          f"along every row of poles and across the gaps between them, so a tall cable fence now runs all the way round the "
          f"T-rex. {WHOLE} {GREEN} {KEEP} {ONLYREX}"),
 # ---- loop 2: the ha-ha ----
 "F2a": (f"{STYLE} {LOCKG} Change only this: the T-rex leans out over the cable fence on the right: his feet stay "
         f"where they are, his body tips forward and his neck stretches out and down over the top cables, and his snout is "
         f"in the neighbor's pool, drinking; the pool's water is half gone, and in the cut face its level is half way down "
         f"too. {TREXW}. {WHOLE} {GREEN} {KEEP} "
         f"{ONLYREX}"),
 "F2": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: the neighbor's pool is now empty: its pale blue floor is bare "
        f"and dry, and in the cut face its section is empty too; and a little water drips from the T-rex's chin. {WHOLE} "
        f"{GREEN} {KEEP} {ONLYREX}"),
 "S2_1": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: a wide ditch is now dug into the lawn along the inside of "
          f"the right-hand cable fence, between the T-rex and that fence, from the back corner of the lawn to the front, about "
          f"10% of the frame wide. It is only as deep as a man is tall: its bottom is about a third of the way down the cut "
          f"face, not deeper. Its side toward the fence is steep; its side toward the T-rex slopes gently down. Where it "
          f"reaches the front of the lawn it shows in the cut face as a V-shaped notch in the top soil layers; the rest of the "
          f"cut face, with both concrete footings, does not change. The cable fence stays standing on the far side of the "
          f"ditch. The rest of the lawn stays whole. {GREEN} {KEEP} {ONLYREX}"),
 "S2_2": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: a black drain pipe now lies along the bottom of the ditch, and in "
          f"the cut face it shows as a black circle at the bottom of the ditch's profile. {GREEN} {KEEP} {ONLYREX}"),
 "S2_3": (f"{STYLE} {LOCKG} {REXSTAY} The ditch with its drain pipe stays exactly as it is, and the cut face of the "
          f"ground at the front stays exactly as it is: dark soil layers with the two concrete footings. Change only this: "
          f"inside the ditch, its far side, the side next to the right-hand cable fence, is now faced with a smooth vertical "
          f"grey concrete wall from the bottom of the ditch up to the edge of the lawn, along the whole length of the ditch. "
          f"The near side of the ditch, toward the T-rex, is still bare soil. {GREEN} {KEEP} {ONLYREX}"),
 "S2_4": (f"{STYLE} {LOCKG} {REXSTAY} The ditch stays open and exactly as deep as it is, with its concrete wall "
          f"on the T-rex's side and its drain at the bottom; do not fill it in, and the cut face does not change. Change only "
          f"this: the bare brown soil on the ditch's other side, the slope that rises from the bottom of the ditch to the "
          f"right-hand cable fence, is now covered in a layer of fresh green turf, so that slope is green instead of brown. "
          f"{KEEP} {ONLYREX}"),
 # ---- loop 3: the wallow ----
 "F3": (f"{STYLE} {LOCKG} Change only this: the T-rex has spun round to face the camera: his long tail has swept "
        f"round behind him across the back left of the lawn and smashed the garden shed there flat into a heap of broken "
        f"planks and grey shingles. He now stands facing straight toward the camera in the middle of the lawn, his feet about "
        f"where they were, his head lowered over the front of the lawn and his small arms in front of his chest; his tail "
        f"points away toward the back of the lawn. {TREXW}. The cable fence, the ditch and the picket ring stay as they are. "
        f"{NONEW} {GREEN} {KEEP} {ONLYREX}"),
 "S3_1": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: one wide, shallow, round hollow now dips into the lawn at the "
          f"very front of the lawn, between the left front corner and the end of the ditch, in front of the white picket "
          f"ring; its front edge is the front edge of the lawn, so its bowl shows in the cut face as a curved dip in the soil "
          f"layers. Everything else stays exactly as it is: the white picket ring, every pole and cable of the fence, both "
          f"concrete footings in the cut face, and the rest of the lawn, which stays whole. There is only this one hollow. "
          f"{GREEN} {KEEP} {ONLYREX}"),
 "S3_2": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: the inside of the hollow is now lined with smooth grey clay; the "
          f"cut face does not change. {GREEN} {KEEP} {ONLYREX}"),
 "S3_3": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: big rounded grey boulders now sit round the rim of the hollow. "
          f"{GREEN} {KEEP} {ONLYREX}"),
 "S3_4": (f"{STYLE} {LOCKG} Change only this: the hollow is full of translucent cyan water to the rim, with the boulders "
          f"round it; the T-rex has lowered his head and dipped his snout into the water, splashing. "
          f"{TREXW}. {GREEN} {KEEP} {ONLYREX}"),
 # ---- loop 4: the night house ----
 "F4": (f"{STYLE} {LOCKG} Change only this: the T-rex has lifted his head out of the water and stands upright again, "
        f"facing the camera, and in his jaws he holds a small grey robot lawn mower, crunched; water drips from his chin. "
        f"{TREXW}. The water, the boulders and everything else stay as they are. {GREEN} {KEEP} {ONLYREX}"),
 "S4_1": (f"{STYLE} {LOCKG} {REXSTAY} Change only this: a flat rectangle of smooth grey concrete now lies on the lawn round "
          f"the T-rex's feet, from behind his tail to just behind the water, wide enough for his whole body; the water, the "
          f"boulders and the heap of planks stay as they are. {GREEN} {KEEP} {ONLYREX}"),
 "S4_2": (f"{STYLE} {LOCKG} The T-rex stays exactly where he is, the same size and in exactly the same pose: his head, "
          f"with the mower in his jaws, stays exactly where it is in the frame. Change only this: grey corrugated steel walls "
          f"now rise on the edges of the concrete close round him, a little taller than his back: a back wall, a left wall, a "
          f"right wall and a front wall, the one facing the camera, with a wide open doorway right in front of him so his "
          f"head, the mower and his chest show through it; there is no roof yet. The building is only just big enough to hold "
          f"him. The water and the boulders stay outside, in front. {GREEN} {KEEP} {ONLYREX}"),
 "S4_3": (f"{STYLE} {LOCKG} {REXSTAY} The walls stay exactly as they are. Change only this: a grey corrugated steel roof "
          f"now sits on top of the walls, covering the building and the T-rex's back; he still stands in the wide front "
          f"doorway with his head and the mower in his jaws showing outside it. {GREEN} {KEEP} {ONLYREX}"),
 "S4_4": (f"{STYLE} {LOCKG} The steel building stays exactly the same size and shape, in exactly the same place: its left wall, "
          f"its right wall, its roof edges and its front wall do not move. Change only this: the T-rex is now inside "
          f"the building, out of sight; the roof is whole over him, and a big grey corrugated steel sliding door has closed "
          f"the front doorway. And a small grey robot lawn mower now sits on the lawn at the left of the water, with a freshly "
          f"mown stripe behind it. {GREEN} {KEEP} {NOANIMAL}"),
 # ---- loop 5: the laminated glass ----
 "S5_1": (f"{STYLE} {LOCKG} The steel building stays exactly the same size and shape, with its sliding door shut. "
          f"Change only this: a wide rectangular hole is now cut in the building's front wall beside the door, at the "
          f"height of the T-rex's head, and his face shows inside it, facing the camera and looking out; the cut-out steel "
          f"panel lies flat on the grass below the hole. {TREXW}. {GREEN} {KEEP} {ONLYREX}"),
 "S5_2": (f"{STYLE} {LOCKG} {REXSTAY} The water, its boulders and the cut face of the ground stay exactly as they are. "
          f"Change only this: a thick steel frame is now bolted round the edges of the opening in the steel building's front "
          f"wall, the opening where the T-rex's face shows. {GREEN} {KEEP} {ONLYREX}"),
 "S5_3": (f"{STYLE} {LOCKG} {REXSTAY} The water, its boulders and the cut face of the ground stay exactly as they are. "
          f"Change only this: a thick slab of clear glass, as thick as a brick, now fills the steel frame in the building's "
          f"front wall; the T-rex's face shows through it. {GREEN} {KEEP} {ONLYREX}"),
 "S5_4": (f"{STYLE} {LOCKG} {REXSTAY} The building, its glass window, the water and the cut face stay exactly as they "
          f"are. Change only this: a round red dog bed now sits on the grass right in front of the glass window, and in it "
          f"sits {DOGW}, his nose up against the glass, nose to nose with the T-rex behind it. {GREEN} {KEEP} {REXDOG}"),
 # ---- the close: a closer view ----
 "CLOSE_a": (f"{STYLE} The same steel building, glass window, T-rex, dog and dog bed as the first reference image, with the "
             f"same parts, colours, materials and light. New camera position: low and close, in front of the window, so the "
             f"window and the dog bed fill most of the frame: the T-rex's face behind the thick glass in the upper half and "
             f"{DOGW}, in the bed, his nose to the glass, nose to nose with the T-rex. This is a close view on the lawn: the "
             f"grass is whole and nothing is cut open. {TREXW}. {REXDOG}"),
 "CLOSE_b": (f"{STYLE} Same scene as the first reference image. Keep exactly the same camera position, zoom and framing. "
             f"Change only this: the dog has curled up asleep in his bed against the glass, and the T-rex has lowered his head "
             f"to rest against the other side of the glass, eyes closed, asleep. {TREXW}. {KEEP} {REXDOG}"),
}
DOG = "DOG"  # video 16's dog key, job 51460339-c4b8-4537-9078-bd28de9305f8 (listed in 17-jobs.tsv)
REFS = {
 "K0": [], "KV": ["K0"], "KT": [],
 "S0a": ["BASE", "KT"], "S0": ["S0a", "KT", DOG], "H": ["S0", "KT", DOG],
 "F1": ["H", "KT"], "S1_1": ["F1", "KT"], "S1_2": ["S1_1", "KT"], "S1_3": ["S1_2", "KT"], "S1_4": ["S1_3", "KT"],
 "F2a": ["S1_4", "KT"], "F2": ["S1_4", "KT"], "S2_1": ["F2", "KT"], "S2_2": ["S2_1", "KT"], "S2_3": ["S2_2", "KT"],
 "S2_4": ["S2_3", "KT"],
 "F3": ["S2_4", "KT"], "S3_1": ["F3", "KT"], "S3_2": ["S3_1", "KT"], "S3_3": ["S3_2", "KT"], "S3_4": ["S3_3", "KT"],
 "F4": ["S3_4", "KT"], "S4_1": ["F4", "KT"], "S4_2": ["S4_1", "KT"], "S4_3": ["S4_2", "KT"], "S4_4": ["S4_3"],
 "S5_1": ["S4_4", "KT"], "S5_2": ["S5_1", "KT"], "S5_3": ["S5_2", "KT"], "S5_4": ["S5_3", "KT", DOG],
 "CLOSE_a": ["S5_4", "KT", DOG], "CLOSE_b": ["CLOSE_a", "KT", DOG],
}
ASPECT = {"KT": "16:9"}

# ---- clips (wan2_7, 720p, 9:16): from the stage before to the stage after (CLAUDE.md 6.3) ----
CLOCK = "The camera is locked and never moves."
SELF = "Nobody is there: the parts move by themselves."
STAYC = ("The house, the porch, the fences, the lawn and the cut face of the ground stay exactly as they are: no hole, pit or "
"trench opens anywhere, and no soil appears on the lawn.")
REXC = ("The T-rex is the same animal from start to end: a Tyrannosaurus rex with scaly moss-green and grey skin and a pale "
"cream belly; he keeps his shape and size.")
def tail(animals):
    who = {"rex": "The only animal is the T-rex.", "rexdog": "The only animals are the T-rex and the dog.",
           "none": "No animals."}[animals]
    return f"Real speed. Motion starts on frame 1. No people, no characters. {who} No text, no captions, no letters."
C = {
 # key: (start, end, seconds, motion, stay, animals, sound)
 "HOOK": ("S0", "H", 4, "White wooden pickets shoot up out of the grass one after another in a curve round the T-rex's feet, "
          "from the left round to the right, and close into a ring within the first second. The T-rex stands still and blinks. "
          "On the porch the small dog barks twice, then sits down.", STAYC, "rexdog",
          "Sound: quick hollow wooden taps one after another as the pickets pop up, a small dog barking twice, a deep slow "
          "breath, quiet birdsong."),
 "FC1": ("H", "F1", 3, "The T-rex lifts one foot, steps forward over the white picket ring and puts his foot down on the "
         "right side of it; the pickets under his foot snap and fall flat. At the same moment the small dog on the porch jumps up "
         "and darts in through the open back door.", STAYC, "rexdog",
         "Sound: a huge heavy footstep thud, wooden pickets cracking and snapping, a small dog's yelp and paws on wood, quiet "
         "birdsong."),
 "W1_1": ("F1", "S1_1", 2, "Round holes drill themselves into the lawn one after another along the back, the left and the "
          "right edges, each throwing up a little ring of soil, and two deep shafts open straight down in the cut face of the "
          "ground at the front; the house's back door swings shut. The T-rex stands still.",
          "Apart from these holes the lawn and the cut face stay exactly as they are.", "rex",
          "Sound: a quick run of deep drilling thuds and soil spraying, a door clicking shut, quiet birdsong."),
 "W1_2": ("S1_1", "S1_2", 2, "Tall grey steel poles drop straight down out of the sky into the holes one after another, each "
          "landing with a thump and a small puff of dust; the two at the front slide down into their shafts in the cut face. The "
          "T-rex stands still.", STAYC, "rex",
          "Sound: heavy steel poles clanging down one after another, a low metallic ring, quiet birdsong."),
 "W1_3": ("S1_2", "S1_3", 2, "Wet grey concrete pours into every hole round the foot of each pole and settles smooth, and in the "
          "cut face the two shafts fill up with grey concrete round their poles. The T-rex stands still.", STAYC, "rex",
          "Sound: wet concrete pouring and slapping, a low glug, quiet birdsong."),
 "W1_4": ("S1_3", "S1_4", 3, "Six thick steel cables zip out from pole to pole one after another, from the bottom up, along the "
          "back, the left and the right, and pull taut; along the right side the old wooden fence gives way to more steel poles "
          "and cables. The T-rex stands still.", STAYC, "rex",
          "Sound: steel cables zipping taut and twanging one after another, quiet birdsong."),
 "FC2a": ("S1_4", "F2a", 2, "The T-rex leans out over the cables on the right, stretches his neck down and dips his snout into "
          "the neighbor's pool, gulping; the water ripples.", STAYC, "rex",
          "Sound: steel cables creaking under weight, deep slurping gulps, water lapping."),
 "FC2b": ("F2a", "F2", 2, "The water in the neighbor's pool drains away fast as the T-rex slurps it up, until the pool is empty "
          "and its level has dropped in the cut face too; then he lifts his head back up over the lawn, water dripping from his "
          "chin.", STAYC, "rex",
          "Sound: loud slurping and gurgling, a big satisfied snort, water dripping."),
 "W2_1": ("F2", "S2_1", 3, "The turf along the inside of the right-hand cable fence sinks away into a wide ditch from the back of "
          "the lawn to the front, and at the front its profile opens in the cut face as a deep notch. The T-rex stands still.",
          "Apart from this ditch the lawn stays whole and the rest of the cut face does not change.", "rex",
          "Sound: a deep rumble, soil sliding and settling, quiet birdsong."),
 "W2_2": ("S2_1", "S2_2", 2, "A black drain pipe drops into the bottom of the ditch and settles, its round end showing in the "
          "cut face. The T-rex stands still.", "The lawn, the ditch and the rest of the cut face stay as they are.", "rex",
          "Sound: a hollow plastic pipe thunking down into soil, quiet birdsong."),
 "W2_3": ("S2_2", "S2_3", 2, "A smooth grey concrete wall rises up out of the ditch along its side nearest the T-rex, the whole "
          "length of the ditch. The T-rex stands still.", "The lawn and the rest of the cut face stay as they are.", "rex",
          "Sound: concrete grinding upward, a heavy thud, quiet birdsong."),
 "W2_4": ("S2_3", "S2_4", 2, "Fresh green turf unrolls down the ditch's far slope, from the back of the lawn to the front. The "
          "T-rex stands still.", "The ditch stays open; the lawn and the cut face stay as they are.", "rex",
          "Sound: turf unrolling with a soft swish and a pat, quiet birdsong."),
 "FC3": ("S2_4", "F3", 3, "The T-rex swings round to face the camera, and as he turns his long tail sweeps across the back left "
         "of the lawn and smashes the garden shed into a burst of planks and dust.", STAYC, "rex",
         "Sound: a heavy whoosh, a wooden shed collapsing in a crash of planks, a big snort."),
 "W3_1": ("F3", "S3_1", 2, "The turf at the front of the lawn, right in front of the T-rex, slumps down into a wide round hollow. "
          "The T-rex stands still.", "Apart from this hollow the lawn stays whole.", "rex",
          "Sound: an earthy rumble, a soft thud, quiet birdsong."),
 "W3_2": ("S3_1", "S3_2", 2, "Smooth grey clay spreads across the inside of the hollow and lines it. The T-rex stands still.",
          STAYC, "rex", "Sound: a wet, squelchy smear, quiet birdsong."),
 "W3_3": ("S3_2", "S3_3", 2, "Big grey boulders roll in round the rim of the hollow one after another and settle. The T-rex "
          "stands still.", STAYC, "rex", "Sound: boulders rolling and knocking into place, quiet birdsong."),
 "W3_4": ("S3_3", "S3_4", 3, "Translucent cyan water floods into the hollow and fills it to the rim; the T-rex lowers his head "
          "and dips his snout into the water, splashing.", STAYC, "rex",
          "Sound: water gushing in, a splash, a happy deep snort."),
 "FC4": ("S3_4", "F4", 4, "A small grey robot lawn mower rolls in from the left edge of the frame across the grass toward the "
         "water, humming; the T-rex lifts his head out of the water, swings it down and snaps the mower up in his jaws.",
         STAYC, "rex", "Sound: the soft electric whirr of a small mower, a crunch of plastic and metal, a big gulp."),
 "W4_1": ("F4", "S4_1", 2, "Grey concrete spreads out flat round the T-rex's feet, from behind his tail to just behind the "
          "water, and sets smooth. The T-rex stands still with the mower in his jaws.", STAYC, "rex",
          "Sound: wet concrete spreading and slapping, quiet birdsong."),
 "W4_2": ("S4_1", "S4_2", 3, "Grey corrugated steel walls shoot up out of the edges of the concrete one after another round the "
          "T-rex: the back, the left, the right, then the front with its wide doorway. The T-rex stands still.", STAYC, "rex",
          "Sound: steel panels clanging up one after another."),
 "W4_3": ("S4_2", "S4_3", 2, "A grey corrugated steel roof drops down onto the walls and settles over the T-rex's back; his head "
          "stays out over the front doorway.", STAYC, "rex", "Sound: a booming metal clang, a short rattle."),
 "W4_4": ("S4_3", "S4_4", 3, "The T-rex ducks his head back inside the building, a big steel door slides across the doorway and "
          "clunks shut, and a small robot mower rolls out on the left and mows a stripe in the grass.", STAYC, "rex",
          "Sound: a steel door rumbling along its track and clunking shut, then a small mower's soft whirr."),
 "FC5": ("S4_4", "S4_4", 3, "The steel building shudders as a huge animal roars inside it: its walls rattle, dust shakes off "
         "the roof edges, and the windows of the house rattle in their frames. Nothing else moves.", STAYC, "none",
         "Sound: a deep animal roar muffled by steel walls, metal rattling, window glass buzzing."),
 "W5_1": ("S4_4", "S5_1", 2, "The steel door panel falls forward out of the building's front wall and lands flat on the grass, "
          "and the T-rex's face appears in the opening, looking out.", STAYC, "rex",
          "Sound: a metal screech, a steel panel clanging down flat."),
 "W5_2": ("S5_1", "S5_2", 2, "A thick steel frame swings into the opening and bolts tight round its edges. The T-rex stays "
          "still.", STAYC, "rex", "Sound: a steel frame clanking in, bolts ratcheting tight."),
 "W5_3": ("S5_2", "S5_3", 2, "A thick slab of clear glass lowers down into the frame and settles; the T-rex's face shows through "
          "it.", STAYC, "rex", "Sound: glass sliding into a frame, a deep soft thunk."),
 "W5_4": ("S5_3", "S5_4", 3, "A round red dog bed slides across the grass up to the glass, and the small dog trots in from the "
          "left, hops into the bed and puts his nose to the glass, nose to nose with the T-rex.", STAYC, "rexdog",
          "Sound: a soft bed sliding on grass, a small dog's paws, a happy little huff."),
 "CLOSE": ("CLOSE_a", "CLOSE_b", 4, "The dog and the T-rex touch noses through the glass; then the dog yawns, turns round in his "
           "bed and curls up asleep, and the T-rex slowly lowers his head against the glass and closes his eyes.",
           "The glass, the steel wall and the grass stay as they are.", "rexdog",
           "Sound: a soft breath on glass, a small dog's sleepy sigh, quiet birdsong."),
}
def clip_prompt(k):
    a, b, secs, motion, stay, animals, sound = C[k]
    rex = REXC + " " if animals != "none" else ""
    return f"{motion} {SELF} {CLOCK} {stay} {rex}{tail(animals)} {sound}"

def jobs():
    J = {}
    try:
        for l in open(__file__.replace("17-prompts.py", "17-jobs.tsv")):
            if l.startswith("# Higgsfield folder "): J["FOLDER"] = l.split()[3]
            if l.strip() and not l.startswith("#") and not l.startswith("key"):
                k, j = l.split("\t")[:2]; J[k.split(".")[0]] = j.strip()
    except FileNotFoundError:
        pass
    J.setdefault("BASE", J.get("KV", J.get("K0")))   # the stage view: KV if one was made, else the set key itself
    return J

if __name__ == "__main__":
    kind, keys = sys.argv[1], sys.argv[2:]; J = jobs(); out = []
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
                   "prompt": clip_prompt(k)}
        if "FOLDER" in J: prm["folder_id"] = J["FOLDER"]
        out.append({"index": i, "params": prm})
    print(json.dumps(out, ensure_ascii=False))
