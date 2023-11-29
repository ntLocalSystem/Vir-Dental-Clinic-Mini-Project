import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()

canvas = tk.Canvas(root, bg="red")
canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

frame = tk.Frame(canvas)
# resize the canvas scrollregion each time the size of the frame changes
frame.bind('<Configure>', on_configure)

# display frame inside the canvas
canvas.create_window(0, 0, window=frame)


scrolly = tk.Scrollbar(root, command=canvas.yview)
scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
canvas.configure(yscrollcommand=scrolly.set)

# populate the frame
for i in range(20):
    tk.Label(frame, text='Label %i' % i).pack()

root.mainloop()