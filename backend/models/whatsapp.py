from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class WhatsAppMessageDB(Base):
    _tablename_ = "whatsapp_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())