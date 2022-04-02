#This file will need to use the DataManager,FlightSearch, FlightData,
#NotificationManager classes to achieve the program requirements.

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
    flight = flight_search.get_flight_details(
        origin_city=FROM,
        city_code=destination['iataCode']
    )
    if flight is None:
        continue

    if flight.price < destination['lowestPrice']:
        users = data.get_customer_emails()
        emails = [row["email"] for row in users]

        message = f"Subject: New Low Price Alert! \n\nLow price alert! "\
                f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "\
                f"{flight.destination_city}-{flight.destination_airport}, "\
                f"from {flight.out_date} to {flight.return_date}.\nhttps://www.google.co.uk/flights?hl=en#flt=" \
                  f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}" \
                  f".{flight.origin_airport}.{flight.return_date}"

        if flight.stop_over > 0:
            message += f"\nFlight has {flight.stop_over} stop over, via {flight.via_city}."

        # print(message)
        notification.send_msg(message)
        notification.send_email(emails, message)


# flight = flight_search.get_flight_details(
#     origin_city=FROM,
#     city_code=sheet[-1]['iataCode']
# )
# if flight is None:
#     continue
#
# if flight.price < sheet[-1]['lowestPrice']:
#     message = f"Low price alert! "\
#             f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "\
#             f"{flight.destination_city}-{flight.destination_airport}, "\
#             f"from {flight.out_date} to {flight.return_date}."
#     if flight.stop_over > 0:
#         message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
#
#     print(message)
