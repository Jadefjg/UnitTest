import unittest
from parameterized import parameterized, param
from src.demo.calculator import Calculator

class TestCalculator(unittest.TestCase):
    @parameterized.expand([
        param(3,5,8),
        param(1,2,3),
        param(2,2,4)
    ])

    def test_add(self,num1,num2,total):
        c = Calculator()
        result = c.add(num1,num2)
        self.assertEqual(result,total)

unittest.main()
