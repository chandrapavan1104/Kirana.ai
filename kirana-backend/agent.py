# backend/agent.py

from phi.agent import Agent
from phi.model.groq import Groq
from inventory_toolkit import InventoryToolkit
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the Groq model
groq_model = Groq(
    id="gemma2-9b-it",  # Replace with your specific model ID
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize the Inventory Toolkit
inventory_toolkit = InventoryToolkit()

# Create the AI agent with the Groq model and Inventory Toolkit
agent = Agent(
    model=groq_model,
    tools=[inventory_toolkit],
    description="An AI agent for managing inventory using natural language commands.",
    instructions=[
        "You can add, update, delete, or list items in the inventory.",
        "For example: 'Add 10 units of rice', 'Update wheat to 15 units', 'Delete sugar from inventory', 'List all items'.",
        "Always confirm actions with the user before executing them."
    ],
    markdown=True,
    show_tool_calls=True,
)

if __name__ == "__main__":
    while True:
        user_input = input("Enter your inventory command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.run(user_input)
        print(response.content)
