catNames = []

while True:
    print(f'Enter the name of the cat {len(catNames) + 1} or enter "nothing to stop.":')
    name = input()
        
    if name == '':
        break

    catNames = catNames + [name] #List concatenation
    print('The cat names are:')
    for name in catNames:
        print(f'  {name}')
    # catName6 = input()
    # print('The cat names are:')
    # print('')

