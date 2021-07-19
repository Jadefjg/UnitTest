class ForTest:
    field = 'origin'

    def method(self):
        pass


def test_for_test(mocker):
    test = ForTest()
    # 方法
    mock_method = mocker.patch.object(test, 'method')
    test.method()
    # 检查行为
    assert mock_method.called

    # 域
    assert 'origin' == test.field
    mocker.patch.object(test, 'field', 'mocked')
    # 检查结果
    assert 'mocked' == test.field