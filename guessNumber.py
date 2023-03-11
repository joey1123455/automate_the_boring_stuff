#This is the guess no game.
import random

secretNumber = random.randint(1, 200)
print('I am thinking of a number between 1 and 200.')

def guessLeft(left):
    left -= 1
    return left

#Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    guessLeft = 6

    if guess < secretNumber:
        guessLeft(guessLeft)
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This is the correct guess break from loop
    
# return guessLeft

if guess == secretNumber:
    print(f'Good job! You gussed my number in {guessesTaken} guesses')
else:
    print(f'Nope. The number i was thinking of was {secretNumber}')

