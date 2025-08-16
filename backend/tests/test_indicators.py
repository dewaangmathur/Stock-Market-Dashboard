# backend/tests/test_indicators.py
from backend.indicators import calculate_indicators
import pandas as pd

def test_calculate_indicators():
    # Fake data for testing
    df = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=60, freq="D"),
        "Close": [100 + i for i in range(60)],
        "Volume": [1000 + i * 10 for i in range(60)]
    })

    result = calculate_indicators(df)
    assert "sma_20" in result.columns
    assert "rsi_14" in result.columns
    assert "52_week_high" in result.columns
    assert "52_week_low" in result.columns
    assert "avg_volume" in result.columns
