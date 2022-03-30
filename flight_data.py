import requests
import datetime

flight_endpoint = "https://tequila-api.kiwi.com/v2/search"

header = {
    "apikey": "iWqm-26D0V_tjhwhaMp9bl512ZV8JdX3"
}
TODAY = datetime.datetime.now()
SIX_MONTHS = TODAY+datetime.timedelta(days=180)

class FlightData:
    #This class is responsible for structuring the flight data.
    def get_flight_details(self, city_code):
        details = {
            "max_stopovers": 0,
            "fly_from": "LON",
            "fly_to": city_code,
            "one_for_city": 1,
            "date_from": TODAY.strftime("%d/%m/%Y"),
            "date_to": SIX_MONTHS.strftime("%d/%m/%Y"),
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
        }
        search_response = requests.get(url=flight_endpoint, params=details, headers=header)
        flights = search_response.json()
        flights_slice = flights["data"][:1]
        city = flights_slice[0]["cityTo"]
        fare = flights_slice[0]["price"]
        out_bound = flights_slice[0]['route'][0]['local_departure']
        in_bound = flights_slice[0]['route'][1]['local_departure']
        ob_date = out_bound[0:10]
        ib_date = in_bound[0:10]

        # return f"{city}: £{fare}"
        return city, fare, ob_date, ib_date
