
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Place Example")

# Set the window size
root.geometry("350x250")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Place buttons at specific positions
button1.place(x=50, y=50)
button2.place(x=100, y=100)
button3.place(x=150, y=150)

# Run the application
root.mainloop()
