# 8. ENUMERATE
'''
Ye kya hai?
Loop mein number (index) aur value dono chahiye? Enumerate use karo!
'''
# Problem:
fruits = ['apple', 'banana', 'mango']

# Mushkil tareeqa
for i in range(len(fruits)):
    print(f"{i}. {fruits[i]}")

# Aasan tareeqa:
fruits = ['apple', 'banana', 'mango']

for index, fruit in enumerate(fruits):
    print(f"{index}. {fruit}")

# Output:
# 0. apple
# 1. banana
# 2. mango

# 1 se start karna hai?
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. mango

# Real examples:
# Menu:
menu = ['Pizza', 'Burger', 'Pasta', 'Salad']

print("=== MENU ===")
for num, item in enumerate(menu, start=1):
    print(f"{num}. {item}")

# Output:
# === MENU ===
# 1. Pizza
# 2. Burger
# 3. Pasta
# 4. Salad


# Roll numbers:
students = ['Ahmed', 'Ali', 'Sara', 'Fatima']

for roll, name in enumerate(students, start=101):
    print(f"Roll #{roll}: {name}")
# Output:
# Roll #101: Ahmed
# Roll #102: Ali
# Roll #103: Sara
# Roll #104: Fatima


# Kahan use hota hai?
# Numbered lists banane mein
# Menu systems
# Roll numbers, serial numbers print karne mein
# Jab position aur value dono chahiye