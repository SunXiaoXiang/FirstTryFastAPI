from fastapi.testclient import TestClient
from FirstTryFastAPI.subdependencies1 import app  # 导入 FastAPI 应用

client = TestClient(app)

# 在测试客户端中设置默认 cookies
client.cookies.set("last_query", "cookie_value")

def test_read_query_with_query_param():
    response = client.get("/items/?q=test")
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "test"}

def test_read_query_with_cookie():
    response = client.get("/items/")  # 使用默认的 cookie
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "cookie_value"}

def test_read_query_with_both():
    response = client.get("/items/?q=test")  # 使用默认的 cookie
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": "test"}

def test_read_query_with_no_query_or_cookie():
    # 创建一个新的客户端实例，不带 cookies
    client_no_cookies = TestClient(app)
    response = client_no_cookies.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"q_or_cookie": None}
