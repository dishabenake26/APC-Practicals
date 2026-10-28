
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Grid Example")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Arrange buttons in rows and columns
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0, columnspan=2)

# Run the application
root.mainloop()
