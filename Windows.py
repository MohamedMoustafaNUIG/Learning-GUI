from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from os import listdir
from os.path import isfile, join,abspath


cwd = abspath(__file__+"/..")

root = Tk()
root.title('File Explorer')

top = Toplevel()

file_list = [x for x in listdir(cwd)]
file_button_list = []

for file in file_list:
	newB = button = Button(top, text=file).pack()

root.mainloop()