
from tkinter import *

# Create the main window
master = Tk()

master.title("Checkbutton Example")

# Create variables
var1 = IntVar()
var2 = IntVar()

# Create checkbuttons
c1 = Checkbutton(master, text="Male", variable=var1)
c1.pack()

c2 = Checkbutton(master, text="Female", variable=var2)
c2.pack()

# Run the application
mainloop()
