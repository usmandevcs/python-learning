# RECURSION 
# Recursion is a function which calls itself.          
'''
Recursion: 
    Aik function jo apne aap ko dobara call karta ha.
ye khud ko call is liye karta ha bcz iska logic khud se 
connected hota.
Yeh tab use hota ha jab problem apni hi chhoti copies me toot 
sakti ho.
'''
'''
recursion jo ha hmari help karta ha complex code ko asan karny
ma bary code ko hum recursion ki help se chhoti chhoti functions
ma convert kar sakty ha.
'''
# Core structure:
# base case:
'''
aik base condition lazmi hoti ha recursion ma ta k code 
infinite loop ma na chala jaye.
'''
        # jahan call ruk jaye
# recursive step: 
        # jahan function khud ko chhoti input ke sath call kare
# It is used to directly use a mathematical formula as function.  
# Example: 
'''factorial(n) = n x factorial (n-1) 
This function can be defined as follows: 
def factorial(n) 
if i == 0 or i==1: # base condition which doesn’t call the 
function any further.
return 1 
else: 
return n*factorial(n-1) # function calling itself'''

# Example of factorial
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x n-1 x.....3 x 2 x 1
             or
factorial(n) = n x n * factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the number:"))
print(f"The factorial of this number is: {factorial(n)}")
# Note 
'''The programmer needs to be extremely careful while working 
with recursion to ensure that the function doesn’t infinitely 
keep calling itself. Recursion is sometimes the most direct way 
to code an algorithm.
'''
