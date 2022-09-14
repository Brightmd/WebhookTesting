from fastapi.testclient import TestClient

from webhooktesting.main import app

client = TestClient(app)  # Beware cache is not cleared between tests...


def test_basic_round_trip():
    response = client.put("/webhooktesting", json={"data": "test"})
    assert response.status_code == 200
    assert response.json() == "Successfully added {'data': 'test'}"

    response = client.get("/webhooktesting/search?query=data")
    assert response.status_code == 200
    assert response.json() is True

    response = client.get("/webhooktesting")
    assert response.status_code == 200
    assert response.json() == '[{"data": "test"}]'

    response = client.delete("/webhooktesting")
    assert response.status_code == 200
    assert response.json() == "Successfully cleared cache"

    response = client.get("/webhooktesting")
    assert response.status_code == 200
    assert response.json() == "[]"


def test_no_data():
    response = client.get("/webhooktesting/search?query=foo")
    assert response.status_code == 200
    assert response.json() is False


def test_missing_data():
    client.put("/webhooktesting", json={"foo": "bar"})

    response = client.get("/webhooktesting/search?query=fooz")
    assert response.status_code == 200
    assert response.json() is False


def test_unreliable_add():
    for i in range(1, 100):
        response = client.put("/webhooktesting/unreliable", json={"add": "unreliable"})
        assert response.status_code in [200, 400]
        assert response.json() in [
            {"detail": "Failed to add data"},
            "Successfully added {'add': 'unreliable'}",
        ]

    response = client.get("/webhooktesting/search?query=unreliable")
    assert response.status_code == 200
    assert response.json() is True
