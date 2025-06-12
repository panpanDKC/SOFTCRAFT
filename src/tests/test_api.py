from fastapi.testclient import TestClient
import pytest
from api.blueprints import app

client = TestClient(app)

def test_api_success():
    response = client.get("/blueprints/analyze")
    assert response.status_code == 200
    data = response.json()
    assert data["bestBlueprint"] == "2"
    assert data["blueprints"][0]["quality"] == 3
    assert data["blueprints"][1]["quality"] == 6
