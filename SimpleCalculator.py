from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5, state=DISABLED)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def shiftList(li, startPos):
	i=startPos
	while li[i] !=None and i<len(li):
		li[i] = li[i+1]
		i=i+1
	li[i] = None

def split(word):
	return [char for char in word]

def button_write(sym):
	curr = e.get()
	e['state'] = NORMAL
	e.delete(0, END)
	#e.insert(0, curr+" "+sym+" ")
	e.insert(0, curr+sym)
	e['state'] = DISABLED

def evaluateExp():
	exp = split(e.get())
	numBuffer = []
	opBuffer = []
	i=0
	while i<len(exp):
		temp=[]
		while(i<len(exp) and (exp[i]!='+' and exp[i]!='-')):
			temp.append(exp[i])
			i=i+1
		numBuffer.append(temp)
		if(i<len(exp)):
			opBuffer.append(exp[i])
		i=i+1

	while numBuffer[1] is not None:
		if opBuffer[0] == '+':
			numBuffer[0] = int(''.join(numBuffer[0])) + int(''.join(numBuffer[1]))
			numBuffer = shiftList(numBuffer, 1)
			opBuffer = shiftList(opBuffer, 1)
		elif opBuffer[1] == '-':
			numBuffer[0] = int(''.join(numBuffer[0])) - int(''.join(numBuffer[1]))
			numBuffer = shiftList(numBuffer, 1)
			opBuffer = shiftList(opBuffer, 1)


def clearScreen():
	e['state'] = NORMAL
	e.delete(0, END)
	e['state'] = DISABLED

b0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_write("0"))
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_write("1"))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_write("2"))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_write("3"))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_write("4"))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_write("5"))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_write("6"))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_write("7"))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_write("8"))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_write("9"))

plusB = Button(root, text="+", padx=40, pady=20, command=lambda: button_write("+"))
minusB = Button(root, text="-", padx=40, pady=20, command=lambda: button_write("-"))
equalB = Button(root, text="=", padx=39, pady=20, command=evaluateExp)

clearB = Button(root, text="Clear", padx=86, pady=20, command=clearScreen)

b0.grid(row=4, column=0)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

plusB.grid(row=4, column=1)
minusB.grid(row=4, column=2)
equalB.grid(row=5, column=0)
clearB.grid(row=5, column=1, columnspan=2)


root.mainloop()