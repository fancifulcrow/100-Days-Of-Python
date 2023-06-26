import tkinter
from tkinter import END
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# recall from Day 5
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # Convert from list to string with the join() function
    password = "".join(password_list)

    password_field.delete(0, END)
    password_field.insert(0, password)

    # Copy passowrd to clipboard
    pyperclip.copy(password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_field.get()
    email = username_field.get()
    password = password_field.get()

    # make use of messageboxes for pop ups

    # Check if any field is empty
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")

        return

    # Confirm the info 
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \nPassword:{password}")

    if is_ok:
        with open("passwords_list.txt", "a") as f:
            f.write(f"Website: {website}, Email: {email}, Password: {password}\n")

        website_field.delete(0, END)
        password_field.delete(0, END)



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
website_field.focus()

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_field = tkinter.Entry(width=35)
username_field.grid(row=2, column=1, columnspan=2)
username_field.insert(0, "johndoe@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_field = tkinter.Entry(width=35)
password_field.grid(row=3, column=1)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=1)

add_button = tkinter.Button(text="Add", width=30, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()