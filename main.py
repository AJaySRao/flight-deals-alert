#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.
import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


FROM = "LON"

data = DataManager()
flight_search = FlightSearch()

sheet = data.define_data()
# print(sheet)

# Filling blank spaces with IATA codes in sheets
if sheet[0]["iataCode"] == "":
    for city in sheet:
        city["iataCode"] = flight_search.get_code(city["city"])
    data.get_data = sheet
    data.update_data()


# Fare
notification = NotificationManager()
for destination in sheet:
    flight = flight_search.get_flight_details(origin_city=FROM, city_code=destination['iataCode'])

    if flight.price < destination['lowestPrice']:
        notification.send_msg(
            body=f"Low price alert! "
                 f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                 f"{flight.destination_city}-{flight.destination_airport}, "
                 f"from {flight.out_date} to {flight.return_date}."
        )


# fare_details = flight_data.get_flight_details(city_code="CPT")