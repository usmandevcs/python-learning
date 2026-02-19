'''A function can accept some value it can work with.
We can put these values in the parentheses.''' 
# Function with arguments:
'''code block jahan tum function ko input
dete ho taake wo us input per operation kare. Argument sirf
value hoti ha jo function call k waqt pass hoti ha.'''
# Example
def goodday(name):
    print("Have a Good day! " + name)
goodday("Usman")
# is goodday(name) me jo name ha wo aik parameter ha mtlb 
# vo aik value ha
# hum multiples parameters use kar skty hain e.g;

# A function can also return value as shown below: 
def greet(name): 
    gr = "hello "+ name  
    return gr  
a = greet("Usman")
print(a)
# a will now contain "hello Usman"  
# return ka concept
'''return ma hum jo b value store kary gy wo humny jo variable
create kiya hoga wo us se assign ho jaye gi jese uper humny 
a = greet("Usman") ka variable bnaya ha '''
# when we use return value 
'''jab humy koi value variable k sath assign karni ho'''

def goodday(name, ending):
    print("Have a Good day!" + name)
    print(ending)
goodday("Usman","Thank you!")

