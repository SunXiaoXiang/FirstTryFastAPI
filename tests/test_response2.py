from fastapi.testclient import TestClient
from FirstTryFastAPI.response2 import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }

def test_create_user_invalid_email():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "invalid-email",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 422  # Unprocessable Entity
