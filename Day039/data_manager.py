import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.sheety_headers = {
            "Authorization": f"Bearer {self.sheety_token}",
        }
        self.sheety_parameters = {

        }

    
    def get_sheety_data(self):
        sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        return sheety_response.json()["prices"]
    

    def edit_row_iata_code(self, row_index, iata_code):
        edit = {
            "iataCode" : iata_code,
        }
        sheety_response = requests.put(url=f"{self.sheety_endpoint}/{row_index}", json=edit, headers=self.sheety_headers)
        sheety_response.raise_for_status()