from tkinter import *
from PIL import ImageTk, Image

from os import listdir
from os.path import isfile, join,abspath


cwd = abspath(__file__+"/..")
imgDir = cwd+"/Images/"

image_name_list = [x for x in listdir(imgDir)]
image_list = []


root = Tk()
root.title('Image Viewer')
root.iconbitmap('C:\\Users\\mmoustafa\\Desktop\\PythonGUI\\imgIcon.ico')

'''
root.geometry("600x500")
root.resizable(0, 0)
'''

for i in range(0,len(image_name_list)):
	my_img = ImageTk.PhotoImage(Image.open("Images/"+image_name_list[i]))
	image_list.append(my_img)


def forward(image_number):
	global my_label
	global button_forward
	global button_back
	global status_bar

	toGet_num = (image_number+1)%len(image_list)

	my_label.grid_forget()
	my_label = Label(image = image_list[toGet_num])
	my_label.grid(row=0, column=0, columnspan=3)

	button_back = Button(root, text="<<", command=lambda: back(toGet_num))
	button_exit = Button(root, text="Exit Program", command=root.quit)
	button_forward = Button(root, text=">>", command=lambda: forward(toGet_num))


	button_back.grid(row=1, column=0)
	button_exit.grid(row=1, column=1)
	button_forward.grid(row=1, column=2)

	status_bar.grid_forget()
	status_bar = Label(root, text="Image "+str(toGet_num+1)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
	global my_label
	global button_forward
	global button_back
	global status_bar

	toGet_num = (image_number-1)%len(image_list)

	my_label.grid_forget()
	my_label = Label(image = image_list[toGet_num])
	my_label.grid(row=0, column=0, columnspan=3)

	button_back = Button(root, text="<<", command=lambda: back(toGet_num))
	button_exit = Button(root, text="Exit Program", command=root.quit)
	button_forward = Button(root, text=">>", command=lambda: forward(toGet_num))


	button_back.grid(row=1, column=0)
	button_exit.grid(row=1, column=1)
	button_forward.grid(row=1, column=2)

	status_bar.grid_forget()
	status_bar = Label(root, text="Image "+str(toGet_num+1)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=	image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=lambda: back(0))
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(0))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


status_bar = Label(root, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()