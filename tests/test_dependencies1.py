import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.dependencies1 import app  # 导入 FastAPI 应用

@pytest.fixture
def client():
    """创建一个测试客户端的 fixture"""
    return TestClient(app)

@pytest.mark.parametrize("path, params, expected", [
    ("/items/", {"q": "test", "skip": 10, "limit": 20}, {"q": "test", "skip": 10, "limit": 20}),
    ("/users/", {"q": "test"}, {"q": "test", "skip": 0, "limit": 100}),
])
def test_routes(client, path, params, expected):
    """测试多个路由的参数化测试"""
    response = client.get(path, params=params)
    assert response.status_code == 200
    assert response.json() == expected
