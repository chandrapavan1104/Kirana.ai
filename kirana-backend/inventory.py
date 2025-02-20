# In-memory inventory list
inventory = [
    {"name": "Rice", "quantity": 10},
    {"name": "Wheat", "quantity": 20}
]

# CRUD Functions

def add_item(name: str, quantity: int) -> str:
    """
    Adds an item to the inventory. If the item exists, updates the quantity.

    Args:
        name (str): The name of the item.
        quantity (int): The number of units to add.

    Returns:
        str: A message indicating the success of the operation.
    """
    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            return f"Added {quantity} more units of {name}."
    
    inventory.append({"name": name, "quantity": quantity})
    return f"Added {quantity} units of {name}."

def update_item(name: str, quantity: int) -> str:
    """
    Updates the quantity of an existing item in the inventory.

    Args:
        name (str): The name of the item.
        quantity (int): The new quantity to set.

    Returns:
        str: A message indicating whether the update was successful or if the item was not found.
    """
    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] = quantity
            return f"Updated {name} to {quantity} units."
    
    return f"Item '{name}' not found in inventory."

def delete_item(name: str) -> str:
    """
    Deletes an item from the inventory.

    Args:
        name (str): The name of the item to delete.

    Returns:
        str: A message indicating whether the deletion was successful or if the item was not found.
    """
    global inventory
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory = [i for i in inventory if i["name"].lower() != name.lower()]
            return f"Deleted {name} from inventory."
    
    return f"Item '{name}' not found in inventory."

def get_inventory() -> dict:
    """
    Retrieves the current inventory.

    Returns:
        dict: A dictionary where keys are item names and values are their quantities.
    """
    if not inventory:
        return {"message": "Inventory is empty."}

    return {item["name"]: item["quantity"] for item in inventory}
