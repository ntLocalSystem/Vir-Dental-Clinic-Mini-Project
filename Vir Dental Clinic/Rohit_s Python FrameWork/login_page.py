from tkinter import *
from tkinter import ttk


class LoginApplication:
    def __init__(self, parent):
        parent.resizable(False, False)
        parent.title = 'Login Page'
        global root
        root = parent

        parent.configure(background='white')
        # Style declaration
        self.style = ttk.Style()
        self.style.theme_use('vista')
        self.style.configure('TFrame', background='white')
        self.style.configure('logo.TLabel', font=('Times', 14, 'bold'))
        self.style.configure('Warning.TLabel', foreground='red', background='white',
                             font=('Times', 14, 'bold underline'))
        self.style.configure('normal.TLabel', background='white', foreground='#222649', font=('Times', 14, 'bold'))
        self.style.configure('TEntry', font=('Times', 14, 'bold'))
        self.style.configure('btn.TButton', foreground='#222649', background='#222649')
        self.style.map('btn.TButton', background=[('hover', 'white'), ('pressed', 'white')], forground=[('hover', 'red'), ('pressed', 'red')])

        #  Frame declaration
        self.frame_logo = ttk.Frame(parent, relief=RAISED)
        self.frame_login = ttk.Frame(parent)
        self.frame_logo.pack(side=LEFT, anchor='nw')
        self.frame_login.pack(side=RIGHT, padx=10)

        #  Label Declarations
        self.logo = PhotoImage(file='logo_resized.gif')

        ttk.Label(self.frame_login, text='Username :', style='normal.TLabel').grid(row=2, column=0, pady=20, sticky='e',
                                                                                   padx=5)
        ttk.Label(self.frame_login, text='Login Details', style='normal.TLabel',
                  font=('Arial', 32, 'bold underline')).grid(row=0, column=0, columnspan=2, pady=15, sticky='n')
        ttk.Label(self.frame_login, text='Password :', style='normal.TLabel').grid(row=3, column=0, pady=20, sticky='e',
                                                                                   padx=5)
        ttk.Label(self.frame_login, text="Don't have an account? Sign Up!", style='Warning.TLabel').grid(row=6,
                                                                                    column=0, columnspan=2, pady=20)
        ttk.Label(self.frame_login, text='The entered combination of username and password is incorrect.',
                  wraplength=60, style='normal.TLabel')
        ttk.Label(self.frame_login, text='Select Account Type :', style='normal.TLabel').grid(row=1,
                                                                                              column=0,
                                                                                              pady=14,
                                                                                              sticky='e', padx=5)
        ttk.Label(self.frame_logo, image=self.logo, compound='image',
                  style='logo.TLabel').grid(row=0, column=0, sticky='nsew')

        #  Combobox Declarations
        self.acc_type = StringVar()
        self.acc_type.set('User')
        self.acc_all_types = ['User', 'Doctor', 'Patient']
        ttk.Combobox(self.frame_login, textvariable=self.acc_type, values=self.acc_all_types).grid(row=1, column=1,
                                                                                                   pady=20, sticky='w')
        #  Use acc_type.get() to retrieve the value of the combobox

        #  Entry Widget Declarations
        self.username_entry = ttk.Entry(self.frame_login, width=25)
        self.username_entry.grid(row=2, column=1, pady=20, sticky='w')
        self.password_entry = ttk.Entry(self.frame_login, width=25, show='*')
        self.password_entry.grid(row=3, column=1, pady=20, sticky='w')
        #  Use username_entry.get() to retrieve the value of the entry widget

        #  Button Declarations
        ttk.Button(self.frame_login, text='Login', command=self.login,
                   style='btn.TButton').grid(row=5, column=0, pady=20, sticky='e', padx=0)
        ttk.Button(self.frame_login, text='Reset', command=self.reset,
                   style='btn.TButton').grid(row=5, column=1, pady=20, sticky='w', padx=80)
        ttk.Button(self.frame_login, text='Sign Up',
                   style='btn.TButton').grid(row=7, column=0, pady=14, sticky='e', padx=0)
        ttk.Button(self.frame_login, text='Exit', command=parent.destroy,
                   style='btn.TButton').grid(row=7, column=1, pady=14, sticky='w', padx=80)

    def reset(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def login(self):
        if self.username_entry.get() == 'admin' and self.password_entry.get() == 'admin':
            ttk.Label(self.frame_login, text='Entered details are correct, logging in...', style='Warning.TLabel',
                      wraplength=240).grid(row=4, column=0, columnspan=2)


def main():
    root_window = Tk()
    window = LoginApplication(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    main()