import requests
import os

flight_endpoint = "https://tequila-api.kiwi.com/locations/query"

header = {
    "apikey": "iWqm-26D0V_tjhwhaMp9bl512ZV8JdX3"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.city_name = city_name
        self.details = {
            "term": self.city_name,
            "locale": "en-US"
        }
        self.search_response = requests.get(url=flight_endpoint, params=self.details, headers=header)

