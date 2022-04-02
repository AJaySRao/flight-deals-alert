from flight_club import FlightClub
from data_manager import DataManager

club = FlightClub()
data = DataManager()

club.person_details()
data.add_data(club.users)

message = f"Subject: New Low Price Alert! \n\nLow price alert! "\
            f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "\
            f"{flight.destination_city}-{flight.destination_airport}, "\
            f"from {flight.out_date} to {flight.return_date}.\nhttps://www.google.co.uk/flights?hl=en#flt=" \
              f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}" \
              f".{flight.origin_airport}.{flight.return_date}"
