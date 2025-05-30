from inventory_toolkit import InventoryToolkit
from command_parser_agent import CommandParserAgent
from typing import Dict, Any, Union, List

class ExecutionAgent:
    """Handles inventory management commands after they are parsed."""

    def __init__(self):
        """Initialize the command parser and inventory toolkit."""
        self.inventory_toolkit = InventoryToolkit()
        self.pending_confirmation = None  # Stores the last operation for confirmation
        self.pending_confirmations = []   # Queue for batch confirmations
        self.command_parser = CommandParserAgent()  # Initialize the command parser agent

    def process_command(self, command: str) -> Dict[str, Any]:
        """
        Processes and executes an inventory command.

        Args:
            command (str): The user's natural language command.

        Returns:
            Dict[str, Any]: The response message and operation details.
        """
        # Handle confirmation responses for batch
        if command.lower() in ["yes", "no"] and self.pending_confirmations:
            if self.pending_confirmations:
                current_cmd = self.pending_confirmations.pop(0)
                if command.lower() == "yes":
                    result = self.execute_operation(current_cmd)
                else:
                    result = {
                        "success": False,
                        "response": "Operation canceled."
                    }
                # If more commands remain, ask for next confirmation
                if self.pending_confirmations:
                    next_cmd = self.pending_confirmations[0]
                    return {
                        "success": True,
                        "response": f"{result['response']}\nConfirm: {next_cmd['operation']} {next_cmd.get('quantity', '')} {next_cmd.get('unit type', '')} of {next_cmd['item']}? (yes/no)"
                    }
                else:
                    return result

        # Handle confirmation responses for single
        if command.lower() in ["yes", "no"]:
            if self.pending_confirmation:
                if command.lower() == "yes":
                    operation_response = self.execute_operation(self.pending_confirmation)
                    self.pending_confirmation = None  # Reset pending command
                    return operation_response
                else:
                    self.pending_confirmation = None
                    return {
                        "success": False,
                        "response": "Operation canceled."
                    }
            return {
                "success": False,
                "response": "No pending command to confirm."
            }

        # Parse the command using the CommandParserAgent
        parsed_data = self.command_parser.parse_command(command)

        # If multiple commands are parsed, queue confirmations for each actionable command
        if isinstance(parsed_data, list):
            actionable_cmds = [cmd for cmd in parsed_data if cmd["operation"] in ["add", "update", "delete"]]
            non_actionable_results = []
            for cmd in parsed_data:
                if cmd["operation"] == "list":
                    result = self.inventory_toolkit.list_inventory()
                    non_actionable_results.append(result["response"])
            if actionable_cmds:
                self.pending_confirmations = actionable_cmds
                first_cmd = self.pending_confirmations[0]
                msg = f"Confirm: {first_cmd['operation']} {first_cmd.get('quantity', '')} {first_cmd.get('unit type', '')} of {first_cmd['item']}? (yes/no)"
                if non_actionable_results:
                    return {
                        "success": True,
                        "response": "\n".join(non_actionable_results + [msg])
                    }
                return {
                    "success": True,
                    "response": msg
                }
            elif non_actionable_results:
                return {
                    "success": True,
                    "response": "\n".join(non_actionable_results)
                }
            else:
                return {
                    "success": False,
                    "response": "Invalid command."
                }

        # If parsing fails or operation is unknown, return error message
        if parsed_data["operation"] == "unknown":
            return {
                "success": False,
                "response": "Invalid command."
            }

        # If operation is "list", execute immediately
        if parsed_data["operation"] == "list":
            return self.inventory_toolkit.list_inventory()

        # Otherwise, confirm before execution
        self.pending_confirmation = parsed_data
        return {
            "success": True,
            "response": f"Confirm: {parsed_data['operation']} {parsed_data.get('quantity', '')} {parsed_data.get('unit type', '')} of {parsed_data['item']}? (yes/no)"
        }

    def execute_operation(self, operation_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the confirmed inventory operation.

        Args:
            operation_data (Dict[str, Any]): Structured command details.

        Returns:
            Dict[str, Any]: Response after execution.
        """
        operation = operation_data["operation"]
        item = operation_data["item"]
        quantity = operation_data.get("quantity")
        unit_type = operation_data.get("unit type", "unknown")

        if operation == "add":
            result = self.inventory_toolkit.add_item(item, quantity, unit_type)
            if result["success"]:
                result["item"]["operation"] = "add"  # Add operation type for frontend
            return result
        elif operation == "update":
            result = self.inventory_toolkit.update_item(item, quantity, unit_type)
            if result["success"]:
                result["item"]["operation"] = "update"  # Add operation type for frontend
            return result
        elif operation == "delete":
            return self.inventory_toolkit.delete_item(item)
        
        return {
            "success": False,
            "response": "Invalid operation."
        }

# If running directly, provide interactive CLI
if __name__ == "__main__":
    execution_agent = ExecutionAgent()

    while True:
        user_input = input("Enter your inventory command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = execution_agent.process_command(user_input)
        print(response)
