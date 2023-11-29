from tkinter import *
from tkinter import ttk

# '#b6cbd6'


class MainUser:
    def __init__(self, parent):
        global windowroot
        windowroot = parent
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
        #  frame_refresh_nothing.pack(fill=BOTH)
        frame_refresh_add_doc = ttk.Frame(self.frame_refresh)
        frame_refresh_add_doc.pack(fill=BOTH)
        self.frame_doc_gender = ttk.Frame(frame_refresh_add_doc)
        self.frame_doc_gender.grid(row=3, column=1, sticky='w', padx=(5, 25), pady=(0, 30))
        self.frame_refresh_add_doc_details = ttk.Frame(frame_refresh_add_doc).pack(side=LEFT)

        # Label declaration

        self.logo = PhotoImage(file='logo_doctor_main.gif')
        ttk.Label(self.frame_logo, image=self.logo, compound='image', background='#87949b').pack()

        self.image_nothing = PhotoImage(file='thumbnail-full01_03.gif')
        ttk.Label(frame_refresh_nothing, image=self.image_nothing, compound='image', background='white').pack()

        # Doc frame label declarations
        ttk.Label(frame_refresh_add_doc, text='Enter Details :', font=('Times', 14, 'bold')).grid(row=0, column=0, columnspan=4, pady=(8, 35), sticky='w')
        ttk.Label(frame_refresh_add_doc, text='Doctor ID :').grid(row=1, column=0, sticky='e', pady=(0, 30), padx=(5, 0))
        ttk.Label(frame_refresh_add_doc, text='Name :').grid(row=2, column=0, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Gender :').grid(row=3, column=0, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Email :').grid(row=4, column=0, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Qualification :').grid(row=1, column=2, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Experience (In Yrs) :').grid(row=2, column=2, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Speciality :').grid(row=3, column=2, sticky='e', pady=(0, 30))
        ttk.Label(frame_refresh_add_doc, text='Phone No. :').grid(row=4, column=2, sticky='e', pady=(0, 30))

        self.image_side = PhotoImage(file='main_side.gif')
        ttk.Label(frame_refresh_add_doc, image=self.image_side, compound='image').grid(row=0, column=4, rowspan=6)
        # Entry widget declaration

        # Doc entry widget declaration
        self.doc_id_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_id_entry.grid(row=1, column=1, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_name_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_name_entry.grid(row=2, column=1, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_email_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_email_entry.grid(row=4, column=1, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_qual_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_qual_entry.grid(row=1, column=3, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_exp_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_exp_entry.grid(row=2, column=3, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_spec_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_spec_entry.grid(row=3, column=3, sticky='w', padx=(5, 25), pady=(0, 30))
        self.doc_phn_entry = ttk.Entry(frame_refresh_add_doc, width=30)
        self.doc_phn_entry.grid(row=4, column=3, sticky='w', padx=(5, 25), pady=(0, 30))

        # Button Declaration

        self.btn_add_doc = ttk.Button(self.frame_buttons, text='Add Doctor', command=self.add_doc)
        self.btn_add_doc.grid(row=0, column=0, sticky='nsew', ipadx=50, ipady=7)
        self.btn_remove_doc = ttk.Button(self.frame_buttons, text='Remove Doctor')
        self.btn_remove_doc.grid(row=1, column=0, pady=(15, 15), sticky='nsew', ipadx=50, ipady=7)
        self.btn_exit = ttk.Button(self.frame_buttons, text='Exit')
        self.btn_exit.grid(row=4, column=0, pady=(15, 5), sticky='nsew', ipadx=50, ipady=7)
        self.btn_exit = ttk.Button(self.frame_buttons, text='Sign Out')
        self.btn_exit.grid(row=3, column=0, pady=(190, 0), sticky='nsew', ipadx=50, ipady=7)

        # add_doc button declaration
        ttk.Button(frame_refresh_add_doc, text='Submit').grid(row=5, column=0, columnspan=2, ipadx=50, ipady=7, pady=(15, 5))
        ttk.Button(frame_refresh_add_doc, text='Reset', command=self.reset_details).grid(row=5, column=2, columnspan=2, ipadx=50, ipady=7, pady=(15, 5))

        # Radio Button Declaration
        self.gender_val = StringVar()
        self.rd_btn_mal = ttk.Radiobutton(self.frame_doc_gender, text='Male', variable=self.gender_val, value='Male')
        self.rd_btn_fem = ttk.Radiobutton(self.frame_doc_gender, text='Female', variable=self.gender_val, value='Female')
        self.rd_btn_mal.grid(row=0, column=0, sticky='w', padx=(5, 10))
        self.rd_btn_fem.grid(row=0, column=1, sticky='w', padx=(5, 10))

    def signout(self):
        # Code goes here
        pass

    @staticmethod
    def add_doc(self):
        frame_refresh_nothing.pack_forget()

    def reset_details(self):
        self.doc_id_entry.delete(0, 'end')
        self.doc_name_entry.delete(0, 'end')
        self.doc_qual_entry.delete(0, 'end')
        self.doc_phn_entry.delete(0, 'end')
        self.doc_exp_entry.delete(0, 'end')
        self.doc_email_entry.delete(0, 'end')
        self.doc_spec_entry.delete(0, 'end')


def main():
    root_window = Tk()
    window = MainUser(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    main()