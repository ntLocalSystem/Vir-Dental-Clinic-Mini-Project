from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class ApplicationWindow():

    def __init__(self, parent):

        global window
        window = parent
        parent.title('Sign Up Details')
        parent.resizable(False, False)

        # global style declarations
        global style
        style = ttk.Style()
        style.configure('normal.TLabel', foreground='#222649', font=('Times', 12))
        style.configure('heading.TLabel', foreground='#222649', font=('Times', 20, 'bold underline'))
        style.configure('normal.TButton', foreground='#222649', font=('Times', 12, 'bold'))
        style.map('normal.TButton', foreground=[('hover', 'red'), ('pressed', 'red')])
        style.theme_use('vista')
        style.configure('btn.TButton', foreground='#222649', background='#222649')
        style.map('btn.TButton', background=[('hover', 'white'), ('pressed', 'white')],
                       forground=[('hover', 'red'), ('pressed', 'red')])
        # frame declarations
        self.frame_logo = ttk.Frame(parent, relief=RAISED)
        self.frame_logo.pack(side=LEFT, anchor='nw')
        self.frame_type = ttk.Frame(parent)
        global frame_details, frame_user, frame_patient
        frame_details = ttk.Frame(parent)
        frame_user = ttk.Frame(frame_details)
        frame_patient = ttk.Frame(frame_details)
        self.frame_type.pack(side=TOP, padx=15)
        frame_details.pack()

        # label declaration
        self.logo = PhotoImage(file='logo_resized.gif')
        ttk.Label(self.frame_logo, image=self.logo, compound='image',
                  style='logo.TLabel').grid(row=1, column=0, sticky='nsew')
        ttk.Label(self.frame_type, text='Select Account Type :', style='normal.TLabel').grid(row=1, column=0, sticky='e')
        ttk.Label(self.frame_type, text='Sign Up Details :', style='heading.TLabel').grid(row=0, column=0, columnspan=2, pady=20)

        # combobox declarations
        global acc_type
        acc_type = StringVar()
        acc_type.set('Select Account Type')
        self.acc_all_types = ['User', 'Patient']
        self.cb = ttk.Combobox(self.frame_type, textvariable=acc_type, values=self.acc_all_types)
        self.cb.grid(row=1, column=1, sticky='w', padx=10)

        self.cb.bind('<<ComboboxSelected>>', lambda e: self.combomethod())

    @staticmethod
    def combomethod():
        if acc_type.get() == 'User':
            window.update()
            frame_patient.pack_forget()
            # Label widgets
            ttk.Label(frame_user, text='Username :', style='normal.TLabel').grid(row=0, column=0, sticky='e', padx=5, pady=(65, 20))
            ttk.Label(frame_user, text='Password :', style='normal.TLabel').grid(row=1, column=0, sticky='e', padx=5)
            ttk.Label(frame_user, text='Email :', style='normal.TLabel').grid(row=2, column=0, sticky='e', padx=5)
            ttk.Label(frame_user, text='Phone No. :', style='normal.TLabel').grid(row=3, column=0, sticky='e', padx=5)

            # Entry Widgets
            global entry_u_username, entry_u_password, entry_u_email, entry_u_phone
            entry_u_username = ttk.Entry(frame_user, width=25).grid(row=0, column=1, sticky='w', pady=(65, 20))
            entry_u_password = ttk.Entry(frame_user, width=25).grid(row=1, column=1, sticky='w', pady=20)
            entry_u_email = ttk.Entry(frame_user, width=25).grid(row=2, column=1, sticky='w', pady=20)
            entry_u_phone = ttk.Entry(frame_user, width=25).grid(row=3, column=1, sticky='w', pady=20)

            # Button Widgets
            global button_u_submit, button_u_exit
            button_u_submit = ttk.Button(frame_user,
                                         text='Submit', style='btn.TButton')
            button_u_submit.grid(row=4, column=0, sticky='e', pady=(50, 10), padx=(20, 10))
            button_u_exit = ttk.Button(frame_user, text='Exit', command=window.destroy, style='btn.TButton')
            button_u_exit.grid(row=4, column=1, sticky='w', pady=(50, 10), padx=(50, 5))
            frame_user.pack()
            window.update()

        elif acc_type.get() == 'Patient':
            window.update()
            frame_user.pack_forget()
            # Label widgets
            ttk.Label(frame_patient, text='Patient ID :', style='normal.TLabel').grid(row=0, column=0, sticky='e', pady=(40, 10), padx=5)
            ttk.Label(frame_patient, text='Name / Username :', style='normal.TLabel').grid(row=2, column=0, sticky='e', padx=5)
            ttk.Label(frame_patient, text='Gender :', style='normal.TLabel').grid(row=4, column=0, sticky='e', padx=5)
            ttk.Label(frame_patient, text='Password :', style='normal.TLabel').grid(row=3, column=0, sticky='e', padx=5)
            ttk.Label(frame_patient, text='Allergies :', style='normal.TLabel').grid(row=5, column=0, sticky='e', padx=5)
            ttk.Label(frame_patient, text='Phone No. :', style='normal.TLabel').grid(row=6, column=0, sticky='e', padx=5)
            ttk.Label(frame_patient, text='For Patient ID, enter any 5 digit numerical code.', style='normal.TLabel').grid(row=1, column=0, columnspan=2, pady=(5, 10))

            # Entry Widgets
            global entry_p_username, entry_p_password, entry_p_phone, entry_p_gender, entry_p_allergies, entry_p_pid
            entry_p_username = ttk.Entry(frame_patient, width=25).grid(row=2, column=1, sticky='w', pady=10)
            entry_p_password = ttk.Entry(frame_patient, width=25).grid(row=3, column=1, sticky='w', pady=10)
            entry_p_phone = ttk.Entry(frame_patient, width=25).grid(row=6, column=1, sticky='w', pady=10)
            entry_p_gender = ttk.Entry(frame_patient, width=25).grid(row=4, column=1, sticky='w', pady=10)
            entry_p_allergies = ttk.Entry(frame_patient, width=25).grid(row=5, column=1, sticky='w', pady=10)
            entry_p_pid = ttk.Entry(frame_patient, width=25).grid(row=0, column=1, sticky='w', pady=(40, 10))

            # Button Widgets
            global button_p_submit, button_p_exit
            button_p_submit = ttk.Button(frame_patient, text='Submit', style='btn.TButton')
            button_p_submit.grid(row=7, column=0, sticky='e', pady=(33, 10), padx=(20, 10))
            button_p_exit = ttk.Button(frame_patient, text='Exit', command=window.destroy, style='btn.TButton')
            button_p_exit.grid(row=7, column=1, sticky='w', pady=(33, 10), padx=(50, 5))
            frame_patient.pack()
            window.update()
        else:
            strret = messagebox.showinfo(title='Account type', message='Please select a valid account type')


def main():
    root = Tk()
    app = ApplicationWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()