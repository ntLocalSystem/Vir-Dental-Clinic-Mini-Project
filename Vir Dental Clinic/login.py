import tkinter as tk
from tkinter import ttk
import signup as sp
import dashOOP as dash_board
from tkinter import messagebox as msg
import mysql.connector
import time
import add_doc as ad
# import splash

# root = tk.Tk()
# logo = tk.PhotoImage(file="avatar2.png")

# root.geometry("1920x1080")

class login_page:
	def __init__(self, master):
		self.master = master
		# time.sleep(2)
		master.title("Vir Dental Clinic")
		# root.attributes("-transparentcolor", "#222649")
		self.logo = tk.PhotoImage(file="avatar2.png")

		self.frame1 = tk.Frame(root, bg="white")
		self.frame1.place(relx=0.35, rely=0.1, relwid=0.22, relheight=0.7)
		

		self.frame = tk.Frame(self.frame1, bg="#fff", highlightbackground="lightblue", highlightthickness=2)
		self.frame.place(relx=0, rely=0.1, relwid=1, relheight=0.9)


		# --------------BUTTONS-------------
		self.frameBtn = tk.Frame(self.frame, bg="black")
		self.frameBtn.place(relx=0, rely=0.8, relwid=1, relheight=0.2)



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

		def signup():
			root.destroy()
			sp.main()

		# ===========Labels============

		self.username = tk.Label(self.frame, text="Username", bg="white", font="helvetica 20")
		self.username.place(relx=0, rely=0.15, relwidth=0.35, relheight=0.1)

		self.password = tk.Label(self.frame, text="Password", bg="white", font="helvetica 20")
		self.password.place(relx=0, rely=0.32, relwidth=0.35, relheight=0.1)

		self.type = tk.Label(self.frame, text="Select Account Type", bg="white", font="helvetica 20")
		self.type.place(relx=0, rely=0.5, relwidth=0.68, relheight=0.1)

		# ==========Combobox=============

		self.acc_type = tk.StringVar()
		self.acc_type.set('User')
		self.acc_all_types = ['User', 'Doctor', 'Patient']
		self.combo = ttk.Combobox(self.frame, textvariable=self.acc_type, values=self.acc_all_types, font="helvetica 20")
		self.combo.place(relx=0.03, rely=0.6, relwid=0.94, relheight=0.08)
		self.combo.bind('<<ComboboxSelected>>', lambda e: combomethod())

		# @staticmethod
		def combomethod():
			self.acctype = self.acc_type.get()


		# ========Entry Fields=========

		self.uname = tk.Entry(self.frame, bd=0, bg="lightgray", font="helvetica 18")
		self.uname.place(relx=0.03, rely=0.25, relwidth=0.94, relheight=0.08)

		self.passwd = tk.Entry(self.frame, bd=0, bg="lightgray", show="*", font="helvetica 30")
		self.passwd.place(relx=0.03, rely=0.42, relwidth=0.94, relheight=0.08)

		# global user_name
		# global pass_worduse
		# global acctype
		

		def check():
			msg.showinfo("data", self.acc_type)
			user_name = self.uname.get()
			pass_word = self.passwd.get()
			combomethod()
			database = mysql.connector.connect(host='localhost', user='root', passwd='', port = 3306, database='mini_project')
			mycursor = database.cursor()
			query_patient = 'SELECT password FROM patient where username=%s'
			query_user = 'SELECT password FROM user where username=%s'
			query_doctor = 'SELECT password FROM doctor where username=%s'
			# msg.showinfo(user_name, pass_word)
			# msg.showinfo("details", self.acctype)
			if(self.acctype=='Patient'):
				mycursor.execute(query_patient, (user_name, ))
				for row in mycursor:
					if row[0] == pass_word:
						# msg.showinfo("Congrats","Balle Balle")
						msg.showinfo("Vir Dental Clinic","Welcome, {}".format(user_name))
						root.destroy()
						dash_board.main()
						return True
					else:
						return False

			elif(self.acctype=='User'):
				# msg.showinfo("Congrats","Balle Balle")
				mycursor.execute(query_user, (user_name, ))
				for row in mycursor:
					if row[0] == pass_word:
						msg.showinfo("Vir Dental Clinic","Welcome, {}".format(user_name))
						root.destroy()
						ad.main(user_name)
						return True
					else:
						return False

			elif(self.acctype=='Doctor'):
				mycursor.execute(query_doctor, (user_name, ))
				for row in mycursor:
					if row[0] == pass_word:
						return True
					else:
						return False

		# ========Bottom Buttons=========

		# ----login button-----
		self.login = tk.Button(self.frameBtn, text="Login", font="helvetica 18", bd=0, bg="green", fg="white", activebackground="darkgreen", activeforeground="#fff", command=check)
		self.login.place(relx=0, rely=0, relwid=1, relheight=0.5)

		# ----sign in button-----
		self.signup = tk.Button(self.frameBtn, text="Signup", font="helvetica 18", bd=0, bg="gray", fg="white", activebackground="darkgray", activeforeground="#fff", command=signup)
		self.signup.place(relx=0, rely=0.5, relwid=1, relheight=0.5)




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
	dentalClinic = login_page(root)
	root.mainloop()

main()

# dentalClinic = login_page(root)
# root.mainloop()