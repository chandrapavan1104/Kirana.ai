import React from "react";
import Link from "next/link";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-gray-800 text-white px-6 py-4">
      <ul className="flex space-x-6">
        <li>
          <Link href="/">
            <span className="hover:text-yellow-400">Dashboard</span>
          </Link>
        </li>
        <li>
          <Link href="/items">
            <span className="hover:text-yellow-400">Inventory Items</span>
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
