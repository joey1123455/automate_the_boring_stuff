#! python3
# coinToss.py - Flips a coin multiple times

import random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')
logging.disable()
option = ['heads', 'tails']
guess = ''
while guess not in option:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess in option:
        pass
            
key = random.randint(0, 1)
toss = option[key]
logging.critical(f'value of guess:{guess}')
logging.critical(f'value of toss: {toss}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.critical(f'value of guess:{guess}')
    logging.critical(f'value of toss: {toss}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of the program')