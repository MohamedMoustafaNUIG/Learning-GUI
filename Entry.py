from tkinter import *

root = Tk()

#e = Entry(root, width=50, bg="red", fg="white", borderwidth=5)
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")

def myClick():
	myLabel = Label(root, text=e.get())
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()