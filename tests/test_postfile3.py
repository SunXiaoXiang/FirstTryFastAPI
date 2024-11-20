from fastapi.testclient import TestClient
from FirstTryFastAPI.postfile3 import app  # 导入你的 FastAPI 应用实例
from io import BytesIO

client = TestClient(app)

def test_upload_multiple_files():
    # 创建多个模拟的文件对象
    file_contents = [b"Hello from file 1.", b"Hello from file 2."]
    file_names = ["file1.txt", "file2.txt"]

    # 使用 BytesIO 创建文件对象
    files = [
        (file_name, BytesIO(file_content), "text/plain")
        for file_name, file_content in zip(file_names, file_contents)
    ]

    # 发送 POST 请求上传多个文件
    response = client.post("/uploadfiles/", files=[("files", (file_name, file_like, content_type)) for file_name, file_like, content_type in files])

    # 验证响应
    assert response.status_code == 200
    assert response.json() == {"filenames": file_names}

def test_upload_no_files():
    # 发送 POST 请求而不上传文件
    response = client.post("/uploadfiles/")

    # 验证响应
    assert response.status_code == 422  # FastAPI 会返回 422 Unprocessable Entity
