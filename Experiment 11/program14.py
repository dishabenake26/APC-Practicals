
from tkinter import *

master = Tk()
master.title("Scale Example")

# Vertical scale
w = Scale(master, from_=0, to=42)
w.pack()

# Horizontal scale
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

mainloop()
