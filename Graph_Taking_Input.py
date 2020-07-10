import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

x = [1,2,3,4,5]
y = [5,2,3,4,1]

fig, axes = plt.subplots(1,1)
axes.plot(x , y)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

index = 6

print(fig.axes)

def _input():
	global index
	global x, y
	global fig
	global root

	try:
		txt = ((new_data.get("1.0","end")).replace(" ", "")).replace("\n", "")		
		y.append(int(txt))
		x.append(index)
		index+=1
	except:
		print("value issue")
	#print(x)
	#print(y)

	fig.axes[0].clear()
	fig.axes[0].plot(x , y)	
	canvas.draw()
	#root.update()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button_q = tkinter.Button(master=root, text="Quit", command=_quit)
button_q.pack(side=tkinter.BOTTOM)

new_data = tkinter.Text(root, height=1, width=20)
new_data.pack(side=tkinter.BOTTOM)

button_i = tkinter.Button(master=root, text="Input", command=_input)
button_i.pack(side=tkinter.BOTTOM)

tkinter.mainloop()