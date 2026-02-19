import random

youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

computer = random.choice([-1, 1, 0])
you = youDict[input("Enter your choice (s/w/g): ").lower()]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if you == computer:
    print("Tie")
elif (you - computer) in [1, -2]:
    print("You win")
else:
    print("You lose")
