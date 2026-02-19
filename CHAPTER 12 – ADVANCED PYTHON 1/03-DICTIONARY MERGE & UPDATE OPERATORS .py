# DICTIONARY MERGE & UPDATE OPERATORS 
'''
New operators | and |= allow for merging and updating dictionaries. 
'''
dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
dict1 |= dict2  # use for updating
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
print(dict1)   # Output: {'a': 1, 'b': 3, 'c': 4}


# MULTIPLE CONTEXT MANAGER
'''
You can now use multiple context managers in a single with statement 
more cleanly using the parenthesised context manager. simply hum "with"
statement ko use kar k multiple files ko open ya read kar skty hain. 
'''
# SYNTAX
with ( 
open('file1.txt') as f1, 
open('file2.txt') as f2 
): 
    pass
# Process files 