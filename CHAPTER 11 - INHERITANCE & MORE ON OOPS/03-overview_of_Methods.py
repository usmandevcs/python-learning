# Methods In OOP:
'''
There are different types of methods in OOP, each serving a 
specific purpose.
These methods are given below:
'''

# CLASS METHOD 
'''
A class method is a method which is bound to the class and not the 
object of the class. 
in simple word ye aik treeqa ha method k andar class ko access karny ka.
we all know that k instance/opject attributes ko class attributes per
preference hasil ha agr aik program ma instance attributes or class 
attributes dono presnt hain but hum class attributes ko access karna 
chahty hain to hum class method ka use karty hain.
'''
# class method use (cls) instead of (self).
# @classmethod decorator is used to create a class method.

# Syntax: 
'''
@classmethod 
def (cls,p1,p2):
'''
# Example
class Employee():
    company_name = "Sky Groups"   #class attributes
    @classmethod
    def show(cls):
        return f"company name is {cls.company_name}"
company = Employee()
compny_name = "Techbazar"
print(company.show()) #output: company name is Sky Groups

# @PROPERTY DECORATORS 

# 1. @property Decorator (Getter, Setter, Deleter)
'''
Python ma @property decorator ka use encapsulated attribute access 
k liye hota ha.Normal class ma agar hum direct attributes access 
karty hain, to validation/control possible nahi hota.@property allow 
karta ha attribute ko method ki tarah control karna without changing 
syntax.
'''
# Example Without Property
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Ab koi b directly:

p = Person("Usman", 19)
p.age = -5  # invalid but allowed


# Validation nahi hui.

# Using @property (Getter, Setter)
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age  # underscore means internal/private

    @property
    def age(self):  # Getter
        return self._age

    @age.setter
    def age(self, value):  # Setter
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# Usage:

p = Person("Usman", 19)
print(p.age)   # getter auto call
p.age = 25     # setter auto call
p.age = -5     # error raise


# Benefit:
'''
→ Validation aur logic maintain hoti hai
→ Access syntax natural rehta hai (p.age, not p.get_age())
'''
# Deleter (optional)
# @age.deleter
def age(self):
    print("Deleting age...")
    del self._age
'''
Consider the following class: 
class Employee: 
@property 
def name(self): 
    return self.ename 
If e = Employee() is an object of class employee, we can print 
(e.name) to print the ename by internally calling name() function. 
'''


# @.GETTERS AND @.SETTERS 
'''
The method name with ‘@property’ decorator is called getter method. 
We can define a function + @ name.setter decorator like below: 
'''
# @name.setter 
'''
def name (self,value): 
    self.ename = value 
'''
# concept summary
'''
| Concept              | Purpose                      | Key Advantage               |
| -------------------- | ---------------------------- | --------------------------- |
| `@property`          | Encapsulate attribute access | Validation, cleaner syntax  |
| `@setter`            | Control attribute mutation   | Prevent invalid data        |
'''