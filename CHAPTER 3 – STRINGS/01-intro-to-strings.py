# name = "Alice"
# name = 'Bob'
# name = """Charlie"""
# name = '''Diana'''
# string is immuteable or sting is unchangeable

# String Slicing
#  in string slicing we use index to get a part of string
name = "Alice"
nameshort = name[0:3] # Output: Ali
print(name[0:3]) # Output: Ali
print(nameshort)
# in python index starts from 0
print(name[1:4]) # Output: lic
print(name[:4]) # Output: Alic
character3 = name[3] # Output: c
print(character3)

# in python we can use negative slicing/index also
print(name[-1]) # Output: e
print(name[-3:-1]) # Output: ic
print(name[:-1]) # Output: Alic
print(name[-4:]) # Output: lice and is same as [-4:-1]
print(name[-4:-1]) # Output: lic