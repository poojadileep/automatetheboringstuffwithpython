inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(Inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
          print(v , k)
          item_total += v
        print("Total number of items: " + str(item_total))
  
def addToInventory(inventory, addedItems):
    # your code goes here
 print(inventory)
  
  


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
