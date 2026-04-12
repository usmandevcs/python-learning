# CLASS:
# Defining a class
'''
A class is a blueprint/blank sheet for creating objects.
It defines a set of attributes and methods that the created 
objects will have.
'''
# Example of a class definition:
'''
imagine class aik blueprint ("jis me jaga define ha kya kya data 
aye ga kis jaga jesa ka aik empty form jis me define hota kaha 
name aye ga kaha father name etc") ha blank/khali ya aik template
jisme hum name wagera fill karty hain jab hum us me name aur
doosri cheezy fill karty hain to wo aik object ki shape ikhtyar
kar leti ha jab tak wo form khali thi tab tak wo class thi jese
hi us my data enter kiya wo object ki shakal ikhtyar kar gya 
'''

# Syntax:
#class Employee: # Class name is written in pascal case 
# Methods & Variables 
class Owner:
    def __init__(self): # Constructor Method
        # Attributes
        self.name = "Usman"
        self.age = 19
        self.salary = 10000000
usman = Owner() # Creating an Object of the Class here usman is object
# Accessing Object Attributes
print(f"Owner Name: {usman.name}")
print(f"Owner Age: {usman.age}")
print(f"Owner Salary: {usman.salary}")

# OBJECT:
'''
An object is an instance/attributes of a class. When a class is defined, 
no memory is allocated until an object of that class is created.
Each object can hold different data, even though they share the 
same structure defined by the class.

When class is defined, a template (info) is defined. Memory is 
allocated only after object instantiation.

Objects of a given class can invoke the methods available to it 
without revealing the implementation details to the user.
'''
# Abstraction & Encapsulation
'''
Abstractions & Encapsulation! .Abstractions and Encapsulation ka
mtlb k aik object apny andr jo data ha wo apny andr rakhta ha aur 
bahir nai nikalta. aur apny andr jo methods ha wo apny andr hi use 
karta ha aur bahir nai nikalta.andr hi apny andr data ko manipulate 
karta ha.
hum is topic ko chapter 11 me detail me samjhy gy.
'''
# For example:
'''
consider a class 'Owner' that has attributes like name, 
age, and salary. When we create an object 'usman' of the class 'Owner',
memory is allocated for 'usman', and it holds specific values for
its attributes, such as 'Usman' for name, 19 for age, and 10000000 for 
salary.
'''