# CLASS ATTRIBUTES 
'''An attribute that belongs to the class rather than a particular 
object. mtlb jo class k attributes hain wo sab objects k liye valid 
ha but jo object k attributes hain wo sirf usi object k liye valid 
hain.'''
# These attributes are shared across all instances/objects of the class. 

# Example: 

class Car:
    wheels = 4 # class attribute
    def __init__ (self, model, year):    # This is constructor
        self.model = model         # And also instance attribute
        self.year = year 

    def start(self):
        print(f"Engine is start of {self.model}")
    def stop(self):
        print(f"Engine is off of {self.model} ")

car1 = Car("Toyota", 2025)
print(f"Car Model: {car1.model}")
print(f"Car Year: {car1.year}")
print(f"Car Wheels: {car1.wheels}")

car1.start()
car1.stop()


# INSTANCE ATTRIBUTES or Object Attributes
'''
An attribute that belongs to the object. Assuming the 
class from the previous 
example, if we create an object 'harry' of the class 'Employee',
we can assign an instance attribute 'name' to 'harry' and set it to
"Harry". This attribute is specific to the 'harry' object and is not
shared with other instances of the class. If we create another object
'john' of the class 'Employee', it will not have the 'name' attribute
unless we explicitly assign it to 'john'. Each object can have its own
set of instance attributes that can differ from other objects of the same
class.
'''
# example: 

#harry.name = "harry" # ye dono objects k apny attributes hain jo k specific hain
#harry.salary = "30k"  # Adding instance attribute 

# Note: 
'''
    Instance attributes, take preference over class attributes 
during assignment & retrieval. mtlb k agar aik object k andr aur class 
k andr aik hi attribute ha to object k andr wala attribute zyada
prefer kiya jata hai.'''

# When looking up for harry.attribute it checks for the following: 
# 1) Is attribute present in object? 
# 2) Is attribute present in class? 
# 3) Is attribute present in parent class?
# 4) Raise AttributeError.