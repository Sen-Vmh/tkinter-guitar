NATURAL = ["A", "B", "C", "D", "E", "F", "G"]
SHARPS = ["A#", "C#", "D#", "F#", "G#"]
FLATS = ["A♭", "B♭", "D♭", "E♭", "G♭"]

CHROMATIC = NATURAL + SHARPS
CHROMATIC.sort()

TUNING = [["E"], ["A"], ["D"], ["G"], ["B"], ["E"]]

for i in range(len(TUNING)):
    note = TUNING[i][0]
    index = CHROMATIC.index(note)

    TUNING[i] = (list(CHROMATIC*2)[index:index+13])

APP_NAME = "Cool guitar app"
INPUT_ERROR = "invalid input, try again"