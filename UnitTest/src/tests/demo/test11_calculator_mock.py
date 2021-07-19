import unittest

from unittest import mock

from src.demo.calculator import Calculator


def multiple(a,b):
    return a * b

class TestCalculator(unittest.TestCase):
    @mock.patch('test11_calculator_mock.multiple')
    def test_function_multiple(self,mock_multiple):
        mock_return = 1
        mock_multiple.return_value = mock_return
        result = multiple(3,5)
        self.assertEqual(result,mock_return)

if __name__=='__main__':
    unittest.main()
