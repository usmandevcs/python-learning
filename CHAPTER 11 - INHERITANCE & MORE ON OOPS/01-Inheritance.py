# Inheritance
'''
Inheritance is a fundamental concept in object-oriented programming 
(OOP) that allows a class (called a subclass or derived class) to 
inherit attributes and methods from another class (called a 
superclass or base class). This promotes code reusability and 
establishes a hierarchical relationship between classes.
In simple words, Inheritance is a way of creating a new class from 
an existing class.
'''
# Syntax of Inheritance
'''
class Employee:  # Base class/original class
# Code 


    class Programmer(Employee): # Derived or child class/subclass jo base class se linked hai
# Code 


1. We can use the method and attributes of 'Employee' in 
'Programmer' object.

2. Also, we can overwrite or add new attributes and methods in 
'Programmer' class.
3. We can create multiple levels of inheritance, where a class can
inherit from a class that is itself a subclass of another class.
'''
# Example of Inheritance
class Employee:  # Base class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Programmer(Employee):  # Derived class
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}"
# Creating an instance of the Programmer class
prog = Programmer("Alice", 70000, "Python")
print(prog.show_details())  # Output: Name: Alice, Salary: 70000, Programming Language: Python
# In this example, the Programmer class inherits from the Employee class. The Programmer class has access to the attributes and methods of the Employee class, 
# and it also adds its own attribute (programming_language) and overrides the show_details method to include additional information.
