from fastapi.testclient import TestClient
from FirstTryFastAPI.postfile1 import app  # 导入你的 FastAPI 应用实例
from io import BytesIO

client = TestClient(app)

def test_upload_file():
    # 创建一个模拟的文件对象
    file_content = b"Hello, this is a test file."
    file_name = "testfile.txt"

    # 使用 BytesIO 创建一个文件对象
    file_like = BytesIO(file_content)
    file_like.name = file_name  # 设置文件名

    # 发送 POST 请求上传文件
    response = client.post("/uploadfile/", files={"file": (file_like.name, file_like, "text/plain")})

    # 验证响应
    assert response.status_code == 200
    assert response.json() == {"filename": file_name}
