import React from "react";
import Dashboard from "./components/Dashboard";
import BookkeepingForm from "./components/BookkeepingForm";
import ChatInterface from "./components/ChatInterface";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>SMEFlow Agent</h1>
      <ChatInterface />
      <BookkeepingForm />
      <Dashboard />
    </div>
  );
}

export default App;