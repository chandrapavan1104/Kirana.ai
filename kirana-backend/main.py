from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str
    quantity: int

inventory = [
    {"id": 1, "name": "Rice", "quantity": 10},
    {"id": 2, "name": "Wheat", "quantity": 20},
]

@app.get("/items", response_model=List[Item])
def get_items():
    return inventory

@app.post("/items")
def add_item(item: Item):
    inventory.append(item.dict())
    return {"message": "Item added"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i in range(len(inventory)):
        if inventory[i]["id"] == item_id:
            inventory[i] = item.dict()
            return {"message": "Item updated"}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global inventory
    inventory = [item for item in inventory if item["id"] != item_id]
    return {"message": "Item deleted"}