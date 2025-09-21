from pydantic import BaseModel

class WhatsAppMessage(BaseModel):
    sender: str
    receiver: str
    content: str

    class Config:
        orm_mode = True