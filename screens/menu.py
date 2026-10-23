import tkinter as tk

class MenuScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        for text, name in [("Note practice", "practice"),
                           ("Fretboard", "fretboard")]:
            tk.Button(self, text=text, command=lambda n=name: app.show(n)).pack(pady=5)
