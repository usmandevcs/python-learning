# Problem 5:
'''
You have a file named 'data.txt' which contains multiple lines 
of text.
'''
words = ["Donkey", "Monkey", "Elephant"]
with open("list.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#####")
with open("list.txt", "w") as f:
    f.write(content)