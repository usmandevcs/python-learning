# THE BREAK STATEMENT 
'''‘break’ is used to come out of the loop when encountered. 
It instructs the program to – exit the loop now.'''

# Example: 
for i in range (80):
    if (i==34):
        break #this means exit the loop 
    print(i)
# this will print 0,1,2 and 3 


# THE CONTINUE STATEMENT 
'''‘continue’ is used to stop the current iteration of the
loop and continue with the next one. It instructs the 
Program to “skip this iteration”.'''

# Example: 
for i in range(80):
    if(i == 34):
        continue # is ka mtlb ha k jo 34 iteration ha usko skip kardo
    print(i)


# PASS STATEMENT 
'''pass is a null statement in python. 
It instructs to “do nothing”.'''
# Example: 
l = [1,7,8] 
for item in l:
    pass
# without pass, the program will throw an error 