import React, { useState } from "react";

function BookkeepingForm() {
  const [form, setForm] = useState({ type: "income", description: "", amount: "" });

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:8000/bookkeeping/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    }).then(() => alert("Transaction Added!"));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Transaction</h2>
      <select
        value={form.type}
        onChange={(e) => setForm({ ...form, type: e.target.value })}
      >
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>
      <input
        type="text"
        placeholder="Description"
        value={form.description}
        onChange={(e) => setForm({ ...form, description: e.target.value })}
      />
      <input
        type="number"
        placeholder="Amount"
        value={form.amount}
        onChange={(e) => setForm({ ...form, amount: parseFloat(e.target.value) })}
      />
      <button type="submit">Add</button>
    </form>
  );
}

export default BookkeepingForm;