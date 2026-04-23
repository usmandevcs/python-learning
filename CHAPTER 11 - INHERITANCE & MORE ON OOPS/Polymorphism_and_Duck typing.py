# Polymorphism:
'''
Poly = many
Morph = forms

Polymorphism is the ability of an object to take on many forms. 
It allows us to use a single interface to represent different 
types of objects, and it enables us to write code that can work 
with objects of different classes in a uniform way.
'''
'''
In simple terms, polymorphism humy ek interface ke through 
alag-alag types ke objects ko represent karne ki ability hai.
Iska matlab hai ki hum ek hi function ya method ko alag-alag 
classes ke objects ke saath use kar sakte hain, aur woh 
function ya method har class ke objects ke liye alag-alag 
behavior show karega.
'''
# Example:
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
'''
is class Animal me function aik hi ha Speak ka but jab hum 
dog aur cat class me usko override karte hain to jab hum speak
function ko call karte hain to wo dog aur cat ke hisab se
alagalag output deta hai. Isse hum kehte hain ki speak function
polymorphic hai, kyunki wo alag-alag classes ke objects ke
saath alag-alag behavior show karta hai.
'''

# How we achieve polymorphism in Python?
'''
In Python, polymorphism is achieved through method overriding and
duck typing.
Method overriding allows a subclass to provide a specific implementation
of a method that is already defined in its superclass. 
This means that a subclass can have its own version of a 
method that is different from the one defined in the superclass, 
and when we call that method on an object of the subclass, the 
subclass's version of the method will be executed instead of 
the superclass's version.
'''
# DUCK TYPING:
'''
Duck typing is a concept in Python that allows us to use an 
object of any type as long as it has the necessary methods or 
attributes.

The name "duck typing" comes from the phrase "If it looks like 
a duck and quacks like a duck, then it must be a duck."
In duck typing, the type of an object is determined by its 
behavior rather than its class.

This means that if an object has the necessary methods or 
attributes to perform a certain task, it can be used in that 
context, regardless of its actual type.

For example, if we have a function that expects an object with 
a "quack" method, we can pass any object that has a "quack" 
method, regardless of its class.
'''
# Example:
class Duck:
    def quack(self):
        return "Quack!"
class Person:
    def quack(self):
        return "I'm a person who can quack!"
def make_it_quack(duck):
    print(duck.quack())
duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)
'''
In this example, we have a function make_it_quack that expects an
object with a quack method. We can pass both a Duck object and a
Person object to the function, and it will work as long as both
objects have a quack method. This is an example of duck typing,
where the type of the object is determined by its behavior 
(having a quack method) rather than its class.
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())

