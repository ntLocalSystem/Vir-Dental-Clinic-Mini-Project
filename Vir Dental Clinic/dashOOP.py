import tkinter as tk
from tkinter import ttk
import calendar as cal
import time


# foto = tk.PhotoImage(file="logo_doctor_main.gif")

# root.geometry("1920x1080")

class dashboard:
	
	def __init__(self, master):
		# time.sleep(5)
		self.master = master
		master.title("Vir Dental Clinic")
		self.foto = tk.PhotoImage(file="logo_doctor_main.gif")
		# ---------Main Frame----------------

		self.frame = tk.Frame(root, bg="green")
		self.frame.place(relx=0, rely=0, relwid=1, relheight=1)

		# ---------Logo / Header Frame-------

		self.frameProj = tk.Frame(root, bg="#222649")
		self.frameProj.place(relx=0, rely=0, relwid=1, relheight=0.15)

		self.icon1 = tk.Label(self.frameProj, image=self.foto)
		self.icon1.place(relx=0.02, rely=0.1, relwidth=0.07, relheight=0.81)
		self.icon1['bg'] = self.icon1.master['bg']

		self.projName = tk.Label(self.frameProj, text="Vir Dental Clinic", font="helvetica 45", bg="#222649", fg="#fff")
		self.projName.place(relx=0.09, rely=0, relwid=0.25, relheight=1)


		# ---------EMPTY Work Area Frame-----------
		self.frameWork = tk.Frame(root, bg="#fff")
		self.frameWork.place(relx=0.15, rely=0.15, relwidth=0.655, relheight=0.85)
		
		self.innerworkFrame1 = tk.Frame(self.frameWork, bg="#fff")
		self.innerworkFrame1.pack(fill=tk.BOTH, expand=1)


		# ---------HOME Work Area Frame-----------
		def homeframe():
			self.innerworkFrame1.pack_forget()
			self.innerworkScheduleFrame.pack_forget()
			self.innerworkFrame.pack(fill=tk.BOTH, expand=1)
			# master.update()
			# self.innerworkFrame.pack_forget()
			# self.frameWork1 = tk.Frame(root, bg="#fff")
			# self.frameWork1.place(relx=0.155, rely=0.16, relwidth=0.655, relheight=0.83)

		self.innerworkFrame = tk.Frame(self.frameWork, bg="#fff")
		

		self.doc = tk.Label(self.innerworkFrame, text="Hello, Dr.Vir Navalkar", font="helvetica 40 bold", bd=0, bg="#fff", fg="#222649")
		# self.doc.place(relx=0.3, rely=0.3)
		self.doc.pack(pady=200)


		# ===================SCHEDULE MODULE====================
		def scheduleFrame():

			self.innerworkFrame1.pack_forget()
			self.innerworkFrame.pack_forget()
			self.innerworkScheduleFrame.pack(fill=tk.BOTH, expand=1)

			# self.frameWork = tk.Frame(root, bg="lightgray")
			# self.frameWork.place(relx=0.155, rely=0.16, relwidth=0.655, relheight=0.83)

		self.innerworkScheduleFrame = tk.Frame(self.frameWork, bg="#fff")
			

		# self.schedule.configure(enable='false')


		# self.frameWork = tk.Frame(self.innerworkFrame, bg="lightblue")
		# self.subinnerworkFrame.place(relx=0.02, rely=0.05, relwid=0.96, relheight=0.9)


		# ----------------Schdule Card--------------
		# self.scheduleCard = tk.Frame(self.subinnerworkFrame, bg="pink")
		# self.scheduleCard.place(relx=0.02, rely=0, relwid=0.13, relheight=0.27)

		# self.scheduleCard1 = tk.Frame(self.subinnerworkFrame, bg="pink")
		# self.scheduleCard1.place(relx=0.02, rely=0.30, relwid=0.13, relheight=0.27)\

		# window.update()
		# innerworkFrame.pack_forget()

		self.displayFrame = tk.Frame(self.innerworkScheduleFrame, bg="#222649")
		self.displayFrame.place(relx=0.315, rely=0.03, relwid=0.665, relheight=0.45)

		# ---------BOTTOM FRAME------------------
		self.detailsFrame = tk.Frame(self.innerworkScheduleFrame, bg="#222649")
		self.detailsFrame.place(relx=0.02, rely=0.5, relwid=0.96, relheight=0.48)

		self.calender = tk.Frame(self.innerworkScheduleFrame, bg="#222649", highlightbackground="#222649", highlightthickness=2)
		self.calender.place(relx=0.02, rely=0.03, relwid=0.275, relheight=0.45)

		self.calenderHead = tk.Frame(self.calender, bg="black")
		self.calenderHead.place(relx=0, rely=0, relwid=1, relheight=0.13)

		self.prevMonth = tk.Button(self.calenderHead, bg="#fff", text="<", font="freesans 16", bd=0)
		self.prevMonth.place(relx=0, rely=0, relwid=0.15, relheight=1)

		self.nextMonth = tk.Button(self.calenderHead, bg="#fff", text=">", font="freesans 16", bd=0)
		self.nextMonth.place(relx=0.85, rely=0, relwid=0.15, relheight=1)

		# -----------------Dynamic month names
		self.calenderTitle = tk.Label(self.calenderHead, bg="#fff", text="")
		self.calenderTitle.place(relx=0.15, rely=0, relwid=0.7, relheight=1)

		self.dates = tk.Frame(self.calender, bg="pink")
		self.dates.place(relx=0, rely=0.23, relwid=1, relheight=0.77)
		# ------------------Dynamic Month Values
		# month = [ 'January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

		def monthPrev():
			year = 2019
			month = [ 'January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December' ]
			month = month[3]


		year = 2019
		month = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ]
		list1 = []
		for i in month:
			list1.insert(i,cal.month(year, i))

		self.calenderTitle = tk.Label(self.calenderHead, bg="#fff", text="March", fg="#222649", font="helvetica 16")
		self.calenderTitle.place(relx=0.15, rely=0, relwid=0.7, relheight=1)	
		week = [ 'MON' , 'TUE', 'WED' , 'THU' , 'FRI' , 'SAT' , 'SUN']
		wid = 0
		for i in week:
			self.week = tk.Label(self.calender, bg="#222649", text=i, fg="#fff", bd=1)
			self.week.place(relx=wid, rely=0.13, relwid=0.14, relheight=0.1)
			wid = wid + 0.142857

		x = 0
		y = 0
		d = 1

		for i in range(5):
			j = 7
			x = 0
			for j in range(7):
				self.dateFrame = tk.Button(self.dates, bg="#fff", fg="#222649", bd=0, text=d)
				self.dateFrame.place(relx=x, rely=y, relwid=0.142857, relheight=0.2)
				d = d + 1
				x = x + 0.142857
			y = y + 0.2

			# for i  in range (0, 36):
			# 	self.date = tk.Button(self.dateFrame, bg="#fff", bd=1)
			# 	self.place(relx=0, rely=0, relwidth=)


		self.treeview_doctor_display = ttk.Treeview(self.displayFrame)
		self.style = ttk.Style()
		self.style.configure('Treeview', rowheight=45, font=("helvetica",12))
		self.style.configure("Treeview.Heading", font=("helvetica", 14, "bold"))
		self.scroll_y = ttk.Scrollbar(self.displayFrame, orient=tk.VERTICAL, command=self.treeview_doctor_display.yview)
		self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
		self.treeview_doctor_display.pack(fill=tk.BOTH, expand=1)
		self.treeview_doctor_display.config(columns=("Qualification", "Doctor_Username", "Gender", "Email", "Speciality"))
		self.treeview_doctor_display.column('#0',  width=150, anchor='center')
		self.treeview_doctor_display.column('Qualification',  width=150, anchor='center')
		self.treeview_doctor_display.column('Doctor_Username',  width=180, anchor='center')
		self.treeview_doctor_display.column('Gender',  width=170, anchor='center')
		self.treeview_doctor_display.column('Email',  width=20, anchor='center')
		# self.treeview_doctor_display.column('Speciality',  width=150, anchor='center')
		self.treeview_doctor_display.heading('#0', text='Patient ID')
		self.treeview_doctor_display.heading('Doctor_Username', text='Patient Username')
		self.treeview_doctor_display.heading('Qualification', text='Patient Age')
		self.treeview_doctor_display.heading('Gender', text='Gender')
		self.treeview_doctor_display.heading('Email', text='Email')
		# self.treeview_doctor_display.heading('Speciality', text='Speciality')

		
		self.treeview_doctor_display.config(yscrollcommand = self.scroll_y.set)
		# self.scroll_y = ttk.Scrollbar(deleteDoc, orient=tk.VERTICAL, command=treeview_doctor_display.yview)

		def refresh_func():
		    conn = mysql.connector.connect(user='root', passwd='', port=3306, host='localhost', database='mini_project')
		    cur = conn.cursor()
		    query = 'SELECT * FROM patient'
		    cur.execute(query)
		    for x in cur:
		        self.treeview_doctor_display.insert('', 'end', text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
    		# conn.close()




		# ------Shcedule--------
		def on_configure(event):
			self.subCanvasNote.configure(scrollregion=self.subCanvasNote.bbox('all'))

		self.frameNote = tk.Frame(root, bg="gray", highlightbackground="gray", highlightthickness=2)
		self.frameNote.place(relx=0.805, rely=0.15, relwid=0.195, relheight=0.53)

		self.upnext = tk.Label(self.frameNote, text="Upnext", bd=0, bg="gray", fg="white", font="helvetica 16", pady=10)
		# self.upnext.place(relx=0, rely=0, relwid=1, relheight=0.08)
		self.upnext.pack(side=tk.TOP)

		# self.scrollFrame = tk.Frame(self.frameNote, bg="black")
		# self.scrollFrame.place(relx=0.96, rely=0.08, relwid=0.04, relheight=1)

		# self.subCanvasNote = tk.Canvas(self.frameNote, bg="#fff", bd=0, scrollregion=(0,0,0,750))
		self.subCanvasNote = tk.Canvas(self.frameNote, bg="#fff", bd=0, width=350, height=700)
		# self.subCanvasNote.place(relx=0, rely=0.08, relwid=1, relheight=0.92)
		self.subCanvasNote.pack(side=tk.LEFT,expand=True)	

		# self.subCanvasNote.pack(side=tk.LEFT,expand=True)
		# , relheight=0.92



		self.vscrollbar = tk.Scrollbar(self.frameNote, orient=tk.VERTICAL, bd=0, highlightthickness=0, command=self.subCanvasNote.yview)
		self.vscrollbar.place(relx=1, rely=0.08, relwid=0.05, relheight=0.92, anchor='ne')

		# self.subframeNote = tk.Frame(self.subCanvasNote, bg="pink", bd=0)

		# self.subCanvasNote.create_window(0, 0, window=self.subframeNote)
		# self.subframeNote.place(relx=0, rely=0, relwid=0.95, relheight=1)


		# self.subframeNote.pack(fill=tk.BOTH, expand=1)

		# self.subCanvasNote.bind('<Configure>', on_configure)
		# self.subCanvasNote.create_window(0, 0, window=self.subframeNote)


		# self.vscrollbar.config(command=self.subCanvasNote.yview)
		# self.subCanvasNote.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)	

		# -------LIST----------

		def schedule(self):
			name = [ 'Mildeep' , 'Rohit', 'Vir' , 'Virti' , 'Nishit', 'visible??' , 'ashwini' , 'janvi']
			time = [ '14:30' , '15:15']
			y1 = 0
			y2 = 0.16
			for i in name:
				self.visitor1 = tk.Frame(self.subCanvasNote, bg="#fff", width=350, height=90)
				# self.visitor1.place(relx=0, rely=y1, relwid=1, relheight=0.15)
				# self.visitor1.place(relx=0, rely=y1)
				self.visitor1.pack()
				# self.visitor1.grid(row=0, column=0)

				self.vistorPic1 = tk.Label(self.visitor1, bg="#fff")
				self.vistorPic1.place(relx=0, rely=0, relwid=0.25, relheight=1)

				self.visitorDetail1 = tk.Frame(self.visitor1, bg="black")
				self.visitorDetail1.place(relx=0.25, rely=0, relwid=0.75, relheight=1)

				self.visitorName1 = tk.Label(self.visitorDetail1, bg="white", fg="black", text=i, font="arial 18 bold", anchor="sw")
				self.visitorName1.place(relx=0, rely=0, relwid=1, relheight=0.6)

				self.visitingTime1 = tk.Label(self.visitorDetail1, bg="white", fg="black", text="Time: {}".format(time), font="areil 12", anchor="nw")
				self.visitingTime1.place(relx=0, rely=0.6, relwid=1, relheight=0.4)

				self.seperator1 = tk.Label(self.subCanvasNote, text="_______________________", font="helvetica 5 bold", fg="gray", width=350, height=1)
				# self.seperator1.place(relx=0.05, rely=y2, relwid=0.9, relheight=0.005)
				# self.seperator1.place(relx=0.05, rely=y2)
				self.seperator1.pack()
				# self.seperator1.grid(row=1, column=0)

				y1 = y1 + 0.165
				y2 = y2 + 0.165

				self.subCanvasNote.bind('<Configure>', on_configure)

		schedule(self)


		# self.subCanvasNote.bind('<Configure>', on_configure)

		self.subCanvasNote.config(yscrollcommand=self.vscrollbar.set)

		

		# --------------------------------------------------VISITOR-2

		'''------------INCREASE Y---------------'''
		# self.visitor2 = tk.Frame(self.subframeNote, bg="#fff")
		# self.visitor2.place(relx=0, rely=0.165, relwid=1, relheight=0.15)

		# self.vistorPic2 = tk.Label(self.visitor2, bg="#fff")
		# self.vistorPic2.place(relx=0, rely=0, relwid=0.25, relheight=1)

		# self.visitorDetail2 = tk.Frame(self.visitor2, bg="black")
		# self.visitorDetail2.place(relx=0.25, rely=0, relwid=0.75, relheight=1)

		# self.visitorName2 = tk.Label(self.visitorDetail2, bg="white", fg="black", text="Rohit Mutalik, 30", font="areil 18 bold", anchor="sw")
		# self.visitorName2.place(relx=0, rely=0, relwid=1, relheight=0.6)

		# self.visitingTime2 = tk.Label(self.visitorDetail2, bg="white", fg="black", text="Time: 15:15", font="areil 12", anchor="nw")
		# self.visitingTime2.place(relx=0, rely=0.6, relwid=1, relheight=0.4)
		# '''-----------INCREASE Y---------------'''
		# self.seperator2 = tk.Label(self.subframeNote, text="_______________________", font="helvetica 30", fg="gray")
		# self.seperator2.place(relx=0.05, rely=0.325, relwid=0.9, relheight=0.005)

		# --------NOTE--------

		self.frameNote2 = tk.Frame(root, bg="gray")
		self.frameNote2.place(relx=0.805, rely=0.68, relwid=0.195, relheight=0.35)

		self.note = tk.Label(self.frameNote2, text="Note", bd=0, bg="gray", fg="white", font="helvetica 16")
		self.note.place(relx=0, rely=0, relwid=1, relheight=0.15)

		self.subframeNote2 = tk.Frame(self.frameNote2, bg="#f7ef3e")
		self.subframeNote2.place(relx=0, rely=0.14, relwid=1, relheight=0.9)


		#-----------Navigation Frame---------

		self.frameNav = tk.Frame(root, bg="gray")
		self.frameNav.place(relx=0, rely=0.15, relwid=0.15, relheight=1)


		# ------------Nav Buttons-------------

		self.home = tk.Button(self.frameNav, text="Home", bg="#dbdbdb", bd=0, relief="flat", font="helvetica 14", activebackground="gray", activeforeground="white", command=homeframe)
		self.home.place(relx=0, rely=0, relwid=1, relheight=0.07)

		self.schedule = tk.Button(self.frameNav, text="Schedule", bg="#dbdbdb", font="helvetica 14", bd=0, command=scheduleFrame)
		self.schedule.place(relx=0, rely=0.07, relwid=1, relheight=0.07)

		self.chart = tk.Button(self.frameNav, text="Chart", bg="#dbdbdb", font="helvetica 14", bd=0)
		self.chart.place(relx=0, rely=0.14, relwid=1, relheight=0.07)

		self.b3 = tk.Button(self.frameNav, text="b3", bg="#dbdbdb", font="helvetica 14", bd=0)
		self.b3.place(relx=0, rely=0.21, relwid=1, relheight=0.07)

		self.setting = tk.Button(self.frameNav, text="Settings", bg="#dbdbdb", font="helvetica 14", bd=0)
		self.setting.place(relx=0, rely=0.28, relwid=1, relheight=0.07)

		self.logout = tk.Button(self.frameNav, text="Logout", bg="#dbdbdb", font="helvetica 14", bd=0, activebackground="red", activeforeground="white")
		self.logout.place(relx=0, rely=0.35, relwid=1, relheight=0.07)


# --------------END-----------------
def main():
	global root
	root = tk.Tk()
	root.geometry("1920x1080")
	dentalDashboard = dashboard(root)
	root.mainloop()

# main()