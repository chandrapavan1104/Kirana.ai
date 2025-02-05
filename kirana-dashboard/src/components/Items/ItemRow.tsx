import React from "react";

interface ItemRowProps {
  id: number;
  name: string;
  quantity: number;
  onEdit: (id: number) => void;
  onDelete: (id: number) => void;
  onAddToCart: (id: number) => void;
}

const ItemRow: React.FC<ItemRowProps> = ({ id, name, quantity, onEdit, onDelete, onAddToCart }) => {
  return (
    <tr className="bg-white border-b">
      <td className="px-4 py-2">{name}</td>
      <td className="px-4 py-2">{quantity}</td>
      <td className="px-4 py-2 flex gap-2">
        <button
          className="px-3 py-1 text-white bg-blue-500 rounded-md hover:bg-blue-600"
          onClick={() => onEdit(id)}
        >
          Edit
        </button>
        <button
          className="px-3 py-1 text-white bg-red-500 rounded-md hover:bg-red-600"
          onClick={() => onDelete(id)}
        >
          Delete
        </button>
        <button
          className="px-3 py-1 text-white bg-green-500 rounded-md hover:bg-green-600"
          onClick={() => onAddToCart(id)}
        >
          Add to Cart
        </button>
      </td>
    </tr>
  );
};

export default ItemRow;
