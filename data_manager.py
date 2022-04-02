import requests

s_data_endpoint = "https://api.sheety.co/3f956a9a288358e3b83a7ce2fa7c271f/flightDeals/prices"
s_endpoint = "https://api.sheety.co/3f956a9a288358e3b83a7ce2fa7c271f/flightDeals/users"


class DataManager:
    def __init__(self):
        self.get_data = {}
        self.customer_data = []

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

    def add_data(self, user_details):
        read_response = requests.post(url=s_endpoint, json=user_details)
        sheet_data = read_response.json()

    def get_customer_emails(self):
        response = requests.get(url=s_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data


