# Video 15 (V6, "Why This NFL Field Is Sitting on 546 Wheels"): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 15-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE is the Cutaway default WITHOUT "translucent cyan water" (6.3; as 10-prompts.py): the only water in this set is inside the
# drain pipe and the sprinkler spray in the layers' close-up (LA0), named there. NOWATER goes on every other still. LOCKZ is
# byte-identical to 14-prompts.py. SET carries the place and its colours; SIDECUT lists the cut face once, for the set key SIDE1
# (the close views repeat what they need). Every other still is an edit of the one(s) named in REFS: LOCK or LOCKZ keeps the
# framing for a change at one position; POS moves the camera to a new position on the same set. The near long side of the
# stadium is sliced away along the field's near edge, so the wheels show side-on (round), not edge-on from the end.
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, tidy and "
"uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
NOWATER = "There is no water anywhere."
SET = ("a big American football stadium in the desert on a bright, hot, clear day, shown as a cutaway model: an oval bowl of grey "
"seats rising in steep tiers, clad outside in pale silver metal panels, under a white fabric roof whose two huge middle panels "
"can slide open; in the middle of the bowl, a natural green grass football field with plain white yard lines and no numbers, no "
"logos and no end-zone markings, grown in one giant steel tray about a metre deep that rides on rows of big round steel wheels "
"along thirteen straight steel rails set in a grey concrete floor; in the right end wall of the bowl, a huge rectangular opening "
"as wide as the field, through which the thirteen rails run straight out across a flat, sunny lot of pale tan desert ground, "
"with a few saguaro cacti and palo verde trees, and hazy mountains far away")
SIDECUT = ("The near long side of the stadium is sliced away like a slice of cake: the near stands, the near part of the roof and "
"the ground beneath them are gone, so the inside of the bowl shows from the side, and the ground under the field is cut straight "
"down along the field's near edge, toward the camera. The cut face shows, from the top: the green grass and its roots; a thick "
"layer of tan sand with fine fibres in it; a thin black plastic drainage mat; a white drain pipe running along the length of the "
"field; the flat steel bottom and side of the tray; under the tray, a long row of big round steel wheels, seen side-on like "
"train wheels, sitting on a steel rail; the grey concrete floor slab; and layers of pale desert soil down to the bottom edge of "
"the frame")
CAMERA = ("Camera: low, just in front of the cut at the middle of the field's near edge, about level with the top of the wheels, "
"looking straight at the cut face and across the field. The cut face fills the lower 55% of the frame and runs off both side "
"edges: the edge of the grass about 45% down, the row of six to eight big round wheels on their rail about 70% down, the soil "
"layers at the bottom edge. Above it, the green field with its white yard lines running straight away from the camera to the far "
"sideline, the grey stands rising on the far side, and the roof's two huge middle panels open on a blue sky, with hot sunlight "
"on the grass. There is no ground in front of the cut face")
POS = "The same desert football stadium, field, set and light as the reference image, with the same parts, colours and materials."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"stadium, the field and everything in view stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
TORT = ("a desert tortoise with a high domed brown shell and scaly grey legs")
AIRLOT = ("The desert ground of the lot is whole and flat all round the tray and the rails: there is no trench, no pit, no hole "
"and no cut face of ground anywhere in the lot.")  # added after HI0.B dug a trench into the lot (21 Nov 2026)

P = {
 # ---- SIDE (SIDE1 the set key, cut open; SIDE0 the solid face: the first and last frame) ----
 "SIDE1": f"{STYLE} Scene: {SET}. {SIDECUT}. {CAMERA}. {NOWATER} {NOBODY}",
 # SIDE1 try A (e2a44ba8) came back as a three-quarter view toward the huge opening at the back right (the rails beside the
 # tray run out to it), not straight at the cut face: kept, and the plan fitted to it (7.1). SIDE0 is written for that layout.
 "SIDE0": f"{STYLE} {LOCK} Change only this: the field's front is not cut open: from the edge of the grass down to the bottom of "
          f"the frame, the front of the block under the field is one plain, solid, flat face of smooth grey concrete with pale tan "
          f"soil below it, like the side of a solid block, so no layers, no sand, no mat, no pipe, no tray and no wheels show. The "
          f"rails and the floor at the right, the field, the stands, the open roof and the opening stay exactly as they are. "
          f"{KEEP} {NOWATER} {NOBODY}",
 # ---- WHEELS ----
 "WH0": f"{STYLE} {POS} New camera position: very close to the cut face, down at the level of the wheels, looking straight at "
        f"them. Extreme close-up: the row of big round steel wheels sitting on the steel rail fills most of the frame, the nearest "
        f"wheel large in the middle with its thick steel rim, its hub and its axle, the others running off to the right in a "
        f"straight row; above them, the flat steel bottom of the tray spans the top of the frame; below them, the steel rail and "
        f"the grey concrete floor slab. {NOWATER} {NOBODY}",
 # ---- ROOF (RF0 open, sunlit; RF1 closed, lower, the grass pale) ----
 "RF0": f"{STYLE} {POS} New camera position: high inside the bowl, up near the roof above the cut-away near side, looking down "
        f"along the field toward its right end: the green field with its white yard lines spreads below, bright in hot sunlight "
        f"that falls through the roof's two huge middle panels, which stand open on a blue sky across the top of the frame; the "
        f"grey stands rise on the far side; at the right end of the field, the huge rectangular opening in the end wall, with the "
        f"bright sunny desert lot and the thirteen rails running out through it. {NOWATER} {NOBODY}",
 "RF1": f"{STYLE} {POS} New camera position: lower and closer over the grass than the reference, still looking along the field "
        f"toward its right end. Change: the roof's two huge middle panels are now closed overhead, so no sunlight falls on the "
        f"field: the whole field lies in cool shade, and the grass looks pale, dull and yellowish-green; through the opening at "
        f"the right end, the desert lot outside is still bright in the sun. {NOWATER} {NOBODY}",
 # ---- HIGH (HI0 the field outside; HI1 the field still inside) ----
 "HI0": f"{STYLE} {POS} New camera position: outside the stadium, high in the air above the sunny desert lot beyond the stadium's "
        f"right end, looking back toward the stadium and down at about 45 degrees. The oval stadium fills the upper half of the "
        f"frame: its pale silver walls, its white roof with the two huge middle panels closed, its near long side sliced away like "
        f"a cake so its grey seats and its inside show in section, and the huge rectangular opening in its end wall, facing the "
        f"camera. Change: the field is no longer inside: the whole green football field, on its steel tray, sits outside in the "
        f"lot in the lower half of the frame, on the thirteen steel rails that run from the opening across the pale tan desert "
        f"ground, bright green in full sun; a few saguaro cacti and palo verde trees around; hazy mountains on the horizon. "
        f"{NOWATER} {NOBODY}",
 "HI1": f"{STYLE} {LOCK} Change only this: the field has been rolled back inside the stadium: the lot is empty, just flat pale "
        f"tan desert ground with the thirteen bare steel rails running from the stadium's opening across it; through the opening, "
        f"the green field shows inside the stadium. {AIRLOT} {KEEP} {NOWATER} {NOBODY}",
 # ---- RAIL (RA0; TO0 adds the tortoise) ----
 "RA0": f"{STYLE} {POS} New camera position: down on the ground in the sunny lot, low, beside the long side of the field's steel "
        f"tray, looking along it toward the stadium: the tall, flat steel side of the tray runs from the left of the frame into "
        f"the distance, with the edge of the green grass on top of it; under it, a row of big round steel wheels on a steel rail; "
        f"on the nearest wheel's axle, a small grey electric motor; the thirteen rails run on ahead to the stadium's huge opening "
        f"in the distance; pale tan desert ground, a saguaro cactus, blue sky. {AIRLOT} {NOWATER} {NOBODY}",
 "TO0": f"{STYLE} {LOCKZ} Change only this: {TORT} walks on the ground beside the rail in the foreground, about a quarter of the "
        f"frame, heading the same way as the tray, toward the stadium. {KEEP} {NOWATER} No people; the only animal is the "
        f"tortoise.",
 # ---- LAYERS ----
 "LA0": f"{STYLE} {POS} New camera position: very close to the cut face, at the level of the grass and the layers below it, "
        f"looking straight at them. Extreme close-up of the cut face of the tray, the layers filling the whole frame: at the top, "
        f"the green grass blades, with small round sprinkler heads poking up among them; below, the white roots reaching down into "
        f"a thick layer of tan sand with fine fibres in it; under the sand, a thin black plastic drainage mat; under that, a "
        f"white drain pipe running across the frame, cut open so the clear water inside it shows; at the bottom, the flat steel "
        f"bottom of the tray. The only water is inside the pipe. {NOBODY}",
 # ---- FLOOR (FL0 bare; FL1 the basketball court) ----
 "FL0": f"{STYLE} {POS} New camera position: inside the bowl, low over the stadium floor near the middle of the cut-away near "
        f"side, looking along the floor toward the right end. Change: the field and its steel tray are gone: the floor is bare, "
        f"flat grey concrete with the thirteen steel rails set into it, running straight to the huge rectangular opening in the "
        f"right end wall; the roof's middle panels are closed, so the inside is in cool shade; through the opening, outside in "
        f"bright sun, the whole green field sits on its tray on the rails in the desert lot; the grey stands rise on both sides. "
        f"{NOWATER} {NOBODY}",
 "FL1": f"{STYLE} {LOCK} Change only this: in the middle of the bare concrete floor stands a basketball court: a rectangle of "
        f"pale wooden boards with plain white lines and no logos, with a hoop on a stand at each end, and rows of temporary grey "
        f"seats around it; bright white lights shine down on the court. {KEEP} {NOWATER} {NOBODY}",
}

REFS = {"SIDE1": [], "SIDE0": ["SIDE1"], "WH0": ["SIDE1"], "RF0": ["SIDE1"], "RF1": ["RF0"], "HI0": ["SIDE1"], "HI1": ["HI0"],
        "RA0": ["HI0"], "TO0": ["RA0"], "LA0": ["SIDE1"], "FL0": ["SIDE1"], "FL1": ["FL0"]}
# HI0 try A (53bb8e49) drew the field outside in the lot but ALSO green grass inside the bowl (through the open roof and the end
# opening), and left the roof open: HI0.B is a LOCK edit of try A that empties the inside and closes the roof.
P["HI0.B"] = (f"{STYLE} {LOCK} Change only this: inside the stadium there is no grass at all: the floor inside the bowl, wherever "
              f"it shows through the roof and through the huge opening in the end wall, is bare grey concrete with steel rails running "
              f"out through the opening; and the roof is closed: its two huge middle panels have slid together and now cover the whole "
              f"middle of the bowl, so the seats inside cannot be seen from above. The green field outside on its tray in the lot "
              f"stays exactly where it is. {KEEP} {NOWATER} {NOBODY}")
REFS["HI0.B"] = ["HI0.A"]
# HI0.B (13f3d385) emptied the inside and closed the roof, but zoomed in and dug a big trench of rocks into the lot in front of the
# tray (the STYLE line's cut ground leaking into an aerial view, 7.1). HI0.C redoes the fix from try A, holding the framing and
# naming the whole, flat lot.
P["HI0.C"] = (f"{STYLE} {LOCK} The camera stays far back and high: the whole stadium and the whole field fit in the frame with "
              f"desert all round, exactly as in the reference. Change only this: inside the stadium there is no grass at all: the "
              f"floor inside the bowl, wherever it shows through the huge opening in the end wall, is bare grey concrete with steel "
              f"rails running out through the opening; and the roof is closed: its two huge middle panels have slid together and "
              f"now cover the whole middle of the bowl, so the inside of the bowl cannot be seen from above. The green field outside "
              f"on its tray stays exactly where it is, on its rails. This is a view from the air: the desert ground of the lot is "
              f"whole and flat all round the tray and the rails: there is no trench, no pit, no hole and no cut face of ground "
              f"anywhere in the lot. {KEEP} {NOWATER} {NOBODY}")
REFS["HI0.C"] = ["HI0.A"]
# TO0 try A (18ded007) drew the tortoise well but zoomed in and dug a pit of rocks into the ground beside it (the STYLE line's cut
# ground again): TO0.B redoes it from RA0 with AIRLOT and the foreground named whole.
P["TO0.B"] = (f"{STYLE} {LOCKZ} Change only this: {TORT} walks on the ground beside the rail in the foreground, about a quarter "
              f"of the frame, heading the same way as the tray, toward the stadium. The ground under and around the tortoise is "
              f"whole, flat pale tan desert ground: nothing is cut open in the foreground. {AIRLOT} {KEEP} {NOWATER} No people; "
              f"the only animal is the tortoise.")
REFS["TO0.B"] = ["RA0"]
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
