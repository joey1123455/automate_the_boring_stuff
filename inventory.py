backPack = {
   'arrows': 12, 'torch': 6, 'rope': 1, 'gold coin': 42, 'dagger': 1 
}



def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) +  ' ' + k )
        itemTotal += v 
    print(f'Total number of items {itemTotal}')


displayInventory(backPack)



inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addeditems):
    for i in addeditems:
        inventory = inventory.append(addeditems)
    return inventory

def totalAmount(inventory, item):
    totlaAmount = 0
    for k, v in inventory.items():
        totalAmount = totalAmount + v.get(item, 0)
    return totalAmount


# addToInventory(inv, dragonLoot)
print('Number of things:')
print(' - Gold coin     ' + str(totalAmount(inv, 'gold coin')))
print(' - Gold coin     ' + str(totalAmount(inv, 'dagger')))
print(' - Gold coin     ' + str(totalAmount(inv, 'ruby')))
print(' - Gold coin     ' + str(totalAmount(inv, 'rope')))