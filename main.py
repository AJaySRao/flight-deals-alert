#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager()

sheet = data.define_data()
# print(sheet)


if sheet[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet:
        row["iataCode"] = flight_search.get_code(row["city"])
    data.get_data = sheet
    data.update_data()


