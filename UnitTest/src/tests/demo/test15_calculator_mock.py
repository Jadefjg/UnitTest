import unittest
from unittest import mock

from src.demo.calculator import Calculator

# Mock 多个方法

def multiple(a, b):
    return a * b

class TestCalculator(unittest.TestCase):
    @mock.patch.object(Calculator, 'add')
    @mock.patch('test15_calculator_mock.multiple')
    def test_both(self, mock_multiple, mock_add):
        c = Calculator()
        mock_add.return_value = 1
        mock_multiple.return_value = 2

        self.assertEqual(c.add(3, 5), 1)
        self.assertEqual(multiple(3, 5), 2)


if __name__ == '__main__':
    unittest.main()