import React, { useState } from "react";

interface CRUDModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (item: { id?: number; name: string; quantity: number }) => void;
  initialData?: { id?: number; name: string; quantity: number };
}

const CRUDModal: React.FC<CRUDModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = { name: "", quantity: 0 },
}) => {
  const [name, setName] = useState(initialData.name);
  const [quantity, setQuantity] = useState(initialData.quantity);

  if (!isOpen) return null;

  const handleSubmit = () => {
    onSubmit({ id: initialData.id, name, quantity });
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg shadow-lg w-96">
        <h2 className="text-lg font-bold mb-4">
          {initialData.id ? "Edit Item" : "Add Item"}
        </h2>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Item Name
          </label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="mt-1 block w-full border rounded-md px-3 py-2"
            placeholder="Enter item name"
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Quantity
          </label>
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(Number(e.target.value))}
            className="mt-1 block w-full border rounded-md px-3 py-2"
            placeholder="Enter quantity"
          />
        </div>
        <div className="flex justify-end gap-2">
          <button
            className="px-4 py-2 bg-gray-500 text-white rounded-md"
            onClick={onClose}
          >
            Cancel
          </button>
          <button
            className="px-4 py-2 bg-blue-500 text-white rounded-md"
            onClick={handleSubmit}
          >
            {initialData.id ? "Update" : "Add"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default CRUDModal;
