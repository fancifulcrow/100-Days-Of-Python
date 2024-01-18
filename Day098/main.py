import smtplib
import datetime as dt
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# This reminds you to pay for your bills by sending you an email.

EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")


with open("subscriptions.json", mode="r") as file:
    data = json.load(file)


for subscription in data:
    if subscription["day"] == dt.datetime.now().day:
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Pay {subscription['service']} subscription Today!!!\n\nGo to {subscription['website']} to pay for the next month"
            )