#! python3
#Inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'gold coin': 42, 'rope': 1}

def displayInventory(inv):
    print('Inventory')
    itemTotal = 0
    for key, val in inv.items():
        print(f'{str(key)} {val}')
        itemTotal += val
    print(f'Total number of items: {itemTotal}')

def displayUpdatedInventory(inv):
    print('Updated Inventory')
    itemTotal = 0
    for key, val in inv.items():
        print(f'{str(key)} {val}')
        itemTotal += val
    print(f'Total number of items: {itemTotal}')

def addToInventory(inv, nInv):
    count = inv
    for character in nInv:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    return count

def printInventory(inv, nInv):
    addToInventory(inv, nInv)
    print(f'inv has been updated with nInv succesfully')
    displayUpdatedInventory(inv)

# displayInventory(stuff)
# addToInventory(inventory, dragonLoot)
# displayInventory(inventory)

printInventory(inventory, dragonLoot)