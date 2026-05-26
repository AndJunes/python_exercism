"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
    
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    if item in inventory:
        inventory.pop(item)
        return inventory
    else:
        return inventory.pop(item, inventory)

def list_inventory(inventory):
    list = []
    for item in inventory:
        if inventory[item] > 0:
            tuple_item = tuple([item, inventory[item]])
            list.append(tuple_item)
    return list
