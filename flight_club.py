class FlightClub:
    def __init__(self):
        self.users = {}

    def person_details(self):
        f_name = input("Please enter your first name: ")
        l_name = input("Please enter your last name: ")
        email = input("Please enter your valid email: ")
        email1 = input("Please enter the same email: ")
        if email == email1:
            self.users = {
                "user": {
                    "firstName": f_name,
                    "lastName": l_name,
                    "email": email
                }
            }
            print("Success! We added your details.")
        else:
            print("Email does not match")
