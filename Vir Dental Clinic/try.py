import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.place(relx=0, rely=0, relwid=1, relheight=1)
x = 0
y = 0
i = 5
j = 7

list1 = [0, 0.2, 0.4, 0.6, 0.8]

for y in list1:
	j=7
	x=0
	while j!=0:
		l = tk.Button(root, text=j)
		l.place(relx=x, rely=y, relwid=0.142857, relheight=0.2)
		x = x + 0.142857
		j = j - 1
	# i = i -1
	# y = y + 0.2

# for y in list1:
# 	for j in range(7):
# 		l = tk.Button(root, text=y)
# 		l.place(relx=x, rely=y, relwid=0.142857, relheight=0.2)
# 		x = x + 0.142857
		# j = j - 1

	
root.mainloop()
