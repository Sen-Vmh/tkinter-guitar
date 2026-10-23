import random
import time
import tkinter as tk

class PracticeScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.button = tk.Button(self, text="start practice", command=self.toggle_practice)

        self.running = False
        self.after_id = None

    def destroy(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None
        super().destroy()

    def toggle_practice(self):
        if self.running:
            self.stop_practice()
        else:
            self.start_practice()

    def start_practice(self, callbackFn):
        self.running = True
        self.count = 0
        self.start = time.monotonic()
        self.button.configure(text="stop practice")
        if not self.running:
            return
        self.callbackFn()

    def next_note(self):
        self.note_box.configure(text=random.choice(self.notes))
        self.count += 1

        self.after_id = self.after(int(float(self.spinbox_interval.get()) * 1000), self.next_note)

    def stop_practice(self):
        self.running = False
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None
        elapsed = time.monotonic() - self.start
        self.button.configure(text="start practice")
        self.stats_label.configure(text=f"You practiced {self.count} notes for {elapsed/60:.1f} minutes")
