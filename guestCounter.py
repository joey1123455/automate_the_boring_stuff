allGuest = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}    
    }

def totalBought(guests, item):
    numBought = 0
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return numBought

print('Number of things being bought:')
print(' - Apples     ' + str(totalBought(allGuest, 'apples')))
print(' - Cups     ' + str(totalBought(allGuest, 'cups')))
print(' - Cakes     ' + str(totalBought(allGuest, 'cakes')))
print(' - Ham sandwiches     ' + str(totalBought(allGuest, 'ham sandwiches')))
print(' - Apple pies     ' + str(totalBought(allGuest, 'apple pies')))
