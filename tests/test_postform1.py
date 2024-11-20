from fastapi.testclient import TestClient
from FirstTryFastAPI.postform1 import app  # 导入你的 FastAPI 应用实例

client = TestClient(app)

def test_login_success():
    data = {"username": "testuser", "password": "testpass"}
    response = client.post("/login/", data=data)
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}
    print("请求正文:", data)  # 输出请求正文

def test_login_missing_username():
    data = {"password": "testpass"}
    response = client.post("/login/", data=data)
    assert response.status_code == 422  # FastAPI 会返回 422 Unprocessable Entity
    print("请求正文:", data)  # 输出请求正文

def test_login_missing_password():
    data = {"username": "testuser"}
    response = client.post("/login/", data=data)
    assert response.status_code == 422  # FastAPI 会返回 422 Unprocessable Entity
    print("请求正文:", data)  # 输出请求正文

def test_login_empty_fields():
    data = {"username": "", "password": ""}
    response = client.post("/login/", data=data)
    assert response.status_code == 200  # FastAPI 会返回 200 OK
    print("请求正文:", data)  # 输出请求正文
