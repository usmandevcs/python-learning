
class Train:
    def __init__(self, name, total_seats, base_fare):
        self.name = name
        self.total_seats = total_seats
        self.base_fare = base_fare
        self.booked_seats = 0

    def seats_available(self):
        return self.total_seats - self.booked_seats

    def get_status(self):
        print(f"{self.name} | Available Seats: {self.seats_available()}")

    def calculate_fare(self, travel_class):
        multipliers = {
            "standard": 1.0,
            "sleeper": 1.6,
            "business": 2.4
        }
        return int(self.base_fare * multipliers[travel_class])

    def get_fare_info(self, fro, to):
        print(f"{self.name} Fare Chart | {fro} → {to}")
        for cls in ["standard", "sleeper", "business"]:
            print(f"{cls.capitalize()}: {self.calculate_fare(cls)} PKR")

    def book_ticket(self, num_tickets, fro, to, travel_class):
        if num_tickets > self.seats_available():
            print("Insufficient seats.")
            return
        cost = self.calculate_fare(travel_class) * num_tickets
        self.booked_seats += num_tickets
        print(f"Booked {num_tickets} seat(s) {fro} → {to} in {travel_class} class. Cost: {cost} PKR")

    @staticmethod
    def greet_user():
        print("Wellcome to Pakistan Railways!")

Train.greet_user()
train1 = Train("Badar Express", 100, 900)
fro = "Faisalabad"
to = "Lahore"
train1.get_fare_info(fro, to)
train1.get_status()
train1.book_ticket(int(input("Enter Number of tickets: ")),fro , to , input("prefer class:"))
train1.get_status()



