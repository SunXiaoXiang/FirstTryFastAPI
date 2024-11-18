import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.requestBody6 import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)


# 测试PUT请求，传入有效的Item对象
def test_update_item_valid_input():
    response = client.put(
        "/items/1",
        json={
            "item": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        },
    )
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 1,
        "item": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    }


# 使用parametrize来测试多种异常场景
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (
            {
                "item": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": -1.0,
                    "tax": 3.2,
                }
            },
            422,
        ),  # 价格小于0
        (
            {
                "item": {
                    "name": "",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            },
            200,
        ),  # 名称为空
        (
            {"item": {"description": "A very nice Item", "price": 35.4, "tax": 3.2}},
            422,
        ),  # 缺少名称
        (
            {"item": {"name": "Foo", "description": "A very nice Item", "tax": 3.2}},
            422,
        ),  # 缺少价格
        (
            {
                "item": {
                    "name": "Foo",
                    "description": "A very long description that exceeds the maximum length of 300 characters. A very long description that exceeds the maximum length of 300 characters. A very long description that exceeds the maximum length of 300 characters.",
                }
            },
            422,
        ),  # 描述超过最大长度
        (
            {
                "item": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 0,
                    "tax": 3.2,
                }
            },
            422,
        ),  # 价格等于0
    ],
)
def test_update_item_invalid_input(payload, expected_status):
    response = client.put("/items/1", json=payload)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == expected_status
