import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="avatar2.png")

root.geometry("1920x1080")


frame1 = tk.Frame(root, bg="white")
frame1.place(relx=0.1, rely=0.1, relwid=0.8, relheight=0.8)

frame = tk.Frame(frame1, bg="white")
frame.place(relx=0.37, rely=0.1, relwid=0.25, relheight=0.8)

frameBtn = tk.Frame(frame, bg="black")
frameBtn.place(relx=0, rely=0.8, relwid=1, relheight=0.2)


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

icon1 = tk.Label(frame1, image=logo)
icon1.place(relx=0.45, rely=0, relwidth=0.1, relheight=0.2)
icon1['bg'] = icon1.master['bg']



# =======Labels=========

username = tk.Label(frame, text="Username", bg="white", font="helvetica 18")
username.place(relx=-0.08, rely=0.15, relwidth=0.5, relheight=0.1)

password = tk.Label(frame, text="Password", bg="white", font="helvetica 18")
password.place(relx=-0.08, rely=0.35, relwidth=0.5, relheight=0.1)

# ========Bottom Buttons=========

# ----login button-----
login = tk.Button(frameBtn, text="Login", font="helvetica 18", bd=0, bg="green", fg="white", activebackground="white", activeforeground="green")
login.place(relx=0, rely=0, relwid=1, relheight=0.5)

# ----sign in button-----
signup = tk.Button(frameBtn, text="Signup", font="helvetica 18", bd=0, bg="gray", fg="white", activebackground="white", activeforeground="gray")
signup.place(relx=0, rely=0.5, relwid=1, relheight=0.5)


# ========Entry Fields=========

uname = tk.Entry(frame, bd=0, bg="lightgray", font="helvetica 18")
uname.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.08)

passwd = tk.Entry(frame, bd=0, bg="lightgray", font="helvetica 18")
passwd.place(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.08)


# --------CREATE A RECTANGLE--------
# C = tk.Canvas(root, bg="grey", height=250, width=300)

# C.create_line(15, 25, 200, 25)
# C.create_line(200, 25, 200, 55)
# C.create_line(200, 55, 15, 55)
# C.create_line(15, 55, 15, 25)

# C.pack()

root.mainloop()