import requests
import os

flight_endpoint = "https://tequila-api.kiwi.com/locations/query"

header = {
    "apikey": "iWqm-26D0V_tjhwhaMp9bl512ZV8JdX3"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_code(self, city_name):

        details = {
            "term": city_name,
            "locale": "en-US"
        }
        search_response = requests.get(url=flight_endpoint, params=details, headers=header)
        flight_search_data = search_response.json()
        details = flight_search_data["locations"]
        code = details[0]["code"]
        return code

