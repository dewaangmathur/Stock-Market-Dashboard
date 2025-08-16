# backend/indicators.py
import pandas as pd

def calculate_indicators(df: pd.DataFrame):
    df = df.copy()

    # 50-day Simple Moving Average
    df["sma_50"] = df["Close"].rolling(window=50).mean()

    # RSI (14)
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    # 52-week high / low (252 trading days)
    df["high_52w"] = df["Close"].rolling(window=252, min_periods=1).max()
    df["low_52w"] = df["Close"].rolling(window=252, min_periods=1).min()

    # Average Volume (20-day)
    df["avg_volume"] = df["Volume"].rolling(window=20).mean()

    return df
