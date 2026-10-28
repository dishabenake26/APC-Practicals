
import tkinter as tk

# Create the main window
r = tk.Tk()

# Set the window title
r.title("Counting Seconds")

# Create a button
button = tk.Button(
    r,
    text="Stop",
    width=40,
    command=r.destroy
)

# Display the button
button.pack()

# Run the application
r.mainloop()
