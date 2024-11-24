from fastapi.testclient import TestClient
from FirstTryFastAPI.globaldependecies1 import app  # 导入 FastAPI 应用

client = TestClient(app)

def test_read_items_with_valid_headers():
    response = client.get("/items/", headers={"X-Token": "fake-super-secret-token", "X-Key": "fake-super-secret-key"})
    assert response.status_code == 200
    assert response.json() == [{"item": "Portal Gun"}, {"item": "Plumbus"}]

def test_read_items_with_invalid_token():
    response = client.get("/items/", headers={"X-Token": "invalid-token", "X-Key": "fake-super-secret-key"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}

def test_read_items_with_invalid_key():
    response = client.get("/items/", headers={"X-Token": "fake-super-secret-token", "X-Key": "invalid-key"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Key header invalid"}

def test_read_items_with_missing_headers():
    response = client.get("/items/")
    assert response.status_code == 422  # 由于缺少必要的头部，应该返回400错误
    assert "detail" in response.json()  # 确保返回的 JSON 中包含 detail 字段

def test_read_users_with_valid_headers():
    response = client.get("/users/", headers={"X-Token": "fake-super-secret-token", "X-Key": "fake-super-secret-key"})
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]

def test_read_users_with_invalid_token():
    response = client.get("/users/", headers={"X-Token": "invalid-token", "X-Key": "fake-super-secret-key"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}

def test_read_users_with_invalid_key():
    response = client.get("/users/", headers={"X-Token": "fake-super-secret-token", "X-Key": "invalid-key"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Key header invalid"}

def test_read_users_with_missing_headers():
    response = client.get("/users/")
    assert response.status_code == 422  # 由于缺少必要的头部，应该返回400错误
    assert "detail" in response.json()  # 确保返回的 JSON 中包含 detail 字段
