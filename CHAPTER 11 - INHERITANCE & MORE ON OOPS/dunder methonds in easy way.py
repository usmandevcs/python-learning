# Dunder Methods - “Secret Magic Buttons inside objects”

# Dunder = double underscore
# Example: __init__, __str__, __len__
'''
Ye special functions hotay hain jo Python khud automatically 
call karta hai jab tum koi action karte ho.
'''
# for example
'''
Socho tumhare paas ek toy robot hai.
Us robot ke andar hidden buttons hain.
Tum bahar se sirf command dete ho:

. print(robot)

. len(robot)

. robot + robot

Robot khud decide karta hai kya karna hai → ye dunder methods 
ka kaam hai.
Jab tum print(robot) karte ho, toh robot ke andar ek button hota 
hai jiska naam __str__() hai, wo button automatically chalu ho 
jata hai aur tumhe robot ke baare mein information deta hai.
Jab tum len(robot) karte ho, toh robot ke andar ek aur button 
hota hai jiska naam __len__() hai, wo button chalu ho jata hai 
aur tumhe robot ke size ke baare mein information deta hai.
Jab tum robot + robot karte ho, toh robot ke andar ek aur 
button hota hai jiska naam __add__() hai, wo button chalu ho 
jata hai aur tumhe do robots ko jod kar ek naya robot deta hai.
'''

# 1. __init__ → “Robot ko janam dena”
'''
Jab object banta hai, ye method run hota hai. Isme hum object ke 
attributes set karte hain. Ye method automatically call hota hai 
jab hum class ka object banate hain. Iska kaam hai object ko 
initialize karna, yani uske properties ko set karna.
'''
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
print(d)  # Output: Buddy
# Yahan __init__ dog ko naam deta hai.
# Real life: baby born hota hai → uska naam rakha jata hai.

# 2. __str__ → “Robot ko bolna kya dikhana hai” kya print krna hai
'''
Jab hum print() function use karte hain, toh Python automatically
__str__() method ko call karta hai. Is method ka kaam hai object 
ke baare mein ek readable string return karna. Agar hum __str__() 
method define nahi karte hain, toh Python default mein object ka 
memory address print karta hai, jo ki zyada useful nahi hota.
'''

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
print(d)
# By default weird output aata hai.

# Ab __str__ method add karte hain:

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog ka naam hai {self.name}"
d = Dog("Buddy")
print(d)

# 3.3. __len__ → “Kitni cheezen hain” ya kitni length hai
'''
Jab hum len() function use karte hain, toh Python automatically
__len__() method ko call karta hai. Is method ka kaam hai object 
ke baare mein ek integer return karna, jo ki object ki length ya 
size ko represent karta hai. Agar hum __len__() method define 
nahi karte hain, toh Python default mein error throw karta hai, 
kyunki len() function ko pata nahi hota ki object ki length kaise 
calculate karni hai.
'''
class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

b = Box(["toy","ball","car"])
print(len(b))

# 4.__add__ → “Robot ko jodna” ya add karna
'''
Jab hum + operator use karte hain, toh Python automatically 
__add__() method ko call karta hai. Is method ka kaam hai do 
objects ko add karna aur ek naya object return karna. Agar hum 
__add__() method define nahi karte hain, toh Python default mein 
error throw karta hai, kyunki + operator ko pata nahi hota ki 
objects ko kaise add karna hai.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
p1 = Point(2, 3)
p2 = Point(5, 7)
p3 = p1 + p2
print(f"p3 ke coordinates hain: ({p3.x}, {p3.y})")

# 2nd example of __add__:

class Toy:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Toy(self.count + other.count)

t1 = Toy(3)
t2 = Toy(2)

t3 = t1 + t2
print(t3.count)

# 5. __eq__ → “Dono same hain ya nahi”
'''
Jab hum == operator use karte hain, toh Python automatically
__eq__() method ko call karta hai. Is method ka kaam hai do 
objects ko compare karna aur boolean value return karna. Agar 
hum __eq__() method define nahi karte hain, toh Python default 
mein object ke memory addresses ko compare karta hai, jo ki zyada 
useful nahi hota.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(2, 3)
p2 = Point(2, 3)
print(p1 == p2)  # Output: True

# 6. __call__ → “Object ko function bana do”
'''
Jab hum kisi object ko function ki tarah call karte hain, toh 
Python automatically __call__() method ko call karta hai. Is 
method ka kaam hai object ko function ki tarah behave karna aur 
ek naya value return karna. Agar hum __call__() method define 
nahi karte hain, toh Python default mein error throw karta hai, 
kyunki object ko function ki tarah call karna allowed nahi hota.
'''
class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x
add_five = Adder(5)
result = add_five(10)
print(result)  # Output: 15

# Other common dunder/magic methods in Python:
'''
| Method        | Purpose                                      |
| ------------- | -------------------------------------------- |
| `__str__`     | Define string representation of the object    |
| `__repr__`    | Define developer-friendly string representation |
| `__len__`     | Define behavior for len() function            |
| `__add__`     | Define behavior for + operator                |
| `__sub__`     | Define behavior for - operator                |
| `__mul__`     | Define behavior for * operator                |
| `__truediv__` | Define behavior for / operator                |
| `__eq__`      | Define behavior for == operator               |
| `__lt__`      | Define behavior for < operator                |
| `__le__`      | Define behavior for <= operator               |
| `__gt__`      | Define behavior for > operator                |
| `__ge__`      | Define behavior for >= operator               |
| `__call__`    | Define behavior for calling the object as a function |
'''