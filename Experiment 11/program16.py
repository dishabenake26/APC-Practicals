
from tkinter import *

main = Tk()
main.title("Message Example")

ourMessage = "This is our Message"

messageVar = Message(main, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()

main.mainloop()
