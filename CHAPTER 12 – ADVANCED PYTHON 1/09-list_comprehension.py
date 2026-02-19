# LIST COMPREHENSIONS 
'''
List Comprehension is an elegant way to create lists based 
on existing lists. 
'''
# SYNTAX
# [expression for item in iterable if condition]
# Example:
list1 = [1,7,12,11,22,] 
list2 = [x for x in list1 if x > 8]
print(list2)
# Ye kya hai?
'''
List banane ka ek line wala smart tareeqa.
'''
# Problem:
# List banana chahte hain numbers ke squares ki:
# python# Purana lamba tareeqa
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print(squares)  # [1, 4, 9, 16, 25]
# List Comprehension:
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in range(1,11)]
print(squares)  

# Parho aise:
"Har number ke liye, us number ka square"


# Condition ke saath:
# Sirf even numbers chahiye:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sirf even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
# Parho aise:
"Har number ke liye (agar even hai), wo number"

# Real examples:
# 1. Pass students:
marks = [45, 67, 89, 23, 90, 56, 78]

# Sirf pass students (50+)
passed = [mark for mark in marks if mark >= 50]
print(passed)  # [67, 89, 90, 56, 78]

# 2. Names uppercase:
names = ['ahmed', 'ali', 'sara']

# Sab uppercase
upper = [name.upper() for name in names]
print(upper)  # ['AHMED', 'ALI', 'SARA']

# 3. Price with tax:
prices = [100, 200, 300, 400]

# 17% tax add karo
with_tax = [price * 1.17 for price in prices]
print(with_tax)  # [117.0, 234.0, 351.0, 468.0]

# 4. Filter long names:
names = ['Ali', 'Ahmed', 'Fatima', 'Sara', 'Hassan']

# Sirf 5+ letters wale
long_names = [name for name in names if len(name) >= 5]
print(long_names)  # ['Ahmed', 'Fatima', 'Hassan']

# If-else ke saath:
numbers = [1, 2, 3, 4, 5, 6]

# Even ko "E", Odd ko "O"
labels = ['E' if num % 2 == 0 else 'O' for num in numbers]
print(labels)  # ['O', 'E', 'O', 'E', 'O', 'E']

# Kahan use hota hai?
# Data filtering (sirf kuch items chahiye)
# Transformations (har item ko change karna)
# Quick calculations
# Jab code chota rakhna ho

# Faida:
# Code fast chalta hai
# Code short aur readable hai
# Pythonic style hai (professional)
