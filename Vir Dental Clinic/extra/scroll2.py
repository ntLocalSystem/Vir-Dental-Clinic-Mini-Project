from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,0,500))
def schedule():
	name = [ 'Mildeep' , 'Rohit', 'Vir' , 'Virti' , 'Nishit', 'visible??' , 'ashwini' , 'janvi']
	time = [ '14:30' , '15:15']
	y1 = 0
	y2 = 0.16
	for i in name:
		visitor1 = Frame(canvas, bg="#fff", width=350, height=90)
		# self.visitor1.place(relx=0, rely=y1, relwid=1, relheight=0.15)
		# self.visitor1.place(relx=0, rely=y1)
		visitor1.pack()
		# self.visitor1.grid(row=0, column=0)

		vistorPic1 = Label(visitor1, bg="#fff")
		vistorPic1.place(relx=0, rely=0, relwid=0.25, relheight=1)

		visitorDetail1 = Frame(visitor1, bg="black")
		visitorDetail1.place(relx=0.25, rely=0, relwid=0.75, relheight=1)

		visitorName1 = Label(visitorDetail1, bg="white", fg="black", text=i, font="arial 18 bold", anchor="sw")
		visitorName1.place(relx=0, rely=0, relwid=1, relheight=0.6)

		visitingTime1 = Label(visitorDetail1, bg="white", fg="black", text="Time: {}".format(time), font="areil 12", anchor="nw")
		visitingTime1.place(relx=0, rely=0.6, relwid=1, relheight=0.4)

		seperator1 = Label(canvas, text="_______________________", font="helvetica 5 bold", fg="gray", width=350, height=1)
		# self.seperator1.place(relx=0.05, rely=y2, relwid=0.9, relheight=0.005)
		# self.seperator1.place(relx=0.05, rely=y2)
		seperator1.pack()
		# self.seperator1.grid(row=1, column=0)

		# subCanvasNote.bind('<Configure>', on_configure)

schedule()
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()