#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheet_data = data.response
print(sheet_data)

flight_search = FlightSearch()
flight_search_data = flight_search.search_response

print(flight_search_data.json())
