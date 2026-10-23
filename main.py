import tkinter as tk
from tkinter import font

from music import APP_NAME
from screens.fretboard import FretboardScreen
from screens.menu import MenuScreen
from screens.practice import PracticeScreen

class MyGuitarApp:
    SCREENS = {
        "menu": MenuScreen,
        "practice": PracticeScreen,
        "fretboard": FretboardScreen,
    }

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=14, family="Times new roman")
        self.label = tk.Label(self.root, text=APP_NAME)
        self.label.pack(padx=12, pady=12)

        self.current = None
        self.show("menu")

        self.root.mainloop()

    def show(self, name):
        if self.current is not None:
            self.current.destroy()
        self.current = self.SCREENS[name](self.root, self)
        self.current.pack(fill="both", expand=True)

if __name__ == "__main__":
    MyGuitarApp()
