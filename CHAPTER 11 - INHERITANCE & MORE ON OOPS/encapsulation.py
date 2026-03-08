# ENCAPSULATION - “Apna khazana lock karna”

# Encapsulation ka simple matlab:
'''
Data ko andar lock karna aur bahar walon ko direct touch 
na karne dena.

Real life analogy:
Piggy bank 🐷
Tum coins andar daal sakte ho
Lekin bina tod ke direct nikal nahi sakte.
'''
# Python me encapsulation kaise hota hai?
'''
Python me encapsulation ke liye hum private variables aur 
methods ka use karte hain. 
Private variables aur methods ko hum double underscore __ se
start karte hain. 
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance  # Public method to access private variable
# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)  # Deposit 500
account.withdraw(200)  # Withdraw 200
print(f"Current balance: {account.get_balance()}")  # Get current balance

# Output:
# 500 deposited. New balance: 1500
# 200 withdrawn. New balance: 1300
# Directly accessing private variable will raise an error
# print(account.__balance)  # This will raise an AttributeError

# Encapsulation ke benefits:
'''
1. Data Protection: Data ko unauthorized access se bachata 
hai.
2. Code Maintainability: Code ko modular banata hai, jisse 
maintain karna easy hota hai.
3. Flexibility: Internal implementation ko change kar sakte 
hain bina external code ko affect kiye.
'''
