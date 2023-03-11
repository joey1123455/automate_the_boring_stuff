#! python3
# coinFlip.py Simulates fliping a coin 1000 times

import random
heads = 0
for i in range(0,1001):
    if random.randint(0,1) == 1:
        heads = heads + 1
    elif i == 500:
        print('Halfway done!')
print(f'Heads came up {str(heads)} times.')