def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC_ITEMS'.center(leftWidth + rightWidth, '_'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))

items = {'sandwitches ': 4, 'apples ': 12, 'cups ': 4, 'cookies ': 8000}
printPicnic(items, 12, 5)
printPicnic(items, 20, 6)
