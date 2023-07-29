import post_sheet_users

print("Welcome to the Flight Club")
print("We find the best flight deals and email you")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

email_confirmation = False

while(email_confirmation == False):
    email = input("What is your email? ").title()
    email_again = input("Your email again: ").title()

    if (email == email_again and email != ""):
        email_confirmation = True
    else:
        print("The emails do not match. Please try again.")

post_sheet_users(first_name, last_name, email)