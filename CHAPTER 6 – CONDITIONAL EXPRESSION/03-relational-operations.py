'''Relational Operators are used to evaluate conditions 
inside the if statements. Some examples of relational 
operators are: 
==: equals. 
> =: greater than/ equal to. 
< =: lesser than/ equal to. '''
# LOGICAL OPERATORS 
'''In python logical operators operate on conditional statements. 
For Example: 
• and – true if both operands are true else false. 
• or – true if at least one operand is true or else false. 
• not – inverts true to false & false to true. '''

# Example: Logical operators in Python using if, elif, else

age = int(input("enter your age:"))
has_ticket = True
is_vip = False

if age >= 18 and has_ticket:  # AND operator
    print("Entry allowed for regular ticket holder.")
elif age >= 18 and is_vip:    # AND operator with different condition
    print("Entry allowed for VIP guest.")
elif not has_ticket:          # NOT operator
    print("Entry denied: No ticket.")
else:
    print("Entry denied: Underage or invalid status.")

# Additional OR example
day = "Sunday"
if day == "Saturday" or day == "Sunday":  # OR operator
    print("It's weekend, enjoy!")
else:
    print("It's a weekday, work hard.")
