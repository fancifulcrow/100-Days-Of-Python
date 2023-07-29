import requests
from dotenv import load_dotenv
import os

load_dotenv()

sheet_users_endpoint = f"{os.getenv('SHEETY_ENDPOINT')}/users"
sheet_token = os.getenv("SHEETY_TOKEN")

def post_sheet_users(first_name, last_name, email):
    sheet_headers = {
    "Authorization" : f"Bearer {sheet_token}",
    "Content-Type": "application/json",
    }

    sheety_users_post_json = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    sheet_users_response = requests.post(url=sheet_users_endpoint, json=sheety_users_post_json, headers=sheet_headers)
    sheet_users_response.raise_for_status()
    print(sheet_users_response.text)