
from tkinter import *

root = Tk()
root.title("Text Example")

T = Text(root, height=2, width=30)
T.pack()

T.insert(END, "Python Tkinter ")

mainloop()
