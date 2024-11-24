from fastapi.testclient import TestClient
from FirstTryFastAPI.dependencies2 import app  # 导入 FastAPI 应用

client = TestClient(app)

def test_read_items_with_query_params():
    response = client.get("/items/?q=test&skip=0&limit=10")
    assert response.status_code == 200
    assert response.json() == {
        "q": "test",
        "skip": 0,
        "limit": 10
    }

def test_read_items_without_query_params():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "q": None,
        "skip": 0,
        "limit": 100
    }
