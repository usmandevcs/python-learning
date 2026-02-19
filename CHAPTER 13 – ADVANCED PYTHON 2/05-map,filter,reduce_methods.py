# MAP, FILTER & REDUCE Methods:
# MAP:
'''
Map applies a function to all the items in an input_list. 
'''
# Syntax of Map:
map(function, ["input_list"]) 
# the function can be lambda function 
# Har element par function apply hota hai.
# Example 1: list(map(lambda x: x*2, [1,2,3])) # output → [2,4,6]
# Example 2: list(map(str, [1,2,3]))      #output → ["1","2","3"]

# FILTER:
'''
Filter creates a list of items for which the function returns true. 
'''
# SYNTAX:
list(filter(function)) 
# the function can be lambda function 
# Jo elements True return karte hain sirf woh rehte hain.
# Example 1: list(filter(lambda x: x>5, [2,7,8])) → [7,8]
# Example 2: list(filter(lambda x: x%2==1, [1,2,3,4])) → [1,3]
# REDUCE:
'''
Reduce applies a rolling computation to sequential pair of elements. 
'''
# SYNTAX:
from functools import reduce 
val=reduce (function, ["list1"])        
# the function can be lambda function 
# Puri list ko cumulative result me compress karta hai.
# Example 1: reduce(lambda x,y: x+y, [1,2,3]) → 6
# Example 2: reduce(lambda x,y: x*y, [2,3,4]) → 24