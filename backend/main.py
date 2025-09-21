from fastapi import FastAPI
from backend.routers import whatsapp_integration
from backend.database import Base, engine   # adjusted import

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SMEFlow Agent")

# include router
app.include_router(whatsapp_integration.router, prefix="/whatsapp", tags=["WhatsApp"])

@app.get("/")
def root():
    return {"message": "Welcome to SMEFlow Agent API"}