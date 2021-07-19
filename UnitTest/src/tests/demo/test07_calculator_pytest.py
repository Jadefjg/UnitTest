import pytest

from src.demo.calculator import Calculator

class TestCalculator():

    def test_add(self):
        c = Calculator()
        result = c.add(3,5)
        assert result == 8

    def test_sub(self):
        c =  Calculator()
        result = c.sub(10,5)
        assert result == 5

    def test_mul(self):
        c = Calculator()
        result = c.mul(5,7)
        assert result == 35

    def test_div(self):
        c = Calculator()
        result =c.div(10,5)
        assert result == 2

if __name__=='__main__':
    pytest.main(['-s','test07_calculator_pytest.py'])