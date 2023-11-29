import tkinter as tk
# from dashOOP import dashboard
import login as log_in
import time



class visitagain():
	
	def __init__(self, master):
		self.master = master
		master.title("Vir Dental Clinic")
		
		self.logo = tk.PhotoImage(file="logo2.gif")
		

		def login_page_nav():
			root.destroy()
			log_in.main()
		# ---------Main Frame----------------

		self.background = tk.Frame(root, bg="#222649")
		self.background.place(relx=0, rely=0, relwid=1, relheight=1)

		self.icon1 = tk.Label(self.background, bg="pink", image=self.logo)
		self.icon1.place(relx=0.2, rely=0.27, relwidth=0.2, relheight=0.35)
		# self.icon1['bg'] = self.icon1.master['bg']

		self.proj = tk.Label(self.background, text="Vir Dental Clinic", font="helvetica 55",fg="#fff", bd=0, bg="#222649")
		self.proj.place(relx=0.4, rely=0.35)

		self.tagline = tk.Label(self.background, text="Because Teeth Have Feelings Too!", font="helvetica 14",fg="#fff", bd=0, bg="#222649")
		self.tagline.place(relx=0.41, rely=0.43)

		self.loginBtn = tk.Button(self.background, text="Login", font="helvetica 18", fg="#222649", bd=0, bg="#fff", command=login_page_nav)
		self.loginBtn.place(relx=0.4, rely=0.5, relwid=0.15, relheight=0.06) 


 

# --------------END-----------------
def main():
	global root
	root = tk.Tk()
	# foto = tk.PhotoImage(file="logo_doctor_main.gif")
	root.geometry("1920x1080")
	splash = visitagain(root)
	root.mainloop()
main()