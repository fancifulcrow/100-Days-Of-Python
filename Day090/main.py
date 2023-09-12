from tkinter import *

# LOGIC
timer = None


# reset the app
def reset_text():
    global timer
    typing_area.delete(1.0, END)
    timer = None


# Check if the user is still typing
def check_text(event):
	global timer

	# stop the timer if user is still typing
	if timer is not None:
		window.after_cancel(timer)

	# wait for 2 seconds before clearing the text if the user is not typing
	if event.char:
		timer = window.after(2000, reset_text)


# UI SETUP
window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=20, pady=10)

heading_label = Label(text="Disappearing Text Writing App", padx=10, pady=10, font=("Times New Roman", 24, "bold"))
heading_label.grid(row=0, column=0)

info_label = Label(text="Text will disappear if you don't keep writing for 2 seconds", pady=10)
info_label.grid(row=1, column=0)

# Typing Area
typing_area = Text(width=60, height=20, wrap='w', padx=10, pady=10)
typing_area.bind('<KeyPress>', check_text)
typing_area.grid(row=2, column=0)

window.mainloop()
