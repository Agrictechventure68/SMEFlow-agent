from fastapi import APIRouter

router = APIRouter()

@router.get("/overview")
def dashboard_overview():
    """Provide SME business dashboard overview"""
    return {"status": "success", "overview": "Dashboard data placeholder"}

@router.get("/metrics")
def dashboard_metrics():
    """Return business performance metrics"""
    return {"status": "success", "metrics": {"revenue": 100000, "growth": "15%"}}