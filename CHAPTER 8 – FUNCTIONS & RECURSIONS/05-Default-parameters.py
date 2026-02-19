# Default value parameter:
'''function definition me parameter ko pehle se koi value assign 
kar dena. Agar caller wo argument na bheje to ye pre-set value 
use hogi.'''
'''We can have a value as default as default argument in a function. 
If we specify name = “stranger” in the line containing def, this
value is used when no argument is passed.''' 
# Example: 
'''def greet(name = "stranger"): 
greet() # name will be "stranger" in function body (default) 
greet("harry") # name will be "harry" in function body (passed)'''

def goodday(name,ending = "Thank you!"):
    print(f"have a good day {name}")
    print(ending)
goodday("Usman")

'''is ma humny ending ki jo value ha wo by default Thank you
rakhi ha agr hum ending ki value koi b assign nhi karty to 
wo by default thank you run ho jaye gi agr kar dety hain to 
jo hum assign kary gy wo run hogi jese hum function with 
arguments me by default koi value assign nhi karty'''
# Example
def goodday(name,ending = "Thank you!"):
    print(f"have a good day {name}")
    print(ending)
goodday("Usman","Thanks!")
'''idher humny value assign ki ha'''