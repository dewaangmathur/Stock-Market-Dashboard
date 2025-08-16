# backend/app.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine, get_db
from backend.models import StockData
from backend.utils import df_to_records
from backend.indicators import calculate_indicators
from backend.predict import train_and_predict
import pandas as pd
import yfinance as yf

# Create DB tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock Market Dashboard API")

# ✅ Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Helpers
# ---------------------------
def fetch_live_data(symbol: str) -> pd.DataFrame:
    df = yf.download(symbol, period="1y", interval="1d")
    if df.empty:
        raise HTTPException(status_code=404, detail=f"No data found for {symbol}")
    df.reset_index(inplace=True)
    df.rename(columns=str.capitalize, inplace=True)
    return df

# ---------------------------
# Routes
# ---------------------------
@app.get("/companies")
def get_companies(db: Session = Depends(get_db)):
    companies = db.query(StockData.symbol).distinct().all()
    return [c[0] for c in companies]

@app.get("/stock/{symbol}")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    rows = (
        db.query(StockData)
        .filter(StockData.symbol == symbol.upper())
        .order_by(StockData.date)
        .all()
    )
    if not rows:
        df = fetch_live_data(symbol)
    else:
        df = pd.DataFrame(
            [{
                "Date": r.date,
                "Open": r.open,
                "High": r.high,
                "Low": r.low,
                "Close": r.close,
                "Volume": r.volume,
            } for r in rows]
        )
    return {"symbol": symbol, "historical": df_to_records(df)}

@app.get("/history/{symbol}")
def get_history(symbol: str, db: Session = Depends(get_db)):
    rows = (
        db.query(StockData)
        .filter(StockData.symbol == symbol.upper())
        .order_by(StockData.date)
        .all()
    )

    if not rows:
        df = fetch_live_data(symbol)
    else:
        df = pd.DataFrame(
            [{
                "Date": r.date,
                "Open": r.open,
                "High": r.high,
                "Low": r.low,
                "Close": r.close,
                "Volume": r.volume,
            } for r in rows]
        )
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    return df_to_records(df)

@app.get("/indicators/{symbol}")
def get_indicators(symbol: str, db: Session = Depends(get_db)):
    rows = (
        db.query(StockData)
        .filter(StockData.symbol == symbol.upper())
        .order_by(StockData.date)
        .all()
    )

    if not rows:
        df = fetch_live_data(symbol)[["Date", "Close", "Volume"]]
    else:
        df = pd.DataFrame(
            [{"Date": r.date, "Close": r.close, "Volume": r.volume} for r in rows]
        )

    df = calculate_indicators(df)
    latest = df.iloc[-1].replace({pd.NA: None, float("nan"): None}).to_dict()

    # ✅ match lowercase keys from calculate_indicators()
    return {
        "high_52w":   latest.get("high_52w"),
        "low_52w":    latest.get("low_52w"),
        "sma_50":     latest.get("sma_50"),
        "rsi":        latest.get("rsi"),
        "avg_volume": latest.get("avg_volume"),
    }

@app.get("/predict/{symbol}")
def predict_price(symbol: str, db: Session = Depends(get_db)):
    rows = (
        db.query(StockData)
        .filter(StockData.symbol == symbol.upper())
        .order_by(StockData.date)
        .all()
    )

    if not rows:
        df = fetch_live_data(symbol)[["Date", "Close"]]
    else:
        df = pd.DataFrame([{"Date": r.date, "Close": r.close} for r in rows])

    prediction = train_and_predict(df)
    return {"symbol": symbol, "predicted_close": prediction}
