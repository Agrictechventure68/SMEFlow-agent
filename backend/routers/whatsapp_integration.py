from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal          # fixed import
from app.models.whatsapp import WhatsAppMessageDB
from app.schemas.whatsapp import WhatsAppMessage

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send")
def send_message(message: WhatsAppMessage, db: Session = Depends(get_db)):
    """Send (store) a WhatsApp message"""
    msg = WhatsAppMessageDB(
        sender=message.sender,
        receiver=message.receiver,
        content=message.content
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {"status": "success", "sent_message": msg}

@router.get("/messages")
def list_messages(db: Session = Depends(get_db)):
    """List all stored WhatsApp messages"""
    messages = db.query(WhatsAppMessageDB).all()
    return {"status": "success", "messages": messages}