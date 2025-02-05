from phidata.ai import AiAgent, AiTool
from groq import Groq
import os
from main.py import add_item, update_item, delete_item, get_inventory

# Set up Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# Function to process natural language inventory commands
def process_inventory_command(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "user", "content": f"Extract the operation and details from this inventory command: {prompt}"}],
        temperature=0.6,
        max_completion_tokens=100,
        top_p=0.95,
        stream=False
    )
    
    response = completion.choices[0].message.content.lower()
    
    # Extract intent and perform CRUD operation
    if "add" in response:
        parts = response.split()
        quantity = int(parts[-2])  # Assuming format: "Add 5 kg of rice"
        name = " ".join(parts[1:-2])
        return add_item(name, quantity)
    
    elif "update" in response:
        parts = response.split()
        quantity = int(parts[-2])
        name = " ".join(parts[1:-2])
        return update_item(name, quantity)
    
    elif "delete" in response or "remove" in response:
        name = response.replace("delete ", "").replace("remove ", "").strip()
        return delete_item(name)
    
    elif "list" in response or "show" in response:
        inventory = get_inventory()
        return "\n".join([f"{name}: {quantity}" for name, quantity in inventory])
    
    else:
        return "Sorry, I couldn't understand the request."

# Define AI Tool for handling CRUD
inventory_tool = AiTool(
    name="inventory_tool",
    description="A tool to manage inventory via natural language",
    run_fn=process_inventory_command,
)

# Create Phidata AI Agent with the inventory tool
inventory_agent = AiAgent(
    name="inventory_agent",
    description="An AI agent for managing inventory using DeepSeek LLM",
    tools=[inventory_tool],
)

if __name__ == "__main__":
    while True:
        user_input = input("Enter your inventory command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print(inventory_agent.run(user_input))