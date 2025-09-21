from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for messages coming into the API
class WhatsAppMessage(BaseModel):
    sender_id: str
    receiver_id: str
    message: str
    timestamp: Optional[datetime] = datetime.utcnow()

# Database model (mock for now)
class WhatsAppMessageDB(WhatsAppMessage):
    id: int
    status: str = "sent"  # sent, delivered, read