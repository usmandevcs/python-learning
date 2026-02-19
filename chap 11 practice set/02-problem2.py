# Problem 2:
'''
Create a class ‘Pets’ from a class ‘Animals’ and further create a 
class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
'''
class Animals:
    def __init__(self, species):
        self.species = species
    def info(self):
        return f"Species:{self.species}"
class Pets(Animals):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name
    def info(self):
        return f"Pet name: {self.name}, Species: {self.species}"
class Dog(Pets):
    def __init__(self, name, Breed):
        super().__init__('Dog', name)
        self.Breed = Breed
    def info(self):
        return f"Dog name: {self.name}, Breed: {self.Breed}"
    @staticmethod
    def bark():
        return "Bow! Bow!"
b = Animals("Dog")
print(b.info())
d = Dog("Simbha", "Golden Retriever")
print(d.info())
print(d.bark())