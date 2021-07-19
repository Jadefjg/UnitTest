
import unittest

from src.demo.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        result = c.add(3,5)
        self.assertEqual(result,8)

    def test_sub(self):
        c = Calculator()
        result = c.sub(10,5)
        self.assertEqual(result,5)

    def test_mul(self):
        c = Calculator()
        result = c.mul(5,7)
        self.assertEqual(result,35)

    def test_div(self):
        c = Calculator()
        result = c.div(10,5)
        self.assertEqual(result,2)

if __name__=='__main__':
    unittest.main()
