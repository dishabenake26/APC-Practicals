
from tkinter import *

# Create the main window
master = Tk()

# Set the window title
master.title("Entry Example")

# Create a label
Label(master, text="First Name").grid(row=0, column=0)

# Create an entry field
e1 = Entry(master)

# Place the entry field
e1.grid(row=0, column=1)

# Run the application
mainloop()
