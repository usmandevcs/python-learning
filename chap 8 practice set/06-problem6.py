# 6. Write a python function which converts inches to cms. 

def in_to_cm(n):
    return n*2.54
inches = int(input("Enter length in inches: "))
print(in_to_cm(inches),"cm")
