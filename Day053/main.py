import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By

import time

from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_FORMS_LINK = os.getenv("GOOGLE_FORMS_LINK")
ZILLOW_LINK = "https://www.zillow.com/los-angeles-ca/rentals/"

# to avoid being detected as a bot
zillow_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Accept-Language": "en-US,en;q=0.9",
}
path_to_webdriver = r"..\msedgedriver.exe"

response = requests.get(url=ZILLOW_LINK, headers=zillow_headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

rent_list = []

for rented_property in soup.find_all(class_="list-card_for-rent", name="article"):
    address = rented_property.find(name="address").text
    rent = rented_property.find(name="span").text
    link = rented_property.find(name="a").get("href")
    if "https://www.zillow.com" not in link:
        link = f"https://www.zillow.com{link}"

    rent_list.append(
        {
            "address" : address,
            "rent" : rent,
            "link" : link,
        }
    )

service = service.Service(path_to_webdriver)
driver = webdriver.Edge(service=service)

for rented_property in rent_list:
    driver.get(url=GOOGLE_FORMS_LINK)
    # There are 3 input fields
    input_fields = driver.find_elements(By.CLASS_NAME, "whsOnd")
    time.sleep(2)
    input_fields[0].send_keys(rented_property["address"])
    time.sleep(2)
    input_fields[1].send_keys(rented_property["rent"])
    time.sleep(2)
    input_fields[2].send_keys(rented_property["link"])
    time.sleep(2)
    btn = driver.find_element(By.CSS_SELECTOR, ".NPEfkd")
    btn.click()
    time.sleep(2)