from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_PRICES_ENDPOINT = f"{os.getenv('SHEETY_ENDPOINT')}/prices"
SHEETY_USERS_ENDPOINT = f"{os.getenv('SHEETY_ENDPOINT')}/users"
sheet_token = os.getenv("SHEETY_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {sheet_token}",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, headers=sheety_headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
