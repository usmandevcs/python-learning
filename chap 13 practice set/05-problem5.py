# Problem 5:
'''
Write a program to find the maximum of the numbers in a 
list using the reduce function. 
'''
from functools import reduce
def greater(a, b):
    if(a > b):
        return a
    else:
        return b

l = [20, 13, 12, 15, 70, 23, 65, 21, 100]

s = (reduce(greater, l))

print(f"The greatest number is {s}.")

# Output is the greatest number in the list.