# 🤖 SMEFlow Agent — WhatsApp + Auto-Bookkeeping + Dashboard

SMEFlow is an *AI-assisted business helper* for Nigerian SMEs. It:
- answers customer FAQs on *WhatsApp*,
- *auto-logs sales* to *Google Sheets*, and
- shows a simple *Streamlit dashboard* with daily/weekly totals.

## ✨ Features
- *WhatsApp bot (Twilio Sandbox / Meta Cloud API)* for FAQs + order capture  
- *Auto-bookkeeping to Google Sheets* (timestamp, item, qty, price, total, customer)  
- *Streamlit dashboard* for KPIs, recent transactions, and quick “chat simulation” fallback  
- *FastAPI backend* with endpoints for webhook + summaries

## 🏗 Architecture

WhatsApp → FastAPI webhook → Google Sheets ↘  Streamlit dashboard (reads summaries)

## 🧩 Tech Stack
- *Backend:* FastAPI, Uvicorn
- *Data:* Google Sheets (gspread + service account)
- *Messaging:* Twilio WhatsApp Sandbox (or Meta WhatsApp Cloud API)
- *Dashboard:* Streamlit
- *Lang/Tools:* Python 3.10+, ngrok for local webhooks

## 📦 Project Structure

smeflow-agent/ ├─ backend/ │  ├─ main.py │  ├─ routes/ │  │  ├─ init.py │  │  ├─ business.py │  │  └─ users.py │  ├─ services/ │  │  ├─ init.py │  │  ├─ analyzer.py │  │  └─ recommender.py │  ├─ models/ │  │  ├─ init.py │  │  ├─ agent.py │  │  └─ utils.py │  ├─ requirements.txt │  ├─ .env.example │  └─ tests/ │     ├─ test_agent.py │     └─ test_routes.py ├─ dashboard/ │  ├─ app.py │  ├─ requirements.txt │  └─ .env.example ├─ docs/ │  └─ SMEFlow_Project_Summary.md └─ README.md

## ⚙ Quick Start

### 1) Backend
bash
cd backend
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

2) Expose webhook (dev)

ngrok http 8000
# set Twilio WhatsApp Sandbox webhook to: https://<ngrok-id>.ngrok.io/webhook/whatsapp

3) Dashboard

cd ../dashboard
pip install -r requirements.txt
streamlit run app.py

🔐 Environment

Create backend/.env:

OPENAI_API_KEY=sk-...                # optional for LLM replies
GOOGLE_SA_FILE=service_account.json
GSHEET_ID=your_google_sheet_id
WHATSAPP_PROVIDER=twilio
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_WHATSAPP_NUMBER=whatsapp:‪+14155238886‬

Create dashboard/.env:

GSHEET_ID=your_google_sheet_id
GOOGLE_SA_FILE=../backend/service_account.json
BACKEND_BASE_URL=http://localhost:8000

📸 Demo Script

1. Send price rice5kg on WhatsApp → bot replies

2. Send order 2 rice5kg for tolu → bot confirms + logs to Google Sheet

3. Open Streamlit → see KPIs + new row in “Recent Sales”


🗺 Roadmap

Inventory sync, receipts, expense tracking, multi-store roles, local languages


📝 License

MIT