import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.response2 import app

client = TestClient(app)

@pytest.mark.parametrize("username, password, email, full_name, expected_status, expected_response", [
    ("testuser", "testpassword", "test@example.com", "Test User", 200, {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }),
    ("existinguser", "testpassword", "test@example.com", "Test User", 200, None),  # 用户名已存在
    ("testuser", "testpassword", "invalid-email", "Test User", 422, None)  # 无效的电子邮件
])
def test_create_user(username, password, email, full_name, expected_status, expected_response):
    response = client.post(
        "/user/",
        json={
            "username": username,
            "password": password,
            "email": email,
            "full_name": full_name
        }
    )
    assert response.status_code == expected_status
    if expected_response is not None:
        assert response.json() == expected_response
