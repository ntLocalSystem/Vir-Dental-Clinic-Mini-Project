import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import login as login
import mysql.connector
# import mysql.connector as mysqlcon

# root = tk.Tk()
# logo = tk.PhotoImage(file="user-edit-icon1.png")
# logo2 = tk.PhotoImage(file="signup_image.gif")


# root.geometry("1920x1080")

class sign_up:
	def __init__(self,parent):
		self.frame1 = tk.Frame(root, bg="white")
		self.frame1.place(relx=0.35, rely=0.1, relwid=0.22, relheight=0.7)

		self.frame = tk.Frame(self.frame1, bg="white", highlightbackground="#ffb916", highlightthickness=2)
		self.frame.place(relx=0, rely=0.1, relwid=1, relheight=0.9)


		self.logo = tk.PhotoImage(file="user-edit-icon1.png")
		self.logo2 = tk.PhotoImage(file="signup_image.gif")



		# =======Imgs=========

		# canvas = tk.Canvas(frame1, width=180, height=180, bd=0,
		#                 highlightthickness=0)
		# canvas.pack()

		# mask = tk.PhotoImage(width=200, height=200)
		# cx,cy = 100,100 # image & circle center point
		# r = 63         # circle radius
		# r_squared = r*r
		# for y in range(200):
		#     for x in range(200):
		#         # using the formula for a circle:
		#         # (x - h)^2 + (y - k)^2 = r^2
		#         # any pixel outside our circle gets filled
		#         if (x - cx)**2 + (y - cy)**2 > r_squared:
		#             mask.put('blue', (x,y))

		# canvas.create_image(100,100, image=mask, anchor='c')

		# myimage = tk.PhotoImage(file='avatar2.png')
		# item = canvas.create_image(100,100, image=myimage, anchor='c')
		# canvas.lower(item)

		self.icon1 = tk.Label(self.frame1, image=self.logo)
		self.icon1.place(relx=0.34, rely=0, relwidth=0.35, relheight=0.2)
		self.icon1['bg'] = self.icon1.master['bg']

		self.acc_type_frame = tk.Frame(self.frame, bg="#fff", bd=0)
		self.acc_type_frame.place(relx=0.03, rely=0.21, relwidth=0.94, relheight=0.58)

		self.acc_type_innerEmptyframe = tk.Frame(self.acc_type_frame, bg="#fff", bd=0)
		self.acc_type_innerEmptyframe.pack(fill=tk.BOTH, expand=1)

		self.icon2 = tk.Label(self.acc_type_innerEmptyframe, image=self.logo2)
		self.icon2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
		# self.icon2.place(relx=0.45, rely=0.4)
		self.icon2['bg'] = self.icon2.master['bg']

		self.acc_type_innerframe_patient = tk.Frame(self.acc_type_frame, bg="#fff", bd=0)

		self.acc_type_innerframe_admin = tk.Frame(self.acc_type_frame, bg="#fff", bd=0)


		# ==========AccType=============
		self.logType = tk.Label(self.frame, text="Select Type", bg="white", font="helvetica 20")
		self.logType.place(relx=0, rely=0.08, relwidth=0.4, relheight=0.08)
		global acc_type
		self.acc_type = tk.StringVar()
		self.acc_type.set('Patient')
		self.acc_all_types = [ 'Patient', 'User' ]
		self.comboacc = ttk.Combobox(self.frame, textvariable=self.acc_type, values=self.acc_all_types, font="helvetica 16")
		self.comboacc.place(relx=0.03, rely=0.15, relwid=0.94, relheight=0.05)

		self.comboacc.bind('<<ComboboxSelected>>', lambda e: combomethod())

		# @staticmethod
		def combomethod():
			if self.acc_type.get()=='Patient':
				self.acc_type_innerEmptyframe.pack_forget()
				self.acc_type_innerframe_admin.pack_forget()
				self.acc_type_innerframe_patient.pack(fill=tk.BOTH, expand=1)

			elif self.acc_type.get()=='User':
				self.acc_type_innerEmptyframe.pack_forget()
				self.acc_type_innerframe_patient.pack_forget()
				self.acc_type_innerframe_admin.pack(fill=tk.BOTH, expand=1)
		
		# self.acc_type_innerframe_patient.pack(fill=tk.BOTH, expand=1)		

		# # -------Username---------
		self.username = tk.Label(self.acc_type_innerframe_patient, text="Username", bg="white", font="helvetica 20")
		self.username.place(relx=0, rely=0, relwidth=0.32, relheight=0.1)

		self.uname = tk.Entry(self.acc_type_innerframe_patient, bd=0, bg="lightgray", font="helvetica 16")
		self.uname.place(relx=0, rely=0.1, relwidth=1, relheight=0.08)

		# ----------Password--------
		self.password = tk.Label(self.acc_type_innerframe_patient, text="Password", bg="white", font="helvetica 20")
		self.password.place(relx=0, rely=0.19, relwidth=0.3, relheight=0.1)

		self.passwd = tk.Entry(self.acc_type_innerframe_patient, bd=0, bg="lightgray", show="*", font="helvetica 20")
		self.passwd.place(relx=0, rely=0.29, relwidth=1, relheight=0.08)

		# ------------Email----------
		self.email = tk.Label(self.acc_type_innerframe_patient, text="Email Id", bg="white", font="helvetica 20")
		self.email.place(relx=0, rely=0.38, relwidth=0.25, relheight=0.1)

		self.emailid = tk.Entry(self.acc_type_innerframe_patient, bd=0, bg="lightgray", font="helvetica 16")
		self.emailid.place(relx=0, rely=0.48, relwidth=1, relheight=0.08)

		# ------------Age----------=
		self.age = tk.Label(self.acc_type_innerframe_patient, text="Age", bg="white", font="helvetica 20")
		self.age.place(relx=0, rely=0.57, relwidth=0.14, relheight=0.1)

		self.agefield = tk.Entry(self.acc_type_innerframe_patient, bd=0, bg="lightgray", font="helvetica 16")
		self.agefield.place(relx=0, rely=0.67, relwidth=1, relheight=0.08)

		# ----------=Gender----------=
		self.gender = tk.Label(self.acc_type_innerframe_patient, text="Gender", bg="white", font="helvetica 20")
		self.gender.place(relx=0, rely=0.76, relwidth=0.23, relheight=0.1)

		self.gender_type = tk.StringVar()
		self.gender_type.set('Female')
		self.gender_types_all = [ 'Female', 'Male' ]
		self.combo_gender = ttk.Combobox(self.acc_type_innerframe_patient, textvariable=self.gender_type, values=self.gender_types_all, font="helvetica 16")
		self.combo_gender.place(relx=0, rely=0.87, relwid=1, relheight=0.1)

		self.combo_gender.bind('<<ComboboxSelected>>', lambda e: comboGenderMethod())

		# @staticmethod
		def comboGenderMethod():
			global gender_select
			gender_select = self.gender_type.get()

		def showgender():
			comboGenderMethod()
			msg.showinfo("Gender",gender_select)

		def login_page_nav():
			root.destroy()
			login.main()




		# self.genderMale = tk.Radiobutton(self.acc_type_innerframe_patient, bd=0, value="Male", text="Male", bg="#fff", font="helvetica 16")
		# self.genderMale.place(relx=0, rely=0.87, relwidth=0.25, relheight=0.08)

		# self.genderFemale = tk.Radiobutton(self.acc_type_innerframe_patient, bd=0, value="Female", text="Female", bg="#fff", font="helvetica 16")
		# self.genderFemale.place(relx=0.5, rely=0.87, relwidth=0.25, relheight=0.08)

		# self.cnfpassword = tk.Label(self.frame, text="Confirm Password", bg="white", font="helvetica 20")
		# self.cnfpassword.place(relx=0, rely=0.44, relwidth=0.6, relheight=0.08)



		# =============Admin=============

		# --------USERNAME----------
		self.usernameAdmin = tk.Label(self.acc_type_innerframe_admin, text="Username", bg="white", font="helvetica 20")
		self.usernameAdmin.place(relx=0, rely=0.05, relwidth=0.32, relheight=0.1)

		self.unameAdmin = tk.Entry(self.acc_type_innerframe_admin, bd=0, bg="lightgray", font="helvetica 18")
		self.unameAdmin.place(relx=0, rely=0.15, relwidth=1, relheight=0.08)

		# ---------PASSWORD-----------
		self.passwordAdmin = tk.Label(self.acc_type_innerframe_admin, text="Password", bg="white", font="helvetica 20")
		self.passwordAdmin.place(relx=0, rely=0.24, relwidth=0.3, relheight=0.1)

		self.passwdAdmin = tk.Entry(self.acc_type_innerframe_admin, bd=0, bg="lightgray", show="*", font="helvetica 30")
		self.passwdAdmin.place(relx=0, rely=0.34, relwidth=1, relheight=0.08)

		# --------EMAIL ID------------
		self.emailidAdmin = tk.Label(self.acc_type_innerframe_admin, text="Email Id", bg="white", font="helvetica 20")
		self.emailidAdmin.place(relx=0, rely=0.43, relwidth=0.25, relheight=0.1)

		self.emailFieldAdmin = tk.Entry(self.acc_type_innerframe_admin, bd=0, bg="lightgray", font="helvetica 18")
		self.emailFieldAdmin.place(relx=0, rely=0.53, relwidth=1, relheight=0.08)

		# --------PHONE NO.-----------
		self.phoneNumAdmin = tk.Label(self.acc_type_innerframe_admin, text="Phone No.", bg="white", font="helvetica 20")
		self.phoneNumAdmin.place(relx=0, rely=0.62, relwidth=0.32, relheight=0.1)

		self.phoneNumFieldAdmin = tk.Entry(self.acc_type_innerframe_admin, bd=0, bg="lightgray", font="helvetica 18")
		self.phoneNumFieldAdmin.place(relx=0, rely=0.72, relwidth=1, relheight=0.08)



		def insertData():
			# combomethod()
			# msg.showinfo("data", self.acc_type)
			# -------------------user
			user_name_admin = self.unameAdmin.get()
			pass_word_admin = self.passwdAdmin.get()
			email_id_admin = self.emailFieldAdmin.get()
			phone_no_admin = self.phoneNumFieldAdmin.get()
			
			# --------------------patient
			comboGenderMethod()
			user_name_patient = self.uname.get()
			pass_word_patient = self.passwd.get()
			email_id_patient = self.emailid.get()
			age_patient = self.agefield.get()
			gender_patient = gender_select

			database = mysql.connector.connect(host='localhost', user='root', passwd='', port = 3306, database='mini_project')
			mycursor = database.cursor()
			# query_patient = 'SELECT password FROM patient where username=%s'
			query1 = 'INSERT INTO patient(username, age, gender, password, email) VALUES(%s, %s, %s, %s, %s)'
			# query_user = 'SELECT password FROM user where username=%s'
			query_user = 'INSERT INTO user VALUES(%s, %s, %s, %s)'
			# query_doctor = 'SELECT password FROM doctor where username=%s'
			# msg.showinfo(user_name, pass_word)
			# msg.showinfo("details", self.acctype)
			if self.acc_type.get()=='Patient':
				mycursor.execute(query1, (user_name_patient, age_patient, gender_patient, pass_word_patient, email_id_patient))
				database.commit()
				# mycursor.execute(query_patient, ("Patient1", 24, "Male", "patient1","patient@gmail.com"))
				msg.showinfo("Signup", "Patient Successfully Registered!! \nWelcome, {}".format(user_name_patient)) 	

			elif self.acc_type.get()=='User':
				# msg.showinfo("Congrats","Balle Balle")
				mycursor.execute(query_user, (user_name_admin, email_id_admin, pass_word_admin, phone_no_admin))
				database.commit()
				msg.showinfo("Signup", "Welcome, {} \nYou are registerd as an Admin".format(user_name_admin))

			# elif(self.acctype=='Doctor'):
			# 	mycursor.execute(query_doctor, (user_name, ))
			# 	for row in mycursor:
			# 		if row[0] == pass_word:
			# 			return True
			# 		else:
			# 			return False
		# ========Bottom Buttons=========


		# ===========================================HOW TO PASS THE CORRESPODING ACCOUNT TYPE DETAILS 1.)SEPERATE THE BUTTON CODE FOR EACH ACC TYPE 2.) PASS SM SORTA VALUE!!!!

		# --------------BUTTONS-------------
		self.frameBtn = tk.Frame(self.frame, bg="black")
		self.frameBtn.place(relx=0, rely=0.8, relwid=1, relheight=0.2)

		# ----sign up button-----
		self.signup = tk.Button(self.frameBtn, text="Signup", font="helvetica 18", bd=0, bg="#ffb916", fg="white", activebackground="#e5960d", activeforeground="#fff", command=insertData)
		self.signup.place(relx=0, rely=0, relwid=1, relheight=0.5)

		# ----navigation to login button-----
		self.cancel = tk.Button(self.frameBtn, text="Cancel", font="helvetica 18", bd=0, bg="gray", fg="white", activebackground="darkgray", activeforeground="#fff", command=login_page_nav)
		self.cancel.place(relx=0, rely=0.5, relwid=1, relheight=0.5)


		# ========Entry Fields=========

		# self.uname = tk.Entry(self.frame, bd=0, bg="lightgray", font="helvetica 18")
		# self.uname.place(relx=0.03, rely=0.16, relwidth=0.94, relheight=0.07)

		# self.passwd = tk.Entry(self.frame, bd=0, bg="lightgray", show="*", font="helvetica 30")
		# self.passwd.place(relx=0.03, rely=0.34, relwidth=0.94, relheight=0.07)

		# self.cnfpasswd = tk.Entry(self.frame, bd=0, bg="lightgray", show="*", font="helvetica 30")
		# self.cnfpasswd.place(relx=0.03, rely=0.52, relwidth=0.94, relheight=0.07)


		# ------------Not To Put the select type cuz a patient can signup as an admin and pamper with the software!!!!!!!!!!!1-----------------
		# ---------------------------------so if asked how to do login for admin and user, admin has the priveledge to edit software............
		# ----------------------------------------------------IF WE WANT TO ADD DROPDOWN FOR TYPE SELECTION, WE NEED TO ADD A SEPERATE PASSWORD WHICH WILL BE GIVEN TO THE ADMIN FOR AS HIM/HER
		# ----------------------------------------------------TO ADD ANOTHER ADMIN OR DOCTOR.SO AFTER FILLING FORM AS ADMIN AND CLICKING SIGNUP,IT WILL ASK FOR PASSWORD TO DO THE SIGNUP

		# self.stype = tk.StringVar(self.frame)
		# self.stype.set("Patient")

		# self.typeSelect = tk.OptionMenu(self.frame, self.stype, "Patient", "Admin", "Doctor")
		# self.typeSelect.place(relx=0.03, rely=0.68, relwidth=0.94, relheight=0.08)

		

		# logtype = self.stype.get()

		# if logtype == Patient:
		# 	mydb = mysqlcon.connect(host='localhost', user='root', passwd='', database='dental_clinic')

		# 	mycursor = mydb.cursor()

		# 	mycursor.execute("select password,type from auth where name")




		# --------CREATE A RECTANGLE--------
		# C = tk.Canvas(root, bg="grey", height=250, width=300)

		# C.create_line(15, 25, 200, 25)
		# C.create_line(200, 25, 200, 55)
		# C.create_line(200, 55, 15, 55)
		# C.create_line(15, 55, 15, 25)

		# C.pack()


def main():
	global root
	root = tk.Tk()
	root.geometry("1920x1080")
	dentalSignup = sign_up(root)
	root.mainloop()


# main()
# root = tk.Tk()
# logo = tk.PhotoImage(file="user-edit-icon1.png")
# logo2 = tk.PhotoImage(file="signup_image.gif")

# dentalSignup= sign_up(root)
# root.mainloop()