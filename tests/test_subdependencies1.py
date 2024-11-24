from fastapi.testclient import TestClient
from FirstTryFastAPI.subdependencies1 import app  # 导入 FastAPI 应用

client = TestClient(app)

def test_read_query_with_query_param():
    response = client.get("/items/?q=test")
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "test"}

def test_read_query_with_cookie():
    response = client.get("/items/", cookies={"last_query": "cookie_value"})
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "cookie_value"}

def test_read_query_with_both():
    response = client.get("/items/?q=test", cookies={"last_query": "cookie_value"})
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "test"}

def test_read_query_with_no_query_or_cookie():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": None}
