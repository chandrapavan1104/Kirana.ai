from inventory import add_item, update_item, delete_item, list_inventory
from typing import Dict, Any

class InventoryToolkit:
    """A toolkit for managing inventory with CRUD operations, including unit types."""

    def add_item(self, name: str, quantity: float, unit: str) -> Dict[str, Any]:
        """
        Adds an item to the inventory.

        Args:
            name (str): The name of the item.
            quantity (float): The number of units to add.
            unit (str): The unit of measurement (kg, litre, etc.).

        Returns:
            Dict[str, Any]: Response with success status and item details.
        """
        if not unit:
            unit = "unknown"  # Default to "unknown" if no unit is provided

        return add_item(name, quantity, unit)

    def update_item(self, name: str, quantity: float, unit: str) -> Dict[str, Any]:
        """
        Updates an item's quantity in the inventory.

        Args:
            name (str): The name of the item.
            quantity (float): The new quantity.
            unit (str): The unit of measurement (kg, litre, etc.).

        Returns:
            Dict[str, Any]: Response with success status and item details.
        """
        if not unit:
            unit = "unknown"

        return update_item(name, quantity, unit)

    def delete_item(self, name: str) -> Dict[str, Any]:
        """
        Deletes an item from the inventory.

        Args:
            name (str): The name of the item.

        Returns:
            Dict[str, Any]: Response with success status.
        """
        return delete_item(name)

    def list_inventory(self) -> Dict[str, Any]:
        """
        Lists all items in the inventory, including unit type.

        Returns:
            Dict[str, Any]: Response with success status and inventory list.
        """
        return list_inventory()
