from tkinter import *


class mFrame: 

	def __init__(self):

		
		frame = Tk()
		frame.title("test");

		label = Label(frame, text="Hello World")
		label.pack()

		frame.mainloop()

