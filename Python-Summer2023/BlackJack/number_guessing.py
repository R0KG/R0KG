import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def take_inp():
    temp = input("Choose the difficulty: 'hard' or 'easy': ")
    if not (temp == 'hard' or temp == 'easy'):
        print("One more time")
        take_inp()
    return temp
        
    
print("hello to the Number guessing game\nI am thinking of a number between 1 and 100: ")
diff = take_inp()
lives = 0

if diff == "hard":
    lives = 5
    rand_num = random.randint(1,100)
    while lives > 0:
        guess = int(input("Take a guess: "))
        if guess == rand_num:
            print("Nice job. You won")
            break
        elif guess < rand_num:
            print("Too cold")
            lives -= 1
        elif guess > rand_num:
            print("Too hot")
            lives -= 1        
else:
    lives = 10
    rand_num = random.randint
    print(f"random number is {rand_num}")
    while lives > 0:
        guess = int(input("Take a guess: "))
        if guess == rand_num:
            print("Nice job. You won")
            break
        elif guess < rand_num:
            print("Too cold")
            lives -= 1
        elif guess > rand_num:
            print("Too hot")
            lives -= 1        
