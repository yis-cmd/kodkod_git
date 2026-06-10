import pytest
from fastapi.testclient import TestClient
from main import app, load_weapons


# @pytest.fixture
# def make_client():
#     def _make(weapons):
#         app.dependency_overrides[load_weapons] = lambda: weapons
#         return TestClient(app)
#     yield _make
#     app.dependency_overrides.clear()


# def test_get_full_list_with_weapons(make_client):
#     client = make_client([
#         {"id": 2, "type": "launcher", "model": "LAW", "ammo_type": "rocket", "condition": "damaged"},
#         {"id": 5, "type": "machine_gun", "model": "Negev", "ammo_type": "5.56mm", "condition": "damaged"}
#         ])
#     response = client.get("/weapons")
#     assert response.status_code == 200
#     assert len(response.json()) == 2

# def test_get_full_list_with_no_weapons(make_client):
#     client = make_client([])
#     response = client.get("/weapons")
#     assert response.status_code == 200
#     assert len(response.json()) == 0


# response_all_weapons = requests.get("http://127.0.0.1:8000/weapons")
# assert response_all_weapons.status_code == 200
# assert len(response_all_weapons.json()) == 70

# response_weapons_by_condition = requests.get("http://127.0.0.1:8000/weapons/by-condition")
# assert response_weapons_by_condition.status_code == 200

# requests.get("http://127.0.0.1:8000")
# requests.get("http://127.0.0.1:8000")
# requests.get("http://127.0.0.1:8000")


import pytest
from fastapi.testclient import TestClient
from main import app, load_weapons

@pytest.fixture
def make_client():
    app.dependency_overrides.clear()
    def _make(data):
    
        app.dependency_overrides[load_weapons] = lambda : data
        return TestClient(app)
    yield _make
    app.dependency_overrides.clear()

def test_with_data(make_client):
    client = make_client([])
    response = client.get("/weapons")
    assert len(response.json()) == 0
    assert response.status_code == 200