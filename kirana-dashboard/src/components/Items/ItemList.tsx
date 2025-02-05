import React, { useState } from "react";
import ItemRow from "./ItemRow";
import CRUDModal from "./CRUDModal";

interface Item {
  id: number;
  name: string;
  quantity: number;
}

const ItemList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([
    { id: 1, name: "Rice", quantity: 10 },
    { id: 2, name: "Wheat", quantity: 20 },
    { id: 3, name: "Sugar", quantity: 15 },
  ]);
  const [isModalOpen, setModalOpen] = useState(false);
  const [editItem, setEditItem] = useState<Item | null>(null);

  const handleAdd = () => {
    setEditItem(null);
    setModalOpen(true);
  };

  const handleEdit = (id: number) => {
    const item = items.find((item) => item.id === id);
    if (item) {
      setEditItem(item);
      setModalOpen(true);
    }
  };

  const handleDelete = (id: number) => {
    setItems(items.filter((item) => item.id !== id));
  };

  const handleAddToCart = (id: number) => {
    console.log(`Add item with ID: ${id} to cart`);
  };

  const handleModalSubmit = (item: { id?: number; name: string; quantity: number }) => {
    if (item.id) {
      // Edit existing item
      setItems(
        items.map((existingItem) =>
          existingItem.id === item.id ? { ...existingItem, ...item } : existingItem
        )
      );
    } else {
      // Add new item
      setItems([...items, { id: Date.now(), ...item }]);
    }
  };

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Inventory Items</h1>
      <button
        className="mb-4 px-4 py-2 bg-green-500 text-white rounded-md"
        onClick={handleAdd}
      >
        Add Item
      </button>
      <table className="w-full border-collapse bg-white">
        <thead>
          <tr className="bg-gray-200">
            <th className="px-4 py-2 text-left">Item Name</th>
            <th className="px-4 py-2 text-left">Quantity</th>
            <th className="px-4 py-2 text-left">Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <ItemRow
              key={item.id}
              id={item.id}
              name={item.name}
              quantity={item.quantity}
              onEdit={handleEdit}
              onDelete={handleDelete}
              onAddToCart={handleAddToCart}
            />
          ))}
        </tbody>
      </table>
      <CRUDModal
        isOpen={isModalOpen}
        onClose={() => setModalOpen(false)}
        onSubmit={handleModalSubmit}
        initialData={editItem || undefined}
      />
    </div>
  );
};

export default ItemList;
