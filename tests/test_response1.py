import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.response1 import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)

# 测试POST请求，传入有效的UserIn对象
def test_create_user_valid_input():
    response = client.post("/user/", json={
        "username": "johndoe",
        "password": "secret",
        "email": "johndoe@example.com",
        "full_name": "John Doe"
    })
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe"
    }

# 使用parametrize来测试多种异常场景
@pytest.mark.parametrize("payload, expected_status", [
    ({"username": "johndoe", "password": "secret", "email": "invalid_email"}, 422),  # 无效的电子邮件
    ({"username": "", "password": "secret", "email": "johndoe@example.com"}, 200),  # 空的用户名
    ({"username": "johndoe", "password": "", "email": "johndoe@example.com"}, 200),  # 空的密码
    ({"username": "johndoe", "email": "johndoe@example.com"}, 422),  # 缺少密码
    ({"password": "secret", "email": "johndoe@example.com"}, 422),  # 缺少用户名
    ({"username": "johndoe", "password": "secret", "email": "johndoe@example.com", "full_name": "x" * 1000}, 200),  # 姓名过长
])
def test_create_user_invalid_input(payload, expected_status):
    response = client.post("/user/", json=payload)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == expected_status