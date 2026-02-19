# TRY WITH ELSE CLAUSE  
'''
Sometimes we want to run a piece of code when try was successful. 
'''
# SYNTAX 
try: 
    pass    # Somecode 
except: 
    pass    # Somecode 
else: 
    pass    # Code         
# This is executed only if the try was successful 

# Example of Try with else clause
'''a simple example of this is:'''
try:
    a = int(input("Enter a number: "))
    
except Exception as e:
    print(e)

else:
    print(f"you enter the number {a}")



# TRY WITH FINALLY 
'''
Python offers a ‘finally’ clause which ensures execution of a 
piece of code inspective of the exception. 
simple mtlb ye k finnaly chaly ga hi chaly ga chahu try: block 
run ho ya except block run ho. 
iska mainly use function ma hota ha agr try: block return ho 
chahy except block return ho jaye tab b finally block run hoga.
'''
# SYNTAX 
try: 
    pass    # Some Code 
except: 
    pass    # Some Code 
finally: 
    pass    # Some Code           
# Executed regardless of error! 

# Example of Try with finally 

try:
    a = int(input("Enter a number: "))
    
except Exception as e:
    print(e)

finally:
    print("Hey")


