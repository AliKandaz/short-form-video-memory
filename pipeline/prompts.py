STYLE = ("Stylized 3D CG render with a real-time game-engine look: semi-realistic PBR textures on simple low-to-mid-poly models, "
"soft natural sunlight, soft contact shadows, gentle ambient occlusion, mild depth of field. Small diorama-like outdoor set seen from "
"a slightly elevated three-quarter angle. Natural earthy desert palette: ochre sand, terracotta mud, sun-bleached wood, pale blue sky. "
"Clean readable shapes, uncluttered composition, subject in the centre third of a vertical 9:16 frame. Not photorealistic, not cartoon "
"cel-shaded. No text, no letters, no captions, no logos, no watermark, no UI.")
MASCOT = ("a stocky man in a yellow hard hat, navy blue work overalls over a white t-shirt, brown work boots, short dark beard, "
"simple friendly face, game-character proportions")
SET = ("a low sandy rise above a wide dry riverbed of cracked mud and pebbles, scattered low desert scrub, one tall cactus, "
"distant flat-topped mesas under a clear sky")
CAMERA = ("Camera: elevated three-quarter view from the front-left, the build site centred on the rise, the dry riverbed curving "
"across the bottom of the frame")
SAME = "Same scene, same camera angle and framing as the first reference image."
KEEP = "Everything else identical."

P = {
 "S0": f"{STYLE} Scene: {SET}. {CAMERA}. The build site on the rise is bare sand with a small pile of loose rough rocks. {MASCOT} stands on the rise beside the rock pile, looking at the site.",
 "MASCOT": f"{STYLE} Full-body character render of {MASCOT}, standing in a relaxed neutral pose, front view, plain light sand-coloured studio backdrop, soft even light.",
 "S1": f"{STYLE} {SAME} Change only this: on the rise, a waist-high ring of stacked rough desert rocks now forms a circular wall about three metres across, with a small gap for an entrance facing the camera. {MASCOT} stands inside the ring placing the last rock on top. {KEEP}",
 "BRICK": f"{STYLE} Ground-level close-up on the same sandy rise. {MASCOT} kneels beside a shallow pit of wet brown mud mixed with golden straw, pressing mud into a rectangular wooden brick mould on the sand. Beside him, three fresh wet mud bricks sit in a row. A wooden bucket of water and a bundle of straw nearby. Warm late-morning light.",
 "DRYING": f"{STYLE} Low-angle shot across the same sandy rise: neat rows of dozens of rectangular mud-and-straw adobe bricks laid out drying under a bright sun, pale dry surfaces with fine cracks, the rows receding toward the dry riverbed and distant mesas. No people.",
 "S1HEAT": f"{STYLE} {SAME} Change only the lighting and mood: harsh midday, a blinding white-hot sun high overhead, washed-out pale sky, strong heat shimmer rising off the rocks, short hard shadows. {MASCOT} sits inside the rock ring, sweating, wiping his brow. {KEEP}",
 "S2": f"{STYLE} {SAME} Change only this: the rock ring has been cleared away; in its place stands the footprint of a small square one-room house made of low, thin, single-brick-wide adobe mud-brick walls, knee-high, with a doorway gap facing the camera. {MASCOT} stands beside the walls holding one brick. {KEEP}",
 "S3": f"{STYLE} {SAME} Change only this: the adobe walls are now very thick, about two feet wide, built from stacked mud bricks with mud mortar, and rise to full height of about two and a half metres, forming a small square one-room house with a doorway facing the camera and one small window. There is no roof yet; the tops of the walls are open to the sky. {MASCOT} stands in the doorway. {KEEP}",
 "CUTAWAY": f"{STYLE} Educational cross-section cutaway shot: one thick adobe wall sliced open to show its two-foot-thick interior of stacked mud bricks and mortar, seen from the side at sunset. A warm orange glow on the sun-facing outer face fades gradually into the middle of the wall, while the inner face stays cool blue-grey. Low golden sunset light, long shadows, desert and mesas in the background.",
 "NIGHT": f"{STYLE} {SAME} Change only the time of day: night, deep blue moonlit desert, starry sky, a thin layer of white frost on the sand and bushes. The thick adobe walls glow with soft warm orange light from inside the open-topped room. {MASCOT} sits inside against the wall, relaxed and warm. {KEEP}",
 "S4": f"{STYLE} {SAME} Change only this: the house now has a flat roof: round wooden log beams span across the tops of the walls and poke out a little through the front wall, covered with a layer of sticks and a thick layer of smooth packed mud on top, with a low mud parapet around the roof edge. {MASCOT} stands on the ground beside the door. {KEEP}",
 "STORM": f"{STYLE} {SAME} Change only the weather: the sky has turned dark and stormy, towering black-grey thunderclouds over the mesas, a curtain of heavy rain sweeping toward the house across the desert, the first big raindrops darkening the sand, dramatic low light. The dry riverbed below is still empty. No people. {KEEP}",
 "S5": f"{STYLE} {SAME} Change only this: two wooden trough rain spouts now stick straight out through the roof parapet near the front corners, angled slightly down; and the bottom half-metre of every wall now sits on a visible base of grey fitted stones. {MASCOT} stands beside the door. {KEEP}",
 "S6": f"{STYLE} {SAME} Change only this: every outside wall and the parapet are now painted bright chalky white with lime wash; the wooden beams, wooden spouts, doorway and grey stone base keep their natural colours. {MASCOT} holds a wide brush and a bucket of white lime beside the wall. {KEEP}",
 "CANALE": f"{STYLE} Close-up from below of one wooden trough rain spout sticking out through the mud parapet at the roof edge of the same adobe house, during heavy rain: a thick stream of rainwater pours off the end of the spout in an arc and splashes onto the sand well clear of the wall. Dark stormy sky, rain streaks, the grey stone base of the wall visible at the bottom of the frame.",
 "STONE": f"{STYLE} Low close-up at the base of the same adobe house wall during rain: the mud-brick wall sits on a base of grey fitted stones about half a metre high; rain splashes off the stones into puddles on the ground while the mud wall above stays intact. Dark stormy light.",
 "FLOOD": f"{STYLE} The same scene from a slightly higher and wider camera angle than the first reference image, during a violent storm: a churning brown flash-flood wave roars down the dry riverbed below the rise, carrying broken branches and uprooted bushes, muddy water filling the whole riverbed; heavy rain, dark clouds. The white adobe house stands safe and dry on the rise above the water. No people.",
 "PAYOFF": f"{STYLE} Medium shot from in front of the same white adobe house in heavy rain: {MASCOT} stands dry in the open doorway with arms crossed, calm and smiling, while just below the rise a raging brown flood rushes past along the riverbed. Water arcs out of the wooden roof spouts. Dark stormy light with warm light glowing from inside the house.",
 "END": f"{STYLE} {SAME} Change only this: it is now a bright, clear, sunny morning after the rain. The white adobe house is finished with a wooden plank door, a dome-shaped clay bread oven beside it, and a striped woven blanket hanging over the parapet to dry; small puddles drying on the sand and the riverbed damp. {MASCOT} stands in front of the house waving at the camera with one arm raised. {KEEP}",
}
if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
