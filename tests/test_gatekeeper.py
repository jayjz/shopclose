import json
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8-sig"))


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_missing_refrigerant():
    response = client.post(
        "/review",
        json=load_fixture("job_missing_charge.json"),
    )
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "review_needed"
    assert result["possible_omissions"] == ["refrigerant"]
    assert result["requires_human_approval"] is True


def test_clean_invoice():
    response = client.post(
        "/review",
        json=load_fixture("job_clean.json"),
    )
    assert response.status_code == 200
    assert response.json()["possible_omissions"] == []


def test_invalid_request():
    response = client.post("/review", json={"job_id": "123"})
    assert response.status_code == 422
