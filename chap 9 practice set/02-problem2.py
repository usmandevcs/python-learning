# Problem 2:
'''
2. The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score.
'''
# Function that simulates a game and returns the score
def game():
    # yahan tum apna actual game ka logic likh sakte ho
    # filhal example ke liye random score return karte hain
    import random
    return random.randint(0, 100)

# Main program
def update_highscore():
    score = game()  # current game score
    print(f"Your score: {score}")

    try:
        # File read karne ki koshish
        with open('Hi-score.txt', 'r') as f:
            content = f.read().strip()
            if content == '':
                highscore = 0
            else:
                highscore = int(content)
    except FileNotFoundError:
        highscore = 0

    # Check agar naya score zyada hai to update karo
    if score > highscore:
        with open('Hi-score.txt', 'w') as f:
            f.write(str(score))
        print("New High Score!")
    else:
        print("No new high score.")

# Run the function
update_highscore()
