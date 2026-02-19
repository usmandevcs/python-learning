# Problem 4:
'''
Write a program to filter a list of numbers which are 
divisible by 5.
'''
def divisible5(n):
    if(n%5 == 0):
        return True
    else:
        return False

l = [20, 13, 12, 15, 70, 23, 65, 21, 100]
s = list(filter(divisible5, l))
print(s)

