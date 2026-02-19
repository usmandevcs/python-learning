# operations of sets
# 1st operation is len() operation
'''len() is use to find length of a set it 
is use in sets,dictionaries,lists,tuples'''
set = {1,2,3,4,5,6}
print(len(set)) #output is 6

# 2nd operation is remove() operation
'''this operation is use to remove a element from set 
and update the set'''
set.remove(3)
print(set) # remove 3 from set

# 3rd operation is pop() operation
'''this operation is use to remove a random element from
set means k koi b element remove ho skta ha set se'''
set.pop()
print(set)

# 4th operation is clear() operation
'''this operation is use to clear the all value from 
the set'''
print(set.clear()) # output is set() means empty set
