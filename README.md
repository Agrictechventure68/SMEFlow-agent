# SMEFlow Agent

SMEFlow Agent is a *Smart AI-powered SaaS platform* designed to help Small and Medium Enterprises (SMEs) automate bookkeeping, financial insights, customer engagement, and growth recommendations.  
It integrates *WhatsApp business communication, financial tracking, and intelligent analysis* into a single lightweight solution that improves connectivity and decision-making for entrepreneurs.

---

## 🚀 Features

- *WhatsApp Integration*  
  Seamless business communication and notifications via WhatsApp.

- *Bookkeeping Module*  
  Simple accounting tools to track income, expenses, and cashflow.

- *Business Dashboard*  
  Centralized analytics dashboard for quick insights into SME operations.

- *Analyzer & Recommender*  
  AI-driven analysis of SME data to provide actionable growth strategies.

- *Extensible Design* (Coming Soon)  
  - 📦 Inventory management  
  - 💳 Loan/credit profiling  
  - 🤝 CRM for customer relationship management  

---

## 🛠 Tech Stack

- *Backend:* [FastAPI](https://fastapi.tiangolo.com/) (Python)  
- *Frontend:* React.js (planned)  
- *Database:* SQLite / PostgreSQL  
- *Hosting:* [Render](https://render.com/)  
- *Version Control:* Git + GitHub  

---

## 📂 Project Structure

backend/ │   main.py                # FastAPI entry point │   database.py            # Database configuration │   bookkeeping.py         # Bookkeeping routes │   dashboard.py           # Dashboard routes │   whatsapp_integration.py# WhatsApp communication routes │ ├── app/ │   ├── routers/           # API routes │   ├── services/          # Business logic (analyzer, recommender, etc.) │   └── models/            # Database models (future expansion) │ frontend/                  # React frontend (planned) docs/                      # Documentation and pitch deck

---

## ⚙ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Agrictechventure68/SMEFlow-agent.git
cd SMEFlow-agent/backend

2. Create Virtual Environment

python -m venv venv
source venv/Scripts/activate   # On Windows PowerShell

3. Install Dependencies

pip install -r requirements.txt

4. Run Development Server

uvicorn main:app --reload


---
🔗 API Endpoints

Route	Method	Description

/	GET	Root welcome message
/whatsapp/send	POST	Send message via WhatsApp
/bookkeeping/records	GET	Fetch bookkeeping records
/dashboard/summary	GET	Business summary insights
/analyzer/analyze	POST	Analyze SME data
/analyzer/recommend	POST	Recommend strategies for SME growth
/users/register	POST	Register new SME user
/users/login	POST	SME user login



---
🚀 Deployment (Render)

1. Push repo to GitHub (done ✅).


2. Create new Render Web Service → Connect to GitHub.


3. Select backend/ as the deploy root.


4. Start command:

uvicorn main:app --host 0.0.0.0 --port 10000


5. Render auto-deploys on future GitHub pushes.


---
🌍 Vision & Impact

SMEFlow Agent is designed to bridge the digital divide for SMEs by:

Reducing bookkeeping complexity

Providing business insights without hiring consultants

Helping SMEs grow through AI-based recommendations

Leveraging WhatsApp — the most accessible tool for African entrepreneurs



---
🤝 Contribution

We welcome contributions to expand SMEFlow Agent:

Add inventory, loans, CRM modules

Improve UI/UX

Add multi-language support


---
📜 License

MIT License © 2025 Bright Doro / AgricTech Venture