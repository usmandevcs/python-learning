# Problem 7:
'''
Write a program to find out the line number where python is 
present from ques 6. 
'''
with open("log.txt", "r") as f:
    lines = f.readlines()
# Iterate through lines to find 'python'
# Using enumerate to get line numbers
# Line numbers start from 1
# so we add 1 to the index
# If found, print the line number and break
for i, line in enumerate(lines):
    if "python" in line:
        print(f"'python' found in line {i + 1}")
        break
else:
    print("'python' not found in log file.")