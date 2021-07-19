import pytest

from src.demo.calculator import Calculator


'''
基础知识:
如果只有一个参数，里面则是值的列表，比如@pytest.mark.parametrize("num1", [3, 5, 8])
如果有多个参数，则需要用元祖来存放值，一个元祖对应一组参数的值，比如@pytest.mark.parametrize("num1, num2, total", [(3, 5, 8), (1, 2, 3), (2, 2, 4)])
当装饰器 @pytest.mark.parametrize装饰测试类时，会将数据集合传递给类的所有测试用例方法
一个函数或一个类可以装饰多个 @pytest.mark.parametrize，当参数化有多个装饰器时，用例数是 N*M...
'''


class TestCalculator():
    @pytest.mark.parametrize("num1,num2,total",[(3,5,8),(1,2,3),(2,2,4)])
    def test_add(self,num1,num2,total):
        c = Calculator()
        result = c.add(num1,num2)
        assert result == total

if __name__=="__main__":
    pytest.main(['test_calculator_pytest_with_patameterize.py'])