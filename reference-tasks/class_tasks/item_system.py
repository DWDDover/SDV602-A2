# Item
# Must have at least three attributes: name, price, and description
# Must have a use() method that prints what happens when the item is used
# Must implement __str__() to return a human-readable string representation

class Item:
    
    def __init__(self, name: str, price: int, description: str):
        self.name = name
        self.price = price
        self.description = description

    def use():
        ...
        
    def __str__(self):
        print(f"Item name: {self.name}, Item price: {str(self.price)}gp, Description: {self.description}")

# Two subclasses of Item
# Ideas: Consumable, Equipment, Key, Weapon, Armour, or something creative
# Each must add at least one unique attribute that the base Item doesn't have
# Each must call super().__init__() in their constructor
# Each must override the use() method with behaviour specific to that item type
# Each should customize __str__() to include the unique attribute(s)

class Consumable(Item):
    def __init__(self, name: str, price: int, description: str, resource: str, amount: int):
        super().__init__(name, price, description)
        self.resource = resource
        self.amount = amount
        
    def use(self):
        print(f"You consume the {self.name}, it restores {str(self.amount)} {self.resource}")
    
    def __str__(self):
        print(f"Item name: {self.name}, Item price: {str(self.price)}gp, Description: {self.description}, Effect: restores {str(self.amount)} {self.resource}")
        


class Weapon(Item):
    def __init__(self, name: str, price: int, description: str, damage: int, slot: str):
        super().__init__(name, price, description)
        self.damage = damage
        self.slot = slot
        self.equipped = False

    def use(self):
        if self.equipped:
            print(f"You swing the {self.name}, it deals {str(self.damage)} damage")
        else:
            print(f"The {self.name} must be equipped first")
            
    def equip(self):
        if self.equipped:
            print(f"The {self.name} is already equipped in the {self.slot} slot")
        else:
            self.equipped = True
            print(f"The {self.name} is now equipped in the {self.slot} slot")
            
    def __str__(self):
            print(f"Item name: {self.name}, Item price: {str(self.price)}gp, Description: {self.description}, Damage: {str(self.damage)}, Equipment slot: {self.slot}")
            


# Inventory:
# Must store multiple Item instances
# Must have an add_item() method to add items to the inventory
# Must have a remove_item() method that removes an item by name
# Must have a list_items() method that prints all items currently stored
# Must implement __len__() so that calling len(inventory) returns the item count

class Inventory:
    def __init__(self, contents: list = []):
            self.contents = []

    def add_item(self, item):
        self.contents.append(item)
        
    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)
            
    def list_items(self):
        for item in self.contents:
            item.__str__()
            
    def __len__(self):
        print(len(self.contents))
    


if __name__ == "__main__":
    
    healthPotion = Consumable("health potion", 5, "A red potion", "HP", 30)
    manaPotion = Consumable("mana potion", 7, "A blue potion", "MP", 20)
    rustySword = Weapon("Rusty Sword", 20, "A worn looking sword", 5, "right hand")
    inventory = Inventory()

    healthPotion.use()
    manaPotion.use()
    
    rustySword.equip()
    rustySword.use()
    rustySword.__str__()

    inventory.add_item(rustySword)
    inventory.add_item(healthPotion)
    inventory.add_item(manaPotion)
    inventory.list_items()
    inventory.__len__()
    inventory.remove_item(rustySword)
    inventory.list_items()