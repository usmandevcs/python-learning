# Problem 6:
'''
Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. 
'''
class Programmer:
    company = "Microsoft"
    def __init__ (slf, name, sallary, experience):
        slf.name = name
        slf.sallary = sallary
        slf.experience = experience
    def getInfo(self):
        print(f"The name of the programmer is {self.name}, they work at {self.company}, earn {self.sallary} and have {self.experience} years of experience.")
p1 = Programmer("John", 50000, 5)
p2 = Programmer("Alice", 70000, 7)
p1.getInfo()
p2.getInfo()


'''Nothing is happen bcz hum self parameter is liye 
use karty hain ta k code ki read abilty bary bas 
isi liye'''
print