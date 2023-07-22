#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()

sheet_data = data_manager.get_sheety_data()

# pprint(DataManager().getSheetyData())

flight_search = FlightSearch()

for row_index, row in enumerate(sheet_data):
    if row["iataCode"] == "":
        # data started on row 2
        data_manager.edit_row_iata_code(row_index=row_index+2, iata_code=flight_search.find_iata_code(row["city"]))

ORIGIN_CITY_IATA = "ABV"

# notification_manager = NotificationManager()

for destination in sheet_data:
    flight = flight_search.find_flight_prices(ORIGIN_CITY_IATA, destination["iataCode"])
    print(flight)

    # if flight.price < destination["lowestPrice"]:
    #         notification_manager.send_sms(
    #             message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    #         )