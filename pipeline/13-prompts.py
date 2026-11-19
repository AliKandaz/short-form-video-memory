# Video 13 (V2, "Why Firefighters Drop Frozen Turkeys Into Fryers"): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 13-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE, WIDE and LOCKZ are byte-identical to 12-prompts.py (STYLE is the Cutaway default without "translucent cyan water": the
# only water on this set is in the pot during the water test, R0 and R1). SET carries the place and its colours; HOUSE and FRYER
# list the objects once, for W0 (ST0 repeats the fryer's parts for the close-ups). Every other still is an edit of the one(s)
# named in REFS: LOCK or LOCKZ keeps the framing for a change at one position; POS moves the camera to a new position on the same
# set. LAWNZ (close views at the fryer) and INDOOR (the kitchen and the living room) stop the STYLE line's cut ground from leaking
# into close-ups (7.1). The pot's own cut-open front is intended: it is how the oil, the ice and the steam show.
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, tidy and "
"uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a suburban back yard on a cool, bright late-November afternoon, shown as a cutaway model: a lawn of green-brown grass "
"with a few fallen orange leaves; at the back, a wooden deck with three wide steps down to the lawn, built against the back of a "
"one-storey house with pale grey siding and a dark grey roof; a bare maple tree at one side and a plain wooden fence along the "
"back. The yard stands on a deep block of ground cut straight down like a slice of cake toward the camera, so the cut face shows "
"dark topsoil over even layers of brown earth")
CAMERA = ("Camera: from the front, slightly raised, looking over the cut face and across the lawn toward the back of the house, "
"which faces the camera. The roof, the house and the deck fill the top third of the frame; the turkey fryer stands on the lawn "
"about 45% down from the top, a little right of centre, far out from the deck; the front edge of the lawn runs across the frame "
"about 58% down. Below that the block of ground is cut straight down all the way to the bottom edge of the frame: deep, even "
"layers of dark topsoil and brown earth with nothing in them. There is no ground in front of the block")
HOUSE = ("The back wall of the house is cut away like a dollhouse, so two rooms show behind the deck, warmly lit: on the left a "
"kitchen with a white fridge, a white stove with steaming pots on it, an oven and a counter; on the right a living room with a "
"grey sofa and a flat black TV on the wall. An empty folding lawn chair stands on the deck")
FRYER = ("The fryer: a tall stainless-steel stockpot standing on a low three-legged black steel stand over a round cast-iron "
"burner; the front half of the pot is cut away like a slice of cake, so the golden-yellow cooking oil inside shows as if through "
"glass; a long steel lifting hook rises out of the top of the pot, holding a whole turkey on a vertical steel rack; a white "
"propane tank with no lettering stands on the grass beside the stand, joined to the burner by a black rubber hose")
OIL = "The pot holds golden-yellow cooking oil, not water. There is no water anywhere."
OILDROPS = ("The pot holds golden-yellow cooking oil, not water; the only water is a few clear drops falling from the turkey.")
WATER = "The pot holds clear water instead of oil."
LAWNZ = ("This is a close view at the fryer on the lawn: only the pot is cut open; the grass under the stand is whole, and there "
"is no soil, no cut face of ground and nothing buried anywhere in the frame.")
INDOOR = ("This is an indoor close-up: nothing is cut open, and there is no soil, no ground, no pit and nothing buried anywhere in "
"the frame.")
DECKZ = ("This is a close view on the deck: only the back wall of the house is cut away; the deck and the lawn are whole, and "
"there is no pit, no hole, no soil and no cut face of ground anywhere in the frame.")
POS = "The same back yard, set and light as the reference image, with the same parts, colours and materials."
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"house, the deck, the lawn, the fryer and the cut face of the ground stay exactly where they are and the same size.")
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: "
"everything in view stays exactly where it is and the same size.")
KEEP = "Everything else identical."
NOPEOPLE = "No people."
FROZEN = ("its skin frosted white with ice crystals and chunks of clear ice packed in its open cavity")
THAWED = "a whole thawed turkey with plain pale golden-pink skin, no frost and no ice"

P = {
 # ---- WIDE (the set key) ----
 "W0": f"{STYLE} {WIDE} Scene: {SET}. {CAMERA}. {HOUSE}. Out on the lawn stands a propane turkey fryer. {FRYER}. The turkey is "
       f"down in the oil and a thin wisp of steam rises from the pot; a ring of small blue flames burns under it. {OIL} {NOPEOPLE}",
 # ---- POT (frame 0, the boil-over, the slow lowering, the last frame) ----
 "ST0": f"{STYLE} {POS} New camera position: close in front of the fryer, at the height of the top of the pot, looking straight "
        f"at its cut-open front. The whole fryer fills the frame from top to bottom. At the top, a whole frozen turkey, {FROZEN}, "
        f"hangs from the long steel lifting hook inside the top of the pot, just an inch above the oil, filling the upper third of "
        f"the frame. In the middle, the cut-open stainless-steel pot shows calm, shimmering golden-yellow oil filling its lower "
        f"two-thirds, as if through glass. At the bottom, under the pot, the round burner glows with a ring of blue flames between "
        f"the legs of the black stand. The white propane tank stands softly blurred at one side; the lawn and the back of the "
        f"house are softly blurred behind. {LAWNZ} {OIL} {NOPEOPLE}",
 "ST1": f"{STYLE} {LOCKZ} Change only this: the turkey has dropped down into the oil, and the oil is boiling over violently: a "
        f"churning mass of pale foam and bubbles surges up through the pot and spills over the rim, golden oil runs down the "
        f"outside of the pot, and the first orange flames lick up from the burner around the base of the pot. {KEEP} {NOPEOPLE}",
 "PT2": f"{STYLE} {LOCKZ} Change only this: the turkey is now {THAWED}; it hangs on the same hook, already half lowered into the "
        f"calm golden-yellow oil, which stays well below the rim of the pot, with a few small bubbles round the bird; the burner "
        f"under the pot is off, with no flames at all. {KEEP} {NOPEOPLE}",
 # ---- HIGH ----
 "H0": f"{STYLE} {POS} New camera position: high above the lawn near the front edge of the block, looking down at about 50 "
       f"degrees toward the house. The turkey fryer stands on the lawn in the lower middle of the frame, its cut-open pot of "
       f"golden-yellow oil with the turkey down in it and a thin wisp of steam rising; a long stretch of empty lawn with a few "
       f"fallen leaves runs between the fryer and the deck; the deck, its empty lawn chair and the cut-open back of the house are "
       f"small at the top of the frame. {OIL} {NOPEOPLE}",
 "H1": f"{STYLE} {LOCK} Change only this: a huge rolling ball of bright orange fire bursts up out of the fryer's pot and engulfs "
       f"the whole fryer, with thick black smoke billowing above it. {KEEP} {NOPEOPLE}",
 # ---- INSIDE (through the pot's cut-open front, below the oil) ----
 "IN0": f"{STYLE} {POS} New camera position: right at the cut-open front of the pot, below the surface of the oil, looking into "
        f"it as into an aquarium. Extreme close-up: the turkey, now down in the oil, fills most of the frame: its skin is frosted "
        f"white with ice crystals, and chunks of clear ice glint in its open cavity; a few clear round drops of water fall from the "
        f"cavity down through the golden-yellow oil; thin streams of tiny bubbles rise from the ice. The steel wall at the back of "
        f"the pot is softly lit. {LAWNZ} {OILDROPS} {NOPEOPLE}",
 "IN1": f"{STYLE} {POS} New camera position: lower than the reference, down at the bottom of the pot, still looking in through "
        f"its cut-open front below the oil. The steel bottom of the pot runs across the lower part of the frame, with the burner's "
        f"blue flames glowing beneath it; big round bubbles of steam swell off the bottom and burst upward through the "
        f"golden-yellow oil, which churns and surges up toward the top of the frame; the lower part of the frosted turkey shows at "
        f"the top of the frame. {LAWNZ} The pot holds golden-yellow cooking oil, not water. {NOPEOPLE}",
 # ---- BURNER ----
 "BU0": f"{STYLE} {POS} New camera position: low beside the fryer, at the height of the burner, looking at the bottom of the pot "
        f"from the front-left: the round cast-iron burner fills the middle of the frame under the steel bottom of the pot, between "
        f"the legs of the black stand; golden oil streams down the outside of the pot onto the burner's flames, and bright orange "
        f"fire flares up the side of the pot; the black hose runs off to the white propane tank at one side. {LAWNZ} {OIL} "
        f"{NOPEOPLE}",
 # BU1 try A (16c2e6fb) zoomed out and dug a pit with soil and an odd object into the grass under the stand (STYLE leak):
 # try B adds LAWNZ and names the parts that must stay the same size.
 "BU1": f"{STYLE} {LOCKZ} The pot, the black stand, the burner and the white propane tank stay exactly the same size and in the "
        f"same place as in that image. Change only this: there is no orange fire anywhere; only a calm ring of small blue flames "
        f"burns under the pot; a few thin drips of golden oil run down the outside of the pot toward the flames, not yet reaching "
        f"them. {KEEP} {LAWNZ} {NOPEOPLE}",
 # ---- RIM (the water test) ----
 "R0": f"{STYLE} {POS} New camera position: lower than the reference and a little to the left, level with the rim of the pot, "
       f"close: the rim runs across the upper part of the frame and the cut-open front shows the inside. The burner under the pot "
       f"is off, with no flames. The pot is now filled with clear water instead of oil, up to about two inches below the brim, and "
       f"{THAWED} sits on its rack completely under the water, with the steel lifting hook rising out of the water above it. "
       f"{LAWNZ} {WATER} {NOPEOPLE}",
 "R1": f"{STYLE} {LOCKZ} Change only this: the turkey has been lifted out on its hook and hangs just above the rim of the pot, "
       f"dripping water; the water in the pot is now a few inches lower than before; a strip of bright blue tape runs along the "
       f"inside wall of the pot exactly at the new waterline. {KEEP} {NOPEOPLE}",
 # ---- KITCHEN ----
 "K0": f"{STYLE} {POS} New camera position: inside the cut-open kitchen of the house, close, looking into the open white fridge. "
       f"A whole frozen turkey, {FROZEN}, lies on a white tray on the middle shelf and fills the middle of the frame; the fridge's "
       f"light glows; the other shelves hold a few plain glass jars and vegetables with no labels. {INDOOR} {NOPEOPLE}",
 "K1": f"{STYLE} {LOCKZ} Change only this: the turkey is now {THAWED}, patted dry, with a few crumpled white paper towels on the "
       f"tray beside it. {KEEP} {NOPEOPLE}",
 # ---- DECK ----
 # D0 try A (1e51b896) dug a pit with soil walls into the lawn and added a second deck in front (the STYLE line's cut ground
 # leaking in, 7.1): try B (e40b78e1) moved the camera onto the deck at head height with DECKZ, but left a strip of lawn between
 # the deck and the house (the line says the deck is attached): try C joins them in so many words.
 "D0": f"{STYLE} {POS} New camera position: standing on the wooden deck near its front steps, at the height of a person's head, "
       f"close, looking straight at the back of the house: the deck's warm brown boards run from the bottom of the frame right up "
       f"to the back wall of the house and are joined to it, with no grass and no gap between the deck and the house; the empty "
       f"folding lawn chair stands on the deck a little left of centre, near the house; the cut-open back of the house fills the "
       f"upper half, showing the warmly lit kitchen with its white fridge and the living room with its sofa and TV, their floors "
       f"level with the deck. There is no fryer on the deck. {DECKZ} {NOPEOPLE}",
 # ---- TV ----
 "TV0": f"{STYLE} {POS} New camera position: inside the cut-open living room of the house, close, facing the flat black TV on "
        f"the wall, which fills most of the frame. On its screen: a turkey fryer standing alone in an empty parking lot erupts in "
        f"a huge orange fireball; a red fire engine with no lettering is parked well behind it, and two tiny firefighters in tan "
        f"gear stand well back, watching. There is no text, no ticker and no logo on the screen or anywhere else. {INDOOR} No "
        f"people in the room; the only figures are the two tiny firefighters on the TV screen.",
}

REFS = {"W0": [], "ST0": ["W0"], "ST1": ["ST0"], "PT2": ["ST0"], "H0": ["W0"], "H1": ["H0"], "IN0": ["ST0"], "IN1": ["IN0"],
        "BU0": ["ST1"], "BU1": ["BU0"], "R0": ["PT2"], "R1": ["R0"], "K0": ["W0"], "K1": ["K0"], "D0": ["W0"], "TV0": ["W0"]}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
