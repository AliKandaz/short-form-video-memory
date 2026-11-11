# Video 05 (idea #1 Aquarius, "How a Steel Tank Becomes a House at the Bottom of the Sea", Classic look): still prompts for
# seedream_v5_pro 1k 9:16 (DIVER 2:3). Usage: python3 05-prompts.py KEY -> prints the prompt as a JSON string.
# References per still are in REFS (keys of 05-jobs.tsv; MASCOT is the locked reference job from 3.4).
# STYLE = the base string of 02-prompts.py with its palette line swapped for one that names colours only (objects named in the
# style string leak into every shot, 3.4f).
STYLE = ("Stylized 3D CG render with a real-time game-engine look: semi-realistic PBR textures on simple low-to-mid-poly models, "
"soft natural sunlight, soft contact shadows, gentle ambient occlusion, mild depth of field. Small diorama-like outdoor set seen from "
"a slightly elevated three-quarter angle. Sunny Caribbean palette: clear turquoise and deep blue water, soft sun rays, pale cream "
"sand, coral pinks, oranges and purples, crisp white, sunny yellow accents, bright blue sky. Clean readable shapes, uncluttered "
"composition, subject in the centre third of a vertical 9:16 frame. Not photorealistic, not cartoon cel-shaded. No text, no letters, "
"no captions, no logos, no watermark, no UI.")
MASCOT = ("a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, brown work boots, short dark beard, "
"simple friendly face, game-character proportions")
DIVER = ("a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, short dark beard, simple friendly face, "
"game-character proportions, dressed for diving: a clear dive mask over his eyes and nose, a black scuba mouthpiece in his mouth, "
"one grey scuba tank strapped to his back and black swim fins on his feet")
TANK = ("a long white-painted steel cylinder as long as a bus, lying on its side, with rounded ends and a row of small round porthole "
"windows along its side")
BASE = "a heavy dark-grey steel base frame standing on four thick round steel legs planted in the sand"
BUOY = ("a big round bright-yellow buoy as wide as a small house, with a short white mast and two thin antennas on top, floating on "
"the surface")
SET = ("the sea shown side-on like a giant cut-open aquarium diorama: across the top fifth of the frame, a strip of bright blue sky with "
"a few small white clouds, and the sea surface seen from the side as a sparkling wavy waterline; below the waterline, clear blue "
"water with soft slanting sun rays and a few small tropical fish; at the bottom, a flat patch of pale cream sand beside a colourful "
"coral reef with sea fans, round brain corals and orange and purple coral heads")
CAMERA = ("Camera: slightly elevated three-quarter view of the cut-open sea, looking slightly down; the waterline runs across the top "
"fifth of the frame, and the sand patch with the tank is centred in the lower half of the frame")
INSIDE = ("inside the long steel tank: a small cosy room with curved white-painted steel walls and ceiling, warm yellow ceiling lights, "
"a few pipes and cables running along the walls")
UNDER = ("The tank is deep underwater: everything seen outside it is deep blue sea with soft sun rays from far above and small "
"fish; no sky, no clouds, no beach and no waterline anywhere in the frame.")
SAME = "Same scene, same camera angle and framing as the first reference image."
KEEP = "Everything else identical."

P = {
 # ---- references ----
 "DIVER": f"{STYLE} Character reference sheet: one full-body front view of the same character as in the reference image, now "
          f"{DIVER}. He stands straight facing the camera with his arms slightly away from his body, on a plain light grey studio "
          f"backdrop, even soft lighting. No water, no other objects, no other people.",
 # ---- ladder on the hero angle ----
 "S0": f"{STYLE} Scene: {SET}. {CAMERA}. At the waterline, a small grey crane barge floats at the top of the frame, and its crane "
       f"cable runs straight down through the water. Hanging level from the cable, {TANK} is being lowered toward the sand patch, "
       f"about two metres above the sand, with a few bubbles trailing up from it. {DIVER}, the same man as in the reference image, "
       f"swims beside the tank with one hand on its side, guiding it down. He is small next to the tank.",
 "FLOAT": f"{STYLE} {SAME} Change only this: the crane cable hangs slack and loose, and the tank has broken free: it tilts nose-up at "
          f"a steep angle and rises off the sand toward the surface, with a big cloud of bubbles and a puff of sand below it. The man "
          f"in the yellow hard hat clings to a strap on the side of the rising tank with both hands, legs dangling, surprised. {KEEP}",
 "S2": f"{STYLE} {SAME} Change only this: the tank now sits level and still on {BASE}, firmly anchored on the sand patch, with small "
       f"puffs of sand around the four legs. The crane barge still floats at the surface with its cable hanging slack and unhooked. "
       f"The man in the yellow hard hat floats beside one of the legs, giving a thumbs-up. {KEEP}",
 "S3": f"{STYLE} {SAME} Change only this: the crane barge is gone. In its place, {BUOY}, right above the tank, and one thick black "
       f"hose runs from the bottom of the buoy straight down through the water to the top of the tank. {KEEP}",
 "STORM": f"{STYLE} {SAME} Change only this: a hurricane rages at the surface. The sky across the top of the frame is black and "
          f"stormy with slanting rain, the waterline is a churning mass of huge grey breaking waves and white foam, and the yellow buoy "
          f"pitches hard on the waves, its hose pulled tight. The water below is darker grey-blue with stirred-up sand near the bottom. "
          f"The tank on its four legs sits in the same place, its round portholes glowing warm yellow. No divers outside, no people. "
          f"{KEEP}",
 "PAYOFF": f"{STYLE} {SAME} Change only this: the yellow buoy is gone from the surface; only a snapped end of the black hose dangles "
           f"from the top of the tank, swaying in the water. The storm still churns the surface at the top of the frame with huge "
           f"breaking waves and foam. Down at the bottom the water is calm and clear, the tank sits perfectly still and level on its "
           f"four legs with its portholes glowing warm yellow, and small fish shelter beside the coral. No people. {KEEP}",
 "END": f"{STYLE} {SAME} Change only this: it is a bright, calm, sunny day. The sky is clear blue, the surface is smooth and "
        f"sparkling, and sun rays slant down through clear turquoise water. The yellow buoy floats at the surface with its black hose "
        f"down to the tank. The tank on its four legs glows warm yellow in its round portholes, and schools of small colourful fish "
        f"swim around it. {DIVER}, the same man as in the second reference image, floats in front of the tank facing the camera, "
        f"waving with one arm raised high. {KEEP}",
 # ---- inside the tank ----
 "DOOR": f"{STYLE} Side-on cutaway {INSIDE}, with a bunk and a small table. A normal door in the side wall has just been opened, and "
         f"the sea blasts in through it as a thick jet of white foaming water, flooding across the floor. {MASCOT}, the same man as in "
         f"the reference image, stumbles backward with his arms up, surprised. Blue water fills the doorway.",
 "MOONPOOL": f"{STYLE} Side-on cutaway of the end room {INSIDE}, and a square opening in the middle of "
             f"the steel floor. Inside the opening, the sea surface sits perfectly flat and calm, level with the floor, glowing blue "
             f"from below, and a short metal ladder goes down into the water. {DIVER}, the same man as in the reference image, climbs "
             f"up the ladder out of the water into the room, water dripping off him, one hand on the edge of the floor. The rest of "
             f"the room is completely dry.",
 "WINDOW": f"{STYLE} Medium shot {INSIDE}. {MASCOT}, the same man as in the reference image, stands at a round porthole window in "
           f"the curved wall with one hand on its latch as if about to open it, looking back at the camera, puzzled. Outside the thick "
           f"glass is blue sea, and a big round-faced grouper fish presses its face against the glass, staring in.",
 "SPONGE": f"{STYLE} Medium shot {INSIDE}, with a bunk along the wall. {MASCOT}, the same man as in the reference image, sits on the "
           f"edge of the bunk breathing in deeply, chest puffed out. A soft translucent blue x-ray glow over his chest shows dozens of "
           f"tiny glowing blue bubbles drifting in from the air and soaking into his body. Simple and clean, no organs, no anatomy "
           f"detail.",
 "SHARK": f"{STYLE} Medium shot {INSIDE}. {MASCOT}, the same man as in the reference image, sits at a big round porthole window in "
          f"the curved wall, calmly holding a steaming mug and looking out. Outside the thick glass, in the blue sea, a big grey reef "
          f"shark glides past close to the window, seen side-on with its whole body visible. Calm, relaxed mood. {UNDER}",
 "DECOMP": f"{STYLE} Medium shot {INSIDE}, with a bunk along the wall. {MASCOT}, the same man as in the reference image, sits on the "
           f"bunk reading a thick book, bored. On the wall beside him hang a big round brass pressure gauge with a needle and a blank "
           f"face with no numbers, and a round wall clock with hands and no numbers. The round door to the rest of the tank is shut "
           f"tight. {UNDER}",
 "NAP": f"{STYLE} {SAME} Change only this: many hours later. The man in the yellow hard hat now lies on the bunk fast asleep, the open "
        f"book resting on his face; the needle of the pressure gauge has swung much further round, and the clock hands have moved. "
        f"{KEEP}",
 # ---- redos after round 2 (DOOR, MOONPOOL came out above water on a beach; CUP showed no air pocket; WINDOW had sky at the far end) ----
 "DOOR2": f"{STYLE} Close-up cutaway of {TANK} resting deep underwater: the near wall is cut away so we see into a small cosy "
          f"room with curved white-painted steel walls, warm yellow ceiling lights, a bunk and a small table. A normal door in the far "
          f"wall of the room has just been opened to the sea, and seawater blasts in through it as a thick jet of white foaming water, "
          f"flooding across the floor. {MASCOT}, the same man as in the reference image, stumbles backward with his arms up, surprised. "
          f"{UNDER}",
 "MOONPOOL2": f"{STYLE} Close-up cutaway of one end of {TANK}, standing on steel legs deep underwater above the sand: the near wall is "
              f"cut away so we see into a small dry room with curved white-painted steel walls and warm yellow ceiling lights. In the "
              f"middle of the room's floor is a square opening that looks straight down into the open sea under the tank; the water "
              f"surface sits perfectly flat and calm inside the opening, exactly level with the floor, held back by the air in the room, "
              f"and a short metal ladder goes down into the water. {DIVER}, the same man as in the reference image, climbs up the "
              f"ladder out of the water into the dry room, water dripping off him. Coral and sand below the tank. {UNDER}",
 "CUP2": f"{STYLE} Extreme close-up, side view through the clear water of a white bathtub: one hand holds a clear drinking glass upside "
         f"down and has pushed it all the way under the water, near the bottom of the tub. Inside the upside-down glass, a big bubble of "
         f"air fills it almost completely, so the inside of the glass stays dry and the water only creeps in at the very rim. Soft "
         f"bathroom light, a few small bubbles. Only the one hand is visible.",
 "WINDOW2": f"{STYLE} {SAME} Change only this: at the far right end of the corridor there is no opening, no sky and no sea view; it is "
            f"a closed curved white steel wall with a round steel hatch door, lit by the warm ceiling lights. {KEEP}",
 "S3b": f"{STYLE} {SAME} Keep exactly the same camera position, zoom and framing as the reference image: the waterline stays at the "
        f"same height near the top of the frame, and the tank, its legs, the sand, the coral and the man stay exactly where they are and "
        f"the same size. Change only this: the crane barge is gone. In its place, a round bright-yellow buoy with a short white mast "
        f"and two thin antennas floats on the waterline at the top of the frame, small in the frame, about the size the barge was, and "
        f"one long thin black hose hangs straight down from it through the deep water to the top of the tank. {KEEP}",
 "ESCAPE2": f"{STYLE} At the sea surface on the open ocean, seen side-on, medium shot: a small orange crew boat speeds across the "
            f"waves toward the right of the frame, throwing white spray. {DIVER}, the same man as in the reference image, sits in the "
            f"boat with two other divers, all in dive gear. Behind the boat, the whole sky is dark grey with low, heavy storm clouds, and "
            f"grey curtains of rain sweep across a darkening sea with growing waves. No island, no land, no smoke, no volcano, no fire.",
 # ---- under the sea, other framings (described in text; references copy the layout, 3.4f) ----
 "WEEKS": f"{STYLE} Underwater on a sunny coral reef, medium shot: {DIVER}, the same man as in the reference image, floats happily "
          f"beside a big round brain coral, holding a yellow measuring ruler against it, relaxed, with schools of small colourful fish "
          f"all around him. Behind him, slightly out of focus, {TANK} stands on four thick steel legs on the sand, its round portholes "
          f"glowing warm yellow. Sun rays slant down through clear turquoise water.",
 "RUSH": f"{STYLE} Underwater in deep blue water, seen from the side and slightly below: {DIVER}, the same man as in the reference "
         f"image, kicks hard and shoots straight up toward the bright shimmering surface far above, arms by his sides. Streams of tiny "
         f"fizzing white bubbles burst out from his arms and legs, like a shaken soda bottle being opened. Sun rays from above.",
 "BOAT": f"{STYLE} The sunny sea shown side-on like a cut-open aquarium: across the top of the frame, a small white dive boat floats "
         f"on the sparkling waterline with its anchor line running straight down to a coral reef. Below, a diver in a black wetsuit "
         f"with a yellow scuba tank and no hat hovers above the reef, looking at a big chunky dive watch on his wrist. Clear turquoise "
         f"water, sun rays, small fish.",
 "AQUANAUTS": f"{STYLE} Underwater on pale sand beside a coral reef, sunny turquoise water: two divers in bulky white astronaut-style "
              f"dive suits with round helmets bounce-walk across the sand in big slow moonwalk steps, carrying tools and a small "
              f"toolbox, like astronauts on the Moon. Behind them, {TANK} stands on four thick steel legs, its round portholes glowing "
              f"warm yellow. Sun rays, small fish. No hard hats.",
 # ---- the surface ----
 "ESCAPE": f"{STYLE} At the sea surface, seen side-on, medium shot in the late afternoon: a small orange crew boat speeds toward a "
           f"green island on the horizon, throwing white spray. {DIVER}, the same man as in the reference image, sits in the boat "
           f"with two other divers, all in dive gear. Behind the boat, a towering wall of black hurricane clouds and rain closes in "
           f"over a darkening grey sea.",
 "BUOYRIP": f"{STYLE} At the stormy sea surface, medium shot from the side: {BUOY} is hit by a huge breaking grey wave in a raging "
            f"hurricane; its thick chain and black hose underneath have snapped, and the buoy tumbles away across the foaming waves. "
            f"Black sky, slanting rain, white spray. No people.",
 # ---- inserts ----
 "CUP": f"{STYLE} Extreme close-up beside a white bathtub full of clear water: one hand pushes a clear drinking glass straight down, "
        f"upside down, into the water. Inside the glass a pocket of air stays trapped, so the water inside the glass stays far below "
        f"the water outside it. Soft bathroom light, a few bubbles. Only the one hand is visible.",
 "FULLSPONGE": f"{STYLE} Extreme close-up on a kitchen counter: a bright yellow kitchen sponge sits in a shallow white dish of water, "
               f"completely soaked and swollen, glistening, with water beading on top and spilling out around it into a puddle. It "
               f"cannot hold another drop. Soft daylight.",
 "PLANE": f"{STYLE} A big white passenger jet with no markings and no logos cruises high above a sea of golden sunset clouds, seen "
          f"from the side, small in the centre of the frame, a long thin contrail behind it. A long-journey feel.",
 "CAPSULE": f"{STYLE} Outer space: a small white cone-shaped crew capsule with no markings and no logos drifts in black space; the big "
            f"grey cratered Moon fills the lower part of the frame close behind it, and the small blue Earth hangs far away in a top "
            f"corner. Stars. A lonely, far-from-home feel.",
}
REFS = {
 "DIVER": ["MASCOT"], "S0": ["MASCOT"], "FLOAT": ["S0", "DIVER"], "S2": ["S0", "DIVER"], "S3": ["S2"], "STORM": ["S3b"],
 "PAYOFF": ["STORM"], "END": ["S3b", "DIVER"], "DOOR": ["MASCOT"], "MOONPOOL": ["DIVER"], "WINDOW": ["MASCOT"], "SPONGE": ["MASCOT"],
 "SHARK": ["MASCOT"], "DECOMP": ["MASCOT"], "NAP": ["DECOMP"], "WEEKS": ["DIVER"], "RUSH": ["DIVER"], "BOAT": [], "AQUANAUTS": [],
 "ESCAPE": ["DIVER"], "BUOYRIP": [], "S3b": ["S2"], "ESCAPE2": ["DIVER"], "DOOR2": ["MASCOT"], "MOONPOOL2": ["DIVER"], "CUP2": [], "WINDOW2": ["WINDOW"], "CUP": [], "FULLSPONGE": [], "PLANE": [], "CAPSULE": [],
}
AR = {"DIVER": "2:3"}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
