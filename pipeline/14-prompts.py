# Video 14 (V3, "Why It Rains Inside a Nuclear Cooling Tower"): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 14-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE is the Cutaway default WITH "translucent cyan water" (6.3): the pond, the rain, the riser and the buried pipe are water.
# WIDE and LOCKZ are byte-identical to 13-prompts.py. SET carries the place and its colours; TOWER lists the cut-open inside once,
# for W0 and ST1 (the close front view repeats it so the inside is drawn the same). Every other still is an edit of the one(s)
# named in REFS: LOCK or LOCKZ keeps the framing for a change at one position; POS moves the camera to a new position on the same
# set. TOWERZ (views inside the tower) and SKYZ (views in the air outside) stop the STYLE line's cut ground from leaking into
# close-ups (7.1). The tower's own cut-away near half is intended: it is how the rain and the empty shell show.
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent "
"cyan water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a nuclear power plant's cooling tower beside a calm river on a bright, clear autumn day, shown as a cutaway model: a very "
"tall hyperbolic cooling tower of smooth pale grey concrete with faint horizontal pour lines, wide at the bottom, narrowing to a "
"waist about two-thirds of the way up and flaring out a little to a round open mouth at the top, stands on a ring of slanted "
"concrete legs with daylight between them, over a round concrete pond; a calm blue-green river with grassy banks runs along the "
"right; a plain, boxy, windowless grey building with a flat roof stands at the left behind the tower, with no markings, no dome "
"and no chimney; behind the tower, in a row along the river, three more cooling towers of the same shape, whole and smaller with "
"distance, each with a soft white cloud of water vapour rising from its mouth. There are no radiation symbols, signs or "
"markings anywhere. Everything stands on a deep block of ground cut straight down like a slice of cake toward the camera, so the "
"cut face shows even layers of brown earth")
CAMERA = ("Camera: from the front, slightly raised, looking at the cut-open tower, which fills about 80% of the frame width and "
"stands in the upper 60% of the frame: its round mouth just below the top edge, its legs and pond about 58% down. Below that the "
"block of ground is cut straight down all the way to the bottom edge of the frame: deep, even layers of brown earth, and buried "
"in them, about 68% down, one huge round pipe that comes in from the left under the grey building and runs under the tower, "
"cut open lengthwise like the tower so the cyan water rushing through it shows. There is no ground in front of the block")
TOWER = ("The near half of the tower is cut away from its mouth down to the ground, straight through its middle like a slice of "
"cake, so its inside shows as a clear diagram, and the cut edge of the concrete shell shows as a thin wall. Inside, from the "
"bottom up: the round pond of translucent cyan water, with rain pouring down into it all over; a wide flat layer of stacked thin "
"white plastic sheets spanning the whole tower a little above the tops of the legs, with water raining off its underside; just "
"above it a grid of grey pipes with nozzles spraying water down onto it; just above the sprays a thin layer of grey zigzag "
"baffles; in the middle, one big round pipe rising straight up out of the pond to the spray grid, joined below to the buried "
"pipe and cut open lengthwise so the cyan water surging up inside it shows. Above the baffles the tower is completely empty: "
"nothing but the smooth curved inner face of the concrete shell rising to the bright round mouth, with faint white mist "
"drifting up it, and a thick white cloud rolling out of the mouth into the blue sky")
TOWERZ = ("This is a view inside the tower: only the tower's near half is cut away; the pond's concrete floor and the ground "
"under the tower are whole, and there is no soil, no pit and no cut face of ground anywhere in the frame.")
SKYZ = ("This is a view in the air: there is no soil, no pit and no cut face of ground anywhere in the frame.")
EMPTY = ("Above the baffles there is nothing inside the tower: no floors, no stairs, no ladders, no pipes, no beams, no machines.")
POS = "The same cooling tower, river, set and light as the reference image, with the same parts, colours and materials."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"tower, its legs, the pond, the river and the cloud stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
DUCK = ("one mallard duck with a glossy green head, a white collar and a grey-brown body")

P = {
 # ---- WIDE (the set key, in the cut-open state S1) ----
 "W0": f"{STYLE} {WIDE} Scene: {SET}. {CAMERA}. {TOWER}. {EMPTY} {NOBODY}",
 # ---- FRONT (ST1 the cut-open tower; ST0 the whole tower: the first and last frame) ----
 "ST1": f"{STYLE} {POS} New camera position: low in front of the tower and much closer, looking slightly up at its cut-open "
        f"front, which fills the frame: its slanted legs and the pond at the bottom of the frame, its round mouth and the thick "
        f"white cloud rolling out of it at the top; the base of the tower is wider than the frame, so the frame's left and right "
        f"edges cut through the legs. {TOWER}. {EMPTY} Only a thin strip of grass shows at the very bottom of the frame. {NOBODY}",
 "ST0": f"{STYLE} {LOCK} Change only this: the tower is whole and closed: its near half is NOT cut away, so none of its inside "
        f"shows: the front of the tower is one smooth curved wall of pale grey concrete with faint horizontal pour lines, from the "
        f"slanted legs at the bottom up to the round mouth at the top; between the legs at the bottom, a glimpse of the pond "
        f"glinting in the shade; the thick white cloud rolls out of the mouth into the blue sky exactly as before. {KEEP} "
        f"{NOBODY}",
 # ---- SHELL ----
 "SH0": f"{STYLE} {POS} New camera position: inside the tower near the cut edge, just above the grey zigzag baffles, looking "
        f"up along the inside of the far half of the shell: the smooth curved inner face of pale grey concrete rises up the "
        f"frame, narrowing toward the waist and flaring out again to the bright round mouth near the top of the frame, where blue "
        f"sky and the white cloud show; faint white mist drifts up the middle; the thin cut edge of the shell runs up the left "
        f"side of the frame with open sky beyond it. {EMPTY} {TOWERZ} {NOBODY}",
 # ---- BASE ----
 "BA0": f"{STYLE} {POS} New camera position: inside the tower at the bottom, low, just above the surface of the pond near the "
        f"cut edge, looking across the pond toward the middle: the big round pipe rises up the middle of the frame, cut open "
        f"lengthwise so the cyan water surging up inside it shows; rain pours down all round it into the pond from the underside "
        f"of the layer of stacked white plastic sheets, which runs across the top of the frame; at the back, between the slanted "
        f"concrete legs, daylight and green grass; {DUCK} floats small on the pond at the right. {TOWERZ} No people; the only "
        f"animal is the duck.",
 # ---- FILL ----
 "FI0": f"{STYLE} {POS} New camera position: inside the tower, close at the grid of spray pipes, level with them, looking "
        f"across. Extreme close-up: the grey pipes with their nozzles fill the middle of the frame, each nozzle spraying a cone of "
        f"water down onto the stacked thin white plastic sheets of the fill, which fill the lower third of the frame, with thin "
        f"films of water running down between them; across the top third, the thin layer of grey zigzag baffles, with faint white "
        f"mist above them. {TOWERZ} {NOBODY}",
 # ---- EDGE ----
 "ED0": f"{STYLE} {POS} New camera position: outside, high in the air, close to the cut edge of the concrete shell at the "
        f"tower's narrow waist, looking at the cut edge end-on. Close-up: the cut face of the shell's wall runs from the top to the "
        f"bottom of the frame as a thin band of pale grey concrete with rows of steel reinforcing bars showing in it, curving in "
        f"toward the waist in the middle of the frame and out again above and below; on the left of it the empty inside of the "
        f"tower with faint mist, on the right the blue sky and, far below, the river. {SKYZ} {NOBODY}",
 # ---- ROW (calm; and the 1965 storm) ----
 "RO0": f"{STYLE} {POS} New camera position: high above the river beside the tower, looking along the row of three whole "
        f"cooling towers that stand along the river behind it, each with a soft white cloud rising from its mouth, the nearest "
        f"one large in the middle of the frame and the other two behind it; the rim of the cut-open tower's mouth shows at the "
        f"near left edge of the frame; the plain grey building small far below; blue sky with a few clouds. {SKYZ} {NOBODY}",
 "RO1": f"{STYLE} {LOCKZ} Change only this: a violent storm: the whole sky is dark grey-black with low, heavy, torn storm "
        f"clouds; heavy rain drives sideways in a gale; the river below is whipped into white-capped waves; the clouds from the "
        f"towers' mouths are torn sideways by the wind; the light is dim and grey. The three towers still stand, whole. No "
        f"lightning, no fire, no smoke. {KEEP} {NOBODY}",
 # ---- TOP ----
 "TO0": f"{STYLE} {POS} New camera position: in the air just above the rim of the cut-open tower's round mouth, looking across "
        f"and down past the rim: the thick white cloud billowing up out of the mouth fills the upper half of the frame, rising "
        f"past the camera; the curved concrete rim runs across the lower middle of the frame; through gaps in the cloud, far "
        f"below, the river, the plain grey building and the row of three towers. {SKYZ} {NOBODY}",
 # ---- DUCK ----
 "DU0": f"{STYLE} {POS} New camera position: right down at the surface of the pond inside the tower, close to the duck. Extreme "
        f"close-up: {DUCK} floats calmly on the translucent cyan water and fills about a third of the frame, rain splashing all "
        f"round it in rings and droplets; behind it, softly blurred, the big round pipe with water surging up inside it and the "
        f"slanted legs with daylight between them. {TOWERZ} No people; the only animal is the duck.",
}

REFS = {"W0": [], "ST1": ["W0"], "ST0": ["ST1"], "SH0": ["ST1"], "BA0": ["ST1"], "FI0": ["ST1"], "ED0": ["ST1"],
        "RO0": ["W0"], "RO1": ["RO0"], "TO0": ["W0"], "DU0": ["BA0"]}

# W0 try A (f8db8273) drew everything right except the order of two layers: the zigzag baffles sat on top of the white sheets
# with the spray pipes above them. W0.B is a LOCK edit of try A that swaps only those two layers (the baffles go above the
# sprays, as the script says).
P["W0.B"] = (f"{STYLE} {LOCK} Change only this: swap the two layers just above the stacked white plastic sheets inside the "
             f"tower: the grid of grey pipes with its nozzles now sits directly on top of the white sheets, spraying water straight "
             f"down onto them, and the thin layer of grey zigzag baffles now spans the whole tower just above the pipes, so the "
             f"zigzag baffles are the highest thing inside the tower and above them it is empty. {KEEP} {NOBODY}")
REFS["W0.B"] = ["W0"]
# W0.B (3510ccfa) got the order right (sheets, sprays, then the baffles on top) but lost most of the rain under the sheets:
# W0.C is a LOCK edit of W0.B that brings back the downpour, the picture the title is about.
P["W0.C"] = (f"{STYLE} {LOCK} Change only this: heavy rain now pours down from the whole underside of the stacked white "
             f"plastic sheets into the pond: dense white curtains of falling water drops fill the open space between the sheets "
             f"and the pond, all the way round the big pipe, and splash on the pond's cyan surface. {KEEP} {NOBODY}")
REFS["W0.C"] = ["W0.B"]
# TO0 try A (f31d4855) drew the mouth as a full ring, but the tower is cut in half from its mouth to the ground: TO0.B is a
# LOCKZ edit of try A that removes the near half of the rim.
P["TO0.B"] = (f"{STYLE} {LOCKZ} Change only this: the tower is cut open: the near half of the round concrete rim and of the "
              f"shell below it is gone, so only the far half of the rim remains, a half ring curving round the back of the mouth, "
              f"and the shell's two cut edges drop straight down from its ends; through the open near side you look down into the "
              f"empty inside of the tower, full of drifting white mist. The white cloud still billows up out of the mouth and past "
              f"the camera. {KEEP} {NOBODY}")
REFS["TO0.B"] = ["TO0.A"]
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
