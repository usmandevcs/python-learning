# Class Method:
'''
Class method is a method that is bound to the class and not the 
instance of the class. It can be called on the class itself or 
on an instance of the class. It takes the class as the first 
argument and can access and modify the class state that applies 
across all instances of the class.
'''
'''
Class method ko define karne ke liye @classmethod decorator ka 
use kiya jata hai.
Class method ka first parameter hamesha cls hota hai, jo class 
ko refer karta hai na ke instance ko. Iska use class level data 
ko access aur modify karne ke liye hota hai.
class method k zariye class functions par prefrence mil jati ha,
aur ye instance method se zyada efficient hoti hai jab hume class
level data ko access karna hota hai.
'''
'''
class method take (cls) as a first parameter, jisme cls class 
ko refer karta hai. Iska use class level data ko access aur 
modify karne ke liye hota hai. Class method ka use factory 
methods banane ke liye bhi hota hai, jisme wo class ke objects 
create karte hain.
'''
# Example:
class Student:
    count = 0  # class attribute to keep track of number of students
    total = 0.0  # class attribute to keep track of total GPA
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1  # increment count when a new student is created
        Student.total += gpa  # add gpa to total when a new student is created

        # instance method
    def get_info(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")
# class method to get total count of students
    @classmethod
    def get_count(cls):
        print(f"Total number of students: {cls.count}")
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            print(f"Average GPA: {cls.total / cls.count:.2f}")

s1 = Student("Usman", 2.5)
s2 = Student("Husnain", 3.8)
s3 = Student("Arham", 3.2)
s1.get_info()
s2.get_info()
s3.get_info()
Student.get_count()
Student.get_average_gpa()