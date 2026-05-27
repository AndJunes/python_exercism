"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    dictionary = {}
    for note in notes:
        dictionary.setdefault(note, 1)
    return dictionary

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    dict(recipe_updates)
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order."""
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information."""

    result = {}

    for key in sorted(cart.keys(), reverse=True):
        quantity = cart[key]
        aisle, refrigerated = aisle_mapping[key]
        result[key] = [quantity, aisle, refrigerated]
    return result

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    result = {}
    for key, value in store_inventory.items():
        stock = value[0]
        aisle = value[1]
        refrigerated = value[2]
        if key in fulfillment_cart:
            ordered_amount = fulfillment_cart[key][0]
            remaining = stock - ordered_amount
            if remaining == 0:
                remaining = 'Out of Stock'
            result[key] = [remaining, aisle, refrigerated]
        else:
            result[key] = value
    return result