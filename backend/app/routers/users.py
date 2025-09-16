from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user(user: dict):
    """Register a new SME user"""
    return {"status": "success", "message": f"User {user.get('name')} registered."}

@router.post("/login")
def login_user(user: dict):
    """Login SME user"""
    return {"status": "success", "message": f"Welcome back {user.get('email')}"}