# DECORATOR - “Gift wrapping function”
'''
Decorator is a fuction that extends the behavior/functionality 
of another function without changing/modifying the base function.

It allows us to add extra functionality to an existing function 
in a clean and maintainable way. It is a powerful tool in Python 
that helps in enhancing the functionality of functions or methods 
without modifying their structure. It is often used in 
scenarios like logging, access control, memoization, and more.

Decorator ek wrapper hota hai jo function ko bina change 
kiye uska behavior modify karta hai.

Real life analogy:
Tumne simple gift diya
Kisi ne usko wrap kar diya ribbon se
Gift same, look better.
'''
'''
in simple words, decorator ek function hai jo dusre function 
ko as an argument leta hai aur usko modify karke return 
karta hai. Iska use hum logging, timing, access control, etc. 
ke liye karte hain.
'''
# Decorator pass the base function as an argument to the decorator 

# Example:
from doctest import Example


def add_sprinkles(func):
    def wrapper():
        print("Adding sprinkles on top! 🍬")
        func()  # Call the original function
    return wrapper
@add_sprinkles  # This is the decorator syntax, it is equivalent to: get_ice_cream = add_sprinkles(get_ice_cream)
def get_ice_cream():
    print("Here is your ice cream! 🍨")

get_ice_cream()


# Benefits of Decorators:
'''
1. Code Reusability: Common functionality ko decorator me 
define karke reuse kar sakte hain.
2. Separation of Concerns: Core functionality ko separate 
rakhte hain, aur additional behavior ko decorators me 
handle karte hain.
3. Flexibility: Existing code ko modify kiye bina naye 
behavior add kar sakte hain.
4. Readability: Code ko cleaner aur more readable banata hai,
kya ho raha hai easily samajh aata hai.
5. Built-in Decorators: Python me kuch built-in decorators
hote hain jaise @staticmethod, @classmethod, @property, etc.
6. Third-party Libraries: Python me kai third-party libraries
hote hain jo powerful decorators provide karte hain, jaise
Flask me route decorators, Django me model decorators, etc.
'''

# Decorator with arguments:
'''
kabhi kabhi humy function k ander arguments pass karny hoty hain,
to humy aese decorator ki zarurat hoti hai jo arguments accept 
kar saky. Iske liye hum wrapper function ke ander 
*args aur **kwargs ka use karte hain, jisse humy function k 
positional aur keyword arguments dono ko handle karne me 
madad milti hai. is sy hum decorator ko arguments asani se 
pass kar sakty hain aur usko modify kar sakty hain.
'''
# Example 1:
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles on top! 🍬")
        func(*args, **kwargs)  # Call the original function
    return wrapper
@add_sprinkles  # This is the decorator syntax, it is equivalent to: get_ice_cream = add_sprinkles(get_ice_cream)
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream! 🍨")

get_ice_cream("vanilla")

# Example 2 of a decorator with arguments:

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):  # args = positional arguments, kwargs = keyword arguments
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
# Usage
greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Example 3: Timer example of a decorator with arguments:
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.3f} seconds")
        return result 
    return wrapper
@timer
def compute_square(n):
    return n * n
print(compute_square(10))

# Example of logger:
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@logger
def add(a, b):
    return a + b
# Usage
print(add(5, 3))
