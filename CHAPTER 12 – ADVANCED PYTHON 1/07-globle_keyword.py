# THE GLOBLE KEYWORD
'''
‘global’ keyword is used to modify the variable outside of the 
current scope. 
Ye kya hai?
Function ke andar se bahar ka variable change karne ke liye.
'''
# Problem samjho:
pythoncounter = 0  # Ye bahar hai (global)

def increase():
    counter = counter + 1  # ERROR! Ye kaam nahi karega

increase()
# Error kyun? Python confuse ho jata hai - counter bahar ka hai ya andar ka?

# Solution:
pythoncounter = 0  # Global variable

def increase():
    global counter  # Ab Python jaanta hai ye bahar wala hai
    counter = counter + 1

increase()
increase()
print(counter)  # 2

# Simple example: Score tracking
pythonscore = 0  # Game score

def add_points(points):
    global score
    score = score + points
    print(f"Score: {score}")

add_points(10)  # Score: 10
add_points(25)  # Score: 35
add_points(5)   # Score: 40

# Kahan use hota hai?
# Counters (jaise kitni baar kuch hua)
# Game scores
# Global settings jo change ho sakte hain

# Warning:
# Global variables ka kam se kam use karo! Zyada use karne se code confusing ho jata hai.

# Better tareeqa:
# python# Instead of global
def add_points(current_score, points):
    return current_score + points

score = 0
score = add_points(score, 10)
score = add_points(score, 25)
print(score)  # 35
