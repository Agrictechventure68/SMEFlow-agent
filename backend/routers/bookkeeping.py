from fastapi import APIRouter

router = APIRouter()

@router.post("/record")
def record_transaction(transaction: dict):
    """Record a financial transaction"""
    return {"status": "success", "transaction": transaction}

@router.get("/summary")
def get_summary():
    """Get financial summary (mockup for now)"""
    return {"status": "success", "summary": "Monthly summary will be here"}