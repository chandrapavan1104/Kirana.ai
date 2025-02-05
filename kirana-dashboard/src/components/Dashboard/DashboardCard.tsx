import React from "react";

interface DashboardCardProps {
  title: string;
  value: string | number;
  description?: string;
  bgColor?: string;
}

const DashboardCard: React.FC<DashboardCardProps> = ({ title, value, description, bgColor }) => {
  return (
    <div
      className={`p-6 rounded-lg shadow-md ${bgColor || "bg-white"} text-gray-800`}
    >
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-3xl font-bold">{value}</p>
      {description && <p className="text-sm text-gray-600 mt-2">{description}</p>}
    </div>
  );
};

export default DashboardCard;
