# backend/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_get_companies():
    response = client.get("/companies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_stock_data():
    symbol = "AAPL"  # assuming dataset contains AAPL
    response = client.get(f"/stock/{symbol}")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data
    assert "historical" in data
