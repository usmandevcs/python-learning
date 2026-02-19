# Problem 8:
'''
Write a program to make a copy of a text file “this. txt” to “this2. txt”
'''

with open("this.txt","r") as f:
    content = f.read()

with open("this2.txt","w") as f:
        f.write(content)
        
