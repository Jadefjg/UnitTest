import pytest

from src.demo.calculator import Calculator

class TestCalculator():

    def test_add(self, mocker):
        c = Calculator()
        mock_return = 10
        mocker.patch.object(c, 'add', return_value=mock_return)

        result = c.add(3, 5)

        assert result == mock_return

if __name__ == '__main__':
    pytest.main(['-s', 'test16_calculator_pytest_mock.py'])