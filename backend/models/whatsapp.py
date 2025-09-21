from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class WhatsAppContact(BaseModel):
    """Represents a WhatsApp user contact."""
    phone_number: str = Field(..., example="‪+2348012345678‬")
    name: Optional[str] = Field(None, example="John Ade")
    is_business: Optional[bool] = False


class WhatsAppMessage(BaseModel):
    """Represents a message sent or received on WhatsApp."""
    id: str = Field(..., example="wamid.HBgLNTEyMzQ1Njc4OTAxFQIAERgSOD")
    from_number: str = Field(..., example="‪+2348012345678‬")
    to_number: str = Field(..., example="‪+2348098765432‬")
    message_type: str = Field(..., example="text")  # text, image, audio, document
    content: str = Field(..., example="Hello! Your invoice is ready.")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: Optional[str] = Field("sent", example="delivered")  # sent, delivered, read


class WhatsAppTemplate(BaseModel):
    """Represents pre-approved WhatsApp templates (for business notifications)."""
    name: str = Field(..., example="invoice_notification")
    language: str = Field(default="en")
    body: str = Field(..., example="Hello {name}, your invoice of {amount} is ready.")
    variables: List[str] = Field(default=[])


class WhatsAppSession(BaseModel):
    """Represents a WhatsApp API session / token for authentication."""
    session_id: str = Field(..., example="session_123456")
    access_token: str = Field(..., example="EAAJZC4qkB...xyz")
    expires_at: datetime = Field(..., example="2025-09-20T12:30:00Z")