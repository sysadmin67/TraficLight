import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
root.withdraw()
for f in sorted(tkfont.families()):
    if "digit" in f.lower():
        print(f)
root.destroy()