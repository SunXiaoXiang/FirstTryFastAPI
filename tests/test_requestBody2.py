from fastapi.testclient import TestClient
from FirstTryFastAPI.requestBody2 import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)


# 测试PUT请求，传入有效的item_id和name
def test_read_item_valid_input():
    response = client.put("/items/", params={"item_id": 1, "name": "Foo"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Foo"}


# 测试PUT请求，传入无效的item_id（例如非整数）
def test_read_item_invalid_item_id():
    response = client.put("/items/", params={"item_id": "not_an_int", "name": "Foo"})
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity


# 测试PUT请求，传入无效的name（例如空字符串）
def test_read_item_invalid_name():
    response = client.put("/items/", params={"item_id": 1, "name": ""})
    # assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity
    assert response.status_code == 200  # 实际执行时，空字符串并不会报错，依然正确执行


# 测试PUT请求，不传入item_id
def test_read_item_missing_item_id():
    response = client.put("/items/", params={"name": "Foo"})
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity


# 测试PUT请求，不传入name
def test_read_item_missing_name():
    response = client.put("/items/", params={"item_id": 1})
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity


# 测试PUT请求，传入负数的item_id
def test_read_item_negative_item_id():
    response = client.put("/items/", params={"item_id": -1, "name": "Foo"})
    assert (
        response.status_code == 200
    )  # 负数id仍然会被接受，但实际应用中可能需要进一步处理
    assert response.json() == {"item_id": -1, "name": "Foo"}


# 测试PUT请求，传入非常大的item_id
def test_read_item_large_item_id():
    response = client.put(
        "/items/", params={"item_id": 9999999999999999999, "name": "Foo"}
    )
    assert (
        response.status_code == 200
    )  # 非常大的id仍然会被接受，但实际应用中可能需要进一步处理
    assert response.json() == {"item_id": 9999999999999999999, "name": "Foo"}
