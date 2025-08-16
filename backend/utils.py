# backend/utils.py
import pandas as pd

def load_csv(filepath):
    """Load CSV into pandas DataFrame with date parsing."""
    return pd.read_csv(filepath, parse_dates=["Date"])

def df_to_records(df):
    """Convert DataFrame to list of dicts for JSON response."""
    return df.to_dict(orient="records")
