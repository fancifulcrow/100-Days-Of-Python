# Tkinter
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=10, y=200)
# Changing the text in a label
my_label["text"] = "New Text"
my_label.config(text="New Text") # preferred

# Button
def button_clicked():
    print("Button got clicked!")
    my_label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack(side="left")

# Entry
entry = tkinter.Entry(width=30)
# Add some text to begin with
entry.insert(tkinter.END, "Some text to begin with")
# Gets text in entry
print(entry.get())
entry.pack(side="left")

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(tkinter.END, "Example of multi-line text entry")
# Get's curret value in text box at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in the spinbox
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    # get the current value in th scale
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # prints 1 if button is checked, otherwise it prints 0
    print(checked_state.get())


# variable to hold om to the checked state, 0 if off, 1 if on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold on to which radio button value is checked
radio_state = tkinter.IntVar()
radiobutton_1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton_1.pack()
radiobutton_2.pack()

# Tkinter Layout Managers: pack(), place(), grid()

# In grid(), the rows and columns start at 0
# grid() and pack() cannot be in the same program

# Always at the end of the program
window.mainloop()
