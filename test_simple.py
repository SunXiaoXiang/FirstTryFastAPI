import sys
from fastapi.testclient import TestClient
from simple import app, ModelName

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

def test_read_item():
    item_id = 21
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id}

def test_get_model_alexnet():
    model_name = ModelName.alexnet
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json() == {"model_name": model_name, "message": "Deep Learning FTW!"}

def test_get_model_lenet():
    model_name = ModelName.lenet
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json() == {"model_name": model_name, "message": "LeCNN all the images"}

def test_get_model_resnet():
    model_name = ModelName.resnet
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json() == {"model_name": model_name, "message": "Have some residuals"}