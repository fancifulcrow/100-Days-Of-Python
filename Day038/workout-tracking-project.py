# API from https://www.nutritionix.com/
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 22

your_text =input("What exercises did you do?")

nutritionix_header = {
    "x-app-id" : app_id,
    "x-app-key" : api_key,
}

nutritionix_parameters = {
    "query" : your_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_response = (requests.post(url=nutritionix_endpoint, json=nutritionix_parameters, headers=nutritionix_header))
nutritionix_response.raise_for_status()

data = nutritionix_response.json()["exercises"]


sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheety_token = os.getenv("SHEETY_TOKEN")

for exercise in data:
    sheety_parameters = {
        "workout": {
            "date": datetime.now().strftime("%d-%m-%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}",
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
sheety_response.raise_for_status()
