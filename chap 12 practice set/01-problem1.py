# Problem 1
'''
Write a program to open three files 1.txt, 2.txt and 3.txt 
if any these files are not present, a message without exiting 
the program must be printed prompting the same. 
'''
files = ["1.txt","2.txt","3.txt"]
for file in files:
    try:
        with open(file) as f:
            print(f.read())

    except FileNotFoundError as e:
        print(f"File not found: {e}")

print("Thank you!")