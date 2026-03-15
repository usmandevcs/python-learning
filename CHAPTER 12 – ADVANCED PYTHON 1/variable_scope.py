# Variable Scope:
'''
where a variable is visible and accessible in the code. 
Python has three main types of variable scope:
1. Local Scope: 
        Variables defined inside a function are in the local 
scope and can only be accessed within that function.
2. Enclosing Scope: 
        This is the scope of any enclosing functions. If a 
function is defined inside another function, the inner function 
can access variables from the outer function's scope.
3. Global Scope: 
        Variables defined at the top level of a script or 
module are in the global scope and can be accessed from anywhere 
in the code.
4. Built-in Scope: 
        This is the scope of built-in functions and 
variables that are always available in Python, such as 
`print()`, `len()`, etc.
'''
# Scope Resolution:
'''
To access variables from different scopes, Python uses the 
LEGB rule (Local, Enclosing, Global, Built-in). When you 
reference a variable, Python looks for it in the local scope 
first, then in the enclosing scope, then in the global scope, 
and finally in the built-in scope.
'''
# Example of variable scope:


