# EXCEPTION HANDLING IN PYTHON 
'''
There are many built-in exceptions which are raised in python when 
something goes wrong. 
Exception in python can be handled using a try statement. The code 
that handles the exception is written in the except clause.
ye mainly tab use hota jab koi invalid cheez input ki jaye ya 
koi aesa kam jis se program crash kary ya eror dy to us cheez ko 
handle karny k exception handling use ki jati ha ta k user ko 
pata b lag jaye k invalid cheez input hoi ha aur eror b na aye.
'''
# Types of Exceptions:
'''
1. ZeroDivisionError: Raised when division by zero is attempted.
2. ValueError: Raised when a function receives an argument of 
the right type but an inappropriate value.
3. TypeError: Raised when an operation or function is applied 
to an object of inappropriate type.
4. IndexError: Raised when a sequence subscript is out of range.
5. KeyError: Raised when a dictionary key is not found.
6. FileNotFoundError: Raised when a file or directory is 
requested but cannot be found.
7. ImportError: Raised when an import statement fails to find 
the module or when a from ... import fails to find a named 
attribute in the module.
'''
try: # Code which might throw exception  
    pass
except Exception as e:  
    print(e)

# Example
try:
    a = int(input("Hey! Enter a number: "))
    print(a)
except Exception as e:
    print(e)
    print("Thank you!")

'''
When the exception is handled, the code flow continues without 
program interruption. 
'''


# We can also specify the exception to catch like below: 
try: 
    pass # Code 
except ZeroDivisionError: 
    pass # Code 
except TypeError: 
    pass # Code 
except: 
    pass # Code       
# All other exceptions are handled here. 
'''
uper diye syntax ka mtlb ha hum chahy to different erors k liye 
different msgs print karwa skty hain except ko use kar k.
'''


# RAISING EXCEPTIONS 
'''
We can raise custom exceptions using the 'raise' keyword in python. 
'''
'''
'''
# Example 1:

def check_age(age):
    if age < 18:
        raise ValueError("Too young")
    else:
        print("you are old enough")
        
a = check_age(int(input("Enter the age: "))) # Raises ValueError
print(a)
# Example 2:

x = int(input("Enter a number: "))
if x < 0:
    raise Exception("Negative value not allowed")
