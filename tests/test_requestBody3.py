from fastapi.testclient import TestClient
from FirstTryFastAPI.requestBody3 import app  # 导入你的FastAPI应用实例

# 创建一个测试客户端
client = TestClient(app)

# 测试PUT请求，传入有效的item_id
def test_read_item_valid_id():
    response = client.put("/items/", json=1)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
    #assert response.json() == {"detail":[{"loc":["string",0],"msg":"string","type":"int_type"}]}
    

# 测试PUT请求，传入无效的item_id（例如非整数）
def test_read_item_invalid_id():
    response = client.put("/items/", json="not_an_int")
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity
    assert response.json() == {'detail': [{'type': 'int_parsing', 'loc': ['body'], 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'not_an_int'}]}

# 测试PUT请求，不传入item_id
def test_read_item_missing_id():
    response = client.put("/items/", json={})
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 422  # 验证错误应返回422 Unprocessable Entity
    assert response.json() == {'detail': [{'type': 'int_type', 'loc': ['body'], 'msg': 'Input should be a valid integer', 'input': {}}]}


# 测试PUT请求，传入负数的item_id
def test_read_item_negative_id():
    response = client.put("/items/", json=-1)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200  # 负数id仍然会被接受，但实际应用中可能需要进一步处理
    assert response.json() == {"item_id": -1}

# 测试PUT请求，传入非常大的item_id
def test_read_item_large_id():
    response = client.put("/items/", json=9999999999999999999)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200  # 非常大的id仍然会被接受，但实际应用中可能需要进一步处理
    assert response.json() == {"item_id": 9999999999999999999}