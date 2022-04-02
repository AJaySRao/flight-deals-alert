
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(
            self,
            price,
            origin_city,
            origin_airport,
            destination_city,
            destination_airport,
            out_date,
            return_date,
            stop_over=0,
            via_city="",
            via_city2=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.stop_over = stop_over
        self.via_city = via_city
        self.via_city2 = via_city2
        self.return_date = return_date
