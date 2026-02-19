# OPERATOR OVERLOADING IN PYTHON  

# Operators in Python can be overloaded using dunder methods. 
# These methods are called when a given operator is used on the objects. 
# Operators in Python can be overloaded using the following methods:
''' 
# Addition: __add__(self, other)
p1+p2 # p1.__add__(p2) 

# Subtraction: __sub__(self, other)
p1-p2 # p1.__sub__(p2) 

# Multiplication: __mul__(self, other)
p1*p2 # p1.__mul__(p2) 

# Division: __truediv__(self, other)
p1/p2 # p1.__truediv__(p2) 

# Floor Division: __floordiv__(self, other)
p1//p2 # p1.__floordiv__(p2) 

Other dunder/magic methods in Python: 
__str__() # used to set what gets displayed upon calling str(obj) 

__repr__() # used to set what gets displayed upon calling repr(obj)

__len__() # used to set what gets displayed upon calling.__len__(obj) 
'''
# Example of Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
# Creating two Point objects
p1 = Point(2, 3)
p2 = Point(5, 7)

# Adding two Point objects
p3 = p1 + p2
print(p3)  # Output: Point(7, 10)

# Common Operator Overloading Methods
'''
| Operator | Method        | Example                  |
| -------- | ------------- | ------------------------ |
| `+`      | `__add__`     | `a + b`                  |
| `-`      | `__sub__`     | `a - b`                  |
| `*`      | `__mul__`     | `a * b`                  |
| `/`      | `__truediv__` | `a / b`                  |
| `==`     | `__eq__`      | `a == b`                 |
| `<`      | `__lt__`      | `a < b`                  |
| `<=`     | `__le__`      | `a <= b`                 |
| `>`      | `__gt__`      | `a > b`                  |
| `>=`     | `__ge__`      | `a >= b`                 |
| `str()`  | `__str__`     | readable output          |
| `len()`  | `__len__`     | custom length            |
| `repr()` | `__repr__`    | developer-friendly print |
'''

# Concept Summary
'''
| Concept              | Purpose                      | Key Advantage               |
| -------------------- | ---------------------------- | --------------------------- |
| Operator Overloading | Redefine operator behavior   | Natural object manipulation |
'''
