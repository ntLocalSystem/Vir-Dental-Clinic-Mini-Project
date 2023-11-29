from tkinter import *
from tkinter import ttk

# '#b6cbd6'


class MainUser:
    def __init__(self, parent):

        parent.title('Dental Clinic Management :  User Configuration Panel')
        parent.resizable(False, False)
        parent.configure(background='white')

        # Style declaration
        style = ttk.Style()
        style.configure('heading_side.TFrame', background='#b2c6cb')

        # Frame declaration
        self.frame_heading = ttk.Frame(parent)

        self.frame_butlog = ttk.Frame(parent, style='heading_side.TFrame')
        self.frame_buttons = ttk.Frame(self.frame_butlog, style='heading_side.TFrame')
        self.frame_logo = ttk.Frame(self.frame_butlog, style='heading_side.TFrame')
        self.frame_logo.grid(row=0, column=0, sticky='nsew', padx=(20, 0), pady=(30, 0))
        self.frame_buttons.grid(row=1, column=0, sticky='nsew', pady=(35, 0), padx=(20, 0))
        self.frame_butlog.grid(row=0, column=0, sticky='nsew', ipadx=20, pady=(0, 0), ipady=5)
        self.frame_refresh = ttk.Frame(parent)
        self.frame_refresh.grid(row=0, column=1, sticky='nsew', pady=(0, 0))
        global frame_refresh_nothing, frame_refresh_add_doc
        frame_refresh_nothing = ttk.Frame(self.frame_refresh)
        frame_refresh_nothing.pack(fill=BOTH)
        frame_refresh_add_doc = ttk.Frame(self.frame_refresh)

        # Label declaration

        self.logo = PhotoImage(file='logo_doctor_main.gif')
        ttk.Label(self.frame_logo, image=self.logo, compound='image', background='#87949b').pack()

        self.image_nothing = PhotoImage(file='thumbnail-full01_03.gif')
        ttk.Label(frame_refresh_nothing, image=self.image_nothing, compound='image', background='white').pack()



        # Button Declaration

        self.btn_add_doc = ttk.Button(self.frame_buttons, text='Add Doctor', command=self.add_doc)
        self.btn_add_doc.grid(row=0, column=0, sticky='nsew', ipadx=50, ipady=7)
        self.btn_remove_doc = ttk.Button(self.frame_buttons, text='Remove Doctor')
        self.btn_remove_doc.grid(row=1, column=0, pady=(15, 15), sticky='nsew', ipadx=50, ipady=7)
        self.btn_exit = ttk.Button(self.frame_buttons, text='Exit')
        self.btn_exit.grid(row=4, column=0, pady=(15, 5), sticky='nsew', ipadx=50, ipady=7)
        self.btn_exit = ttk.Button(self.frame_buttons, text='Sign Out')
        self.btn_exit.grid(row=3, column=0, pady=(190, 0), sticky='nsew', ipadx=50, ipady=7)


    def signout(self):
        # Code goes here
        pass


    def add_doc(self):
        frame_refresh_nothing.pack_forget()









def main():
    root_window = Tk()
    window = MainUser(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    main()