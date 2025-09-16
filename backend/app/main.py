from fastapi import FastAPI
from app.routers import whatsapp_integration
from database import Base, engine

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SMEFlow Agent")

# include router
app.include_router(whatsapp_integration.router, prefix="/whatsapp", tags=["WhatsApp"])

@app.get("/")
def root():
    return {"message": "Welcome to SMEFlow Agent API"}