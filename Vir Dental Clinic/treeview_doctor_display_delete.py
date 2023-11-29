from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()







def del_selected(treeview_doctor_display):
    ret_list = treeview_doctor_display.item(treeview_doctor_display.selection())
    doc_id_to_delete = int(ret_list['text'])
    query = 'delete from doctor where doc_id=%s'
    for i in treeview_doctor_display.get_children():
        treeview_doctor_display.delete(i)
    cur.execute(query,(doc_id_to_delete, ))
    refresh_func()
    

treeview_doctor_display = ttk.Treeview(root)
style = ttk.Style()
style.configure('Treeview', rowheight=25)
treeview_doctor_display.pack()
treeview_doctor_display.config(columns=("Qualification", "Doctor_Username", "Gender", "Email", "Speciality"))
treeview_doctor_display.column('#0',  width=150, anchor='center')
treeview_doctor_display.column('Qualification',  width=150, anchor='center')
treeview_doctor_display.column('Doctor_Username',  width=150, anchor='center')
treeview_doctor_display.column('Gender',  width=150, anchor='center')
treeview_doctor_display.column('Email',  width=220, anchor='center')
treeview_doctor_display.column('Speciality',  width=150, anchor='center')
treeview_doctor_display.heading('#0', text='Doctor ID')
treeview_doctor_display.heading('Qualification', text='Qualification')
treeview_doctor_display.heading('Doctor_Username', text='Doctor Username')
treeview_doctor_display.heading('Gender', text='Gender')
treeview_doctor_display.heading('Email', text='Email')
treeview_doctor_display.heading('Speciality', text='Speciality')


def refresh_func():
    conn = mysql.connector.connect(user='root', passwd='', port=3306, host='localhost', database='mini_project')
    cur = conn.cursor()
    query = 'SELECT * FROM doctor'
    cur.execute(query)
    for x in cur:
        treeview_doctor_display.insert('', 'end', text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
    
refresh_func()

# Adding scroll bar just in case the frame is small
scroll_y = ttk.Scrollbar(root, orient=VERTICAL, command=treeview_doctor_display.yview)
scroll_y.pack(side=RIGHT)
treeview_doctor_display.config(yscrollcommand = scroll_y.set)


ttk.Button(root, text='Delete', command=lambda :del_selected(treeview_doctor_display)).pack(side=BOTTOM)


root.mainloop()