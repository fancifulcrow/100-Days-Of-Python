##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "example@gmail.com"
my_password = "abcd1234"

# 1. Update the birthdays.csv | DONE

# 2. Check if today matches a birthday in the birthdays.csv | DONE

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv | DONE

# 4. Send the letter generated in step 3 to that person's email address. | DONE

birthday_dic = pd.read_csv("birthdays.csv").to_dict(orient="records")

for birthday in birthday_dic:
    if (dt.datetime.now().month, dt.datetime.now().day) == (birthday["month"], birthday["day"]):
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )


# NOTE: Use pythonanywhere.com to run your python code in the cloud