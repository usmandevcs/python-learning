# Problem 11:
'''
 Write a program to copy the content of one file to another 
 file using python.
 '''
with open("xyz.txt","r") as f:
    content = f.read()  # Reading content from the source file
with open("copy_xyz.txt","w") as f1:
    f1.write(content)  # Writing the content to the destination file
