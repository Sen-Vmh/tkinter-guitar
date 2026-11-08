NATURAL = ["A", "B", "C", "D", "E", "F", "G"]
SHARPS = ["A#", "C#", "D#", "F#", "G#"]
FLATS = ["A♭", "B♭", "D♭", "E♭", "G♭"]

CHROMATIC = NATURAL + SHARPS
CHROMATIC.sort()

E_STANDARD = [["E"], ["A"], ["D"], ["G"], ["B"], ["E"]]
D_STANDARD = [["D"], ["G"], ["C"], ["F"], ["A"], ["D"]]

TUNING = E_STANDARD.copy()

for i in range(len(TUNING)):
    note = TUNING[i][0]
    index = CHROMATIC.index(note)

    TUNING[i] = (list(CHROMATIC*2)[index:index+13])

APP_NAME = "Cool guitar app"
INPUT_ERROR = "invalid input, try again"