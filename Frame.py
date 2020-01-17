from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Images and Icons')
root.iconbitmap('C:\\Users\\mmoustafa\\Desktop\\PythonGUI\\imgIcon.ico')


frame1 = LabelFrame(root, padx=100, pady=100)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, padx=100, pady=100)
frame2.grid(row=0, column=2, padx=10, pady=10)

frame3 = LabelFrame(root, text="This is my frame ...", padx=100, pady=100)
frame3.grid(row=1, column=1, padx=10, pady=10)

b1 = Button(frame1, text = "Dont click here")
b1.pack()

b2 = Button(frame2, text = "Dont click here")
b2.pack()

b3 = Button(frame3, text = "Dont click here")
b3.pack()

root.mainloop()