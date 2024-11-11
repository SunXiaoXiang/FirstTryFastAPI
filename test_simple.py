import sys


def test_sys_version(capsys):
    # 调用 print(sys.version)
    print(sys.version)

    # 捕获标准输出
    captured = capsys.readouterr()

    # 断言输出是否符合预期
    assert captured.out.strip() == sys.version.strip()
