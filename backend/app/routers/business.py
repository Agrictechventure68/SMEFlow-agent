from fastapi import APIRouter
from services.analyzer import analyze_data
from services.recommender import recommend_growth

router = APIRouter()

@router.post("/analyze")
def analyze(business_data: dict):
    """Analyze SME business data"""
    result = analyze_data(business_data)
    return {"status": "success", "analysis": result}

@router.post("/recommend")
def recommend(business_data: dict):
    """Recommend strategies for SME growth"""
    result = recommend_growth(business_data)
    return {"status": "success", "recommendations": result}