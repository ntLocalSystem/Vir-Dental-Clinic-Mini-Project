import tkinter as tk

master = tk.Tk()

variable = tk.StringVar(master)
variable.set("one") # default value

w = tk.OptionMenu(master, variable, "one", "two", "three")
w.pack()

master.mainloop()