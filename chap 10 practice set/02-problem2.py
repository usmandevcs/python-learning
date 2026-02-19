# Problem 2:
'''
Write a class “Calculator” capable of finding square, cube and 
square root of a number. 
'''
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number
    
    def square_root(self):
        return self.number ** 0.5
calc = Calculator(int(input("Enter a number: ")))
print(f"Square of {calc.number} is {calc.square()}")
print(f"Cube of {calc.number} is {calc.cube()}")
print(f"Square root of {calc.number} is {calc.square_root()}")
