import React from "react";
import DashboardCard from "./DashboardCard";

const DashboardGrid: React.FC = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-6">
      <DashboardCard
        title="Low Inventory"
        value="12 Items"
        description="Items below the threshold."
        bgColor="bg-red-100"
      />
      <DashboardCard
        title="Most Sold"
        value="Rice, Wheat"
        description="Top 2 selling items this week."
        bgColor="bg-green-100"
      />
      <DashboardCard
        title="Current Orders"
        value="35 Orders"
        description="Active orders in the system."
        bgColor="bg-blue-100"
      />
      <DashboardCard
        title="Cart Items"
        value="5 Items"
        description="Items ready for checkout."
        bgColor="bg-yellow-100"
      />
    </div>
  );
};

export default DashboardGrid;
