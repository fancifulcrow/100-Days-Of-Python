import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_api_key = os.getenv("TEQUILA_API_KEY")
        self.tequila_endpoint = "https://api.tequila.kiwi.com"
        self.tequila_headers = {
            "apikey" : self.tequila_api_key,
        }

    def find_iata_code(self, city):
        tequila_location_parameters = {
            "term" : city,
            "location_types": "city",
        }

        tequila_response = requests.get(url=f"{self.tequila_endpoint}/locations/query", params=tequila_location_parameters, headers=self.tequila_headers)
        tequila_response.raise_for_status()
        iata_code = tequila_response.json()["locations"][0]["code"]
        return iata_code
    

    def find_flight_prices(self, origin_code, destination_code):
        tommorrow = datetime.now() + timedelta(days=1)
        # 6 months in the future
        date_to = datetime.now() + timedelta(days=6*30)
        tequila_search_parameters = {
            "fly_from" : origin_code,
            "fly_to" : destination_code,
            "date_from" : tommorrow.strftime("%d/%m/%Y"),
            "date_to" : date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        tequila_response = requests.get(url=f"{self.tequila_endpoint}/v2/search", params=tequila_search_parameters, headers=self.tequila_headers)
        tequila_response.raise_for_status()

        try:
            data = tequila_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data