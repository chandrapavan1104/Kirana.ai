# backend/inventory_toolkit.py

from phi.tools import Toolkit
from inventory import add_item, update_item, delete_item, get_inventory

class InventoryToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="inventory_toolkit")
        self.register(self.add_item)
        self.register(self.update_item)
        self.register(self.delete_item)
        self.register(self.get_inventory)

    def add_item(self, name: str, quantity: int) -> str:
        """Add an item to the inventory."""
        result = add_item(name, quantity)
        return f"Added {quantity} units of {name}." if result else "Failed to add item."

    def update_item(self, name: str, quantity: int) -> str:
        """Update the quantity of an existing item."""
        result = update_item(name, quantity)
        return f"Updated {name} to {quantity} units." if result else "Failed to update item."

    def delete_item(self, name: str) -> str:
        """Delete an item from the inventory."""
        result = delete_item(name)
        return f"Deleted {name} from inventory." if result else "Failed to delete item."

    def get_inventory(self) -> str:
        """Retrieve the current inventory list."""
        inventory_data = get_inventory()  # Now it returns a dictionary

        if "message" in inventory_data:
            return inventory_data["message"]  # If inventory is empty

        return "\n".join([f"{name}: {quantity}" for name, quantity in inventory_data.items()])

