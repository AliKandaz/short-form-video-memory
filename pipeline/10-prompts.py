# Video 10 (X5, "Why These People Are Frozen Upside Down", cryonics): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 10-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE is the Cutaway default of 3.3 Step 4 without "translucent cyan water": this set has no water (section 2 rule 2), and the
# liquid nitrogen must read clear and colourless (NITRO), never cyan. WIDE goes only into the wide stills; SET carries the place
# and its colours; BUILDING lists the objects once, for W0 only. Every other still is an edit of the one named in REFS: LOCK or
# LOCKZ keeps the framing for a change at one position; POS moves the camera to a new position on the same set (3.3 Step 5).
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, tidy and "
"uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a small modern research building with smooth white walls, pale grey floors and brushed stainless-steel fittings, shown as "
"a cutaway model: its whole front wall is removed like a dollhouse, so every room shows inside. The building stands on a square "
"block of ground with a narrow strip of pale gravel in front of it. The front of the block is cut straight down like a slice of "
"cake, so the cut face shows clean layers of brown and tan soil")
CAMERA = ("Camera: straight-on from the front, slightly raised, centred on the building, which fills about 85% of the frame width. "
"The flat roof sits about 10% down from the top of the frame, with a little pale blue sky above it, and the ground floor meets the "
"gravel about 52% down. The block of ground is deep: below the gravel its front is cut straight down all the way to the bottom "
"edge of the frame, so the whole lower part of the frame is the cut face of the ground, deep, even layers of brown and tan soil "
"with nothing in them. There is no ground in front of the block")
BUILDING = ("Inside, drawn like a clear diagram. The left half of the building has two floors. Its ground floor is a bright "
"cooling room: white double doors, shut, in its left-hand wall; a heart monitor on a wheeled stand beside them; an empty steel "
"operating table in the middle; a steel drip stand holding two clear bags of pale-blue liquid; a small white pump cart with a "
"round rotor on its front; and a white counter along the back wall with a small steel tray of glass vials on it. Its upper floor "
"is a small plain office with a desk and a chair. The right half of the building is one tall storage hall that rises through "
"both floors: tall brushed stainless-steel cylinder tanks, each about twice as tall as a person, stand in rows going back into the "
"hall. The front tank, on the left of the hall, is sliced open from top to bottom with its front half removed, showing its thick "
"double steel wall with a narrow gap between the inner and outer skins; clear, colourless liquid nitrogen fills it almost to the "
"top under rolling white fog, and inside it four long white sealed pods stand upside down, their rounded ends at the bottom of "
"the tank, around a middle column of small white canisters stacked one above the other. To its right stands a second tank with "
"a round lid, closed. A steel catwalk with a railing runs along the tops of the tanks at the level of the upper floor, with a "
"small overhead hoist hanging empty above the second tank. A thick silver insulated hose runs from a tall white storage tank "
"standing outside the right-hand wall of the building, in through the wall and up to the catwalk. At the back of the row stands "
"the oldest tank, duller than the rest and crusted with white frost")
NITRO = ("The liquid nitrogen looks exactly as in the reference: clear and very pale, like cold glass, with white fog rolling on its "
"surface; it is not water and it never glows.")
NOWATER = "There is no water anywhere."
FLOORS = "The floor is solid and nothing below it is in view: no soil, no pipes, no water."
POD = ("a long white sealed pod, smooth and rounded like a cocoon, with nothing written on it and no face, no skin and no body "
"showing")
POS = "The same building, set and light as the reference image, with the same parts, colours and materials."
NOCHANGE = "Nothing in the building changes."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"building, its rooms, the tanks, the catwalk and the cut face of the ground stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
WORKER = ("a small worker in a blue coverall, thick grey gloves, a cap and a frosted face shield, so no face shows")

P = {
 # ---- WIDE ----
 "W0": f"{STYLE} {WIDE} Scene: {SET}. {CAMERA}. {BUILDING}. {NITRO} {NOWATER} {NOBODY}",
 "Wb": f"{STYLE} {WIDE} {POS} New camera position: a little lower and a little to the right of the reference, still in front of "
       f"the building and looking at it, so the storage hall is a little larger and nearer and the building is seen slightly from "
       f"the right; the whole building is still in view in the upper 60% of the frame, with the cut face of the soil below. "
       f"{NITRO} {NOCHANGE} {NOBODY}",
 # ---- DOOR ----
 "D0": f"{STYLE} {POS} New camera position: inside the ground-floor cooling room on the left, low and close, looking toward "
       f"the white double doors in its back wall, on the left. The doors now stand open, and a steel gurney has just rolled in through them: on it "
       f"sits a long white tub, and in the tub lies {POD}. Beside the gurney stand the heart monitor on its wheeled stand, its screen "
       f"showing a bright green beating heart line, and the small white pump cart with its round rotor. The gurney, the tub and the "
       f"monitor fill the middle of the frame. {FLOORS} {NOWATER} {NOBODY}",
 "D0f": f"{STYLE} {POS} New camera position: closer than the reference and a little lower, in front of the gurney: the white tub "
        f"with the white pod in it fills the lower half of the frame, and the heart monitor's screen is large in the upper left. "
        f"Change this: the line on the monitor's screen is now completely flat, one straight green line. {FLOORS} {NOWATER} "
        f"{NOBODY}",
 "D1": f"{STYLE} {LOCKZ} Change only this: the white tub is now packed full of ice cubes around the white pod, up to the rim, with "
       f"only the top of the pod showing; two clear tubes run from the small white pump cart into the side of the pod, and the "
       f"pump's round rotor is turning. The monitor's line stays flat. {KEEP} {NOBODY}",
 # ---- TRAY ----
 "T0": f"{STYLE} {POS} New camera position: right at the white counter along the back wall of the cooling room, low and very close. Extreme "
       f"close-up: the small steel lab tray fills most of the frame. On it, from left to right: a small clear glass vial of water "
       f"standing in a little rack; a single frosty red strawberry on a small white dish; a small clear vial of pale-blue liquid; "
       f"and a small open steel flask. The counter top runs to the bottom edge of the frame, and the room behind is softly blurred. "
       f"Nothing is cut open and there is no soil. {NOBODY}",
 "T1": f"{STYLE} {LOCKZ} Change only this: the water in the left-hand vial has frozen solid white, and sharp white ice crystals "
       f"burst out of its top and split the glass down one side. {KEEP} {NOBODY}",
 "T2": f"{STYLE} {LOCKZ} Change only this: the strawberry has thawed and collapsed into a soft, shapeless red heap sitting in a "
       f"small puddle of red juice on its white dish. The frozen, split vial stays exactly as in the reference. {KEEP} {NOBODY}",
 "T3": f"{STYLE} {POS} New camera position: closer on the right-hand end of the tray, at the height of the vials, so the small "
       f"open steel flask fills the middle of the frame. Change this: the small vial of pale-blue liquid now stands inside the "
       f"flask, which is full of clear, colourless liquid nitrogen; thick white vapour pours over the flask's rim and down its "
       f"sides, and the vial is perfectly clear and glossy, like glass, with no ice and no crystals in it. The collapsed strawberry "
       f"is just in view at the left edge of the frame. {NOBODY}",
 "T3w": f"{STYLE} {LOCKZ} Change only this: the glassy pale-blue vial has been lifted out of the flask and stands on the tray "
        f"beside it; a thin white frost covers it and is melting into small drops running down its sides. {KEEP} {NOBODY}",
 "T4": f"{STYLE} {LOCKZ} Change only this: one sharp crack now runs across the glassy pale-blue vial from one side to the other. "
       f"{KEEP} {NOBODY}",
 # ---- TABLE ----
 "B0": f"{STYLE} {POS} New camera position: inside the ground-floor cooling room at the height of the steel operating table, "
       f"close, looking at it from the front. {POD[0].upper() + POD[1:]} lies along the table; two clear tubes run from the small "
       f"white pump cart into the side of the pod, and the tubes are filled with dark red liquid; above the table, the steel drip "
       f"stand holds two clear bags of pale-blue liquid with a thin tube from them down to the pump. The table and the pod fill the "
       f"middle of the frame. {FLOORS} {NOWATER} {NOBODY}",
 "B1": f"{STYLE} {LOCKZ} Change only this: the two tubes running into the pod are now filled with pale-blue liquid instead of "
       f"dark red, and the two bags on the drip stand are half empty. {KEEP} {NOWATER} {NOBODY}",
 # ---- HOIST ----
 "H0": f"{STYLE} {POS} New camera position: high up on the steel catwalk above the storage hall, beside the second tank, looking "
       f"steeply down into it. The second tank's round lid is open, and thick white fog rises out of its round mouth from the "
       f"liquid nitrogen inside. {POD[0].upper() + POD[1:]}, frosted white, hangs from the cable of the small overhead hoist just "
       f"above the fog. The tank's mouth and the hanging pod fill the middle of the frame, with the catwalk railing along the lower "
       f"edge. {NITRO} {NOWATER} {NOBODY}",
 "H1": f"{STYLE} {LOCKZ} Change only this: the hanging pod has been lowered into the tank: its lower half has gone down into the "
       f"white fog, and only its upper half still shows above the tank's mouth. {KEEP} {NOWATER} {NOBODY}",
 # ---- WALL ----
 "L0": f"{STYLE} {POS} New camera position: inside the storage hall, low and close to the front tank that is sliced open, at its "
       f"cut edge, looking at the cut: the thick double steel wall fills the middle of the frame in cross-section, an inner steel "
       f"skin and an outer steel skin with a narrow empty gap between them, running from the top of the frame down to the tank's "
       f"base standing on the grey floor; through the cut, the clear liquid nitrogen and the white pods show inside. The cool white "
       f"ceiling lights of the hall are on. {NITRO} {FLOORS} {NOBODY}",
 "L1": f"{STYLE} {LOCKZ} Change only this: the hall's ceiling lights are switched off, so the hall is dim and blue-grey, lit only "
       f"by faint daylight; white fog still rolls on the liquid nitrogen. The same nitrogen colour as the reference; nothing "
       f"glows. {KEEP} {NOBODY}",
 "L0b": f"{STYLE} {POS} New camera position: lower and closer than the reference, right at the foot of the front tank: the "
        f"tank's round steel base standing on the smooth grey floor fills the frame, with the cut double wall rising out of the "
        f"top of the frame; nothing is attached to the base: no cable, no plug, no wire and no pipe. {FLOORS} {NOWATER} {NOBODY}",
 # ---- TOP ----
 "P0": f"{STYLE} {POS} New camera position: up on the steel catwalk that runs along the tops of the tanks, close, looking along "
       f"it: the domed steel top of a tank fills the lower middle of the frame, with white fog spilling from a small vent on it and "
       f"falling over its edge; the thick silver insulated hose comes along the catwalk to a nozzle resting beside the tank's fill "
       f"port; on the catwalk railing in the foreground stand a steel coffee thermos and a small cup of steaming coffee. {NOWATER} "
       f"{NOBODY}",
 "P1": f"{STYLE} {LOCKZ} Change only this: {WORKER} now stands on the catwalk holding the hose's nozzle in the tank's fill port. "
       f"The thermos and the steaming cup stay on the railing in the foreground. {KEEP} {NOWATER} This worker is the only person.",
 # ---- INSIDE ----
 "I0": f"{STYLE} {POS} New camera position: right in front of the front tank that is sliced open, close and level with its "
       f"middle, looking straight into the cut: inside the thick double steel wall, clear liquid nitrogen fills the tank almost to "
       f"the top under rolling white fog, and four long white sealed pods stand upside down in it, their rounded head ends at the "
       f"bottom of the tank and their flat foot ends near the top, around a middle column of small white canisters stacked one "
       f"above the other. The pods, the column and the cut wall fill the frame. {NITRO} {NOWATER} {NOBODY}",
 "I1": f"{STYLE} {LOCKZ} Change only this: the liquid nitrogen level has dropped to halfway down the tank: the upper halves of "
       f"the four pods and of the middle column now stand frosted in white fog above the liquid, while their lower halves, with "
       f"the rounded head ends, stay deep in the clear liquid. {KEEP} {NOWATER} {NOBODY}",
 "I2": f"{STYLE} {POS} New camera position: lower and closer than the reference, inside the cut, level with the bottom of the "
       f"tank: the rounded head end of one white pod fills the middle of the frame, deep in the clear liquid nitrogen, with the "
       f"surface of the liquid and the fog high above it at the top of the frame. {NITRO} {NOCHANGE} {NOWATER} {NOBODY}",
 "I3": f"{STYLE} {POS} New camera position: close on the middle column inside the cut tank, between the pods: the stack of small "
       f"white canisters, one above the other, fills the middle of the frame from top to bottom, the lower ones under the clear "
       f"liquid nitrogen and the upper ones in the fog, with a white pod on either side. {NITRO} {NOCHANGE} {NOWATER} {NOBODY}",
 # ---- ROW ----
 "R0": f"{STYLE} {POS} New camera position: inside the storage hall at the height of a person, beside the front tanks, looking "
       f"straight down the row of tall brushed stainless-steel tanks toward the back wall: the tanks line up one behind another, "
       f"and at the far end of the row stands the oldest tank, duller than the rest and crusted with thick white frost. {FLOORS} "
       f"{NOWATER} {NOBODY}",
}
# Matched to the style key (W0, 5e848ad3): a three-quarter view from the front left; the front-left tank has a big see-through
# window in its front instead of a removed half; the hoist's hook hangs over the middle tank; the oldest, frosted tank stands at
# the right end of the line; the catwalk runs along the back wall above the tanks. These replace the first drafts above.
PODC = POD[0].upper() + POD[1:]
P.update({
 "H0": f"{STYLE} {POS} New camera position: high up on the steel catwalk at the back of the storage hall, beside the middle tank "
       f"under the hoist's hook, looking steeply down at the tank's top. The tank's round lid is open, and thick white fog rises out "
       f"of its round mouth from the liquid nitrogen inside. {PODC}, frosted white, hangs from the hoist's cable with its rounded end "
       f"pointing down, just above the fog. The tank's mouth and the hanging pod fill the middle of the frame, with the catwalk "
       f"railing along the lower edge. {NITRO} {NOWATER} {NOBODY}",
 "L0": f"{STYLE} {POS} New camera position: inside the storage hall, low and close to the front-left tank, at the edge of the big "
       f"see-through window in its front: along the window's edge the tank's thick double steel wall shows in cross-section, an "
       f"inner steel skin and an outer steel skin with a narrow empty gap between them, running from the top of the frame down to "
       f"the tank's base standing on the grey floor; through the window, the pale liquid nitrogen and the white pods show inside. "
       f"The cool white ceiling lights of the hall are on. {NITRO} {FLOORS} {NOBODY}",
 "L0b": f"{STYLE} {POS} New camera position: lower and closer than the reference, right at the foot of the front-left tank: the "
        f"tank's round steel base standing on the smooth grey floor fills the frame, with the tank's wall rising out of the top of "
        f"the frame; nothing is attached to the base: no cable, no plug, no wire and no pipe. {FLOORS} {NOWATER} {NOBODY}",
 "P0": f"{STYLE} {POS} New camera position: up on the steel catwalk at the back of the storage hall, above the tanks, close, "
       f"looking down along it: the domed steel top of the middle tank fills the lower middle of the frame, with white fog spilling "
       f"from a small vent on it and falling over its edge; the thick silver insulated hose comes along the catwalk to a nozzle "
       f"resting beside the tank's fill port; on the catwalk railing in the foreground stand a steel coffee thermos and a small cup "
       f"of steaming coffee. {NOWATER} {NOBODY}",
 "I0": f"{STYLE} {POS} New camera position: right in front of the front-left tank, close and level with its middle, looking "
       f"straight in through the big see-through window in its front, which fills the frame: inside, pale liquid nitrogen fills the "
       f"tank almost to the top under rolling white fog, and four long white sealed pods stand upside down in it, each as long as a "
       f"person, their rounded head ends at the bottom of the tank and their flat foot ends up near the surface, around a middle "
       f"column of small white canisters stacked one above the other. {NITRO} {NOWATER} {NOBODY}",
 "I2": f"{STYLE} {POS} New camera position: lower and closer than the reference, at the bottom of the window: the rounded head end "
       f"of one white pod fills the middle of the frame, deep in the pale liquid nitrogen, with the surface of the liquid and the "
       f"fog high above it at the top of the frame. {NITRO} {NOCHANGE} {NOWATER} {NOBODY}",
 "I3": f"{STYLE} {POS} New camera position: close on the middle column, through the window, between the pods: the stack of small "
       f"white canisters, one above the other, fills the middle of the frame from top to bottom, the lower ones under the liquid "
       f"nitrogen and the upper ones in the fog, with a white pod on either side. {NITRO} {NOCHANGE} {NOWATER} {NOBODY}",
 "R0": f"{STYLE} {POS} New camera position: inside the storage hall at the height of a person, in front of the front-left tank, "
       f"looking along the line of tall stainless-steel tanks to the right: the tanks stand one after another, and at the end of "
       f"the line stands the oldest tank, duller than the rest and crusted with thick white frost, large in the right half of the "
       f"frame. {FLOORS} {NOWATER} {NOBODY}",
})
# Redos after round 2 (16 Nov 2026). First tries, for the record:
#  T0A (9f88bd07): a medium shot of the tray standing in the tank hall, not an extreme close-up in the cooling room.
#  B0A (cac6bbbe): the cooling room lost its ceiling (open sky above) and the tanks showed behind the table.
#  I0A (9c14ef0e): four short capsules in two rows, not four long pods standing upside down.
#  L0A (4166baa4): a straight-on view of the window; the double wall did not show in cross-section.
#  P0A (e50e3d32): the thermos and cup were tiny in a corner, and the hall was open to the sky.
#  R0A (19394743): a three-quarter view of the front tank; the frosted oldest tank was a sliver at the edge.
# The cooling-room positions are now edits of D0 (the same room seen close), P0 of H0 (the same catwalk and tank).
P.update({
 "T0": f"{STYLE} {POS} New camera position: in the same cooling room, right at the white counter along its back wall, very low "
       f"and very close. Extreme close-up: a small steel lab tray on the counter fills the whole lower two-thirds of the frame, so "
       f"close that the strawberry looks as big as a fist. On the tray, from left to right: a small clear glass vial of water "
       f"standing in a little rack; one frosty red strawberry on a small white dish; a small clear vial of pale-blue liquid; and a "
       f"small open steel flask. Behind the tray only the white wall of the room shows, softly blurred; no tanks and no gurney are "
       f"in view. Nothing is cut open and there is no soil. {NOBODY}",
 "B0": f"{STYLE} {POS} New camera position: in the same cooling room, at the height of the steel operating table in the middle of "
       f"the room, close, looking at it from the front. The white pod from the gurney now lies along the table, exactly the same "
       f"pod; two clear tubes run from the small white pump cart into the side of the pod, and the tubes are filled with dark red "
       f"liquid; above the table the steel drip stand holds two clear bags of pale-blue liquid. The table and the pod fill the "
       f"middle of the frame. The room's white walls and ceiling close it in: no sky, no tanks and no gurney in view. {FLOORS} "
       f"{NOWATER} {NOBODY}",
 "I0": f"{STYLE} {POS} New camera position: right in front of the front-left tank, close and level with its middle, looking "
       f"straight in through the big see-through window in its front, which fills the frame from top to bottom. Inside, pale liquid "
       f"nitrogen fills the tank almost to the top under rolling white fog. Four long white cocoon pods, exactly like the pod hanging "
       f"in the second reference image, stand in the liquid around a middle column of small white canisters stacked one above the "
       f"other, two on each side of the column, one a little behind the other. Each pod is as long as a person and runs from just "
       f"under the surface all the way down to the bottom of the tank, and each stands upside down: its wider, rounded head end at "
       f"the bottom of the tank and its narrower foot end at the top. {NITRO} {NOWATER} {NOBODY}",
 "R0": f"{STYLE} {POS} New camera position: inside the storage hall, close to the right end of the line of tanks: the oldest "
       f"tank, duller than the others and crusted all over with thick white frost, fills the middle of the frame from top to "
       f"bottom, with the shiny steel tanks beside it on the left. {FLOORS} {NOWATER} {NOBODY}",
 "P0": f"{STYLE} {POS} New camera position: on the same steel catwalk, a little further back and lower, looking at the top of the "
       f"same middle tank: its round lid is now closed, white fog spills from a small vent on the lid and falls over the tank's "
       f"edge, and the hoist's hook hangs empty above. The thick silver insulated hose comes along the catwalk to a nozzle resting "
       f"beside the tank's fill port. In the near foreground, large in the lower left of the frame, a steel coffee thermos and a "
       f"small cup of steaming coffee stand on the catwalk railing. {NOWATER} {NOBODY}",
})
REFS_REDO = {"T0": ["D0"], "B0": ["D0"], "I0": ["W0", "H0"], "R0": ["W0"], "P0": ["H0"]}
# Round 4 (17 Nov 2026). I0B (6055cd4d) kept the tank and window but again drew four short capsules in two rows, so I0 is now
# an edit of I0B that swaps the capsules for long pods. WbA (3e82afae) put a sandy pit in front of the block.
P.update({
 "I0": f"{STYLE} {LOCKZ} Change only this: the four short white capsules inside the tank are gone. In their place stand four "
       f"long white cocoon pods, like the pod hanging in the second reference image, two on each side of the middle column of "
       f"small canisters, one a little behind the other. Each pod runs the full height of the liquid, from just under the surface "
       f"all the way down to the bottom of the tank, and stands upside down: its wider, rounded head end at the bottom and its "
       f"narrower foot end at the top. The middle column of canisters stays exactly as it is. {KEEP} {NITRO} {NOWATER} {NOBODY}",
 "Wb": f"{STYLE} {WIDE} {POS} New camera position: a little lower and a little to the right of the reference, still in front of "
       f"the building and looking at it, so the storage hall is a little larger and nearer and the building is seen slightly from "
       f"the right; the whole building is still in view in the upper 60% of the frame. The block of ground is deep: below the "
       f"gravel its front is cut straight down all the way to the bottom edge of the frame, so the whole lower part of the frame is "
       f"the cut face of the ground, deep, even layers of brown and tan soil; there is no ground, no pit and no sand in front of "
       f"the block. {NITRO} {NOCHANGE} {NOBODY}",
})
REFS_REDO.update({"I0": ["I0B", "H0"]})
# References per still (keys of 10-jobs.tsv). The first reference is the picture being edited.
REFS = {"W0": [], "Wb": ["W0"], "D0": ["W0"], "D0f": ["D0"], "D1": ["D0f"], "T0": ["W0"], "T1": ["T0"], "T2": ["T1"],
        "T3": ["T2"], "T3w": ["T3"], "T4": ["T3w"], "B0": ["W0"], "B1": ["B0"], "H0": ["W0"], "H1": ["H0"], "L0": ["W0"],
        "L1": ["L0"], "L0b": ["L0"], "P0": ["W0"], "P1": ["P0"], "I0": ["W0"], "I1": ["I0"], "I2": ["I1"], "I3": ["I1"],
        "R0": ["W0"]}
REFS.update(REFS_REDO)
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
