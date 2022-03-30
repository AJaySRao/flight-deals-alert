#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.
import datetime

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager()

sheet = data.define_data()
# print(sheet)

# Filling blank spaces with IATA codes in sheets
if sheet[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet:
        row["iataCode"] = flight_search.get_code(row["city"])
    data.get_data = sheet
    data.update_data()

# Fare
flight_data = FlightData()
for code in sheet:
    fare_details = flight_data.get_flight_details(city_code=code['iataCode'])
    print(fare_details)






