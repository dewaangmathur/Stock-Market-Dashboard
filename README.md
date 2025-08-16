# 📊 Stock Market Dashboard

A full-stack stock market dashboard with real-time or mock stock data, technical indicators, and AI-based price predictions.

---

## 🚀 Features
- **Frontend (React + Vite)**
  - Sidebar with 10+ company names
  - Main panel with Chart.js-based stock price charts
  - Technical indicators: 52-week high/low, SMA, RSI, average volume
  - AI-powered next-day price forecast

- **Backend (FastAPI + SQLite/PostgreSQL)**
  - REST API endpoints for companies, stock history, indicators, predictions
  - Data ingestion from Kaggle or Yahoo Finance API
  - ML model training + joblib persistence

- **Extras**
  - Dockerized setup
  - Optional PostgreSQL support
  - Ready for deployment on Render/Railway/Vercel

---

## 🛠 Tech Stack
**Frontend:**
- React, Vite
- Chart.js, react-chartjs-2
- Axios

**Backend:**
- FastAPI, SQLAlchemy
- Pandas, NumPy, scikit-learn, ta
- SQLite/PostgreSQL

---

## 📂 Project Structure

stock-dashboard/
├── backend/                                # Backend API + data processing
│   ├── app.py                              # FastAPI app with REST endpoints
│   ├── db.py                               # SQLite/PostgreSQL connection + session
│   ├── models.py                           # SQLAlchemy ORM models
│   ├── ingest.py                           # Load Kaggle CSV -> SQLite/PostgreSQL
│   ├── indicators.py                       # 52w high/low, SMA, RSI, avg volume
│   ├── predict.py                          # Next-day price forecast (ML baseline)
│   ├── utils.py                            # Common helper functions
│   ├── requirements.txt                    # Backend dependencies
│   ├── Dockerfile                          # Dockerize backend
│   └── tests/                              # Backend unit tests
│       ├── test_api.py
│       ├── test_indicators.py
│       └── test_predict.py
│
├── frontend/                               # Frontend (React + Vite)
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── public/                             # Static assets
│   │   ├── logo.png
│   │   └── favicon.ico
│   └── src/
│       ├── App.jsx
│       ├── api.js                          # Axios API client
│       ├── components/
│       │   ├── Sidebar.jsx                 # Scrollable company list
│       │   ├── ChartPanel.jsx              # Stock chart + historical data
│       │   ├── IndicatorsPanel.jsx         # 52w high/low, SMA, RSI, avg volume
│       │   └── PredictionPanel.jsx         # AI forecast results
│       ├── styles.css                      # Global styles
│       └── hooks/
│           └── useStockData.js             # Custom React hook for data fetching
│
├── dataset/                                # Kaggle dataset & info
│   ├── massive_yahoo_finance_data.csv      # Kaggle dataset file
│   └── README_dataset.md                   # Source, download date, usage notes
│
├── screenshots/                            # For README & submission
│   ├── dashboard.png
│   └── mobile_view.png
│
├── docker-compose.yml                      # Orchestration for backend + frontend + DB
├── README.md                               # Project documentation
└── .gitignore
└── requirements.txt

📦 Setup
Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

Frontend
cd frontend
npm install
npm run dev

Docker (full stack)
docker-compose up --build

📊 Dataset

Kaggle: Massive Yahoo Finance Dataset

🖼 Screenshots

📧 Author

Made for JarNox technical assignment.


---

If you want, I can now **adjust the `docker-compose.yml`** so it automatically builds the backend with SQLite instead of PostgreSQL for simpler setup.  
Do you want me to make it SQLite-only? That way no DB container is needed.