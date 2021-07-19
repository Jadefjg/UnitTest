import pytest

from src.demo.calculator import Calculator

'''
加上 fixture 夹具，有几种方式：

    将夹具函数名称作为参数传递到测试用例函数当中
    @pytest.mark.usefixtures("夹具函数名称")
    @pytest.fixture(autouse=True)，设置了 autouse，就可以不用上述两种手动方式，默认就会使用夹具
    
'''


@pytest.fixture()
def set_up():
    print("[pytest with fixture] start")
    yield                                      # yield 生成器
    print("[pytest with fixture] end")

class TestCalculator():

    def test_add(self,set_up):
        c = Calculator()
        result = c.add(3,5)
        assert result == 8

    def test_sub(self,set_up):
        c =  Calculator()
        result = c.sub(10,5)
        assert result == 5

    @pytest.mark.usefixtures("set_up")
    def test_mul(self):
        c = Calculator()
        result = c.mul(5,7)
        assert result == 35

    @pytest.mark.usefixtures("set_up")
    def test_div(self):
        c = Calculator()
        result =c.div(10,5)
        assert result == 2

if __name__=='__main__':
    pytest.main(['-s','test08_calculator_pytest_with_fixture.py'])