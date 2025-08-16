# backend/ingest.py
import pandas as pd
from backend.database import Base, engine, SessionLocal
from backend.models import StockData

def ingest_all_symbols(filepath):
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    df = pd.read_csv(filepath, parse_dates=["Date"])

    # Get all unique symbols in the "Company" column
    symbols = df["Company"].unique()

    for symbol in symbols:
        company_df = df[df["Company"] == symbol].sort_values("Date").tail(365)
        for _, row in company_df.iterrows():
            stock = StockData(
                symbol=row["Company"],
                date=row["Date"].date(),
                open=row["Open"],
                high=row["High"],
                low=row["Low"],
                close=row["Close"],
                volume=row["Volume"]
            )
            db.add(stock)
        print(f"Loaded last 1 year for {symbol}")

    db.commit()
    db.close()
    print("✅ Data ingestion complete for all companies (last 1 year each)")

if __name__ == "__main__":
    ingest_all_symbols("./dataset/massive_yahoo_finance_data.csv")
