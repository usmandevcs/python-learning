# Problem 2:
'''
Write a program to input name, marks and phone number of 
a student and format it. 
using the format function like below: 
“The name of the student is Harry, his marks are 72 and phone 
number is 99999888” 
'''
name = input("Name: ")
marks = float(input("Enter your marks: "))
p_number = int(input("Enter mobile number: "))

print("The name of the student is {n}, his marks are {m} and" \
" his phone number is {mn}".format(n = name, m = marks,
mn = p_number))