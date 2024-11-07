# test_app.py
import app
import pytest

@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client

def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_create_item(client):
    response = client.post('/items', json={"name": "New Item"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "New Item"

def test_update_item(client):
    # Assuming item with ID 1 exists for the test
    response = client.put('/items/1', json={"name": "Updated Item"})
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated Item"

def test_delete_item(client):
    # Assuming item with ID 2 exists for the test
    response = client.delete('/items/2')
    assert response.status_code == 200
    assert response.get_json()["id"] == 2

def test_get_item(client):
    # Assuming item with ID 1 exists for the test
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.get_json()["id"] == 1