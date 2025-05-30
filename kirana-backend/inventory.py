from typing import Dict, List, Optional, Any
from datetime import datetime

# In-memory storage
inventory_items: Dict[str, Dict] = {}
inventory: Dict[str, Dict] = {}

def add_item(name: str, quantity: float, unit: str) -> Dict[str, Any]:
    """
    Adds an item to the inventory.
    
    Args:
        name (str): The name of the item.
        quantity (float): The number of units to add.
        unit (str): The unit of measurement (kg, litre, etc.).
        
    Returns:
        Dict[str, Any]: Response with success status and item details.
    """
    try:
        # Add to inventory_items if not exists
        if name not in inventory_items:
            inventory_items[name] = {
                "name": name,
                "unit": unit,
                "price": 0.0,  # Default price
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
        
        # Update inventory
        if name in inventory:
            inventory[name]["quantity"] += quantity
            inventory[name]["updated_at"] = datetime.now()
        else:
            inventory[name] = {
                "item_id": name,
                "quantity": quantity,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
        
        return {
            "success": True,
            "item": {
                "id": name,
                "name": name,
                "quantity_added": quantity,
                "unit": unit,
                "price": inventory_items[name]["price"]
            },
            "response": f"✅ Added {quantity} {unit} of {name} to inventory."
        }
    except Exception as e:
        return {
            "success": False,
            "response": f"❌ Error adding item: {str(e)}"
        }

def update_item(name: str, quantity: float, unit: str) -> Dict[str, Any]:
    """
    Updates an item's quantity in the inventory.
    
    Args:
        name (str): The name of the item.
        quantity (float): The new quantity.
        unit (str): The unit of measurement (kg, litre, etc.).
        
    Returns:
        Dict[str, Any]: Response with success status and item details.
    """
    try:
        if name not in inventory:
            return {
                "success": False,
                "response": f"❌ Item {name} not found in inventory."
            }
        
        inventory[name]["quantity"] = quantity
        inventory[name]["updated_at"] = datetime.now()
        
        # Update unit in inventory_items if it exists
        if name in inventory_items:
            inventory_items[name]["unit"] = unit
            inventory_items[name]["updated_at"] = datetime.now()
        
        return {
            "success": True,
            "item": {
                "id": name,
                "name": name,
                "quantity": quantity,
                "unit": unit,
                "price": inventory_items[name]["price"]
            },
            "response": f"✅ Updated {name} to {quantity} {unit}."
        }
    except Exception as e:
        return {
            "success": False,
            "response": f"❌ Error updating item: {str(e)}"
        }

def delete_item(name: str) -> Dict[str, Any]:
    """
    Deletes an item from the inventory.
    
    Args:
        name (str): The name of the item.
        
    Returns:
        Dict[str, Any]: Response with success status.
    """
    try:
        if name not in inventory:
            return {
                "success": False,
                "response": f"❌ Item {name} not found in inventory."
            }
        
        del inventory[name]
        if name in inventory_items:
            del inventory_items[name]
        
        return {
            "success": True,
            "response": f"✅ Deleted {name} from inventory."
        }
    except Exception as e:
        return {
            "success": False,
            "response": f"❌ Error deleting item: {str(e)}"
        }

def list_inventory() -> Dict[str, Any]:
    """
    Lists all items in the inventory.
    
    Returns:
        Dict[str, Any]: Response with success status and inventory list.
    """
    try:
        if not inventory:
            return {
                "success": True,
                "response": "📦 Inventory is empty."
            }
        
        # Format the inventory list
        inventory_list = "📦 Current Inventory:\n"
        for name, data in inventory.items():
            unit = inventory_items.get(name, {}).get("unit", "units")
            inventory_list += f"- {name}: {data['quantity']} {unit}\n"
        
        return {
            "success": True,
            "response": inventory_list
        }
    except Exception as e:
        return {
            "success": False,
            "response": f"❌ Error listing inventory: {str(e)}"
        }

# Note: You will need separate functions/endpoints to manage the inventory_items table (add, update, delete item types with prices and default units).
