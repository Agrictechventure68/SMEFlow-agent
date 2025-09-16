import React, { useState } from "react";

function ChatInterface() {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    fetch("http://localhost:8000/whatsapp/receive", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    })
      .then((res) => res.json())
      .then((data) => alert(Message Sent: ${data.message}));
  };

  return (
    <div>
      <h2>WhatsApp Chat</h2>
      <input
        type="text"
        placeholder="Type message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default ChatInterface;