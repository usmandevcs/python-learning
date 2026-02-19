# Problem 1:
'''
Create a class “Programmer” for storing information of few 
programmers working at Microsoft.  
'''
class Programmer:
    company = "Microsoft"
    def __init__ (self, name, sallary, experience):
        self.name = name
        self.sallary = sallary
        self.experience = experience
    def getInfo(self):
        print(f"The name of the programmer is {self.name}, they work at {self.company}, earn {self.sallary} and have {self.experience} years of experience.")
p1 = Programmer("John", 50000, 5)
p2 = Programmer("Alice", 70000, 7)
p1.getInfo()
p2.getInfo()