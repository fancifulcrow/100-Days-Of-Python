# API from: https://www.weatherapi.com/
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

parameter = {
    "key" : API_KEY,
    "q" : "Abuja",
}

response = requests.get(url=ENDPOINT, params=parameter)
response.raise_for_status()
weather_data = response.json()
response.close()

# print(weather_data)

will_rain = True

day = weather_data["forecast"]["forecastday"][0]

for hour in day["hour"]:
    # Check if the weather is okay
    if hour['condition']['code'] > 1100:
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_EMAIL)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Bring An Umbrella Today!\n\nDon't forget to bring an umbrella"
            )

        break

# Print out to see environemt variables
# print(os.environ)
