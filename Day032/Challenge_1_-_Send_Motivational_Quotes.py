import smtplib
import datetime as dt
import random

with open("quotes.txt", mode="r", encoding="utf-8") as quotes_file:
    quotes_list = quotes_file.readlines()

    # Send emails on Mondays
    if dt.datetime.now().weekday() == 0:
        my_email = "example@gmail.com"
        my_password = "abcd1234"

        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="msgreciever@gmail.com",
                msg=f"Subject:Monday Motivation\n\n{random.choice(quotes_list)}"
            )