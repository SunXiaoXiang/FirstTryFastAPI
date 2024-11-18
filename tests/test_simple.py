import sys
from fastapi.testclient import TestClient
from FirstTryFastAPI.simple import app, ModelName


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
    assert response.json() == {
        "model_name": model_name,
        "message": "Deep Learning FTW!",
    }


def test_get_model_lenet():
    model_name = ModelName.lenet
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json() == {
        "model_name": model_name,
        "message": "LeCNN all the images",
    }


def test_get_model_resnet():
    model_name = ModelName.resnet
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 200
    assert response.json() == {
        "model_name": model_name,
        "message": "Have some residuals",
    }


def test_read_file():
    file_path = "some/file/path.txt"
    response = client.get(f"/files/{file_path}")
    assert response.status_code == 200
    assert response.json() == {"file_path": file_path}


def test_read_item_default():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == [
        {"item_name": "Foo"},
        {"item_name": "Bar"},
        {"item_name": "Baz"},
    ]


def test_read_item_skip_1():
    response = client.get("/items/?skip=1")
    assert response.status_code == 200
    assert response.json() == [{"item_name": "Bar"}, {"item_name": "Baz"}]


def test_read_item_limit_1():
    response = client.get("/items/?limit=1")
    assert response.status_code == 200
    assert response.json() == [{"item_name": "Foo"}]


def test_read_item_skip_1_limit_1():
    response = client.get("/items/?skip=1&limit=1")
    assert response.status_code == 200
    assert response.json() == [{"item_name": "Bar"}]


def test_read_user_item():
    item_id = "4"
    needy = "bar"
    response = client.get(f"/items/{item_id}?needy={needy}")
    assert response.status_code == 200
    # assert response.json() == {"item_id": item_id, "needy": needy}


# 测试缺少 needy 参数的情况
# def test_read_user_item_missing_needy():
#    item_id = "foo"
#    response = client.get(f"/items/{item_id}")
#    assert response.status_code == 422  # 422 Unprocessable Entity
