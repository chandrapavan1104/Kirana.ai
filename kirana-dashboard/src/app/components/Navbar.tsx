import React from "react";
import Link from "next/link";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-gray-800 text-white px-6 py-4">
      <ul className="flex space-x-6">
        <li>
          <Link href="/">
            <a className="hover:text-yellow-400">Dashboard</a>
          </Link>
        </li>
        <li>
          <Link href="/items">
            <a className="hover:text-yellow-400">Inventory Items</a>
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
