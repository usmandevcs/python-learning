''' Write a program to find whether a given username contains less than 10 
characters or not. '''

username = input("Enter username: ")

if(len(username)>10):
    print("username contain more than 10 letters")
else:
    print(username)
