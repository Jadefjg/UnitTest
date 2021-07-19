import unittest
from ddt import data,unpack,ddt
from src.demo.calculator import Calculator

@ddt
class TestCalculator(unittest.TestCase):
    @data((3,5,8),(1,2,3),(2,2,4))
    @unpack
    def test_add(self,num1,num2,total):
        c = Calculator()
        result = c.add(num1,num2)
        self.assertEqual(result,total)

if __name__=='__main__':
    unittest.main()




