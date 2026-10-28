
from tkinter import *

master = Tk()
master.title("Spinbox Example")

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()
