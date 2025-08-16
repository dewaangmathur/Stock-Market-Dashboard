# backend/tests/test_predict.py
from backend.predict import train_and_predict
import pandas as pd

def test_train_and_predict():
    # Fake historical data
    df = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=50, freq="D"),
        "Close": [100 + i for i in range(50)]
    })

    prediction = train_and_predict(df)
    assert isinstance(prediction, float) or isinstance(prediction, int)
