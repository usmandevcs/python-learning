# WHILE LOOP 
# Syntax: 
# while (condition): # The block keeps executing until the condition is true
# means jab tak false nahi ho jati ye chalta rahy ga. 
#Body of the loop 
'''In while loops, the condition is checked first. If it 
evaluates to true, the body of the loop is executed otherwise 
not! '''

'''If the loop is entered, the process of [condition check &
execution] is continued until the condition becomes False. '''

# Quick Quiz 1: 
    # Write a program to print 1 to 50 using a while loop.

# Example: 
i = 0 
while i < 5: # print "Harry" – 5 times! 
    print("Harry")     
    i = i + 1 
# Note: 
#  If the condition never become false, the loop keeps getting executed. 

# Quiz 1

i = 1
while i <= 50:
    print(i)
    i += 1

# Quiz 2:
# Write a program to print the content of a list using while loops. 

member = ["usman","pond","bookh","dawood"]
i = 0
while i < len(member):
    print(member[i])
    i += 1

