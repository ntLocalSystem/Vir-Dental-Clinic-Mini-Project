import tkinter as tk

window = tk.Tk()

window.title("My App")

window.geometry("1920x1080")

#funtions
def phrase_generator():
	phrases = ["Hello" , "Whats up" , "Hey"]
	name = str(entry_field.get())
	return phrases[random.randint(0, 2)] + name

def phrase_display():
	greeting = phrase_generator()

	# This creates a text field
	greeting_display = tk.Text(master=window, height=20, width=30)
	greeting_display.grid(column=1, row=3)
	greeting_display.insert(tk.END, greeting)


# LABEL
title = tk.Label(text="Hello World.", font=("Times New Roman", 20))
title.grid(column=0, row=0)

#BUTTON
button1 = tk.Button(text="Click Me!!", bg="red", command=phrase_display)
button1.grid(column=0, row=1)


#ENTRY FIELD
entry_field = tk.Entry()
entry_field.grid(column=0, row=2)



window.mainloop()