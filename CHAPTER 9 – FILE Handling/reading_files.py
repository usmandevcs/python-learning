# Reading Files:
'''
To read a file in Python, you can use the built-in `open()` 
function. Here's an example of how to read a file and print its 
contents:
'''
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\example2.txt'
with open(file_path, "r") as file:
    content = file.read()
    print(content)
# This will print the data which is present in the file. 

'''
lets suppose if this file is not exist then it will give us an 
error. To handle this error we can use try and except block.
'''
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
        print("File read successfully.")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
# lets suppose if someone lock the file then it will give us an error to handle this we will use another except block.
except PermissionError:
    print(f"Permission denied: Unable to read the file at {file_path}.")

# JSON:
# To Read json file we can use json module:
import json
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\employee.json'
try:
    with open(file_path, "r") as file:
        data = json.load(file)
        print(data)
        print("JSON file read successfully.")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from the file at {file_path}.")

# To read a file line by line we can use readline() method or we can use for loop to iterate through the file.
try:    
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())  
        # strip() is used to remove the newline character  except FileNotFoundError:
except FileNotFoundError:
    print(f"The file at {file_path} was not found.") 

# CSV:
# To read a csv file we can use csv module:
import csv
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\example.csv'
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
'''
in csv file data is stored in the form of rows and columns, so
if we just write content = csv.reader(file) then it will give us 
the memory address of the file, to get the data we need to use 
for loop to iterate through the file and print the rows.
'''   