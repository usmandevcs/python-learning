# Problem 5:
'''
Write a Class ‘Train’ which has methods to book a ticket, get 
status (no of seats) and get fare information of train running 
under Pakistan Railways.
'''
from random import randint

class Train:
    def __init__(self, name, total_seats, fare):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare
        self.booked_seats = 0
            
    def book_ticket(self, num_tickets, fro, to):
        if self.booked_seats + num_tickets <= self.total_seats:
            self.booked_seats += num_tickets
            print(f"Successfully booked {num_tickets} tickets from {fro} to {to}.")
        else:
            print("Not enough available seats.")

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        print(f"Train {self.name} has {available_seats} seats available and running on time")
    
    def get_fare_info(self, fro, to):
        print(f"Fare information for Train {self.name}:")
        print(f"Fare of Standard Class from {fro} to {to} is: {randint(500, 2000)} PKR")
        print(f"Fare of Sleeper Class from {fro} to {to} is: {randint(1000, 2500)} PKR")
        print(f"Fare of Business Class from {fro} to {to} is: {randint(2000, 4000)} PKR")
    @staticmethod
    def greet_user():
        print("Hello, welcome to the Pakistan Railways!")
Train.greet_user()
train1 = Train("Badar Express", 100, 1000)
train1.get_fare_info(input("Enter source station: "), input("Enter destination station: "))
train1.get_status()
train1.book_ticket(2, "source", "destination")
train1.get_status()
