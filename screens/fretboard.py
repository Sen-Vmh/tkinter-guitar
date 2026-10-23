from ctypes import pointer
from random import randint
import tkinter as tk

from music import CHROMATIC, TUNING
from screens.practice_window import PracticeWindow

WIDTH = 800
HEIGHT = 300

TUNING.reverse()

class FretboardScreen(PracticeWindow):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.paint_fretboard()
        self.paint_note_answers()

        self.correct = 0
        self.wrong = 0
        self.current = None

        self.frame_score = tk.Frame(self)
        self.frame_score.pack()

        self.label_correct = tk.Label(self.frame_score, text=self.correct)
        self.label_correct.grid()

        self.label_wrong = tk.Label(self.frame_score, text=self.correct)
        self.label_wrong.grid(row=0, column=1)

    def show_next(self):
        self.string = randint(0, 5)
        self.note = randint(0, 12)

        self.current = self.frets[self.string][self.note]
        self.current.configure(bg="#AAA")        

    def answer_press(self, note):
        if not self.running:
            return

        print(TUNING[self.string][self.note])
        print(note)
        print("---")

        if TUNING[self.string][self.note] == note:
            self.correct += 1
            self.label_correct.configure(text=self.correct)
        else:
            self.wrong += 1
            self.label_wrong.configure(text=self.wrong)

        self.current.configure(bg="#FFF")  
        self.next_note()

    def paint_note_answers(self):
        self.note_anser_grid = tk.Frame(self)
        self.note_anser_grid.pack()

        tk.Label(self.note_anser_grid, text="Select the correct note:").grid(row=0)

        for i in range(len(CHROMATIC)):
            note = CHROMATIC[i]
            tk.Button(self.note_anser_grid, text=note, command=lambda n=note: self.answer_press(n)).grid(row=1, column=i, sticky="nsew")

    def paint_fretboard(self):
        self.frets = []
        self.fretboard_grid = tk.Frame(self)
        self.fretboard_grid.pack()

        distance = 0

        for i in range(1, 13):
            current_distance = 2000 * (1-(1/2**(i/12)))
            self.fretboard_grid.columnconfigure(i, minsize=abs((distance - current_distance)))
            distance = current_distance

        for i in range(len(TUNING)):
            guitar_string = TUNING[i]
            row = []

            for j in range(len(guitar_string)):
                    
                note = guitar_string[j]
                print(j, note)
                b = tk.Button(self.fretboard_grid, background="#FFF")
                b.grid(row=i, column=j, sticky="nsew")
                row.append(b)

                if i == 5 and j in [3, 5, 7, 9, 12]:
                    b.configure(text="◉", font=("Arial", 12))

            self.frets.append(row)