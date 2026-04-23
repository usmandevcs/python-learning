# SUPER() METHOD
'''
The super() method is used to access the methods of a super 
class(Base class) in the derived class.means super() method jo 
ha wo un methods ko access karta ha jo base/parent class ma hoty 
hain.
It is commonly used to call the constructor of the base class from 
the derived class.
This is particularly useful in inheritance when you want to
initialize the base class attributes in the derived class.
'''
'''
Ye sirf constructor ko hi call nahi karta balki agar base class 
ma koi method hai to usko bhi call kar sakta hai.
'''
# super().__init__() is used to call the constructor of the base class from the derived class.
# __init__() Calls constructor of the base class

# Example of super() method
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # calling the constructor of super class
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
# Circle
circle = Circle("Red", True, 5)
print(circle.color)  
print(circle.filled) 
print(circle.radius) 
# Square
square = Square("Blue", False, 4)
print(square.color)  
print(square.filled)
print(square.width)  
# Triangle
triangle = Triangle("Green", True, 3, 4)
print(triangle.color)  
print(triangle.filled) 
print(triangle.width)  
print(triangle.height) 

