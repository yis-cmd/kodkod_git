import pytest
from fastapi.testclient import TestClient
from main import app, load_weapons
from mysql.connector import connect


with connect() as db:
    with db.cursor() as cur:
        

@pytest.fixture
def make_client():
    def _make(data):
        app.dependency_overrides[load_weapons] = lambda: data
        return TestClient(app)
    yield _make
    app.dependency_overrides.clear()

def test(make_client):
    data = {"id":1}
    client = make_client(data)
    response = client.get("/weapons")
    assert response.status_code == 200