import unittest
from unittest import mock

from src.demo.calculator import Calculator

# Mock 抛出异常的方法

# 被调用函数
def multiple(a,b):
    return a * b

# 实际调用函数
def is_error(a,b):
    try:
        return multiple(a,b)
    except Exception as e:
        return -1

class TestCalculator(unittest.TestCase):
    @mock.patch('test14_calculator_mock.multiple')
    def test_function_multiple_exception(self,mock_multiple):
        mock_multiple.side_effect = Exception

        result = is_error(3,5)

        self.assertEqual(result,-1)

if __name__=='__mian__':
    unittest.mian()

