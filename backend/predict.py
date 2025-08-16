# backend/predict.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def train_and_predict(df: pd.DataFrame):
    df = df.copy()
    df["Day"] = np.arange(len(df))
    X = df[["Day"]]
    y = df["Close"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[len(df)]]
    prediction = model.predict(next_day)[0]
    return float(prediction)
