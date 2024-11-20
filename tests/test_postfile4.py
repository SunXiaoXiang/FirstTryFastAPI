from fastapi.testclient import TestClient
from FirstTryFastAPI.postfile4 import app  # 导入你的 FastAPI 应用实例
from io import BytesIO

client = TestClient(app)

def test_create_file_with_token():
    # 创建一个模拟的文件对象
    file_content = b"Hello, this is a test file."
    file_name = "testfile.txt"

    # 使用 BytesIO 创建一个文件对象
    file_like = BytesIO(file_content)
    file_like.name = file_name  # 设置文件名

    # 发送 POST 请求上传文件和 token
    response = client.post(
        "/files/",
        files={"file": (file_like.name, file_like, "text/plain")},
        data={"token": "test_token"}
    )

    # 验证响应
    assert response.status_code == 200
    assert response.json() == {
        "token": "test_token",
        "file_name": file_name,
    }

def test_create_file_without_token():
    # 创建一个模拟的文件对象
    file_content = b"Hello, this is a test file."
    file_name = "testfile.txt"

    # 使用 BytesIO 创建一个文件对象
    file_like = BytesIO(file_content)
    file_like.name = file_name  # 设置文件名

    # 发送 POST 请求上传文件而不提供 token
    response = client.post(
        "/files/",
        files={"file": (file_like.name, file_like, "text/plain")}
    )

    # 验证响应
    assert response.status_code == 422  # FastAPI 会返回 422 Unprocessable Entity
