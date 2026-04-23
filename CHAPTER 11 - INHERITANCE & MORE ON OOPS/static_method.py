# Static Method:
'''
A static method is a method that belongs to a class rather 
than an instance of the class. It can be called on the class 
itself, without needing to create an instance of the class. 
Static methods are defined using the @staticmethod decorator 
and do not have access to the instance (self) or class (cls) 
variables. They are typically used for utility functions that 
perform a task in isolation, without needing to access or modify 
the state of the class or its instances.
'''
'''
in simple words, static method class k sath belong karta hai, 
kisi instance k sath nahi. Iska use hum utility functions means 
aese fuctions k liye karty hain jo class ya instance k 
halat ko modify ya change nhi karty.
static method ko hum class ke naam se directly call kar sakty 
hain bina object/instance banaye.
'''
# Example:
class Animal:
    @staticmethod
    def make_sound():
        print("Animal makes a sound.")
# Usage
Animal.make_sound()  # Output: Animal makes a sound.
# Static method with arguments
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage
result = MathUtils.add(5, 3)  # Output: 8

# Instance vs Static Method:
'''
Instance Method:
    Instance methods are best for operations on the instance of 
the class.

Static Method:
    Static methods are best for utility functions that do not 
access the class data.
'''
# Example:
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        print(f"{self.name} works as a {self.position}.")
    
# this static method check that position is valid or not without needing to access instance data.
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions

print(Employee.is_valid_position("Developer"))  # Output: True
print(Employee.is_valid_position("Intern"))  # Output: False

employee1 = Employee("Alice", "Developer")
employee1.get_info()  

employee2 = Employee("Bob", "Designer")
employee2.get_info()

employee3 = Employee("Charlie", "Manager")
employee3.get_info()