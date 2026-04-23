# __INIT__() CONSTRUCTOR 
'''
__init__ means initialize, it is a special method in Python classes.
It is called a constructor because it is used to construct or 
initialize the attributes of an object when it is created.
The __init__() method is defined within a class and is 
automatically called when an instance of the class is created. 
It allows you to set initial values for the attributes of the 
object.
ye prioritize nhi ki jati kisi bhi method ko, but __init__() is 
a special method that is automatically called when an object is 
created, so it is executed before any other method in the class.
The __init__() method takes at least one parameter, which is 
conventionally named self. The self parameter refers to the 
instance of the class that is being created. It allows you to 
access and modify the attributes of the object within the method.
'''
'''
The __init__() method is a special method in Python it is also
called dunder method in classes,known as the constructor. 
It is automatically called when a new object of the class is created. 
This method is used to initialize the attributes of the class.
'''

# Key Points about __init__():
'''
1: __init__() is a special method which is first run as soon as 
the object is created. 
2: It is used to initialize the attributes of the class.
3: It is called automatically when an object of the class is created.
4: It can take parameters to initialize attributes with specific 
values.
5: The self parameter refers to the current instance of the class.
6: It does not return any value; its purpose is to set up the 
object.
7: It takes 'self' argument and can also take further arguments. 
8: It is defined using double underscores before and after the 
name.
'''
# Example:
class Owner:
    def __init__(self): # Constructor Method
        # Attributes
        self.name = "Usman"
        self.age = 19
        self.salary = 10000000