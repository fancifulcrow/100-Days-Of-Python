import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Working with Images and setting up canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="mypass_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Use tkinter.grid() and columnspan to complete the UI
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_field = tkinter.Entry(width=35)
website_field.grid(row=1, column=1, columnspan=2)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_field = tkinter.Entry(width=35)
username_field.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_field = tkinter.Entry(width=20)
password_field.grid(row=3, column=1, columnspan=2)

generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=30)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()