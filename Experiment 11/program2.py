
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Arrange buttons vertically
button1.pack()
button2.pack()
button3.pack()

# Run the application
root.mainloop()
