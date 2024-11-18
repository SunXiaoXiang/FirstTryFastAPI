import pytest
from fastapi.testclient import TestClient
from FirstTryFastAPI.requestBody5 import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)


# 测试PUT请求，传入有效的Item对象
def test_read_item_valid_input():
    response = client.put(
        "/items/",
        json={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    )
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"name": "Foo", "price": 35.4}


# 使用parametrize来测试多种异常场景
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": "not_a_float",
                "tax": 3.2,
            },
            422,
        ),  # 无效的price
        (
            {"name": "", "description": "A very nice Item", "price": 35.4, "tax": 3.2},
            200,
        ),  # 无效的name
        (
            {"description": "A very nice Item", "price": 35.4, "tax": 3.2},
            422,
        ),  # 缺少name
        (
            {"name": "Foo", "description": "A very nice Item", "tax": 3.2},
            422,
        ),  # 缺少price
        (
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": -35.4,
                "tax": 3.2,
            },
            200,
        ),  # 负数的price
        (
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 9999999999999999999.0,
                "tax": 3.2,
            },
            200,
        ),  # 非常大的price
    ],
)
def test_read_item_invalid_input(payload, expected_status):
    response = client.put("/items/", json=payload)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == expected_status
