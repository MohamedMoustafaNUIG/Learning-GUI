from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images and Icons')

root.iconbitmap('C:\\Users\\mmoustafa\\Desktop\\PythonGUI\\gearIcon.ico')


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open('C:\\Users\\mmoustafa\\Desktop\\PythonGUI\\nuig.jpg'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()