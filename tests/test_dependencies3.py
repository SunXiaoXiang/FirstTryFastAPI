from fastapi.testclient import TestClient
from FirstTryFastAPI.dependencies3 import app  # 导入 FastAPI 应用

client = TestClient(app)

def test_read_items_with_query_params():
    response = client.get("/items/?q=test&skip=0&limit=2")
    print("Response:", response.json())  # 输出响应内容
    assert response.status_code == 200
    assert response.json() == {"q": "test","items": [{"item_name": "Foo"},{"item_name": "Bar"}]}

def test_read_items_without_query_params():
    response = client.get("/items/")
    print("Response:", response.json())  # 输出响应内容
    assert response.status_code == 200
    assert response.json() == {
        "q": None, #LLM 生成的 pytestcase 有问题，q=none commons.q == false。
        "items": [
            {"item_name": "Foo"},
            {"item_name": "Bar"},
            {"item_name": "Baz"}
        ]
    }

def test_read_items_with_skip_and_limit():
    response = client.get("/items/?skip=1&limit=1")
    assert response.status_code == 200
    assert response.json() == {
        "q": None, #LLM 生成的 pytestcase 有问题，q=none commons.q == false。
        "items": [
            {"item_name": "Bar"}
        ]
    }
