'''Tuples is immutable, ordered collection of items.
or immuteable data type in python just like list 
but the difference is that tuples are immutable '''
#tuples are defined using parentheses ()
#example of tuple
fruits = ('apple', 'banana', 'cherry',23,45.6,True)
print(fruits)
a = (1,2,3,4,5,6)
print(a)
print(type(a))
#accessing tuple items
print(fruits[0]) #first item    
print(fruits[3]) #fourth item
'''if you want to create a tuple with a single item
then you have to add a comma after the item 
e.g; a = (1,) not a = (1) because it will be
considered as an integer'''
b = (1) #it will be integer
print(type(b))
b = (1,) #it will be tuple
print(type(b)) 
#slicing a tuple        
print(fruits[1:4]) #from index 1 to index 3
print(fruits[:4]) #from start to index 3
print(fruits[2:]) #from index 2 to end
print(fruits[-4:]) #from fourth last to end
#tuples are immutable means we can not change, add or remove items
