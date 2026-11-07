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

        self.add_interval()

        self.note_box = tk.Label(self, text="", bg="#11F", foreground="#FFF", font=("Times new roman", 48), width=4, relief="ridge", borderwidth=0.5)
        self.note_box.pack(padx=10, pady=10)

        self.stats_label.pack(padx=10, pady=10)

        self.next_note_button = tk.Button(self, text="Next note", command=self.next_note)

        self.update_interval_mode()

    def add_interval(self):
        self.checkbox_interval_state = tk.BooleanVar(value=False)
        self.checkbox_interval = tk.Checkbutton(self, text="Add interval", variable=self.checkbox_interval_state, command=self.update_interval_mode)
        self.checkbox_interval.pack(padx=10, pady=10)

        self.spinbox_interval = tk.Spinbox(self, from_=1, to=10)

    def update_interval_mode(self):
        if self.checkbox_interval_state.get():
            self.next_note_button.pack_forget()
            self.spinbox_interval.pack(after=self.checkbox_interval)
        else:
            self.spinbox_interval.pack_forget()
            self.next_note_button.pack()

    def on_start(self):
        self.notes = (NATURAL + SHARPS + FLATS) if self.checkbox_enharmonic_state.get() else (NATURAL + SHARPS)
        self.checkbox_interval.configure(state="disabled")

    def on_stop(self):
        self.checkbox_interval.configure(state="normal")

    def show_next(self):
        self.note_box.configure(text=random.choice(self.notes))

    def get_interval(self):
        if not self.checkbox_interval_state.get():
            return None
        return float(self.spinbox_interval.get())
