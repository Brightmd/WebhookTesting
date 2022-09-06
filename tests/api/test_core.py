from fastapi.testclient import TestClient

from webhooktesting.main import app

client = TestClient(app)  # Beware cache is not cleared between tests...


def test_basic_round_trip():
    response = client.put("/webhooktesting", json={"data": "test"})
    assert response.status_code == 200
    assert response.json() == "[{'data': 'test'}]"

    response = client.get("/webhooktesting/search?query=data")
    assert response.status_code == 200
    assert response.json() is True


def test_no_data():
    response = client.get("/webhooktesting/search?query=foo")
    assert response.status_code == 200
    assert response.json() is False


def test_missing_data():
    client.put("/webhooktesting", json={"foo": "bar"})

    response = client.get("/webhooktesting/search?query=fooz")
    assert response.status_code == 200
    assert response.json() is False
