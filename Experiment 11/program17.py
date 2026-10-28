
from tkinter import *

top = Tk()
top.title("Menubutton Example")

mb = Menubutton(top, text="Click here")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

cVar = IntVar()
aVar = IntVar()

mb.menu.add_checkbutton(label="Contact", variable=cVar)
mb.menu.add_checkbutton(label="About", variable=aVar)

mb.pack()

top.mainloop()
