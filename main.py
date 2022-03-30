#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.
import datetime

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

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
notification = NotificationManager()
for row in sheet:
    fare_details = flight_data.get_flight_details(city_code=row['iataCode'])
    check = fare_details
    sheet_details = (row['city'], row['lowestPrice'])
    if check[1] < sheet_details[1]:
        notification.send_msg(
            body=f"Lowest Price Alert! "
                 f"only ${check[1]} to fly from London to {check[0]}, from {check[2]} to {check[3]}")


# fare_details = flight_data.get_flight_details(city_code="CPT")