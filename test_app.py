import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_healthz_request(client):
    response = client.get("/healthz")
    assert response.json["status"] == 200
    assert response.json["title"] == "OK"

def test_main_request(client):
    response = client.get("/")
    assert response.json["my public ip"] == "127.0.0.1"
