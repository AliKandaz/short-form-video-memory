# Video 06 (idea #9 Petra, "How a Crack in a Cliff Becomes the Hidden City of Petra", Classic look, one build in one main view):
# still prompts for seedream_v5_pro 1k 9:16. Usage: python3 06-prompts.py KEY -> prints the prompt as a JSON string.
# References per still are in REFS (keys of 06-jobs.tsv; MASCOT is the locked reference job from 3.4). Every ladder still edits the
# one before it with the framing lock (LOCK, 3.4g) so the cliff, the canyon and the plaza never move.
# STYLE = the base string of 02-prompts.py with its palette line swapped for one that names colours only (3.4f, 3.4g).
# Petra and the Treasury are never named in a prompt, so the model does not draw the finished facade early.
STYLE = ("Stylized 3D CG render with a real-time game-engine look: semi-realistic PBR textures on simple low-to-mid-poly models, "
"soft natural sunlight, soft contact shadows, gentle ambient occlusion, mild depth of field. Small diorama-like outdoor set seen from "
"a slightly elevated three-quarter angle. Sunny desert palette: rose-red, salmon-pink and cream sandstone in soft horizontal bands, "
"pale golden sand, warm ochre and terracotta, soft violet shadows, bright blue sky. Clean readable shapes, uncluttered composition, "
"subject in the centre third of a vertical 9:16 frame. Not photorealistic, not cartoon cel-shaded. No text, no letters, no "
"captions, no logos, no watermark, no UI.")
MASCOT = ("a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, brown work boots, short dark beard, "
"simple friendly face, game-character proportions")
SET = ("a sunny desert canyon diorama: a small flat plaza of pale golden sand enclosed by towering rose-red sandstone cliffs with soft "
"horizontal rock bands. Behind the plaza rises one tall, flat, sheer cliff face that faces the camera. On the left side, a very "
"narrow winding slot canyon, only a few metres wide between towering smooth curved rock walls, runs back into the mountain and "
"opens onto the plaza. The front edge of the diorama is cut straight down like a slice of cake, so the bottom of the frame shows a "
"cross-section of the solid rock under the plaza, with soft horizontal bands of red, pink and cream. A strip of bright blue sky "
"with a few small white clouds across the top")
CAMERA = ("Camera: slightly elevated three-quarter view looking at the tall flat cliff face; the cliff face fills the upper middle "
"of the frame, the sandy plaza fills the lower middle, the mouth of the slot canyon is on the left, and the cut cross-section of "
"rock runs along the bottom edge of the frame")
FACADE = ("a grand two-storey facade carved straight out of the cliff in the same rose-red rock: a lower storey with six tall "
"columns, a triangular pediment and a dark doorway in the middle, and an upper storey with a round central kiosk topped by a stone "
"urn, flanked by two half-pediments and more columns, all with sharp crisp edges")
OUTLINE = ("a lower storey with six tall columns, a triangular pediment and a doorway in the middle, and an upper storey with a round "
"central kiosk topped by an urn, flanked by two half-pediments and more columns")
EXPLORER = ("a thin bearded European man in plain white and brown Arab robes and a white headscarf, leading a small brown goat on a "
"rope, with a local guide in a dark robe and headscarf beside him")
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the cliff "
"face, the slot canyon, the plaza and the cut cross-section of rock stay exactly where they are and the same size.")
SAME = "Same scene, same camera angle and framing as the reference image."
KEEP = "Everything else identical."

P = {
 # ---- the main view (stage ladder) ----
 "S0": f"{STYLE} Scene: {SET}. {CAMERA}. The tall cliff face is completely blank: smooth, flat, uncarved rock with no openings. "
       f"{MASCOT}, the same man as in the reference image, has just stepped out of the mouth of the slot canyon into the plaza, holding "
       f"an empty round clay water jar under one arm and squinting up at the blazing sun. The sand is dry and dusty. He is small next "
       f"to the towering cliff, about a tenth of its height.",
 "S1": f"{STYLE} {LOCK} Change only this: a narrow water channel is now carved along the foot of the slot canyon's left wall, running "
       f"out of the canyon and along the edge of the plaza; a line of short round terracotta clay pipes lies in the channel, and clear "
       f"water pours from the end of the pipe into a small square stone basin at the side of the plaza. The man in the yellow hard hat "
       f"kneels beside the basin, filling his clay jar with water, smiling. The cliff face is still blank. {KEEP}",
 "STORM": f"{STYLE} {LOCK} Change only this: a sudden desert storm. The sky across the top of the frame is dark grey with low, heavy "
          f"storm clouds; grey sheets of rain pour down; thin muddy waterfalls stream down the cliff faces, and a shallow brown flood "
          f"rushes across the plaza toward the slot canyon. The man in the yellow hard hat stands in the rain holding his clay jar over "
          f"his head. No lightning, no fire, no smoke. {KEEP}",
 "S2": f"{STYLE} {LOCK} Change only this: it is sunny again under a clear blue sky, and the plaza is dry. The cut cross-section of rock "
       f"along the bottom of the frame now shows a big square tank carved into the rock under the plaza, filled to the brim with clear "
       f"blue water, fed by a short channel from the plaza. The man in the yellow hard hat stands in the middle of the plaza looking up "
       f"at the blank cliff face, holding a rolled-up paper plan in one hand. {KEEP}",
 "S3": f"{STYLE} {LOCK} Change only this: the outline of a grand two-storey temple facade is drawn onto the blank cliff face in "
       f"thin pale chalk lines only: {OUTLINE}. The rock itself is still completely flat and uncarved; only the chalk lines show. At "
       f"the very top of the outline, a small flat ledge has been cut into the cliff, and the man in the yellow hard hat stands on it "
       f"with a hammer and chisel, starting to carve. {KEEP}",
 # redo: S3 showed the man twice (on the ledge and still standing in the plaza); edit the extra one out (3.4f "edit it out")
 "S3b": f"{STYLE} {SAME} Change only this: remove the man standing in the plaza at the foot of the cliff, so that spot is just empty "
        f"sand; the only person in the whole scene is the man on the ledge at the very top of the cliff with the hammer and chisel. {KEEP}",
 "BOTTOMUP": f"{STYLE} {LOCK} Change only this: only the bottom of the cliff face has been carved, into the lower parts of six "
             f"half-finished columns; everything above them is rough, uncut rock with the pale outline lines. The man in the yellow "
             f"hard hat stands at the foot of the cliff with a hammer and chisel and ducks, one arm over his hard hat, as big chunks of "
             f"loose rock fall from high above; one chunk has just smashed a half-carved column into pieces in a puff of dust. The ledge at the top of the cliff is empty: "
             f"the only person in the whole scene is the man at the foot of the cliff. {KEEP}",
 "S5": f"{STYLE} {LOCK} Change only this: the top half of the facade is now carved out of the cliff in crisp detail: the upper storey "
       f"with its round central kiosk topped by a stone urn, two half-pediments and columns, all in the same rose-red rock. Below it, "
       f"the lower half of the cliff is still rough, uncut rock with the pale outline lines, cut into a few wide steps like a giant "
       f"staircase, and the man in the yellow hard hat stands on the highest uncut step, chiselling downward. A small pile of broken "
       f"rock lies at the foot of the cliff. The only person in the whole scene is the man on that step. {KEEP}",
 "S6": f"{STYLE} {LOCK} Change only this: the whole facade is finished: {FACADE}, carved from top to bottom. The rough steps and the "
       f"outline lines are gone and the plaza is swept clean. The man in the yellow hard hat stands in the plaza at the foot of the "
       f"facade, looking up at it proudly with his hands on his hips; he is the only person in the whole scene. {KEEP}",
 "INSIDE": f"{STYLE} {LOCK} Change only this: the rock to the right of the facade is cut away like a cross-section, so we can see "
           f"straight into what lies behind the doorway: one plain square room carved into the rock, with bare smooth walls, a flat "
           f"ceiling and an empty floor, and two small plain side rooms opening off it. No decoration, no furniture, no treasure, "
           f"completely empty. Sunlight falls through the doorway onto the floor. The man in the yellow hard hat stands inside the big "
           f"room, shrugging; he is the only person in the whole scene. {KEEP}",
 "BROKE": f"{STYLE} {LOCK} Change only this: the man in the yellow hard hat stands in the plaza in front of the facade with the "
          f"pockets of his overalls pulled inside out, shrugging, next to an open wooden chest that is completely empty. {KEEP}",
 "S7": f"{STYLE} {LOCK} Change only this: the plaza is now a busy little trading town. A line of camels loaded with bulging cloth "
       f"sacks walks out of the slot canyon into the plaza. The man in the yellow hard hat sits at a small wooden toll table piled with "
       f"gold coins, holding out his hand; he is the only person in the scene. Along the right side of the plaza stand a few small flat-roofed houses and a small temple "
       f"with four columns, all built from stacked square stone blocks. The carved facade in the cliff is unchanged. {KEEP}",
 "S8": f"{STYLE} {LOCK} Change only this: just after an earthquake. The small houses and the little temple on the right side of the "
       f"plaza have collapsed into heaps of broken stone blocks and toppled columns; a haze of dust hangs in the air; a few cracks run "
       f"across the plaza; the camels are gone and the toll table lies on its side with coins scattered. The carved facade in the cliff "
       f"is completely untouched and intact. The man in the yellow hard hat sits up in the rubble, dusty, looking up at the facade in "
       f"relief; he is the only person in the whole scene. {KEEP}",
 "S9": f"{STYLE} {LOCK} Change only this: centuries later, the town is empty and quiet. Golden sand has drifted over the heaps of "
       f"rubble, a few small dry desert shrubs grow between the stones, and there are no people, no camels, no table and no coins. The "
       f"carved facade in the cliff still stands intact, its edges only slightly softened by weather. Warm late-afternoon light with "
       f"long soft shadows. {KEEP}",
 "EXPLORER": f"{STYLE} {LOCK} Change only this: {EXPLORER} have just walked out of the mouth of the slot canyon into the empty plaza; "
             f"the man in robes stops and stares up at the carved facade in awe while the guide points at it. {KEEP}",
 "END": f"{STYLE} {LOCK} Change only this: warm golden sunlight bathes the finished facade and the clean, empty plaza, and the water "
        f"in the basin glitters. The man in the yellow hard hat stands in the middle of the plaza facing the camera, waving with one "
        f"arm raised high, smiling; he is the only person in the whole scene. {KEEP}",
 # ---- one close-up of the build (B21-B23), made from the main view so it matches ----
 "URN": f"{STYLE} Extreme close-up of the top of the same carved facade as in the reference image: the round stone urn on top of the "
        f"central kiosk fills most of the frame, carved from the same rose-red banded rock as the cliff, smooth and unbroken, with the "
        f"tops of the columns below it and a strip of blue sky behind. Warm late-afternoon light. No people.",
 "URNHOLES": f"{STYLE} {SAME} Change only this: the surface of the stone urn is now pitted all over with dozens of small round "
             f"chipped holes, like old bullet marks, each showing paler rock inside. {KEEP}",
 "URNSLICE": f"{STYLE} {SAME} Change only this: the urn is cut clean in half from top to bottom like a cake and its front half is "
             f"gone, showing that inside it is solid rose-red rock all the way through, with the same horizontal bands: no hollow "
             f"space, no gold. {KEEP}",
}
REFS = {
 "S0": ["MASCOT"], "S1": ["S0", "MASCOT"], "STORM": ["S1", "MASCOT"], "S2": ["S1", "MASCOT"], "S3": ["S2", "MASCOT"],
 "S3b": ["S3"], "BOTTOMUP": ["S3b", "MASCOT"], "S5": ["S3b", "MASCOT"], "S6": ["S5", "MASCOT"], "INSIDE": ["S6", "MASCOT"], "BROKE": ["S6", "MASCOT"],
 "S7": ["S6", "MASCOT"], "S8": ["S7", "MASCOT"], "S9": ["S8"], "EXPLORER": ["S9"], "END": ["S6", "MASCOT"], "URN": ["S9"],
 "URNHOLES": ["URN"], "URNSLICE": ["URNHOLES"],
}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
