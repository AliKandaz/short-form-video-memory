# Video 16 (B3, "How to Turn Your House Into a Christmas Light Show"): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 16-prompts.py KEY -> prints the prompt as a JSON string.
# Written before Gate B (21 Nov 2026): nothing here has been generated yet.
# STYLE is section 6.3's Cutaway line with ONE change for this video, approved at Gate A: the lights are the subject, so
# "Bright soft daylight, warm tones, soft shadows" and "translucent cyan water" become blue dusk. Everything else in the look is
# as before. NOWATER goes on every still but the two in the rain (OU1, OU2). LOCK, LOCKZ and POS are as in 15-prompts.py.
# F0 is the set key AND frame 0 (the naive step under way). Every other still is an edit of the one(s) named in REFS; no chain is
# longer than three edits (F0 -> F1 -> GU -> PX is the longest). The dog is drawn into F0 from the words agreed at Gate A; DOG
# (the dog key) is then made from F0 and is the second reference wherever he appears again (ST5, FR6).
# Lessons built in (CLAUDE.md 7.1): close and aerial views name what is whole, so the STYLE line's cut ground doesn't dig pits;
# joins are asked for in so many words; signs are blank (words are overlays, section 5); "No people" on every still.
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Blue dusk just after sunset: a deep blue sky with a soft orange glow low on the horizon, soft even light with no "
"hard shadows, warm light from bulbs and windows, mild depth of field, clean realistic materials, tidy and uncluttered. No text, "
"no letters, no numbers, no captions, no logos, no watermark.")
NOWATER = "There is no water anywhere."
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
DOGW = "a small scruffy tan terrier with a white chest, one folded ear, one upright ear and a red collar"
SET = ("an ordinary two-storey suburban family house in early winter, shown as a cutaway model: pale grey horizontal siding with "
"white trim, a dark grey shingle roof with a straight white gutter along the whole front roof edge, a small covered front porch "
"with a white rail and a dark red front door, two windows upstairs and two downstairs, and a one-storey attached garage on the "
"right with a white garage door and its own low roof; in front, a neat lawn with three low round evergreen bushes under the "
"downstairs windows, a pale concrete driveway on the right leading to the garage door, and along the left side of the lot a strip "
"of dark asphalt road with a concrete curb; one small bare tree at the back left")
CUT = ("The right end of the garage is sliced away like a slice of cake: its end wall and the end of its roof are gone, so the "
"inside shows in section: a bare concrete floor, a grey metal breaker panel on the back wall, a shelf with a few cardboard boxes, "
"and above the ceiling a low attic space with wooden rafters. The rest of the house is whole and closed. The ground is cut "
"straight down along the front edge of the lawn, toward the camera: the cut face shows the grass and dark topsoil, then paler "
"subsoil with a few stones, and a grey plastic conduit running through the soil from under the garage toward the lawn")
CAMERA = ("Camera: in front of the house and a little to the left, at about head height, looking straight at the front of the house. "
"The house fills the upper 60% of the frame: the roof peak about 10% from the top, the front roof edge and its gutter running "
"across the frame about 30% down, the porch and front door left of centre, the garage on the right with its cut-open end at the "
"right edge of the frame, the road and its curb at the left edge. Below the house, the lawn; the block of ground is deep: below "
"the lawn its front is cut straight down all the way to the bottom edge of the frame, and the cut face of soil fills the lowest "
"25% of the frame. There is no ground in front of the block")
POS = "The same house, garage, lawn, set and dusk light as the reference image, with the same parts, colours and materials."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"house, the garage, the lawn and everything in view stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
DOGONLY = "No people; the only animal is the dog."
WHOLE = ("Nothing is cut open in this view: there is no soil, no pit, no trench and no cut face of ground or wall anywhere in the "
"frame.")
AIR = ("This is a view from the air: the lawn, the driveway and the road are whole and flat: there is no trench, no pit and no "
"hole anywhere in them.")
PIXELS = ("lines of small, bright, separate points of light, each a clear bullet-shaped node on a thin black strip")

P = {
 # ---- FRONT: F0 the set key and frame 0; F0b the one string lit; F1 fifty-one strings; F1x the blackout; FR6 the finished build ----
 "F0": (f"{STYLE} {WIDE} Scene: {SET}. {CUT}. {CAMERA}. The naive step is under way: a tall aluminium ladder leans against the "
        f"gutter at the left end of the front roof edge, and one string of small clear Christmas bulbs on a green wire hangs along "
        f"the gutter: its left half is clipped neatly along the roof edge, its right half still hangs loose in a sagging loop down "
        f"to a small coil on the lawn. None of the bulbs is lit. A porch lamp glows by the front door and the downstairs left "
        f"window glows warm from inside; the other windows are dark. On the lawn in the middle, small in the frame, sits {DOGW}, "
        f"wound up in a second unlit string of the same bulbs, looking up at the roof. {NOWATER} {DOGONLY}"),
 "F0b": (f"{STYLE} {LOCK} Change only this: the string of bulbs is now clipped along the whole front roof edge, from the left end "
         f"to the right corner of the house, with no loose loop and no coil on the lawn, and every bulb on it is lit, glowing warm "
         f"white; the string wound round the dog is lit too. The ladder, the porch lamp, the lit window and the dog stay exactly "
         f"where they are. {KEEP} {NOWATER} {DOGONLY}"),
 "F1": (f"{STYLE} {LOCK} Change only this: the house is covered in lit strings of small warm white Christmas bulbs: along the "
        f"whole front roof edge and up both sloping edges of the roof, round all four windows and the front door, along the porch "
        f"rail and its posts, round the garage door and along the garage's roof edge, and draped over the three bushes; every "
        f"bulb is lit. There is no loose string, no coil on the lawn and no ladder. The string wound round the dog is lit. The "
        f"porch lamp and the lit window stay as they are. {KEEP} {NOWATER} {DOGONLY}"),
 "F1x": (f"{STYLE} {LOCK} Change only this: the power is out: every string of bulbs is dark, the porch lamp is off and every "
         f"window is dark, so the house is a dark shape against the blue dusk sky; the unlit strings are all still in place, and "
         f"the string round the dog is dark too. Inside the cut-open garage, one small bright blue-white spark shows at the grey "
         f"breaker panel on the back wall. The sky and its glow stay exactly as they are. {KEEP} {NOWATER} {DOGONLY}"),
 "FR6": (f"{STYLE} {LOCK} Change only this, the finished light show: the warm white strings on the house are replaced by "
         f"{PIXELS}, outlining every edge of the house, the windows, the door and the garage, and showing a smooth wave of colour "
         f"from red at the left through orange, yellow, green and blue to violet at the right. On the lawn at the left stands a "
         f"tall cone-shaped tree made only of strings of light running from a ring on the ground up to the top of a thin pole, as "
         f"tall as the upstairs windows, glowing green with a white star of light on top. Over the driveway on the right stand "
         f"four glowing arches of light in a row, each a half circle taller than a car, striped red and white. By the porch "
         f"stands a snowman made of white lights with two dot eyes, an orange nose and a round open mouth. At the edge of the lawn "
         f"by the road stands a blank white rectangular sign on a short wooden post, with nothing written on it. A thin metal "
         f"aerial stands on the corner of the garage's roof edge. The dog is the same dog as in the second reference image: "
         f"{DOGW}; it now sits beside the snowman, small in the frame, wearing a headband of small reindeer antlers that glow with "
         f"tiny lights, and it is no longer wound in any string. {KEEP} {NOWATER} {DOGONLY}"),
 # ---- GUTTER: GU the LED bulbs close; PX one pixel close ----
 "GU": (f"{STYLE} {POS} New camera position: very close to the front roof edge, just below the white gutter near its left end, "
        f"looking along the gutter toward the right. Extreme close-up: a row of small LED Christmas bulbs on a green wire, held "
        f"on the gutter by small clear plastic clips, runs away from the camera; the nearest bulb fills about a quarter of the "
        f"frame: a clear faceted plastic cap with a tiny square light-emitting diode inside it, glowing warm white. Behind, soft "
        f"and out of focus, the grey siding, one lit window and the deep blue dusk sky. {WHOLE} {NOWATER} {NOBODY}"),
 "PX": (f"{STYLE} {LOCKZ} Change only this: the bulbs on the wire are now pixels: each is a clear bullet-shaped plastic node as "
        f"thick as a finger, pushed through a hole in a thin black strip that runs along the gutter, joined to the next by a "
        f"black cable; inside the nearest node, a tiny green circuit board with one small black square chip and one tiny "
        f"three-colour light is clearly visible. The nearest node glows red, and the next ones glow orange, yellow, green and "
        f"blue in turn. {KEEP} {WHOLE} {NOWATER} {NOBODY}"),
 # ---- OUTLET: OU1 in the rain, the lights out; OU2 the plugs in sealed boxes, the lights back ----
 "OU1": (f"{STYLE} {POS} New camera position: low, close to the ground beside the front wall of the garage, looking straight at "
         f"the wall. In the wall at knee height, an outdoor electrical outlet in a grey weatherproof box with its cover flipped "
         f"up: a white outlet with two sockets and, between them, two small rectangular buttons, one black and one red; the red "
         f"button stands out a little. A green extension cord is plugged into it and runs down to the pale concrete paving, where "
         f"two plug-and-socket joins between green light cords lie in a shallow puddle. Light rain is falling, and the wall and "
         f"the paving are wet. Change: the strings of bulbs that hang on the wall and along the roof edge above are all dark. The "
         f"paving is whole. {WHOLE} {NOBODY}"),
 "OU2": (f"{STYLE} {LOCKZ} Change only this: each of the two plug joins on the paving now sits inside its own small closed "
         f"dark green plastic box, the cords passing through sealed slots at its two ends, and the red button on the outlet is "
         f"pressed in flat; the strings of bulbs on the wall and along the roof edge above are lit again, warm white. The rain "
         f"keeps falling and the puddle stays. {KEEP} {WHOLE} {NOBODY}"),
 # ---- HIGH: HI3 the roof line in pixels, the controller in the garage ----
 "HI3": (f"{STYLE} {POS} New camera position: high in the air above the front lawn, looking down at the house at about 40 "
         f"degrees, the whole house in the frame with lawn round it: the roof, the front wall, the porch, and the garage on the "
         f"right with its end cut open. Change: the warm white strings are gone and every edge of the house is outlined in "
         f"{PIXELS} instead: along the roof edges and the gutter, round the windows, the door and the garage, showing a smooth "
         f"wave of colour from red at the left through orange, yellow, green and blue to violet at the right. On the back wall of "
         f"the cut-open garage, beside the breaker panel, hangs a grey plastic box with its door open: inside it a green circuit "
         f"board and a silver metal power supply. The dog is not in this view. {AIR} {NOWATER} {NOBODY}"),
 # ---- ROOF: RO4 power injected, all white; RO3 the fault before it, white fading to pink ----
 "RO4": (f"{STYLE} {POS} New camera position: at the left end of the front roof edge, level with the gutter and just in front of "
         f"it, looking along the roof edge toward the right end of the house; the gutter runs away from the camera from the lower "
         f"left to the middle right of the frame. Change: along the gutter runs one single line of pixels, {PIXELS}, and every "
         f"one of them, from the nearest to the farthest, is pure bright white. Halfway along, one black cable comes up from "
         f"under the eave and joins the line at a small black T-shaped connector. Behind the line, the dark grey shingles slope "
         f"up; beyond the far end of the house, the deep blue dusk sky. {WHOLE} {NOWATER} {NOBODY}"),
 "RO3": (f"{STYLE} {LOCKZ} Change only this: there is no cable coming up from under the eave and no T-shaped connector; the "
         f"pixels nearest the camera are pure bright white, but from halfway along the line they shade gradually into pale pink, "
         f"and the farthest ones are dim pink. {KEEP} {WHOLE} {NOWATER} {NOBODY}"),
 # ---- STREET: ST5 the cars, the sign, the aerial, the dog howling; SG the sign close ----
 "ST5": (f"{STYLE} {POS} New camera position: low on the dark asphalt road at the left side of the lot, near its front corner, "
         f"looking diagonally across the concrete curb at the front of the house. In the foreground two ordinary cars are parked "
         f"along the curb, seen from behind and from the side, dark and empty, with their dashboards dark. Behind them, the lawn "
         f"and the house. Changes: every edge of the house is outlined in {PIXELS}, showing a wave of colour; at the edge of the "
         f"lawn by the curb stands a blank white rectangular sign on a short wooden post, with nothing written on it; a thin "
         f"metal aerial as long as a forearm stands on the corner of the garage's roof edge with a small black box at its foot; "
         f"far up the road, the windows of two other houses are lit. The dog is the same dog as in the second reference image: "
         f"{DOGW}; it sits on the lawn near the sign, small in the frame, with its head thrown back, howling, and it is not "
         f"wound in any string. The road, the curb and the lawn are whole. {WHOLE} {NOWATER} {DOGONLY}"),
 "SG": (f"{STYLE} {POS} New camera position: at the edge of the lawn, close to the blank white sign on its short wooden post. "
        f"The sign fills about a third of the frame, a little left of centre and in the upper half, facing the camera: a plain "
        f"white rectangle with nothing written on it. Behind it, soft and out of focus, the house with its lines of coloured "
        f"pixel lights; at the right edge of the frame, part of a parked car, its dashboard glowing softly through the "
        f"windscreen. The dog is not in this view. {WHOLE} {NOWATER} {NOBODY}"),
 # ---- the dog key: made from F0, a reference for ST5 and FR6 (4.5) ----
 "DOG": ("Photoreal 3D render, soft even light, clean realistic materials, mild depth of field. The same dog as in the "
         f"reference image, alone: {DOGW}. It stands on all four legs, whole body in view, turned three-quarters toward the "
         "camera, on a plain, flat, pale grey ground with a soft shadow under it. No string of lights, no house, no lawn, "
         "nothing else in the picture. No text, no letters, no logos, no watermark. No people."),
}
REFS = {"F0": [], "F0b": ["F0"], "F1": ["F0"], "F1x": ["F1"], "FR6": ["F1", "DOG"], "GU": ["F1"], "PX": ["GU"],
        "OU1": ["F1"], "OU2": ["OU1"], "HI3": ["F1"], "RO4": ["F1"], "RO3": ["RO4"], "ST5": ["F1", "DOG"], "SG": ["ST5"],
        "DOG": ["F0"]}
AR = {"DOG": "1:1"}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
