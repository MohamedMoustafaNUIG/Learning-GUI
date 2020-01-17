from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Images and Icons')

root.geometry("610x400")
root.resizable(0, 0)

frame1 = LabelFrame(root, padx=100, pady=100)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, padx=100, pady=100)
frame2.grid(row=0, column=2, padx=10, pady=10)

r = IntVar()
r.set("2")

MODES = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
	Radiobutton(frame2, text=text, variable=pizza, value=mode,command  = lambda: clicked2(pizza.get())).pack()

def clicked1(value):
	global myLabel1

	myLabel1.grid_forget()
	myLabel1 = Label(root, text=r.get())
	myLabel1.grid(row=1, column=0, padx=10, pady=10)

def clicked2(value):
	global myLabel2

	myLabel2.grid_forget()
	myLabel2 = Label(root, text=pizza.get())
	myLabel2.grid(row=1, column=2, padx=10, pady=10)

Radiobutton(frame1, text = "Option 1", variable = r, value = 1, command = lambda: clicked1(r.get())).pack()
Radiobutton(frame1, text = "Option 2", variable = r, value = 2, command = lambda: clicked1(r.get())).pack()

myLabel1 = Label(root, text=r.get())
myLabel1.grid(row=1, column=0, padx=10, pady=10)

myLabel2 = Label(root, text=pizza.get())
myLabel2.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()