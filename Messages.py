from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Images and Icons')

#showinfo, showwarning, showerror, askquestion("yes" or "no"), asktocancel(1 or 0), askyesno(1 or 0)
def popup():
	response = messagebox.askquestion("Age Verification", "Are you 18 or above?")

	if response == "yes":
		messagebox.showinfo("", "Then proceed")
	elif response == "no":
		messagebox.showerror("", "Then go back")


Button(root, text = "Popup", command=popup).pack()

root.mainloop()