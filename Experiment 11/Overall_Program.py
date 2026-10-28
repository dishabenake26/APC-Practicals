
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# 1. MAIN WINDOW
# ==========================================
root = tk.Tk()
root.title("Advanced Python - Tkinter All-in-One")
root.geometry("850x750")
root.configure(bg="lightblue")

# ==========================================
# 2. FUNCTIONS
# ==========================================
def show_message():
    messagebox.showinfo("Message", "Welcome to Python Tkinter!")

def show_name():
    name = name_entry.get()
    messagebox.showinfo("Your Name", f"Hello, {name}!")

def show_gender():
    messagebox.showinfo("Gender", f"Selected: {gender.get()}")

def show_checkboxes():
    selected = []
    if male_var.get():
        selected.append("Male")
    if female_var.get():
        selected.append("Female")

    if selected:
        messagebox.showinfo("Checkboxes", ", ".join(selected))
    else:
        messagebox.showinfo("Checkboxes", "Nothing selected")

def show_listbox():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        messagebox.showinfo("Listbox", f"Selected: {item}")
    else:
        messagebox.showwarning("Listbox", "Select an item first!")

def show_combobox(event=None):
    selected = combo.get()
    combo_label.config(text="Selected Item: " + selected)

def show_scale(value):
    scale_label.config(text="Scale Value: " + str(int(float(value))))

def show_spinbox():
    spin_label.config(text="Spinbox Value: " + spinbox.get())

def show_text():
    content = text_area.get("1.0", tk.END).strip()
    messagebox.showinfo("Text Area", content if content else "No text entered")

def clear_entry():
    name_entry.delete(0, tk.END)

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Toplevel Window")
    new_window.geometry("300x150")
    tk.Label(
        new_window,
        text="This is a new Toplevel window!",
        font=("Arial", 12)
    ).pack(pady=25)
    tk.Button(
        new_window,
        text="Close Window",
        command=new_window.destroy
    ).pack()

def draw_canvas():
    canvas.create_line(10, 10, 180, 80, fill="blue", width=3)
    canvas.create_rectangle(30, 100, 120, 160, fill="yellow")
    canvas.create_oval(140, 100, 200, 160, fill="green")

def clear_canvas():
    canvas.delete("all")

def exit_program():
    root.destroy()

# ==========================================
# 3. MENU
# ==========================================
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Window", command=open_new_window)
file_menu.add_command(label="Message", command=show_message)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_message)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# ==========================================
# 4. SCROLLABLE MAIN AREA
# ==========================================
outer_frame = tk.Frame(root, bg="lightblue")
outer_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(outer_frame)
scrollbar.pack(side="right", fill="y")

main_canvas = tk.Canvas(
    outer_frame,
    bg="lightblue",
    yscrollcommand=scrollbar.set
)
main_canvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=main_canvas.yview)

content = tk.Frame(main_canvas, bg="lightblue")
window_id = main_canvas.create_window(
    (0, 0), window=content, anchor="nw"
)

def update_scroll_region(event=None):
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))
    main_canvas.itemconfigure(window_id, width=main_canvas.winfo_width())

content.bind("<Configure>", update_scroll_region)
main_canvas.bind("<Configure>", update_scroll_region)

# ==========================================
# 5. LABEL
# ==========================================
tk.Label(
    content,
    text="ADVANCED PYTHON - TKINTER DEMONSTRATION",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=10)

tk.Label(content, text="1. Label Widget", bg="lightblue").pack()
tk.Label(content, text="Welcome to Tkinter!", bg="white").pack(pady=3)

# ==========================================
# 6. ENTRY AND BUTTON
# ==========================================
tk.Label(content, text="2. Entry and Button Widgets", bg="lightblue").pack(pady=5)

entry_frame = tk.Frame(content, bg="lightblue")
entry_frame.pack()

tk.Label(entry_frame, text="Enter Name:", bg="lightblue").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(entry_frame, width=25)
name_entry.grid(row=0, column=1, padx=5)

tk.Button(entry_frame, text="Submit", command=show_name).grid(row=0, column=2, padx=5)
tk.Button(entry_frame, text="Clear", command=clear_entry).grid(row=0, column=3, padx=5)

# ==========================================
# 7. CHECKBUTTON
# ==========================================
tk.Label(content, text="3. Checkbutton Widget", bg="lightblue").pack(pady=5)

male_var = tk.IntVar()
female_var = tk.IntVar()

tk.Checkbutton(content, text="Male", variable=male_var, bg="lightblue").pack()
tk.Checkbutton(content, text="Female", variable=female_var, bg="lightblue").pack()
tk.Button(content, text="Show Checkboxes", command=show_checkboxes).pack(pady=3)

# ==========================================
# 8. RADIOBUTTON
# ==========================================
tk.Label(content, text="4. Radiobutton Widget", bg="lightblue").pack(pady=5)

gender = tk.StringVar(value="Male")

tk.Radiobutton(content, text="Male", variable=gender, value="Male", bg="lightblue").pack()
tk.Radiobutton(content, text="Female", variable=gender, value="Female", bg="lightblue").pack()
tk.Button(content, text="Show Gender", command=show_gender).pack(pady=3)

# ==========================================
# 9. LISTBOX
# ==========================================
tk.Label(content, text="5. Listbox Widget", bg="lightblue").pack(pady=5)

list_frame = tk.Frame(content, bg="lightblue")
list_frame.pack()

listbox = tk.Listbox(list_frame, height=4, width=25, exportselection=False)
for item in ["Python", "Java", "C++", "JavaScript"]:
    listbox.insert(tk.END, item)
listbox.pack(side="left")

list_scrollbar = tk.Scrollbar(list_frame, command=listbox.yview)
list_scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=list_scrollbar.set)

tk.Button(content, text="Show Selected Item", command=show_listbox).pack(pady=3)

# ==========================================
# 10. COMBOBOX
# ==========================================
tk.Label(content, text="6. Combobox Widget", bg="lightblue").pack(pady=5)

combo = ttk.Combobox(content, values=["Java", "Python", "C++"], state="readonly")
combo.set("Python")
combo.pack()
combo.bind("<<ComboboxSelected>>", show_combobox)

combo_label = tk.Label(content, text="Selected Item: Python", bg="lightblue")
combo_label.pack()

# ==========================================
# 11. SCALE
# ==========================================
tk.Label(content, text="7. Scale Widget", bg="lightblue").pack(pady=5)

scale = tk.Scale(
    content,
    from_=0,
    to=100,
    orient="horizontal",
    command=show_scale,
    length=250
)
scale.pack()

scale_label = tk.Label(content, text="Scale Value: 0", bg="lightblue")
scale_label.pack()

# ==========================================
# 12. SPINBOX
# ==========================================
tk.Label(content, text="8. Spinbox Widget", bg="lightblue").pack(pady=5)

spinbox = tk.Spinbox(content, from_=0, to=10, width=10)
spinbox.pack()

tk.Button(content, text="Show Spinbox Value", command=show_spinbox).pack(pady=3)
spin_label = tk.Label(content, text="Spinbox Value: 0", bg="lightblue")
spin_label.pack()

# ==========================================
# 13. TEXT AND MESSAGE
# ==========================================
tk.Label(content, text="9. Text Widget", bg="lightblue").pack(pady=5)

text_area = tk.Text(content, height=4, width=40)
text_area.pack()
text_area.insert(tk.END, "Write something here...")

tk.Button(content, text="Show Text", command=show_text).pack(pady=3)

tk.Label(content, text="10. Message Widget", bg="lightblue").pack(pady=5)
tk.Message(
    content,
    text="This is the Message widget. It displays text across multiple lines.",
    width=350,
    bg="lightgreen"
).pack(pady=3)

tk.Button(content, text="Show Popup Message", command=show_message).pack(pady=3)

# ==========================================
# 14. MENUBUTTON
# ==========================================
tk.Label(content, text="11. Menubutton Widget", bg="lightblue").pack(pady=5)

menu_button = tk.Menubutton(content, text="Choose an Option", relief="raised")
option_menu = tk.Menu(menu_button, tearoff=0)
menu_button.config(menu=option_menu)

contact_var = tk.BooleanVar()
about_var = tk.BooleanVar()

option_menu.add_checkbutton(label="Contact", variable=contact_var)
option_menu.add_checkbutton(label="About", variable=about_var)
menu_button.pack()

# ==========================================
# 15. CANVAS
# ==========================================
tk.Label(content, text="12. Canvas Widget", bg="lightblue").pack(pady=5)

canvas = tk.Canvas(content, width=230, height=190, bg="white")
canvas.pack()

tk.Button(content, text="Draw Shapes", command=draw_canvas).pack(pady=3)
tk.Button(content, text="Clear Canvas", command=clear_canvas).pack(pady=3)

# ==========================================
# 16. PLACE GEOMETRY MANAGER
# ==========================================
tk.Label(content, text="13. Place Geometry Manager", bg="lightblue").pack(pady=5)

place_frame = tk.Frame(content, width=300, height=100, bg="white")
place_frame.pack(pady=3)
place_frame.pack_propagate(False)

tk.Button(place_frame, text="Position 1").place(x=10, y=10)
tk.Button(place_frame, text="Position 2").place(x=100, y=40)
tk.Button(place_frame, text="Position 3").place(x=190, y=10)

# ==========================================
# 17. PACK AND GRID EXAMPLES
# ==========================================
tk.Label(content, text="14. Pack Geometry Manager", bg="lightblue").pack(pady=5)

pack_frame = tk.Frame(content, bg="lightblue")
pack_frame.pack()

tk.Button(pack_frame, text="Pack 1").pack(side="left", padx=3)
tk.Button(pack_frame, text="Pack 2").pack(side="left", padx=3)
tk.Button(pack_frame, text="Pack 3").pack(side="left", padx=3)

tk.Label(content, text="15. Grid Geometry Manager", bg="lightblue").pack(pady=5)

grid_frame = tk.Frame(content, bg="white")
grid_frame.pack(pady=3)

tk.Button(grid_frame, text="Row 0 Col 0").grid(row=0, column=0, padx=3, pady=3)
tk.Button(grid_frame, text="Row 0 Col 1").grid(row=0, column=1, padx=3, pady=3)
tk.Button(grid_frame, text="Row 1 (Two Columns)",).grid(row=1, column=0, columnspan=2, padx=3, pady=3)

# ==========================================
# 18. EXIT BUTTON
# ==========================================
tk.Button(
    content,
    text="EXIT PROGRAM",
    command=exit_program,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

# ==========================================
# 19. RUN APPLICATION
# ==========================================
root.mainloop()
