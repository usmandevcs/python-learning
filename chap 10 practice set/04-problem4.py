# Problem 4:
'''
Add a static method in problem 2, to greet the user with hello. 
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
    @staticmethod
    def greet_user():
        print("Hello, welcome to the Calculator program!")
Calculator.greet_user()
calc = Calculator(int(input("Enter a number: ")))
print(f"Square of {calc.number} is {calc.square()}")
print(f"Cube of {calc.number} is {calc.cube()}")
print(f"Square root of {calc.number} is {calc.square_root()}")