# Problem 4:
'''
A file contains a word “Donkey” multiple times. You need to 
write a program which replace this word with ##### by updating 
the same file.  
'''
# Open the file in read mode to get its content
with open("file.txt", "r") as f:
    content = f.read()
# Replace all occurrences of the word "Donkey" with "#####"
updated_content = content.replace("Donkey","#####")
# Open the file in write mode to update it with the modified content
with open("file.txt", "w") as f:
    f.write(updated_content)