
from tkinter import *

master = Tk()
master.title("Canvas Example")

w = Canvas(master, width=70, height=100)
w.pack()

w.create_line(10, 10, 70, 70)

mainloop()
