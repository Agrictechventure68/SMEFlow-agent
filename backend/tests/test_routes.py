from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_business_analyze():
    data = {"revenue": 100000, "expenses": 60000}
    response = client.post("/api/v1/business/analyze", json=data)
    assert response.status_code == 200
    assert "profit" in response.json()["analysis"]