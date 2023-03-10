import tkinter

FONT = ("New Times Roman", 16)

window = tkinter.Tk()
window.title("mile to km Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)

label = tkinter.Label(text="is equal to", font=FONT)
label.grid(row=1, column=0)

entry = tkinter.Entry(width=10, font=FONT)
entry.grid(row=0, column=1)

answer = tkinter.Label(text="0", font=FONT)
answer.grid(row=1, column=1)

miles_text = tkinter.Label(text="Miles", font=FONT)
miles_text.grid(row=0, column=2)

km_text = tkinter.Label(text="km", font=FONT)
km_text.grid(row=1, column=2)


def button_clicked():
    sol = round((float(entry.get()) * 1.609), 4)
    answer.config(text=sol)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()