# JOIN METHOD (STRINGS) 

# Creates a string from iterable objects. 
l = ["apple", "mango", "banana"] 
result = ", and, ".join(l) 
print(result) 
# The above line will return “apple,and,mango,and,banana”.
'''
List ke elements ko ek hi string me jor deta hai. 
Separator hum khud define karte hain.
'''
# ", ".join(["a","b","c"]) → "a, b, c"

# Example 1: "-".join(["x","y"]) → x-y
# Example 2: " ".join(["Hello","World"]) → Hello World 