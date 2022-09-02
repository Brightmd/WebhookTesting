from fastapi.testclient import TestClient

from webhooktesting.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/webhooktesting/healthcheck")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_version():
    response = client.get("/webhooktesting/version")
    assert response.status_code == 200
    assert "version" in response.json()
