# Video 09 (C3, "What Lightning Does Inside Your House", the first video with the travelling camera): still prompts for
# seedream_v5_pro 1k 9:16. Usage: python3 09-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE is the Cutaway default of 3.3 Step 4 (no objects, no place); WIDE goes only into the wide stills; SET carries the place and
# its colours; HOUSE lists the objects once, for W0 only. STORM re-grades the daylight wide (3.4 Rule 4), like NIGHT in 08-prompts.py.
# Every other still is an edit of the one named in REFS: LOCK keeps the framing for a change at one position; POS moves the camera
# to a new position on the same set (3.3 Step 5).
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent cyan "
"water, tidy and uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a small two-storey suburban house with cream walls and a terracotta tile roof, shown as a cutaway model: its whole front wall "
"is removed like a dollhouse, so both floors and the attic under the roof show inside. The house stands on a square block of ground "
"with a narrow strip of green lawn in front of it and a strip of grey street along the front edge. The front of the block is cut "
"straight down like a slice of cake, so the cut face shows clean layers of brown and tan soil")
CAMERA = ("Camera: straight-on from the front, slightly raised, centred on the house, which fills about 80% of the frame width. "
"The roof peak sits about 10% down from the top of the frame, with a little sky above it, and the lawn about 50% down. The block of "
"ground is deep: below the lawn its front is cut straight down all the way to the bottom edge of the frame, so the whole lower half "
"of the frame is the cut face of the ground, deep, even layers of brown and tan soil with nothing in them except the copper water "
"pipe just under the lawn. There is no ground in front of the block")
HOUSE = ("Inside, drawn like a clear diagram. The attic under the roof has bare wooden rafters, with one white electrical cable running "
"along a rafter and down into the walls. Upstairs on the right is a bathroom with white tiles: a white bathtub with a chrome shower "
"head on the wall above it, the shower running into the tub, a small yellow rubber duck floating in the bath water, and one copper "
"water pipe running up inside the cut right-hand wall from the floor to the shower head. Upstairs on the left is a small bedroom "
"with a bed. Downstairs is a living room with a grey sofa, a floor lamp and two white wall outlets, and a grey metal electrical "
"panel with its door open hanging on its left-hand wall. Outside, at the left front corner of the block, stands one wooden power "
"pole with a crossarm and a small grey transformer can at its top, and a single black cable runs from the top of the pole to the "
"upper left corner of the house. Under the lawn, one copper water pipe runs through the soil from the front edge of the block to "
"the right foundation corner of the house, where it rises into the right-hand wall. There is no rod on the roof and no cable on "
"the outside walls")
STORM = ("IT IS A THUNDERSTORM, with no sunshine at all (the daylight described above does not apply to this picture): the same "
"picture under a dark blue-grey storm sky full of heavy clouds, with fine grey streaks of rain falling; the outdoor light is cool, "
"dim and even, and warm yellow lamps are lit inside the house, so the rooms stay bright and clear. The water keeps exactly the "
"same translucent cyan colour")
STILLSTORM = ("It is still the thunderstorm, lit exactly like the reference image: dark blue-grey storm light outside, rain, warm "
"lamps on inside.")
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the house, "
"its rooms, the roof, the pole, the lawn and the cut face of the ground stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
POS = "The same house, set and storm as the reference image, with the same parts, colours and materials."
NOCHANGE = "Nothing in the house changes."
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
BOLT = "a jagged white-blue lightning bolt comes down from the dark clouds"
GLOW = "glows bright white-blue, as if electric current is racing through it"
ROD = "a short pointed metal rod, about as tall as a person's arm"
CABLE = "a thick braided copper cable"
GROD = "a long copper rod driven straight down into the soil"

P = {
 # ---- WIDE ----
 # W0A (1ff3d8ef): good house, but the block was a thin slab on a dirt plain, too shallow for the ground rod; W0 asks for a deep cut face.
 "W0": f"{STYLE} {WIDE} Scene: {SET}. {CAMERA}. {HOUSE}. {NOBODY}",
 "W": f"{STYLE} {WIDE} {LOCK} Change only this: {STORM}. {KEEP} {NOBODY}",
 # W1A (782bea5b): the cable and the ground rod were joined to the water pipe (bonding before its beat), and the rod sat on the
 # right slope. W1 places the rod at the gable peak and keeps the ground rod apart from the pipe.
 "W1": f"{STYLE} {WIDE} {LOCK} Change only this: {ROD} now stands upright on the peak of the roof, at the front end of the ridge; "
       f"{CABLE} runs from its foot down along the right-hand edge of the roof to the eave, then straight down the right-hand outside "
       f"corner of the house to the lawn and into the soil just beside the corner, where it is clamped to the top of {GROD}, "
       f"reaching down through the soil layers about as deep as one storey of the house is tall. The copper rod stands a little to "
       f"the right of the copper water pipe and does not touch it; the water pipe stays exactly as it is in the reference, running "
       f"under the lawn and up into the house. The shower in the bathroom is turned off. {STILLSTORM} {KEEP} {NOBODY}",
 # W1BA (7291d60c): the water pipe under the lawn glowed too.
 "W1B": f"{STYLE} {WIDE} {LOCK} Change only this: {BOLT} and strikes the tip of the metal rod on the peak of the roof, and the "
        f"braided copper cable down the corner of the house and the copper rod in the soil glow bright white-blue all the way down. "
        f"Nothing else glows: the copper water pipe under the lawn, every pipe and wire inside the house and the rooms stay exactly "
        f"as in the reference, dark and unlit by the bolt. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- RIDGE ----
 "R0": f"{STYLE} {POS} New camera position: high and close above the right end of the roof ridge, looking along the ridge from "
       f"above and slightly to the right; the ridge and the terracotta roof tiles fill the upper half of the frame, and below the "
       f"cut front edge of the roof the attic's wooden rafters and its white electrical cable show. {STILLSTORM} {NOCHANGE} {NOBODY}",
 "R0B": f"{STYLE} {LOCK} Change only this: {BOLT} and strikes the peak of the roof at the front end of the ridge, with a bright white flash "
        f"where it hits the tiles. {STILLSTORM} {KEEP} {NOBODY}",
 "R1": f"{STYLE} {LOCK} Change only this: {ROD} now stands upright on the peak of the roof at the front end of the ridge, and "
       f"{CABLE} runs from its foot down along the right-hand edge of the roof and out of view. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- ATTIC ----
 # AA (3a0ab9ea): a three-quarter view of the whole house from the left, not the attic. A is an edit of the front wide.
 "A": f"{STYLE} {POS} New camera position: inside the cut-open attic, seen from the front. Extreme close-up: the wooden rafters "
      f"under the roof peak and the white electrical cable running along a rafter fill most of the frame; the cable {GLOW}, with a "
      f"few small sparks along it. {STILLSTORM} {NOBODY}",
 # ---- BATH ----
 "B": f"{STYLE} {POS} New camera position: level with the upstairs bathroom, close, looking straight in from the front: the white "
      f"bathtub with the chrome shower head above it, the shower running into the tub, the small yellow rubber duck floating in the "
      f"bath water, and the copper water pipe rising inside the cut right-hand wall to the shower head fill the frame. {STILLSTORM} "
      f"{NOCHANGE} {NOBODY}",
 "Bg": f"{STYLE} {LOCK} Change only this: the copper water pipe in the right-hand wall {GLOW}, all the way up to the shower head. "
       f"The shower keeps running. {STILLSTORM} {KEEP} {NOBODY}",
 # BdA (a500b492): the tub ended up outdoors on the lawn over a cut in the soil.
 # BdB (767d4cd5): soil and a pipe under the bathroom floor again, as if the bathroom were on the ground.
 "Bd": f"{STYLE} {POS} New camera position: in close to the bathtub inside the upstairs bathroom. The tub fills the lower "
       f"two-thirds of the frame, standing on the white-tiled bathroom floor, which runs to the bottom edge of the frame; the running "
       f"shower, the chrome shower head and the white tiled wall fill the top, and the small yellow rubber duck floats in the bath "
       f"water. Nothing below the bathroom floor is in view: no soil, no lawn and no pipes under the floor. {STILLSTORM} {NOCHANGE} "
       f"{NOBODY}",
 "Bo": f"{STYLE} {LOCKZ} Change only this: the shower is turned off and no water falls from the shower head; the bath water has "
       f"drained away, and the small yellow rubber duck sits on the bottom of the empty tub. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- WALL (middle keyframe of the fly-down) ----
 "D": f"{STYLE} {POS} New camera position: outside the house beside its right-hand wall, high near the edge of the roof, looking "
      f"steeply down along the wall: the thick braided copper cable runs straight down the corner of the house, past the windows, "
      f"to the lawn and into the cut soil below. {STILLSTORM} {NOCHANGE} {NOBODY}",
 # ---- GROUND ----
 # GA (ddbc811d): a low front view with the rod moved to the middle of the lawn, away from the corner.
 "G": f"{STYLE} {POS} New camera position: low, right in front of the cut face of the soil at the right-hand corner of the "
      f"block, close. Extreme close-up: the long copper rod goes straight down through the brown and tan soil layers right under "
      f"the corner of the house and fills the middle of the frame from top to bottom; at the top of the frame, just under the "
      f"grass, the thick braided copper cable from the corner of the house is clamped to the rod's top. The copper water pipe is a "
      f"little to the left and does not touch it. {STILLSTORM} {NOCHANGE} {NOBODY}",
 "Gg": f"{STYLE} {LOCKZ} Change only this: the cable and the copper rod glow bright white-blue, and the glow spreads out from the "
       f"rod into the soil around it in soft, fading branches, like roots of light. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- GAP ----
 "S": f"{STYLE} {POS} New camera position: close on the right-hand wall at the height of the bathroom floor, seen from the front "
      f"where the wall is cut open so its thickness shows: on the outside face of the wall the thick braided copper cable runs down, "
      f"and just inside the wall, a hand-width away and parallel to it, the copper water pipe runs up to the bathroom. The cable and "
      f"the pipe fill the middle of the frame. {STILLSTORM} {NOCHANGE} {NOBODY}",
 "Sa": f"{STYLE} {LOCKZ} Change only this: the copper cable {GLOW}, and a bright white-blue electric arc jumps across the gap from "
       f"the cable to the copper water pipe, with a few small sparks. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- FOOT ----
 # KA (625b7377): the strap and the green wire were right, but the braided lightning cable was gone.
 "K": f"{STYLE} {POS} New camera position: a little closer and lower than the reference, just under the grass at the "
      f"right-hand corner: the copper water pipe's elbow and the top of the long copper rod sit side by side in the soil, and the "
      f"thick braided copper cable still comes down the corner of the house and is clamped to the rod's top, exactly as in the "
      f"reference. Now a short copper strap clamps around the water pipe and is bolted to the same bronze clamp on the rod, and a "
      f"thin green wire coming down the outside of the house's corner beside the braided cable is bolted into it too, joining all "
      f"three to the rod. {STILLSTORM} {NOBODY}",
 # ---- POLE ----
 # PA (b7a417bd): the camera stayed far from the pole and the cut face turned into a pit in front of the block.
 "P": f"{STYLE} {POS} New camera position: close to the top of the wooden power pole at the left front corner, level with its "
      f"small grey transformer can, looking toward the house. The pole top, its crossarm and the transformer can are large and close "
      f"in the left third of the frame; the single black cable runs from the pole top across to the upper left corner of the house, "
      f"whose roof and cut-open attic fill the right side of the frame. The lawn and the block of soil stay exactly as in the "
      f"reference, cut straight down at the front. {STILLSTORM} {NOCHANGE} {NOBODY}",
 "Pb": f"{STYLE} {LOCKZ} Change only this: {BOLT} and strikes the top of the power pole with a bright white flash, and the black "
       f"cable from the pole to the house {GLOW}. {STILLSTORM} {KEEP} {NOBODY}",
 # ---- PANEL ----
 "E0": f"{STYLE} {POS} New camera position: inside the downstairs living room, close, looking at its left-hand wall: the open grey "
       f"electrical panel with its rows of breakers, two white wall outlets below it and the floor lamp beside them fill the frame. "
       f"{STILLSTORM} {NOCHANGE} {NOBODY}",
 # EsA (28fd8f12): the floor was cut open over cyan water (the STYLE line leaking in) and a window appeared.
 "Es": f"{STYLE} {LOCKZ} Change only this: bright blue-white sparks burst out of both wall outlets, and a white-blue glow lights "
       f"the breakers inside the open panel. Keep everything else exactly as in the reference: the same wall, floor, lamp and sofa; "
       f"the floor is solid wood and nothing is cut open; there is no water anywhere. {STILLSTORM} {NOBODY}",
 # E1A (b5800638): the right-hand corner of the room opened onto the storm.
 "E1": f"{STYLE} {LOCKZ} Change only this: a small grey metal box, about the size of a hand, is mounted on the wall just to "
       f"the right of the panel and wired into its side, and a green wire runs from the box straight down the wall to the floor. Keep "
       f"everything else exactly as in the reference: the same wall, floor, lamp, sofa and corner; nothing else is added and nothing "
       f"is cut open. There are no sparks. {STILLSTORM} {NOBODY}",
}
# References per still (keys of 09-jobs.tsv). The first reference is the picture being edited.
REFS = {"W0": [], "W": ["W0"], "W1": ["W"], "W1B": ["W1"], "R0": ["W"], "R0B": ["R0"], "R1": ["R0"], "A": ["W"],
        "B": ["W"], "Bg": ["B"], "Bd": ["B"], "Bo": ["Bd"], "D": ["W1"], "G": ["W1"], "Gg": ["G"], "S": ["W1"], "Sa": ["S"],
        "K": ["G"], "P": ["W"], "Pb": ["P"], "E0": ["W"], "Es": ["E0"], "E1": ["E0"]}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
