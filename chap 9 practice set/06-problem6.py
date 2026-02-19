# Problem 6:
'''
Write a program to mine a log file and find out whether it 
contains ‘python’. 
'''
with open("log.txt", "r") as f:
    content = f.read()
if "python" in content:
    print("Found 'python' in log file.")
else:
    print("'python' not found in log file.")