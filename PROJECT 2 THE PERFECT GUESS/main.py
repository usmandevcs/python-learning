# PROJECT 2: GUESS THE PERFECT NUMBER

import random

actual_number = random.randint(1, 100)

guesses = 0

while True:
    user_guess = int(input("Guess the nmuber: "))
    guesses += 1
    if user_guess <= 0:
        print("Zyada gand na marwa bc!")
    elif user_guess > actual_number:
        print("Lower number guess kar bharwy!")
    elif user_guess < actual_number:
        print("Higher number likh bharwy!")
    else:
        print(f"Congratulations! you guess the Correct number {actual_number} in {guesses} attempts.")
        break