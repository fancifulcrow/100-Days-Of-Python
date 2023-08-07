from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from dotenv import load_dotenv
import os

from internet_speed_twitter_bot import InternetSpeedTwitterBot

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

promised_down = 90 # promised download speed
promised_up = 90 # promised upload speed

internet_speed_bot = InternetSpeedTwitterBot(path_to_edge_webdriver=r"..\msedgedriver.exe")
actual_down, actual_up = internet_speed_bot.get_internet_speed()
print(f"Actual Download Speed: {actual_down}Mbps \nActual Upload Speed: {actual_up}Mbps")

if actual_up < promised_up or actual_down < promised_down:
    internet_speed_bot.tweet_at_provider(twitter_email=TWITTER_EMAIL, twitter_password=TWITTER_PASSWORD)
