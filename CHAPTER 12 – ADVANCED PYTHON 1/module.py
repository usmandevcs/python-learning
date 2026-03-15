# Module:
'''
Module is just a file containing Python code. It can define 
functions, classes, and variables. It can also include runnable 
code. Modules are a way to organize and reuse code across 
different parts of a program or even across different programs.
in simple words, a file containing code you want to reuse in 
our program is called a module.
to use module, we need to import it using the "import" statement.
(built in or our own) 
'''
# print(help("modules"))  # Built in module

# Example of creating and using a module:
import math  # Importing the built-in math module
print(math.pi)

# we can also give a nick name to the module using "as" keyword:
import math as m
print(m.sqrt(16))  # Using the sqrt function from the math module

# from a module we can import specific functions or variables: 
from math import sqrt, pi
# just like this.
