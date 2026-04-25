# Writting Files: (.txt, .csv, .json, etc.)
'''
To write to a file, we can use the built-in open() function 
with the 'w' mode. This will create a new file if it doesn't 
exist or overwrite the existing file if it does. We can then 
use the write() method to add content to the file.
'''
# First we start with Plane text file (.txt):
# Writing to a text file
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\example2.txt'
with open(file_path, 'w') as f:  # f = file object
    f.write("Hello, this is a sample text file.\n")
    f.write("We are learning how to write to files in Python.\n")
    f.write("This is the third line of the file.\n")
'''
is method se aik new file generate hogi jis me uper diya huwa 
text likhha hoga. Agar example.txt file already exist karti hai 
to uska content overwrite ho jayega.
'''
# Another way to write to a file:
text_data = "I like Hot wings."
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\example1.txt'  # this is the path where the file will be created or overwritten
with open(file_path, 'w') as f:
    f.write(text_data)

# Writting Python files in Json:
'''
To write a json file first we need to understand what is mean by 
json means JavaScript Object Notation, which is a lightweight 
data-interchange format. It is easy for humans to read and write, 
and it is also easy for machines to parse and generate. JSON is 
often used for storing and exchanging data between a server and 
a web application, as well as for configuration files and data 
storage in various applications.
''' 
'''
To write a file in json we need to import json module.
'''
import json
employee_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}
file_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\employee.json" 
# this is the path where the file will be created or overwritten
# Make sure to use double backslashes (\\) in the file path to avoid escape character issues.
# Alternatively, we can use (/) instead of (\\) in the file path.  

with open(file_path, 'w') as json_file:
    json.dump(employee_data, json_file, indent=4)
    print("Data has been written to the JSON file successfully.")
'''
Here we use json.dump() method to write the employee_data 
dictionary to a JSON file. The indent parameter is used to 
format the JSON file with indentation for better readability.
'''

# There some other methods to write to a JSON file:
'''
Method 1: json.dumps() method ka use karke hum JSON string ko
file me likh sakte hain.
Method 2: json.dump() method ka use karke hum Python object ko
JSON file me likh sakte hain.
dump() and dumps() methods me farq ye hai ki dump() method 
Python object ko directly file me likhta hai, jabki dumps() method 
Python object ko JSON string me convert karta hai, jise hum 
manually file me likh sakte hain.
Method 3: with open() statement ka use karke hum JSON file me
data likh sakte hain.
Method 4: pandas library ka use karke hum DataFrame ko JSON file me
likh sakte hain.
Method 5: loads() method ka use karke hum JSON string ko Python 
object me convert karke file me likh sakte hain.
'''

# Writing Python file to a CSV file:
'''
To write to a CSV file, first we need to understand what is mean 
by CSV, which stands for Comma-Separated Values. It is a simple 
file format used to store tabular data, such as a spreadsheet 
or database. Each line in a CSV file represents a row of data, 
and each value within that row is separated by a comma. CSV 
files are commonly used for data exchange between different 
applications, as they can be easily read and written by both 
humans and machines. They are often used for importing and 
exporting data in spreadsheet applications, databases, and 
programming languages.
'''
import csv
data = [
    ['Name', 'Age', 'City'], # Its the header of the csv file
    ['Alice', 30, 'New York'], # First row of data
    ['Bob', 25, 'Los Angeles'], # Second row of data
    ['Charlie', 35, 'Chicago'] # Third row of data
]

file_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\example.csv"
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data[0])  # Writing the header
    writer.writerow(data[1])  # Writing the first row of data   
    writer.writerow(data[2])  # Writing the second row of data
    writer.writerow(data[3])  # Writing the third row of data
    print("Data has been written to the CSV file successfully.")
# lets use another method to write to a CSV file:
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)  # Writing all rows at once

# another method to write to a CSV file by using try-except:
try:
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0])  # Using the header as fieldnames
        writer.writeheader()  # Writing the header
        for row in data[1:]:  # Writing the data rows
            writer.writerow({'Name': row[0], 'Age': row[1], 'City': row[2]})
except Exception as e:
    print(f"An error occurred: {e}")
# Methods:
'''
writing to a CSV file ke liye hum csv module ka use karte hain.
is code me humne ek CSV file create ki hai jisme 4 rows hain,
jisme pehli row me column headers hain aur baaki rows me data hai.
writer.writerow() method ka use karke humne rows ko CSV file me 
likha hai.
isi tarah hum aur bhi methods ka use karke csv file me data likh 
sakte hain, 
Method 1: writerows() method ka use karke hum multiple rows 
ko ek saath likh sakte hain.
Method 2: dictwriter() method ka use karke hum dictionary ke 
form me data likh sakte hain.
Method 3: pandas library ka use karke hum DataFrame ko CSV file me 
likh sakte hain.
Method 4: csv.writer() method ka use karke hum manually rows ko 
csv file me likh sakte hain.

'''