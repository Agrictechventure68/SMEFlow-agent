from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
import datetime

# Base model to inherit from
Base = declarative_base()

class WhatsAppMessageDB(Base):
    _tablename_ = "whatsapp_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(100), nullable=False)        # phone number or name
    receiver = Column(String(100), nullable=False)      # phone number or name
    message = Column(Text, nullable=False)              # actual message text
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def _repr_(self):
        return f"<WhatsAppMessage(sender={self.sender}, receiver={self.receiver}, timestamp={self.timestamp})>"