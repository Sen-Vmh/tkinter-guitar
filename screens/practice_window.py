import time
import tkinter as tk

class PracticeWindow(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        window_options_frame = tk.Frame(self)
        window_options_frame.pack(pady=10)

        tk.Button(window_options_frame, text="← back", command=lambda: app.show("menu")).grid(row=0, column=0)
        self.button = tk.Button(window_options_frame, text="start practice", command=self.toggle_practice)
        self.button.grid(row=0, column=1)

        self.stats_label = tk.Label(self, text="")
        self.stats_label.pack()

        self.running = False
        self.after_id = None
        self.count = 0
        self.start_time = None

    def destroy(self):
        self.cancel_timer()
        super().destroy()

    def toggle_practice(self):
        if self.running:
            self.stop_practice()
        else:
            self.start_practice()

    def start_practice(self):
        self.running = True
        self.count = 0
        self.start_time = time.monotonic()
        self.on_start()
        self.button.configure(text="stop practice")
        self.stats_label.configure(text="Good luck")
        self.next_note()

    def next_note(self):
        if not self.running:
            return
        self.show_next()
        self.count += 1

        interval = self.get_interval()
        if interval is not None:
            self.after_id = self.after(int(interval * 1000), self.next_note)

    def stop_practice(self):
        self.running = False
        self.cancel_timer()
        elapsed = time.monotonic() - self.start_time
        self.button.configure(text="start practice")
        self.stats_label.configure(text=f"You practiced {self.count} notes for {elapsed/60:.1f} minutes")

    def cancel_timer(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

    def on_start(self):
        """Prepare a new session, e.g. read settings."""

    def show_next(self):
        """Show the next note to the user."""
        raise NotImplementedError

    def get_interval(self):
        """Seconds until the next note, or None if the screen isn't timed."""
        return None
