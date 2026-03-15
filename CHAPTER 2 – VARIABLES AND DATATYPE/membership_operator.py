# Membership operator:
'''
The membership operator in Python is used to test whether a 
value is present in a sequence (like a list, tuple, string, etc.) 
or not. The two membership operators are:
1. `in`: Returns `True` if the value is found in the sequence, 
otherwise returns `False`.
2. `not in`: Returns `True` if the value is not found in the 
sequence, otherwise returns `False`.
'''
# Example of membership operator:
# Using 'in' operator
my_list = [1, 2, 3, 4, 5]
number = int(input("Enter a number to check if it's in the list: "))
if number in my_list:
    print(f"{number} is in the list.")
else:    
    print(f"{number} is not in the list.")

# Using 'not in' operator
my_string = "Hello, World!"
char = input("Enter a character to check if it's not in the string: ")
if char not in my_string:
    print(f"{char} is not in the string.")
else:
    print(f"{char} is in the string.")