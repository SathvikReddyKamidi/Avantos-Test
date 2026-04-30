
Polkadot Score
How it works
The dress has polkadots represented as O characters. The scoring isn't just a straight count though dots that land within the x-range of her lips get multiplied by the number of characters used to draw both her pupils.
So the formula ends up being:
score = dots_outside_lips + (dots_inside_lips * pupil_char_count)
How I identified the features
Lips - found by scanning for the widest ( ) span in the art. The hint in the problem was that lips and pupils contain no ', backtick, ,, or - characters, which rules out a lot of the noise in the image.
Pupils - the eyes are drawn as two () pairs on the same line. Each () is 2 characters, so both pupils together = 4.
Polkadots  every O in the dress area. Split into inside vs outside based on column position relative to the lip boundaries.
Result
Total dots: 42
Inside lips range: 19
Outside lips range: 23
Pupil chars: 4
Score: 23 + (19 × 4) = 99

Running it
bashpython3 Avantos.py
No dependencies, just plain Python.
