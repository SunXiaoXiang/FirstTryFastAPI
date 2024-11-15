from fastapi.testclient import TestClient
from requestBody import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)

# 测试PUT请求，传入有效的item_id
def test_read_item_valid_id():
    response = client.put("/items/", params={"item_id": 1})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

# 测试PUT请求，传入无效的item_id（例如非整数）
def test_read_item_invalid_id():
    response = client.put("/items/", params={"item_id": "not_an_int"})
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity

# 测试PUT请求，不传入item_id
def test_read_item_missing_id():
    response = client.put("/items/")
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity

# 测试PUT请求，传入负数的item_id
def test_read_item_negative_id():
    response = client.put("/items/", params={"item_id": -1})
    assert response.status_code == 200  # 负数id仍然会被接受，但实际应用中可能需要进一步处理
    assert response.json() == {"item_id": -1}