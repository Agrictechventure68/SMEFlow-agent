# SMEFlow Backend

Backend API for SMEFlow Agent built with *FastAPI*.

## 🚀 Run Locally
bash
# Install dependencies
pip install -r requirements.txt

# Run API server
uvicorn main:app --reload

Access at: http://127.0.0.1:8000

---
📌 API Routes

GET / → Root welcome message

POST /api/v1/business/analyze → Analyze SME business data

POST /api/v1/business/recommend → Get growth recommendations

POST /api/v1/users/register → Register new SME user

POST /api/v1/users/login → User login

---

🧪 Tests

pytest tests/