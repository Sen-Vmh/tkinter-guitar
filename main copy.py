import math
import random
import time
import tkinter as tk
from tkinter import font

NATURAL = ["A", "B", "C", "D", "E", "F", "G"]
SHARPS = ["A#", "C#", "D#", "F#", "G#"]
FLATS = ["A♭", "B♭", "D♭", "E♭", "G♭"]

APP_NAME = "Cool guitar app"
INPUT_ERROR = "invalid input, try again"

# def main():
#     mode = ask_mode()
#     notes = (NATURAL + SHARPS) if mode == "1" else (NATURAL + SHARPS + FLATS)
#     interval = ask_interval()
#     count, elapsed_time = practice(notes, interval)
#     print(f"You practiced {count} notes for {elapsed_time/60:.1f} minutes")




            
class MyGuitarApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)

        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=14, family="Times new roman")

        self.label = tk.Label(self.root, text=APP_NAME)
        self.label.pack(padx=12, pady=12)


        self.checkbox_enharmonic = tk.Checkbutton(self.root, text="Include enharmonics")
        self.checkbox_enharmonic.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="start practice")
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def practice(input_list, interval):
        count = 0
        start = time.monotonic()

        try:
            while True:
                note = random.choice(input_list)
                print(f"play the note {note}")

                count += 1

                time.sleep(interval)

        except KeyboardInterrupt:
            return count, time.monotonic() - start


    def ask_mode():
        while True:
            mode = input("select 1 or 2:\n\t1: 12 notes\n\t2: 12 notes with enharmonics\nselection: ")

            if mode in ("1", "2"):
                return mode
            else:
                print(INPUT_ERROR)

    def ask_interval():
        while True:
            try:    
                duration = float(input("Select a duration in seconds (numbers only): ").strip())
                if duration > 0 and math.isfinite(duration):
                    return float(duration)
                else:
                    raise ValueError
            except ValueError:
                print(INPUT_ERROR)


if __name__ == "__main__":
    MyGuitarApp()    


