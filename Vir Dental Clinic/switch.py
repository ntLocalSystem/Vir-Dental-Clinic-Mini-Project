from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry("800x600")
time.sleep(4)

def switchframe():
	frame2.pack_forget()
	frame3 = Frame(frame1, bg="red")
	frame3.place(relx=0.2, rely=0.2, relwid=0.6, relheight=0.6)
	Button(frame3, text="Hello",command=prevframe).place(relx=0.5, rely=0.5)

def prevframe():
	global frame2
	frame1 = Frame(root, bg="pink")
	frame1.place(relx=0, rely=0, relwid=1, relheight=1)
	frame2 = Frame(frame1, bg="Blue", height=200, width=200)
	frame2.pack()

Button(frame2, text="Portal to Frame 3", command=switchframe).place(relx=0.5, rely=0.5)


root=mainloop()