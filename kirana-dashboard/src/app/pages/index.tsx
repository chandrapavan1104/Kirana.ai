import React from "react";
import DashboardGrid from "../components/Dashboard/DashboardGrid";

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Kirana Inventory Dashboard</h1>
        <p className="text-gray-600 mt-2">Manage your inventory with ease!</p>
      </header>
      <DashboardGrid />
    </div>
  );
};

export default Home;
