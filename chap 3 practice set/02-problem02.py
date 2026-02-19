letter = ''' Dear <|name|>,
congratulations! You are selected!,
on<|date|> '''
print(letter.replace("<|name|>", "Usman").replace("<|date|>", "1st Jan 2026")) 

# this is chaining of replace() function  means we are using two replace function in one statement