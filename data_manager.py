import requests

s_data_endpoint = "https://api.sheety.co/3f956a9a288358e3b83a7ce2fa7c271f/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.get_data = {}

    def define_data(self):
        read_response = requests.get(url=s_data_endpoint)
        sheet_data = read_response.json()
        self.get_data = sheet_data["prices"]
        return self.get_data

    def update_data(self):
        for city in self.get_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{s_data_endpoint}/{city['id']}",
                json=new_data
            )
            # print(response.text)

