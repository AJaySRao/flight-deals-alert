from pprint import pprint

import requests
from flight_data import FlightData
import datetime

flight_endpoint = "https://tequila-api.kiwi.com"

header = {
    "apikey": "iWqm-26D0V_tjhwhaMp9bl512ZV8JdX3"
}

TODAY = datetime.datetime.now()
SIX_MONTHS = TODAY+datetime.timedelta(days=180)


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_code(self, city_name):
        details = {
            "term": city_name,
            "location_types": "city"
        }
        search_response = requests.get(url=f"{flight_endpoint}/locations/query", params=details, headers=header)
        flight_search_data = search_response.json()
        details = flight_search_data["locations"]
        code = details[0]["code"]
        return code

    def get_flight_details(self, origin_city, city_code):
        details = {
            "fly_from": origin_city,
            "fly_to": city_code,
            "date_from": TODAY.strftime("%d/%m/%Y"),
            "date_to": SIX_MONTHS.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        search_response = requests.get(url=f"{flight_endpoint}/v2/search", headers=header, params=details)
        try:
            data = search_response.json()["data"][0]
        except IndexError:
            details["max_stopovers"] = 1
            response = requests.get(
                    url=f"{flight_endpoint}/v2/search",
                    headers=header,
                    params=details
                )
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_details = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_over=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_details

        else:
            flight_details = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

        # return f"{city}: £{fare}"
            return flight_details


