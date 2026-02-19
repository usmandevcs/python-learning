# LIST 
'''list is a collection or a container to 
store multiple items and values of any 
data type in a single variable.
''' 
# for example
friends = ['ali', 'ahmed', 'apple',23,45.6,True]
print(friends)
#accessing list items
print(friends[0]) #first item   
print(friends[3]) #fourth item
print(friends[-1]) #last item
print(friends[-3]) #third last item
#slicing a list
print(friends[1:4]) #from index 1 to index 3
print(friends[:4]) #from start to index 3
print(friends[2:]) #from index 2 to end
print(friends[-4:]) #from fourth last to end

'''lists can be modified, added to, and removed means lists 
are changeable/muteable but strings are immutable thats why 
we can not change a single character of a string and 
use lists '''
friends[0] = 'sami' #changing first item
print(friends)  #it relace ali with sami 