# Video 07 (P4, "1959 Car vs 2009 Car: Only One Driver Walks Away", the first "Who wins?" matchup, Classic look, one arena in one
# main view): still prompts for seedream_v5_pro 1k 9:16. Usage: python3 07-prompts.py KEY -> prints the prompt as a JSON string.
# References per still are in REFS (keys of 07-jobs.tsv; MASCOT is the locked reference job from 3.4). Every ladder still edits the
# one before it with the framing lock (LOCK, 3.4g) so the pad never moves and the cars stay the same size.
# STYLE = the base string of 02-prompts.py with its camera phrase changed to the steep view tested on S0 and its palette line swapped
# for one that names colours only (3.4f, 3.4g). No car makes, model names, badges or plates in any prompt.
STYLE = ("Stylized 3D CG render with a real-time game-engine look: semi-realistic PBR textures on simple low-to-mid-poly models, "
"soft natural sunlight, soft contact shadows, gentle ambient occlusion, mild depth of field. Small diorama-like outdoor set seen from "
"high above at a steep angle. Sunny palette: light-grey concrete, crisp white and warm yellow paint, fresh green grass, pastel "
"turquoise and cream, glossy cherry red, bright chrome, soft cool shadows. Clean readable shapes, uncluttered composition, subject in "
"the centre third of a vertical 9:16 frame. Not photorealistic and not a photograph, not cartoon cel-shaded: clean, slightly toy-like "
"models with smooth simplified surfaces, like a polished video-game diorama. No text, no letters, no captions, no logos, no watermark, "
"no UI.")
MASCOT = ("a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, brown work boots, short dark beard, "
"simple friendly face, game-character proportions")
SET = ("a small sunny diorama: a square block of ground whose flat top is paved as a crash-test pad of smooth light-grey concrete "
"with straight white lane lines and yellow-and-black hazard stripes along its edges, with a thin border of bright green grass and two "
"small slim camera poles with floodlights at its far corners. The front edge of the block is cut straight down like a slice of cake, "
"so a strip along the bottom of the frame shows its cross-section: a layer of grey concrete over soft bands of brown and tan soil")
CAMERA = ("Camera: high above the diorama looking steeply down at it, tilted just enough to see the cut front edge of the block "
"along the bottom of the frame. The two cars are lined up head-on along the vertical centre line of the frame: one in the bottom half "
"pointing up, the other in the top half pointing down, nose to nose")
OLD = ("a 1959 American full-size four-door sedan, long, low and wide; seen from above, its back end spreads into two wide, flat, "
"wing-like tail fins that stick out past the sides of the car, with small cat's-eye tail lights under them; it has a wide chrome grille, chrome bumpers and chrome trim, painted pastel "
"turquoise with a cream upper body, with no badges, no emblems, no hood ornament and no license plates")
TOY = ("Both cars look like chunky, simplified toy models with soft rounded edges and clean smooth paint, like collectible toys, not "
"real cars.")
NEW = ("a 2009 modern mid-size four-door sedan with smooth rounded lines, slim swept-back headlights and a small grille, painted "
"glossy cherry red, with no badges and no license plates")
CUTAWAY = ("The turquoise car is a cutaway model: its roof panel and side windows have been removed, like a convertible, so we look "
"straight down into its cabin and see the bench seat, the steering wheel, the bare metal dashboard and the floor; its windshield is "
"still in place. The red car keeps its roof, and we see the man clearly through its windshield.")
DUMMY = ("a plain light-grey crash-test dummy with black-and-yellow round target stickers on its head and joints and no face")
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the concrete "
"pad, its painted lines, the grass, the camera poles and the cut front edge of the block stay exactly where they are and the same "
"size, and both cars stay the same size.")
SAME = "Same scene, same camera angle and framing as the reference image."
KEEP = "Everything else identical."
STAY = "Both cars stay exactly where they are."

P = {
 # ---- the main view (stage ladder) ----
 # S0T: the base generation (cars already touching, dummy facing the wrong way); S0 is its edit and the first frame of the video,
 # frozen at the instant the bumpers meet (seedream would not leave a gap in three tries, so CONTACT was dropped).
 "S0T": f"{STYLE} Scene: {SET}. {CAMERA}. In the bottom half of the frame is {OLD}, pointing up, with its big tail fins nearest the "
       f"camera at the bottom of the frame; {DUMMY} sits in its driver's seat with no seat belt. In the top half of the frame is {NEW}, "
       f"pointing down toward the old car; {MASCOT}, the same man as in the reference image, sits in its driver's seat facing the camera, "
       f"wearing a seat belt across his chest, smiling and waving up at the camera with one hand. {CUTAWAY} The two cars face each other "
       f"head-on on the same straight line, nose to nose, with about two metres of empty concrete between their front bumpers; they are "
       f"not touching. {TOY} Both cars are completely intact and undamaged. He is the only person in the scene.",
 "S0": f"{STYLE} {SAME} Change only this: the turquoise car's cream roof panel is removed completely, so its whole cabin is open "
       f"from above like a convertible. The crash-test dummy sits on the left side of the turquoise car's front bench seat with its back "
       f"to the camera, facing the top of the frame toward the red car, both hands on a large thin steering wheel in front of it: we see "
       f"the back of its head and shoulders. The right side of the front bench seat is empty. {KEEP}",
 "S1": f"{STYLE} {LOCK} Change only this: the two cars have driven into each other in the middle of the frame. The whole front of the "
       f"red car is crumpled into neat accordion-like zigzag folds, its hood buckled up in pleats and pushed back about a third of the "
       f"way toward its windshield; the front of the turquoise car is crushed too, its chrome grille and bumper bent and torn. Small "
       f"chips of glass and plastic hang in the air. Both cabins are still completely undamaged, and both drivers sit upright in their "
       f"seats; the man in the yellow hard hat grips the steering wheel. {KEEP}",
 # S1b: S1 kept the waving pose from S0; edit him into bracing so the crash reads (the thumbs-up comes in C3)
 "S1b": f"{STYLE} {SAME} Change only this: the man in the yellow hard hat in the red car no longer waves: he grips the steering "
        f"wheel tightly with both hands and braces, eyes wide, his shoulder belt across his chest. {KEEP}",
 "S2": f"{STYLE} {LOCK} {STAY} Change only this: the crash has pushed deeper into the turquoise car: its dashboard and the floor at the "
       f"dummy's feet are shoved back toward the seat, its windshield frame is bent and the glass is cracked, and its big thin steering "
       f"wheel is pushed up and back toward the dummy's head. The red car's front stays folded exactly as before, and the red car's cabin "
       f"behind it is completely unchanged and undamaged, with the man in the yellow hard hat still gripping the steering wheel and "
       f"bracing. {KEEP}",
 # S2b: S2 only cracked the windshield; push the intrusion much deeper so it reads as "two feet"
 "S2b": f"{STYLE} {LOCK} {STAY} Change only this: the turquoise car's front end is crushed much deeper: its hood is folded up into a "
        f"tall heap of torn turquoise metal shoved back over the windshield frame, the windshield frame is bent back toward the dummy, and "
        f"the dashboard and the floor under it are pushed about two feet back into the cabin, so the dashboard now presses against the "
        f"dummy's knees and the space for its legs is gone; its steering wheel is shoved up and back right in front of the dummy's face. "
        f"The red car's front stays folded exactly as before, and its cabin and the man in the yellow hard hat are completely unchanged. "
        f"{KEEP}",
 "CAGE": f"{STYLE} {SAME} Change only this: the strong steel frame around the red car's cabin glows bright orange like an x-ray "
         f"highlight: the pillars on both sides of the windshield, the rails along the edges of the roof, the door pillars and the sills "
         f"along the bottom of the doors form one glowing rigid cage around the man in the yellow hard hat. Nothing else glows; the "
         f"crushed fronts of both cars are not highlighted. {KEEP}",
 "S3": f"{STYLE} {LOCK} {STAY} Change only this: both drivers have been thrown forward. In the turquoise car, the crash-test dummy, with "
       f"no seat belt, has slid forward off its bench seat: its head hits the steering wheel and its chest is pressed against the bare "
       f"metal dashboard. In the red car, the man in the yellow hard hat is held firmly in his seat by a tight shoulder belt across his "
       f"chest, leaning forward only a little. No airbags. The crushed fronts of both cars stay exactly as before. {KEEP}",
 "S4": f"{STYLE} {LOCK} {STAY} Change only this: a big round white airbag has burst out of the red car's steering wheel and is fully "
       f"inflated in front of the man in the yellow hard hat, cushioning his face and chest; his shoulder belt is still tight. The dummy "
       f"in the turquoise car stays exactly as before. {KEEP}",
 # S4b: S4 inflated the bag beside him (like a passenger bag); move it out of his steering wheel, in front of him
 "S4b": f"{STYLE} {SAME} Change only this: the white airbag is now directly in front of the man in the yellow hard hat, bursting out "
        f"of the steering wheel he is holding: it covers his chest and the lower half of his face, so only his yellow hard hat and his "
        f"eyes show above it. There is no airbag anywhere else in the car. {KEEP}",
 "COLUMN": f"{STYLE} {SAME} Change only this: the steering column of each car glows bright red like an x-ray highlight. In the "
           f"turquoise car it is a long straight steel rod running from the dashboard to the steering wheel, bent up toward the dummy's "
           f"head. In the red car it is a short column hidden behind the white airbag, still straight. Nothing else glows. {KEEP}",
 "S6": f"{STYLE} {LOCK} Change only this: the turquoise car is coming apart: its driver's door has swung wide open, its windshield has "
       f"popped out of its frame and lies on its crumpled hood, and its bench seat has torn loose from the floor and tipped forward, with "
       f"the dummy slumped sideways on it. The two cars have bounced a short way apart, so a small gap of concrete shows between their "
       f"crushed fronts. In the red car, the airbag has gone soft and hangs from the steering wheel, and the man in the yellow hard hat "
       f"sits up in his seat, dazed but unhurt; the red car's cabin is still intact. {KEEP}",
 "S7": f"{STYLE} {LOCK} {STAY} Change only this: the man in the yellow hard hat has unbuckled and climbed out of the red car; he stands "
       f"on the concrete right beside its driver's side, balancing on his right foot and rubbing his left foot with one hand, with a wry "
       f"smile; he is the same man as in the second reference image, with his short dark beard, navy overalls and brown boots, and we "
       f"see all of him. The red car's driver's seat is now empty, with the soft airbag hanging from its wheel. The only other figure "
       f"in the scene is the dummy in the turquoise car. {KEEP}",
 "END": f"{STYLE} {LOCK} {STAY} Change only this: the man in the yellow hard hat has walked a few steps away from the wrecked cars "
        f"toward the camera; he stands on the concrete facing the camera, smiling and waving with one arm raised high, and we see all of "
        f"him: the same man as in the second reference image, with his short dark beard. The red car's driver's seat stays empty. The "
        f"only other figure in the scene is the dummy in the turquoise car. {KEEP}",
 # ---- spare: one close-up of the build, only if a push-in on S2 is too soft to read ----
 "FOOT": f"{STYLE} Extreme close-up from the same high angle as the reference image: the driver's footwell of the same crushed "
         f"turquoise car fills most of the frame: the floor and the bare metal dashboard are shoved back against the dummy's bent "
         f"light-grey legs, the pedals pushed up out of place. Same colours and light as the reference. No people other than the dummy.",
}
REFS = {
 "S0T": ["MASCOT"], "S0": ["S0T"], "S1": ["S0", "MASCOT"], "S1b": ["S1"], "S2": ["S1b", "MASCOT"], "S2b": ["S2"], "CAGE": ["S2b"],
 "S3": ["S2b", "MASCOT"], "S4": ["S3", "MASCOT"], "S4b": ["S4"], "COLUMN": ["S4b"], "S6": ["S4b", "MASCOT"], "S7": ["S6", "MASCOT"],
 "END": ["S7", "MASCOT"], "FOOT": ["S2b"],
}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
