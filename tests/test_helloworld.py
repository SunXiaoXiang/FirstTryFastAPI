from FirstTryFastAPI.helloworld import main

def test_main(capsys):
    # 调用 main 函数
    main()
    
    # 捕获标准输出
    captured = capsys.readouterr()
    
    # 断言输出是否符合预期
    assert captured.out == "Hello World from First try fastapi!\n"