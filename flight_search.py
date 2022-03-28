import requests
import os

flight_endpoint = "https://tequila-api.kiwi.com/locations/query"
details = {
    "term": "USA",
    "location_types": "airport",
    "locale": "en-US"
    }
header = {
    "apikey": "iWqm-26D0V_tjhwhaMp9bl512ZV8JdX3"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self.search_response = requests.get(url=flight_endpoint, params=details, headers=header)

