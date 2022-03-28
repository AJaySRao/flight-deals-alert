import requests

s_data_endpoint = "https://api.sheety.co/308a6d2782f06fc8638c04aff1163efc/flightDeals/prices"




class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=s_data_endpoint)
