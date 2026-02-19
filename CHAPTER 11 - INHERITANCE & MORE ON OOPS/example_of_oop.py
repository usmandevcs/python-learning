# EXAMPLE OF OOP CONCEPTS IN PYTHON

from abc import ABC, abstractmethod

# 1. ABSTRACTION (Abstract Class)
class Employee(ABC):
    """
    Yeh ek Abstract Base Class hai. Hum iska Object nahi bana sakte.
    Iska maqsad sirf dusri classes ko naksha (blueprint) dena hai.
    """
    
    # ENCAPSULATION: __ (Private variable)
    def __init__(self, name, salary):
        self.name = name  # Public
        self.__salary = salary # Private: sirf methods ke zariye change hoga

    # ENCAPSULATION: Getter method to access private salary
    def get_salary(self):
        return self.__salary

    # ABSTRACTION: Abstract method. Har aulaad Class ko yeh amal dena zaroori hai
    @abstractmethod
    def calculate_bonus(self):
        pass # Amal (implementation) Child Class degi

    # General method for Polymorphism
    def display_info(self):
        print(f"Name: {self.name}, Role: {self.__class__.__name__}")
        print(f"Base Salary: ${self.get_salary()}")


# 2. INHERITANCE: Developer Class, Employee se Virsat le rahi hai
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Parent Class ka __init__ call karna zaroori hai
        super().__init__(name, salary) 
        self.language = programming_language # New attribute

    # POLYMORPHISM (Method Overriding): calculate_bonus ka amal
    def calculate_bonus(self):
        # Developer ka bonus salary ka 10%
        return self.get_salary() * 0.10

    # display_info ko override kar ke mazeed info add karna (Optional Overriding)
    def display_info(self):
        # Parent ka display_info call kiya
        super().display_info()
        print(f"Skill: {self.language}")


# 3. INHERITANCE: Manager Class bhi Employee se Virsat le rahi hai
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    # POLYMORPHISM (Method Overriding): calculate_bonus ka amal alag hai
    def calculate_bonus(self):
        # Manager ka bonus salary ka 20%
        return self.get_salary() * 0.20 + (self.team_size * 50) # Team size ka extra bonus


# --- Testing aur Polymorphism ---

ali = Developer("Ali", 60000, "Python")
farah = Manager("Farah", 80000, 5)

print("--- Ali (Developer) ---")
ali.display_info() # Polymorphism: Employee ka display_info + Developer ki info
print(f"Bonus: ${ali.calculate_bonus()}") # Polymorphism: Developer ka bonus calculation

print("\n--- Farah (Manager) ---")
farah.display_info() # Polymorphism: Employee ka display_info + Manager ki info
print(f"Bonus: ${farah.calculate_bonus()}") # Polymorphism: Manager ka bonus calculation

# Ab ek general function jahan Polymorphism ka fayda nazar aayega:
def process_employee(emp):
    """Yeh function kisi bhi Employee type ke Object ko process kar sakta hai."""
    print(f"\nProcessing {emp.name}...")
    # Yeh command sab ke liye ek jaisi hai, lekin output alag hai!
    print(f"{emp.name} ka Annual Bonus: ${emp.calculate_bonus()}") 
    # Yahi POLYMORPHISM hai!

process_employee(ali)
process_employee(farah)

# print(ali.__salary) # ERROR! Private variable is protected by Encapsulation
# print(ali.get_salary()) # Ok! Accessible via a Public Getter Method