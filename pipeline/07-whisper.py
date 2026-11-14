# Video 07 (P4, 1959 car vs 2009 car). Runs in the Higgsfield sandbox. Word timestamps for a narration take (faster-whisper small.en,
# CPU int8). usage: python3 07-whisper.py audio/takeN.wav audio/words_takeN.json  -> [[start,end,word],...]
# The initial_prompt lists the rare words in this script so Whisper spells them; change it per video.
import sys, json
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, info = m.transcribe(sys.argv[1], word_timestamps=True, beam_size=5, language="en",
                          initial_prompt="Pick your car. Crumple zone, accordion, totaled, footwell, safety cage, pretensioner, airbag, "
                                         "steering column, telescope, shoulder belt, nineteen fifty-nine, windshield, metal dash")
W = [[round(w.start,3), round(w.end,3), w.word.strip()] for s in segs for w in s.words]
json.dump(W, open(sys.argv[2], 'w')); print(len(W), 'words; last end', W[-1][1])
