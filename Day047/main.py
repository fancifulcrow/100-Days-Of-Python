import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

amazon_url = "https://www.amazon.com/dp/B0C7FYRWF9/"

# To get this information go to https://myhttpheader.com/
my_browser_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Accept-Language" : "en-US,en;q=0.9",
}

# Get the HTML for the webpage of the item on amazon
response = requests.get(url=amazon_url, headers=my_browser_headers)
response.raise_for_status()
# print(response.text)
amazon_html = response.text

# Scrap the webpage using the lxml parser
soup = BeautifulSoup(amazon_html, "lxml")

# Find and return the price of the item
price = float(f"{soup.find(class_='a-price-whole').text}{soup.find(class_='a-price-fraction').text}")
# print(price)

# the price we want to get
target_price = 100

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# send an email if the price is less than or equal to our target price
if price <= target_price:
    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Tracker\n\nCheck out {amazon_url}. It is on sale for {price}!!!"
        )