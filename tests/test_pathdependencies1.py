from fastapi.testclient import TestClient
from FirstTryFastAPI.pathdependencies1 import app  # 导入 FastAPI 应用

client = TestClient(app)

def test_read_items_with_valid_headers():
    response = client.get("/items/", headers={"X-Token": "fake-super-secret-token", "X-Key": "fake-super-secret-key"})
    assert response.status_code == 200
    assert response.json() == [{"item": "Foo"}, {"item": "Bar"}]

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
    assert response.status_code == 422  # 由于缺少必要的头部，应该返回422错误
    assert "detail" in response.json()  # 确保返回的 JSON 中包含 detail 字段
