# Problem 3:
'''
Create a class with a class attribute a; create an object from 
it and set ‘a’ directly using ‘object.a = 0’. Does this change 
the class attribute? 
'''
class MyClass:
    a = 10
obj = MyClass()
print(f"Initial class attribute a: {MyClass.a}")  # Output: 10 because instance attribute not set yet.
obj.a = 0
print(f"Updated class attribute a: {obj.a}")  # Here Output: 0 because instance attribute is set to a = 0.

# NO!, the class attribute remains unchanged. 
'''
The assignment obj.a = 0 creates an instance attribute 'a' for 
the object 'obj', which shadows the class attribute 'a'.
print(f"Instance attribute a: {obj.a}")  # Output: 0
'''