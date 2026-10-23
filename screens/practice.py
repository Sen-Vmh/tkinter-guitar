import random
import tkinter as tk

from music import FLATS, NATURAL, SHARPS
from screens.practice_window import PracticeWindow

class PracticeScreen(PracticeWindow):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.checkbox_enharmonic_state = tk.IntVar()
        self.checkbox_enharmonic = tk.Checkbutton(self, text="Include enharmonics", variable=self.checkbox_enharmonic_state)
        self.checkbox_enharmonic.pack(padx=10, pady=10)

        self.spinbox_interval = tk.Spinbox(self, from_=1, to=10)
        self.spinbox_interval.pack()

        # self.button.pack(padx=10, pady=10)

        self.note_box = tk.Label(self, text="", bg="#11F", foreground="#FFF", font=("Times new roman", 48), width=4, relief="ridge", borderwidth=0.5)
        self.note_box.pack(padx=10, pady=10)

        self.stats_label.pack(padx=10, pady=10)

    def on_start(self):
        self.notes = (NATURAL + SHARPS + FLATS) if self.checkbox_enharmonic_state.get() else (NATURAL + SHARPS)

    def show_next(self):
        self.note_box.configure(text=random.choice(self.notes))

    def get_interval(self):
        return float(self.spinbox_interval.get())
