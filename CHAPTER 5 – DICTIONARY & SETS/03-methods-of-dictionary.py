# methods of dictionary in python
# 1st is .items() method
'''item()method jo ha wo dictionary k sare key:value pairs ko
as a list of tuples k form me return krta ha jisme har tuple
me ek key aur uski corresponding value hoti ha '''
marks = {   
    "Alice": 85,
    "Bob": 92,  
    "Charlie": 78,
    "David": 90
}
print(marks.items())  # dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 90)])

# 2nd method is .keys() method
'''keys() method jo ha wo dictionary k sare keys ko as a
list me return krta ha '''
print(marks.keys())  # dict_keys(['Alice', 'Bob', 'Charlie', 'David'])

# 3rd method is .values() method    
'''values() method jo ha wo dictionary k sare values ko as a
list me return krta ha '''
print(marks.values())  # dict_values([85, 92, 78, 90])

# 4th method is .get() method   
'''get() method jo ha wo dictionary me se kisi specific key
ki value ko return krta ha agar wo key dictionary me exist
krti ha to '''
print(marks.get("Bob"))  # 92

# 5th method is .update() method    
'''update() method jo ha wo dictionary me naye key:value
pairs ko add krne k liye use hota ha ya phir existing
key ki value ko update krne k liye use hota ha '''  
marks.update({"Eve": 88})  # adding new key:value pair
marks.update({"Alice": 95})  # updating existing key's value
print(marks)  # {'Alice': 95, 'Bob': 92, 'Charlie': 78, 'David': 90, 'Eve': 88}

# 6th method is .pop() method
'''pop() method jo ha wo dictionary me se kisi specific
key:value pair ko remove krne k liye use hota ha aur wo
removed value ko return krta ha '''
removed_value = marks.pop("Charlie")
print(removed_value)  # 78  

#7th is dict() method
'''dict() method jo ha wo ek built-in function ha jo
dictionary ko create krne k liye use hota ha '''
new_dict = dict(Fred=75, George=82, Hannah=89)
print(new_dict)  # {'Fred': 75, 'George': 82, 'Hannah': 89}

# 8th is clear() method
'''clear() method jo ha wo dictionary me se sare
key:value pairs ko remove krne k liye use hota ha '''
new_dict.clear()
print(new_dict)  # {}
# ab new_dict empty ho chuka ha

# 9th is copy() method
'''copy() method jo ha wo dictionary ka shallow
copy banane k liye use hota ha '''
marks_copy = marks.copy()
print(marks_copy)  # {'Alice': 95, 'Bob': 92, 'David': 90, 'Eve': 88}
# marks_copy ab marks dictionary ka copy ha

