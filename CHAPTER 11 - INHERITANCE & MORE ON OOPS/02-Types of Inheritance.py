# Types of Inheritance
'''
There are several types of inheritance in object-oriented 
programming, each serving different purposes and allowing for 
various relationships between classes. The main types of 
inheritance include:
'''
# 1st. Single Inheritance

# 2nd. Multi-Level Inheritance

# 3rd. Multiple Inheritance

# 4th. Hierarchical Inheritance

# 5th. Hybrid Inheritance

# 6th. Multipath Inheritance


# 1st. Single Inheritance
'''
In Single Inheritance, a class (derived class) inherits from a single 
base class (parent class). This is the simplest form of inheritance.
'''
# Example of Single Inheritance
# This is also an example of hierarchical inheritance.
class Animal:  # Base class
    def speak(self):
        return "Animal speaks"
class Dog(Animal):  # Derived class
    def bark(self):
        return "Bow! Bow! Bow!"
# Creating an instance of the Dog class
class cat(Animal):  # Derived class
    def meow(self):
        return "Meow! Meow! Meow!"
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Bow! Bow! Bow!
cat = cat()
print(cat.speak())  # Output: Animal speaks
print(cat.meow())   # Output: Meow! Meow! Meow!
# In this example, the Dog class inherits from the Animal class. 
# The Dog class can access the speak method of the Animal class.


# 2nd. Multi-Level Inheritance
'''
In Multi-Level Inheritance, a class (derived class) inherits from a
base class, and another class inherits from that derived class,
forming a chain of inheritance.
'''
# Example of Multi-Level Inheritance
class Animal:  # Base class
    def speak(self):
        return "Animal speaks"
class Dog(Animal):  # Derived class
    def bark(self):
        return "Bow! Bow! Bow!"
class Puppy(Dog):  # Another derived class
    def weep(self):
        return "Wee! Wee! Wee!"
# Creating an instance of the Puppy class
puppy = Puppy()
print(puppy.speak())  # Output: Animal speaks
print(puppy.bark())   # Output: Bow! Bow! Bow!
print(puppy.weep())   # Output: Wee! Wee! Wee!
# In this example, the Puppy class inherits from the Dog class,
# which in turn inherits from the Animal class. The Puppy class
# can access methods from both the Dog and Animal classes.

# 3rd. Multiple Inheritance
'''
In Multiple Inheritance, a class (derived class) can inherit from
more than one base class. This allows the derived class to access
methods and attributes from multiple base classes.
'''
# Example of Multiple Inheritance
class Father:  # Base class 1
    def traits(self):
        return "Father's traits"
class Mother:  # Base class 2
    def traits(self):
        return "Mother's traits"
class Child(Father, Mother):  # Derived class
    def traits(self):
        return "Child's traits"
# Creating an instance of the Child class
child = Child()
print(child.traits())  # Output: Child's traits
# In this example, the Child class inherits from both the Father
# and Mother classes. The Child class can access methods from
# both base classes.

# Another Example of Multiple Inheritance with method resolution order
class Father:  # Base class 1
    def traits(self):
        return "Father's traits"
class Mother:  # Base class 2
    def traits(self):
        return "Mother's traits"
class Child(Father, Mother):  # Derived class
    pass
# Creating an instance of the Child class   
child = Child()
print(child.traits())  # Output: Father's traits
# In this example, the Child class inherits from both the Father
# and Mother classes. Since the Child class does not override the

# 4th. Hierarchical Inheritance
'''
In Hierarchical Inheritance, multiple classes (derived classes) inherit
from a single base class. This creates a hierarchy where one base
class serves as the parent for multiple derived classes.
'''
# Example of Hierarchical Inheritance
class Animal:  # Base class
    def speak(self):
        return "Animal speaks"
class Dog(Animal):  # Derived class 1
    def bark(self):
        return "Bow! Bow! Bow!"
class Cat(Animal):  # Derived class 2
    def meow(self):
        return "Meow! Meow! Meow!"
# Creating instances of the Dog and Cat classes
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Bow! Bow! Bow!
print(cat.speak())  # Output: Animal speaks
print(cat.meow())   # Output: Meow! Meow! Meow!
# In this example, both the Dog and Cat classes inherit from the
# Animal class. They can access the speak method of the Animal class
# as well as their own specific methods.

# 5th. Hybrid Inheritance
'''
Hybrid Inheritance is a combination of two or more types of
inheritance. It allows for more complex relationships between classes
by combining features of different inheritance types.
'''
# Example of Hybrid Inheritance
class Animal:  # Base class
    def speak(self):
        return "Animal speaks"
class Dog(Animal):  # Derived class 1
    def bark(self):
        return "Bow! Bow! Bow!"
class Cat(Animal):  # Derived class 2
    def meow(self):
        return "Meow! Meow! Meow!"  
class Puppy(Dog):  # Derived class from Dog
    def weep(self):
        return "Wee! Wee! Wee!"
# Creating instances of the Cat and Puppy classes
cat = Cat()
puppy = Puppy()
print(cat.speak())   # Output: Animal speaks
print(cat.meow())    # Output: Meow! Meow! Meow!
print(puppy.speak()) # Output: Animal speaks
print(puppy.bark())  # Output: Bow! Bow! Bow!
print(puppy.weep())  # Output: Wee! Wee! Wee!
'''
In this example, the Cat class inherits from the Animal class,
while the Puppy class inherits from the Dog class, which in turn
inherits from the Animal class. This creates a hybrid inheritance 
structure.
'''

# 6th. Multipath Inheritance
'''
In Multipath Inheritance, a class can inherit from multiple classes
that share a common base class. This can lead to ambiguity if the
same method is defined in multiple base classes.
'''
# Example of Multipath Inheritance
class A:  # Base class
    def method(self):
        return "Method from class A"
class B(A):  # Derived class 1
    def method(self):
        return "Method from class B"
class C(A):  # Derived class 2
    def method(self):
        return "Method from class C"
class D(B, C):  # Derived class from both B and C
    pass
# Creating an instance of the D class
d = D()
print(d.method())  # Output: Method from class B
# In this example, the D class inherits from both B and C, which in
# turn inherit from A. Since both B and C have a method named method,
# the method from class B is called due to the method resolution order (MRO) in Python. This can
# lead to ambiguity if not handled properly, and it's important to be aware of the MRO when using multiple inheritance.
