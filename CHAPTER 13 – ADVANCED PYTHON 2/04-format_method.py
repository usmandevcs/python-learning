# FORMAT METHOD (STRINGS): 
'''
Formats the values inside the string into a desired output.
means String ke andar placeholders fill karta hai.
'''
# SYNTAX:
    # template.format(p1,p2...) 
# EXAMPLE: 
print("{} is a good {}".format("harry", "boy"))  #1. 
print("{n} is a good {o}".format(o="harry", n="boy"))  #2. 
# output for 1: 
# harry is a good boy  
# output for 2: 
# boy is a good harry  