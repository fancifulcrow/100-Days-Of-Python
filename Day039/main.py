#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()

sheet_data = data_manager.get_sheety_data()

# pprint(DataManager().getSheetyData())

flight_search = FlightSearch()

for row_index, row in enumerate(sheet_data):
    row_index += 1
    if row["iataCode"] == "":
        data_manager.edit_row_iata_code(row_index=row_index, iata_code=flight_search.find_iata_code(row["city"]))