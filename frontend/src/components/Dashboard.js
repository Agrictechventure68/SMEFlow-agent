import React, { useEffect, useState } from "react";

function Dashboard() {
  const [summary, setSummary] = useState({});

  useEffect(() => {
    fetch("http://localhost:8000/dashboard/summary")
      .then((res) => res.json())
      .then((data) => setSummary(data));
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Total Income: {summary.total_income}</p>
      <p>Total Expense: {summary.total_expense}</p>
      <p>Balance: {summary.balance}</p>
    </div>
  );
}

export default Dashboard;