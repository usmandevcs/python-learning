# 2. Write a python program using function to convert Celsius to Fahrenheit. 
def c_to_f(c):
    return (c * 9/5) + 32
c = float(input("Enter temperature in Celsius: "))
print(f"The temperature is {c_to_f(c)}° F.")

