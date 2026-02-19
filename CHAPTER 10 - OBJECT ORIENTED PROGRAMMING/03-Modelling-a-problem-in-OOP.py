# Modelling a problem in Object-Oriented Programming (OOP):
'''
it involves identifying the key components of the problem and 
mapping them to OOP concepts such as classes, attributes, and 
methods.mtlb k aik problem ko solve karny k liye hum us problem k
key components ko identify kartay hain aur unko OOP concepts jese 
classes, attributes, aur methods k sath map kartay hain.
'''
# We identify the following in our problem. 
# • Noun → Class → Owner
# • Adjective → Attributes → name, age, salary 
# • Verbs → Methods → getSalary(), increment()
# Example:
class Owner:
    def __init__(self): # Constructor Method
        # Attributes
        self.name = "Usman"
        self.age = 19
        self.salary = 1000000

    def getSalary(self): # Method to get salary
        return self.salary
    def increment(self, amount): # Method to increment salary
        self.salary += amount

usman = Owner() # Creating an Object of the Class
print(f"Owner Name: {usman.name}")
print(f"Owner Age: {usman.age}")
print(f"Owner Salary: {usman.getSalary()}")
usman.increment(50000) # Incrementing salary by 50000
print(f"Updated Owner Salary: {usman.getSalary()}") 
