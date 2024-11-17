import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.response1 import app, Item  # 导入你的FastAPI应用实例

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


# 使用parametrize来测试items的异常场景
@pytest.mark.parametrize("item_id, expected_status, expected_detail", [
    ("nonexistent", 404, {"detail": "Item not found"}),  # 测试不存在的项目
    ("foo", 200, {"name": "Foo", "price": 50.2}),  # 测试最小数据的项目
    ("bar", 200, {"name": "Bar", "description": "The bartenders", "price": 62.0, "tax": 20.2}),  # 测试完整数据的项目
])
def test_read_item(item_id, expected_status, expected_detail):
    response = client.get(f"/items/{item_id}")
    print("Get item response:", response.json())
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == expected_detail
    else:
        assert response.json() == expected_detail