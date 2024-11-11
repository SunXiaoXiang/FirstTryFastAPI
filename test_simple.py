import sys
from fastapi.testclient import TestClient
from simple import app

def test_sys_version(capsys):
    # 调用 print(sys.version)
    print(sys.version)

    # 捕获标准输出
    captured = capsys.readouterr()

    # 断言输出是否符合预期
    assert captured.out.strip() == sys.version.strip()

client = TestClient(app)

def test_HelloWorld():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}