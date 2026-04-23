# Property Decorator:
# its uses:
'''
Encapsulation: It allows you to control access to attributes 
and implement validation logic.
'''
'''
Abstraction: It hides the internal implementation details of 
how attributes are accessed and modified.
'''
'''
Property decorator se hum apne class ke attributes ko control kar sakte hain,
jaise ki validation, read-only access, ya computed properties.
'''
# -> property decorator = safe and smart way to access attributes

# Definition:
'''
A property decorator is a built-in function in Python that 
allows you to define methods in a class that can be accessed 
like attributes. It provides a way to encapsulate the access to 
an attribute and add additional logic for getting, setting, or 
deleting the attribute.
'''
# Benefits:
'''
Add additional logic when we want to read, write, or delete an 
attribute.
Encapsulate the internal representation of an attribute and 
provide a public interface for it.
'''
# Property decorator ke teen main components hain:
'''
1. Getter: A method jis se hum attribute ki value ko read karte 
hain.
2. Setter: A method jis se hum attribute ki value ko set/write 
karte hain.
3. Deleter: A method jis se hum attribute ko delete karte hain.
'''

# Example without setter and deleter:
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

    # @property
    # def area(self):
    #     return f"Area: {self._width * self._height:.1f}cm^2"
# Usage:
rect = Rectangle(5, 3)
# Direct access to internal attributes (not recommended):
print(rect._width)   
print(rect._height)
# Using property methods:
print(rect.width)   # Width: 5.0cm
print(rect.height)  # Height: 3.0cm
# print(rect.area)    # Area: 15.0cm^2

# Example with setter:
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @property
    def area(self):
        return f"Area: {self._width * self._height:.1f}cm^2"
# Usage:
rectangle = Rectangle(5, 3)
rectangle.width = 10 # Update width to 10 (valid)
rectangle.height = 6 # Update height to 6 (valid)
'''
without setter, jo value set ki thi object ke ander wo change nhi
hoti thi, but setter ke sath hum value ko update kar sakte hain,
jese uper object ma (5, 3) value pass ki gai ha wo setter k bina 
same hi rahy gi lekin humny uper value update ki ha jese 
rectangle.width ko 10, aur rectangle.height ko 6 set kiya jis 
se object ki values update ho gai. ab 5, 3 show nhi hogi.
''' 
print(rectangle.width)   
print(rectangle.height)  

# calculating Area
print(rectangle.area)  # Area: 15.0cm^2
print(rectangle.area)  # Area: 30.0cm^2
# rectangle.height = -5  # ValueError: Height must be positive   

# Example with deleter:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @property
    def area(self):
        return f"Area: {self._width * self._height:.1f}cm^2"

    @area.deleter
    def area(self):
        print("Deleting area...")
        del self._width
        del self._height

# Usage:
rect = Rectangle(5, 3)
print(rect.width)   # Width: 5.0cm
print(rect.height)  # Height: 3.0cm
print(rect.area)    # Area: 15.0cm^2
del rect.area       # Deleting area...  
print(rect.width)   # AttributeError: 'Rectangle' object has no attribute '_width'
print(rect.height)  # AttributeError: 'Rectangle' object has no attribute '_height
'''
deleter se hum attribute ko delete kar sakte hain, jese uper 
area deleter ma humne area ko delete kiya jis se width aur 
height bhi delete ho gai, ab agar hum width ya height ko access 
karne ki koshish karenge to error raise hoga kyunki wo 
attributes delete ho chuki hain.
'''
