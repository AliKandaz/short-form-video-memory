# Video 12 (V1, "Why Some Manhole Covers Are Full of Holes"): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 12-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE, WIDE and LOCKZ are byte-identical to 10-prompts.py (STYLE is the Cutaway default without "translucent cyan water": the
# only water on this set is slush and a few clear drips). SET carries the place and its colours; W0OBJ lists the objects once,
# for W0 only. Every other still is an edit of the one(s) named in REFS: LOCK or LOCKZ keeps the framing for a change at one
# position; POS moves the camera to a new position on the same set. STREETZ (road-level views) and VAULTZ (views inside the
# concrete room) stop the STYLE line's cut ground from leaking into close-ups (7.1).
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, tidy and "
"uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a short stretch of a two-lane city street on a bright winter day, shown as a cutaway model: grey asphalt under a thin "
"skin of grey-white slush, with slush heaped along the curbs; a sidewalk with a granite curb along the far side; plain red-brick "
"and pale stone building fronts behind the sidewalk, with dark windows and no signs; and one round cast-iron manhole lid in the "
"middle of the near lane. The street stands on a deep block of ground cut straight down like a slice of cake toward the camera, "
"so the cut face shows the road's layers: dark asphalt on top, then grey concrete, then brown packed earth")
CAMERA = ("Camera: from the front, a little from the left and slightly raised, looking at the cut face of the street block, which "
"fills about 90% of the frame width; the street runs from left to right across the frame. The building fronts and a strip of "
"pale winter sky fill the top quarter of the frame; the road surface with the manhole lid sits about 30% down from the top. "
"Right under the lid the cut face opens into a concrete room whose floor sits about 55% down. Below that the block of ground is "
"cut straight down all the way to the bottom edge of the frame, deep, even layers of brown packed earth with nothing in them. "
"There is no ground in front of the block")
LID = ("The lid is plain dark cast iron with a simple raised diamond pattern and one small round pick hole near its edge, and no "
"lettering")
VENTED = ("a round cast-iron manhole lid of the same size, full of evenly spaced round holes, each about the size of a coin, in "
"rings from the centre out to the rim, with no lettering")
W0OBJ = ("Under the lid, drawn like a clear diagram: a short round concrete shaft runs down from the lid into a rectangular "
"concrete room about as deep as a person is tall, whose front wall is removed so its inside shows. Galvanised steel racks on its "
"back and side walls hold thick black power cables in heavy rubbery coats; the cables loop round the room and run into round duct "
"openings in its side walls, and a block of concrete ducts runs off to the right under the street. The room is dim, dry and "
"clean. On the street, an orange salt truck with no lettering drives along the far lane, its spinner at the back throwing white "
"rock salt onto the road; its cab windows are dark. A single grey pigeon stands on the lid")
SLUSH = "The only water is grey-white slush: there are no puddles and no pools."
STREETZ = ("This is a view at road level: nothing is cut open in view, and there is no soil, no cut face and no room anywhere in "
"the frame.")
VAULTZ = ("This is a view inside the concrete room: concrete walls, steel racks and cables fill the frame, and there is no soil, "
"no sky and no street in view.")
POS = "The same street, set and light as the reference image, with the same parts, colours and materials."
NOCHANGE = "Nothing in the scene changes."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"street, the lid, the concrete room and the cut face of the ground stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOPEOPLE = "No people."
NOBODY = "No people, no animals."

P = {
 # ---- SIDE (the wide; the set key) ----
 "W0": f"{STYLE} {WIDE} Scene: {SET}. {CAMERA}. {LID}. {W0OBJ}. {SLUSH} {NOPEOPLE}",
 # ---- STREET (frame 0, the blast, the last frame) ----
 "ST0": f"{STYLE} {POS} New camera position: down at the level of the slush on the road, a short step from the manhole lid, "
        f"looking across the road at it. Low close-up: the round iron lid fills the lower middle third of the frame, seen low and "
        f"close, with a thin skin of grey-white slush on it, and the grey pigeon stands on it; a thin wisp of grey smoke curls up "
        f"from the edge of the lid. Behind it, softly blurred, the slushy road, the building fronts and the orange salt truck with "
        f"its amber lights on. {STREETZ} {SLUSH} {NOPEOPLE}",
 "ST1": f"{STYLE} {LOCKZ} Change only this: the manhole lid is bursting straight up off the road on a tall column of bright "
        f"orange flame and thick grey smoke, already a little above the road and tilting; slush sprays out in all directions; the "
        f"pigeon flaps away into the air with its wings spread wide. {KEEP} {NOPEOPLE}",
 "ST9": f"{STYLE} {LOCKZ} Change only this: the lid is now the lid full of round holes with four small steel latches round its "
        f"rim, exactly as in the second reference image, with a thin skin of grey-white slush on it; the pigeon stands on it "
        f"exactly as in the first reference image; there is no smoke anywhere. {KEEP} {NOPEOPLE}",
 # ---- HIGH ----
 "H0": f"{STYLE} {POS} New camera position: high above the street, about three storeys up, looking steeply down at the road. "
       f"The round hole where the lid was is open in the middle of the near lane and pours a thick column of grey smoke straight "
       f"up; the iron lid tumbles in the air near the camera, large in the upper part of the frame; the orange salt truck is in the "
       f"far lane beside the hole, its spinner throwing white rock salt onto the slushy road. The front edge of the street block "
       f"runs along the bottom of the frame, with its cut face going down. {SLUSH} {NOBODY}",
 "H1": f"{STYLE} {POS} New camera position: higher and further back than the reference, looking along the whole block: the open "
       f"hole still smokes in the near lane in the lower part of the frame, and further along the street two more round manhole "
       f"lids each have thin grey smoke curling up from them; the orange salt truck has moved on along the far lane, and the lid "
       f"is no longer in the air. {SLUSH} {NOBODY}",
 # ---- VAULT ----
 "V0": f"{STYLE} {POS} New camera position: inside the concrete room under the lid, through its open front, at the height of the "
       f"cable racks, close, looking at the back wall: galvanised steel racks hold the thick black power cables, which loop along "
       f"the wall and run into round duct openings in the side walls; the short round shaft rises in the upper part of the frame "
       f"to the underside of the lid, with a tiny speck of daylight at its pick hole. The room is dim, dry and clean. {VAULTZ} "
       f"{NOBODY}",
 "V1": f"{STYLE} {LOCKZ} Change only this: the room is now full of thick grey smoke, so the cables and the racks show only dimly "
       f"through it. {KEEP} {NOBODY}",
 # ---- UNDER-LID ----
 "U0": f"{STYLE} {POS} New camera position: at the bottom of the short round shaft, looking straight up it at the underside of "
       f"the iron lid: the round concrete walls of the shaft frame the dark lid, which fills the upper middle of the frame, with a "
       f"single point of daylight at its small pick hole; clear drops of meltwater fall from the pick hole straight down past the "
       f"camera; the tops of the cable racks show along the bottom edge. {VAULTZ} {NOBODY}",
 "U1": f"{STYLE} {LOCKZ} Change only this: the lid at the top of the shaft is now the lid full of round holes shown in the "
       f"second reference image, seen from below: bright daylight shines down through its many holes in thin beams, and thin grey "
       f"smoke streams up out through the holes. There are no drops of water. {KEEP} {NOBODY}",
 # ---- CABLE ----
 "C0": f"{STYLE} {POS} New camera position: right at the cable racks on the back wall, very close. Extreme close-up: one thick "
       f"black power cable in a heavy rubbery coat fills most of the frame, lying across a galvanised steel rack; a clear drop of "
       f"meltwater lands on the coat and beads on it; the concrete wall behind is softly blurred. {VAULTZ} {NOBODY}",
 "C1": f"{STYLE} {POS} New camera position: closer than the reference, on the same thick black cable where the drop "
       f"landed. Extreme close-up: the cable's black rubbery coat fills the whole frame from edge to edge; along it a crust of "
       f"white salt has formed, and a thin crack runs through the coat in the middle of the crust. {VAULTZ} {NOBODY}",
 # ---- SENSOR ----
 "SEN": f"{STYLE} {POS} New camera position: close to the back wall of the room, beside the cable racks: a small grey plastic "
        f"sensor box, the size of a book, is bolted to the concrete wall next to the cables, with one small round green light "
        f"glowing on its face and a thin grey wire running from it along the wall. The box fills the middle of the frame. "
        f"{VAULTZ} {NOBODY}",
 # ---- RIM ----
 "R0": f"{STYLE} {POS} New camera position: just above the street, about head height, looking straight down at the manhole lid "
       f"in the middle of the near lane, which fills the middle of the frame. The lid is now a different lid: {VENTED}; thin wisps "
       f"of grey smoke rise from some of the holes; grey-white slush lies on the road round its rim. {STREETZ} {SLUSH} {NOBODY}",
 "R3": f"{STYLE} {LOCKZ} Change only this: four small steel latches now hold the lid's rim to its iron frame at four points "
       f"evenly spaced round it, like small hinged clips. {KEEP} {NOBODY}",
 "R2": f"{STYLE} {LOCKZ} Change only this: the lid has lifted a finger's width straight up out of its frame, still held by its "
       f"four latches, and grey smoke puffs out all round the gap at its rim. {KEEP} {NOBODY}",
}

REFS = {"W0": [], "ST0": ["W0"], "ST1": ["ST0"], "ST9": ["ST0", "R3"], "H0": ["W0"], "H1": ["H0"], "V0": ["W0"], "V1": ["V0"],
        "U0": ["V0"], "U1": ["U0", "R0"], "C0": ["V0"], "C1": ["C0"], "SEN": ["V0"], "R0": ["ST0", "H0"], "R3": ["R0"],
        "R2": ["R3"]}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
