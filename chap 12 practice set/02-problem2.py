# Problem 2:
'''
Write a program to print third, fifth and seventh element 
from a list using enumerate function. 
'''
len = ['Apple','Orange','Bnana','Mango','Grapes','Tomato','Kharbuza']

for i, items in enumerate(len):
    if i == 2 or i == 4 or i == 6:
        print(items)