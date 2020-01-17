from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Button Clicked")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
#myButton = Button(root, text="Click Me!", state=DISABLED, padx=50, pady=50)
myButton.pack()

root.mainloop()