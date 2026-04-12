# CLASS ATTRIBUTES 
'''An attribute that belongs to the class rather than a particular 
object. mtlb jo class k attributes hain wo sab objects k liye valid 
ha but jo object k attributes hain wo sirf usi object k liye valid 
hain.'''
# These attributes are shared across all instances/objects of the class. 

# Example: 

'''
consider a class 'Employee' that has a class attribute 
'company'. This attribute is shared across all instances of 
the class.
When we create an object 'harry' of the class 'Employee', it can 
access the class attribute 'company' and it will return "Google".
If we change the class attribute 'company' to "YouTube", then all
objects of the class 'Employee' will reflect this change when they
access the 'company' attribute.
'''

class Employee: # is class k andr aik class attribute define kiya ha company jo k sabhi employee k liye valid ha 
    company = "Google" # Specific to Each Class 
harry = Employee() # Object Instatiation 
harry.company 
Employee.company = "YouTube" # Changing Class Attribute


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

harry.name = "harry" # ye dono objects k apny attributes hain jo k specific hain
harry.salary = "30k"  # Adding instance attribute 

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