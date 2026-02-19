# SELF PARAMETER  
'''
self refers to the instance/object of the class. It is 
automatically passed with a function call from an object. 
'''
'''When a method is called on an object, the object itself is 
passed as the first argument to the method. By convention, this
argument is named 'self'.
This allows the method to access attributes and other methods 
on the same object.
'''
# for example:
# harry.getSalary() # here self is harry
# equivalent to Employee.getSalary(harry)
# The function getSalary() is defined as:
class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is not there")
harry = Employee()
harry.getSalary() # Equivalent to Employee.getSalary(harry)
'''
self is a convention in Python to refer to the instance of the class.
It is used as the first parameter in instance methods to access
attributes and methods of the class.
'''
'''
self method function ma use hota ha jo k object ko refer karta ha
jab hum aik method ko aik object k sath call kartay hain to wo apny
aap object ko as a first parameter pass kar deta ha aur usii 
wajah se hum self parameter ko method k andr define kartay hain
ta k hum us method k andr object k attributes aur methods ko
access kar sakain.
agr hum self parameter ko method k andr define nai kartay to error 
ay ga kyun k jab hum method ko call kartay hain to wo apny aap 
object ko as a first parameter pass kar deta ha aur agar hum self
ko define nai kartay to wo samjhta ha k hum aik aisi method call kar 
rahay hain jo k koi parameter nai leti to wo error throw kar deta ha.
'''

# STATIC METHOD 

'''
static method is a method that does not receive an implicit first 
argument (like self for instance methods or cls for class methods).

static methods are defined using the @staticmethod decorator.
mtlb k aik decorator ki tarah kam karta ha 
'''
'''
Sometimes we need a function that does not use the self-parameter.
We can define a static method like this:
'''
@staticmethod   
# decorator to mark greet as a static method  
def greet(): 
    print("Hello user") 

# For Example:
class Employee:
    company = "Google"

    @staticmethod   
    # decorator to mark greet as a static method  
    def greet(): 
        print("Hello user")
Employee.greet() # Calling static method without creating object