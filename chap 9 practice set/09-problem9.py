# Problem 9:
'''
9. Write a program to find out whether a file is identical & 
matches the content of another file.
'''
with open("this.txt","r") as f1:
    content1 = f1.read()
with open("poem.txt","r") as f2:
    content2 = f2.read()
if content1 == content2:
    print("The files are identical.")
else:
    print("The files are not identical.")
