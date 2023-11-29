import tkinter as tk

root = tk.Tk()
foto = tk.PhotoImage(file="logo_doctor_main.gif")

root.geometry("1920x1080")


# ---------Main Frame----------------

frame = tk.Frame(root, bg="orange")
frame.place(relx=0, rely=0, relwid=1, relheight=1)

# ---------Logo / Header Frame-------

frameProj = tk.Frame(root, bg="#222649")
frameProj.place(relx=0, rely=0, relwid=1, relheight=0.15)

icon1 = tk.Label(frameProj, image=foto)
icon1.place(relx=0.02, rely=0.1, relwidth=0.07, relheight=0.81)
icon1['bg'] = icon1.master['bg']

projName = tk.Label(frameProj, text="Vir Dental Clinic", font="helvetica 45", bg="#222649", fg="#fff")
projName.place(relx=0.09, rely=0, relwid=0.25, relheight=1)


# ---------Work Area Frame-----------

frameWork = tk.Frame(root, bg="#fff")
frameWork.place(relx=0.155, rely=0.16, relwidth=0.655, relheight=0.83)


# ----------Note Frame---------------

# ------Shedule--------

frameNote = tk.Frame(root, bg="gray")
frameNote.place(relx=0.815, rely=0.16, relwid=0.18, relheight=0.52)

upnext = tk.Label(frameNote, text="Upnext", bd=0, bg="gray", fg="white", font="helvetica 16")
upnext.place(relx=0, rely=0, relwid=1, relheight=0.08)

subframeNote = tk.Frame(frameNote, bg="white")
subframeNote.place(relx=0, rely=0.08, relwid=1, relheight=0.95)

# -------LIST----------

# --------------VISITOR-1

visitor1 = tk.Frame(subframeNote, bg="#fff")
visitor1.place(relx=0, rely=0, relwid=1, relheight=0.15)

vistorPic1 = tk.Label(visitor1, bg="#fff")
vistorPic1.place(relx=0, rely=0, relwid=0.25, relheight=1)

visitorDetail1 = tk.Frame(visitor1, bg="black")
visitorDetail1.place(relx=0.25, rely=0, relwid=0.75, relheight=1)

visitorName1 = tk.Label(visitorDetail1, bg="white", fg="black", text="Mildeep Singh, 32", font="areil 18 bold", anchor="sw")
visitorName1.place(relx=0, rely=0, relwid=1, relheight=0.6)

visitingTime1 = tk.Label(visitorDetail1, bg="white", fg="black", text="Time: 14:30", font="areil 12", anchor="nw")
visitingTime1.place(relx=0, rely=0.6, relwid=1, relheight=0.4)

seperator1 = tk.Label(subframeNote, text="_______________________", font="helvetica 30", fg="gray")
seperator1.place(relx=0.05, rely=0.16, relwid=0.9, relheight=0.005)

# --------------VISITOR-2

visitor2 = tk.Frame(subframeNote, bg="#fff")
visitor2.place(relx=0, rely=0.165, relwid=1, relheight=0.15)

vistorPic2 = tk.Label(visitor2, bg="#fff")
vistorPic2.place(relx=0, rely=0, relwid=0.25, relheight=1)

visitorDetail2 = tk.Frame(visitor2, bg="black")
visitorDetail2.place(relx=0.25, rely=0, relwid=0.75, relheight=1)

visitorName2 = tk.Label(visitorDetail2, bg="white", fg="black", text="Rohit Mutalik, 30", font="areil 18 bold", anchor="sw")
visitorName2.place(relx=0, rely=0, relwid=1, relheight=0.6)

visitingTime2 = tk.Label(visitorDetail2, bg="white", fg="black", text="Time: 15:15", font="areil 12", anchor="nw")
visitingTime2.place(relx=0, rely=0.6, relwid=1, relheight=0.4)

seperator2 = tk.Label(subframeNote, text="_______________________", font="helvetica 30", fg="gray")
seperator2.place(relx=0.05, rely=0.32, relwid=0.9, relheight=0.005)

# --------NOTE--------

frameNote2 = tk.Frame(root, bg="gray")
frameNote2.place(relx=0.815, rely=0.69, relwid=0.18, relheight=0.3)

note = tk.Label(frameNote2, text="Note", bd=0, bg="gray", fg="white", font="helvetica 16")
note.place(relx=0, rely=0, relwid=1, relheight=0.15)

subframeNote2 = tk.Frame(frameNote2, bg="white")
subframeNote2.place(relx=0, rely=0.14, relwid=1, relheight=0.9)


#-----------Navigation Frame---------

frameNav = tk.Frame(root, bg="gray")
frameNav.place(relx=0, rely=0.15, relwid=0.15, relheight=1)


# ------------Nav Buttons-------------

home = tk.Button(frameNav, text="Home", bg="#dbdbdb", bd=0, relief="flat", font="helvetica 14", activebackground="gray", activeforeground="white")
home.place(relx=0, rely=0, relwid=1, relheight=0.07)

schedule = tk.Button(frameNav, text="Schedule", bg="#dbdbdb", font="helvetica 14", bd=0)
schedule.place(relx=0, rely=0.07, relwid=1, relheight=0.07)

chart = tk.Button(frameNav, text="Chart", bg="#dbdbdb", font="helvetica 14", bd=0)
chart.place(relx=0, rely=0.14, relwid=1, relheight=0.07)

b3 = tk.Button(frameNav, text="b3", bg="#dbdbdb", font="helvetica 14", bd=0)
b3.place(relx=0, rely=0.21, relwid=1, relheight=0.07)

setting = tk.Button(frameNav, text="Settings", bg="#dbdbdb", font="helvetica 14", bd=0)
setting.place(relx=0, rely=0.28, relwid=1, relheight=0.07)

logout = tk.Button(frameNav, text="Logout", bg="#dbdbdb", font="helvetica 14", bd=0, activebackground="red", activeforeground="white")
logout.place(relx=0, rely=0.35, relwid=1, relheight=0.07)

# --------------END-----------------

root.mainloop()