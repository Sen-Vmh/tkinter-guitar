from operator import indexOf
from webbrowser import Chrome


NATURAL = ["A", "B", "C", "D", "E", "F", "G"]
SHARPS = ["A#", "C#", "D#", "F#", "G#"]

CHROMATIC = NATURAL + SHARPS
CHROMATIC.sort()

TUNING = [["E"], ["A"], ["D"], ["G"], ["B"], ["E"]]

print(CHROMATIC)

for i in range(len(TUNING)):
    note = TUNING[i][0]
    index = CHROMATIC.index(note)
    print(note, index)

    TUNING[i] = (list(CHROMATIC*2)[index:index+13])

print(TUNING)