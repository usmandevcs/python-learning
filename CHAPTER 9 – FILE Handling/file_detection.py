# File Detection:
'''
Before we can read from or write to a file, we need to check 
if the file exists. This is important to avoid errors and 
ensure that our program runs smoothly. Python provides several 
ways to check if a file exists, such as using the os module or 
the pathlib module.
'''
'''
OS means Operating System, and it provides a way to interact 
with the underlying operating system. The os module in Python 
allows us to perform various operations related to the file 
system, such as checking if a file exists, creating directories, 
and more. The pathlib module provides an object-oriented 
approach to handling file system paths and also allows us to 
check if a file exists. Both methods are commonly used for file 
detection in Python.
'''

# Using os module:
import os

file_path = "example.txt"
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")    


# How to check if provided path is a file or directory?
# Syntax:
file_path = "example.txt"
if os.path.isfile(file_path):    
    print(f"The path '{file_path}' is a file.")
elif os.path.isdir(file_path):
    print(f"The path '{file_path}' is a directory.")

# Example of checking that a file exist? and provided path is file or directory?:
file_path = "example.txt"
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")

    if os.path.isfile(file_path):    
        print(f"The path '{file_path}' is a file.")
    elif os.path.isdir(file_path):
        print(f"The path '{file_path}' is a directory.")

else:
    print(f"The file '{file_path}' does not exist.")

'''
hum ye method uper waly code me merge kar ky b check kar 
skty hain jesa k use b kiya gya ha upper.
'''

# Using pathlib module:
import pathlib
from pathlib import Path
file_path = Path("example.txt")
if file_path.exists():
    print(f"The file '{file_path}' exists.")    
else:
    print(f"The file '{file_path}' does not exist.")
'''
Pathlib is often preferred for its cleaner and more intuitive 
syntax, while os is more traditional and widely used in older 
codebases. Both methods are effective for checking file 
existence.  
'''