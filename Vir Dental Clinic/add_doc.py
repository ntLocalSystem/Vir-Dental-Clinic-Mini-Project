import tkinter as tk
import calendar as cal
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as msg
import doctor_operations as dp
import splash as log


class dashboard:
	
	def __init__(self, master, user_name):
		self.master = master
		master.title("Vir Dental Clinic")
		# ---------Main Frame----------------

		self.frame = tk.Frame(root, bg="orange")
		self.frame.place(relx=0, rely=0, relwid=1, relheight=1)

		# ---------Logo / Header Frame-------

		self.frameProj = tk.Frame(root, bg="#222649")
		self.frameProj.place(relx=0, rely=0, relwid=1, relheight=0.15)


		self.foto = tk.PhotoImage(file="logo_doctor_main.gif")

		self.icon1 = tk.Label(self.frameProj, image=self.foto)
		self.icon1.place(relx=0.02, rely=0.1, relwidth=0.07, relheight=0.81)
		self.icon1['bg'] = self.icon1.master['bg']

		self.projName = tk.Label(self.frameProj, text="Vir Dental Clinic", font="helvetica 45", bg="#222649", fg="#fff")
		self.projName.place(relx=0.09, rely=0, relwid=0.25, relheight=1)


		# ---------Work Area Frame-----------
		self.frameWork = tk.Frame(root, bg="lightgray")
		self.frameWork.place(relx=0.155, rely=0.16, relwidth=0.655, relheight=0.83)

		self.innerworkFrame1 = tk.Frame(self.frameWork, bg="lightgray")
		self.innerworkFrame1.pack(fill=tk.BOTH, expand=1)

		# -----------ADD DOCTOR-----------
		self.innerworkFrame = tk.Frame(self.frameWork, bg="lightgray")

		self.adddoc = tk.Label(self.innerworkFrame, bg="#fff", fg="#222649", text="ADD DOCTOR", bd=0, font="arial 42 bold")
		self.adddoc.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.1)
		self.adddoc['bg'] = self.adddoc.master['bg']

		# -----------DOCTOR ID------------
		# self.doc_id = tk.Label(self.innerworkFrame, bg="lightgray",text="Doctor ID:", anchor='w', bd=0, font="helvetica 25")
		# self.doc_id.place(relx=0.05, rely=0.15, relwid=0.2, relheight=0.08)

		# self.doc_id_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		# self.doc_id_field.place(relx=0.05, rely=0.23, relwidth=0.25, relheight=0.05)

		# -----------DOCTOR NAME------------
		self.doc_name = tk.Label(self.innerworkFrame, bg="lightgray",text="Name:", anchor='w', bd=0, font="helvetica 25")
		self.doc_name.place(relx=0.05, rely=0.15, relwid=0.2, relheight=0.08)

		self.doc_name_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		self.doc_name_field.place(relx=0.05, rely=0.23, relwidth=0.25, relheight=0.05)

		# -----------DOCTOR EMAIL-------------
		self.doc_email = tk.Label(self.innerworkFrame, bg="lightgray",text="Email ID:", anchor='w', bd=0, font="helvetica 25")
		self.doc_email.place(relx=0.05, rely=0.47, relwid=0.2, relheight=0.08)

		self.doc_email_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		self.doc_email_field.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.05)

		# -------------DOCTOR QUALIFICATION-----
		self.doc_qualification = tk.Label(self.innerworkFrame, bg="lightgray",text="Qualification:", anchor='w', bd=0, font="helvetica 25")
		self.doc_qualification.place(relx=0.05, rely=0.63, relwid=0.2, relheight=0.08)

		self.doc_qualification_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		self.doc_qualification_field.place(relx=0.05, rely=0.71, relwidth=0.25, relheight=0.05)

		# ----------DOCTOR'S EXPERIENCE--------
		# self.doc_exp = tk.Label(self.innerworkFrame, bg="lightgray",text="Experience in Years:", anchor='w', bd=0, font="helvetica 25")
		# self.doc_exp.place(relx=0.45, rely=0.31, relwid=0.3, relheight=0.08)

		# self.doc_exp_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		# self.doc_exp_field.place(relx=0.45, rely=0.39, relwidth=0.25, relheight=0.05)

		# ----------DOCTOR'S SPECIALITY---------
		self.doc_speciality = tk.Label(self.innerworkFrame, bg="lightgray", text="Speciality:", anchor='w', bd=0, font="helvetica 25")
		self.doc_speciality.place(relx=0.05, rely=0.31, relwid=0.2, relheight=0.08)

		self.doc_speciality_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		self.doc_speciality_field.place(relx=0.05, rely=0.39, relwidth=0.25, relheight=0.05)

		# -----------DOC'S GENDER---------------
		self.gender = tk.Label(self.innerworkFrame, text="Gender:", bg="lightgray", anchor='w', bd=0, font="helvetica 25")
		self.gender.place(relx=0.45, rely=0.15, relwid=0.2, relheight=0.08)

		self.gender_type = tk.StringVar()
		self.gender_type.set('Female')
		self.gender_types_all = [ 'Female', 'Male' ]
		self.combo_gender = ttk.Combobox(self.innerworkFrame, textvariable=self.gender_type, values=self.gender_types_all, font="helvetica 16")
		self.combo_gender.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)

		# -----------PASSWORD---------
		self.pass_admin = tk.Label(self.innerworkFrame, bg="lightgray", text="Password:", anchor='w', bd=0, font="helvetica 25")
		self.pass_admin.place(relx=0.45, rely=0.31, relwid=0.3, relheight=0.08)

		self.pass_admin_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=0, font="helvetica 15")
		self.pass_admin_field.place(relx=0.45, rely=0.39, relwidth=0.25, relheight=0.05)

		def submit():
			dp.doctor_add(self.doc_qualification_field.get(), self.doc_name_field.get(), self.gender_type.get(), self.doc_email_field.get(), self.doc_speciality_field.get(), self.pass_admin_field.get(), user_name)
			self.doc_qualification_field.delete(0, 'end')
			self.doc_name_field.delete(0, 'end')
			self.doc_email_field.delete(0, 'end')
			self.doc_speciality_field.delete(0, 'end')
			self.pass_admin_field.delete(0, 'end')
			msg.showinfo("Vir Dental Clinic","Doctor Added!")



		# -----------SUBMIT--------------
		self.submit = tk.Button(self.innerworkFrame, bd=0, bg="green", fg="#fff", text="Submit", font="helvetica 20", command=submit)
		self.submit.place(relx=0.8, rely=0.9, relwidth=0.15, relheight=0.08)

		# self.doc_speciality_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=2, font="helvetica 16")
		# self.doc_speciality_field.place(relx=0.05, rely=0.23, relwidth=0.2, relheight=0.06)

		# # -------------DOCTOR'S PHONE NO----------
		# self.doc_phoneno = tk.Label(self.innerworkFrame, bg="lightgray",text="Doctor ID:", anchor='w', bd=0, font="helvetica 20")
		# self.doc_phoneno.place(relx=0.05, rely=0.15, relwid=0.2, relheight=0.08)

		# self.doc_phoneno_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=2, font="helvetica 16")
		# self.doc_phoneno_field.place(relx=0.05, rely=0.23, relwidth=0.2, relheight=0.06)

		# # ------------DOCTOR'S GENDER-------------
		# self.doc_gender = tk.Label(self.innerworkFrame, bg="lightgray",text="Doctor ID:", anchor='w', bd=0, font="helvetica 20")
		# self.doc_gender.place(relx=0.05, rely=0.15, relwid=0.2, relheight=0.08)

		# self.doc_gender_field = tk.Entry(self.innerworkFrame, bg="#fff", bd=2, font="helvetica 16")
		# self.doc_gender_field.place(relx=0.05, rely=0.23, relwidth=0.2, relheight=0.06)

		def addDoctor():
			# self.innerworkFrame
			self.innerworkFrame3.pack_forget()
			self.innerworkFrame1.pack_forget()
			self.innerworkFrame.pack(fill=tk.BOTH, expand=1)


		self.innerworkFrame3 = tk.Frame(self.frameWork, bg="lightgray")

		self.viewdoc = tk.Label(self.innerworkFrame3, bg="#fff", fg="#222649", text="DELETE DOCTOR", bd=0, font="arial 42 bold")
		self.viewdoc.place(relx=0.3, rely=0.005, relwidth=0.4, relheight=0.1)
		self.viewdoc['bg'] = self.adddoc.master['bg']

		self.displayDocts = tk.Frame(self.innerworkFrame3, bg="lightgray", bd=0)
		self.displayDocts.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.88)

		self.deleteDoc = tk.Frame(self.displayDocts, bg="#000", bd=0)
		self.deleteDoc.place(relx=0.025, rely=0, relwidth=0.95, relheight=0.9)


		# def viewDoctor():
			# self.innerworkFrame
			# self.innerworkFrame1.pack_forget()
			# self.innerworkFrame3.pack_forget()
			# self.innerworkFrame.pack_forget()
			# self.innerworkFrame3.pack(fill=tk.BOTH, expand=1)


		self.treeview_doctor_display = ttk.Treeview(self.deleteDoc)
		self.style = ttk.Style()
		self.style.configure('Treeview', rowheight=45, font=("helvetica",12))
		self.style.configure("Treeview.Heading", font=("helvetica", 14, "bold"))
		self.scroll_y = ttk.Scrollbar(self.deleteDoc, orient=tk.VERTICAL, command=self.treeview_doctor_display.yview)
		self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
		self.treeview_doctor_display.pack(fill=tk.BOTH, expand=1)
		self.treeview_doctor_display.config(columns=("Qualification", "Doctor_Username", "Gender", "Email", "Speciality"))
		self.treeview_doctor_display.column('#0',  width=150, anchor='center')
		self.treeview_doctor_display.column('Qualification',  width=150, anchor='center')
		self.treeview_doctor_display.column('Doctor_Username',  width=160, anchor='center')
		self.treeview_doctor_display.column('Gender',  width=150, anchor='center')
		self.treeview_doctor_display.column('Email',  width=220, anchor='center')
		self.treeview_doctor_display.column('Speciality',  width=150, anchor='center')
		self.treeview_doctor_display.heading('#0', text='Doctor ID')
		self.treeview_doctor_display.heading('Qualification', text='Qualification')
		self.treeview_doctor_display.heading('Doctor_Username', text='Doctor Username')
		self.treeview_doctor_display.heading('Gender', text='Gender')
		self.treeview_doctor_display.heading('Email', text='Email')
		self.treeview_doctor_display.heading('Speciality', text='Speciality')

		
		self.treeview_doctor_display.config(yscrollcommand = self.scroll_y.set)
		# self.scroll_y = ttk.Scrollbar(deleteDoc, orient=tk.VERTICAL, command=treeview_doctor_display.yview)

		def refresh_func():
		    conn = mysql.connector.connect(user='root', passwd='', port=3306, host='localhost', database='mini_project')
		    cur = conn.cursor()
		    query = 'SELECT * FROM doctor'
		    cur.execute(query)
		    for x in cur:
		        self.treeview_doctor_display.insert('', 'end', text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
    		# conn.close()

		def del_selected():
			conn = mysql.connector.connect(user='root', passwd='', port=3306, host='localhost', database='mini_project')
			cur = conn.cursor()
			ret_list = self.treeview_doctor_display.item(self.treeview_doctor_display.selection())
			doc_id_to_delete = int(ret_list['text'])
			query = 'delete from doctor where doc_id=%s'
			for i in self.treeview_doctor_display.get_children():
			    self.treeview_doctor_display.delete(i)
			cur.execute(query,(doc_id_to_delete, ))
			conn.commit()
			refresh_func()

		def delDoctor():
				# self.innerworkFrame
			self.innerworkFrame1.pack_forget()
			self.innerworkFrame3.pack_forget()
			self.innerworkFrame.pack_forget()
			self.innerworkFrame3.pack(fill=tk.BOTH, expand=1)
			for i in self.treeview_doctor_display.get_children():
			    self.treeview_doctor_display.delete(i)
			refresh_func()

		self.delBtn = tk.Button(self.displayDocts, bd=0, bg="#222649", font="helvetica 22 bold", text="Delete", fg="#fff", command=del_selected)
		self.delBtn.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.08)




		# for i in column:
		# 	for j in row:
		# 		self.dispDoc = tk.Label(self.innerworkFrame3, bg="#222649", bd=2, fg="#fff")
		# 		self.dispDoc.




		# self.frameWork = tk.Frame(self.innerworkFrame, bg="lightblue")
		# self.subinnerworkFrame.place(relx=0.02, rely=0.05, relwid=0.96, relheight=0.9)


		# ----------------Schdule Card--------------
		# self.scheduleCard = tk.Frame(self.subinnerworkFrame, bg="pink")
		# self.scheduleCard.place(relx=0.02, rely=0, relwid=0.13, relheight=0.27)

		# self.scheduleCard1 = tk.Frame(self.subinnerworkFrame, bg="pink")
		# self.scheduleCard1.place(relx=0.02, rely=0.30, relwid=0.13, relheight=0.27)\

		# window.update()
		# innerworkFrame.pack_forget()
		
		# ----------Note Frame---------------

		# ------Shedule--------


		self.foto1 = tk.PhotoImage(file="doc2.gif")

		self.frameDoc = tk.Frame(root, bg="orange")
		self.frameDoc.place(relx=0.815, rely=0.16, relwid=0.18, relheight=0.83)

		self.icon2 = tk.Label(self.frameDoc, image=self.foto1)
		self.icon2.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.icon2['bg'] = self.icon2.master['bg']

		def logout():
			root.destroy()
			log.main()



		#-----------Navigation Frame---------

		self.frameNav = tk.Frame(root, bg="gray")
		self.frameNav.place(relx=0, rely=0.15, relwid=0.15, relheight=1)


		# ------------Nav Buttons-------------

		# self.home = tk.Button(self.frameNav, text="Home", bg="#dbdbdb", bd=0, relief="flat", font="helvetica 14", activebackground="gray", activeforeground="white")
		# self.home.place(relx=0, rely=0, relwid=1, relheight=0.07)

		self.add_doctor = tk.Button(self.frameNav, text="Add Doctor", bg="#dbdbdb", font="helvetica 14", bd=0, command=addDoctor)
		self.add_doctor.place(relx=0, rely=0, relwid=1, relheight=0.07)

		self.del_doctor = tk.Button(self.frameNav, text="Delete Doctor", bg="#dbdbdb", font="helvetica 14", bd=0, command=delDoctor)
		self.del_doctor.place(relx=0, rely=0.07, relwid=1, relheight=0.07)

		# self.b3 = tk.Button(self.frameNav, text="View Doctors", bg="#dbdbdb", font="helvetica 14", bd=0)
		# self.b3.place(relx=0, rely=0.21, relwid=1, relheight=0.07)

		# self.setting = tk.Button(self.frameNav, text="Settings", bg="#dbdbdb", font="helvetica 14", bd=0)
		# self.setting.place(relx=0, rely=0.21, relwid=1, relheight=0.07)

		self.logout = tk.Button(self.frameNav, text="Logout", bg="#dbdbdb", font="helvetica 14", bd=0, activebackground="red", activeforeground="white", command=logout)
		self.logout.place(relx=0, rely=0.14, relwid=1, relheight=0.07)

# --------------END-----------------

def main(user_name):
	global root
	root = tk.Tk()
	root.geometry("1920x1080")
	dentalDashboard = dashboard(root, user_name)
	root.mainloop()
main('admin')