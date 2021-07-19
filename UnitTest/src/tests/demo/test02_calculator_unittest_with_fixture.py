import unittest

from src.demo.calculator import Calculator

class TestCalculatorWithFixture(unittest.TestCase):
    # 测试用例前置动作
    def setUp(self):
        print("test start")

    # 测试用例后置动作
    def tearDown(self):
        print("test end")

    def test_add(self):
        c = Calculator()
        result = c.add(3, 5)
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator()
        result = c.sub(10, 5)
        self.assertEqual(result, 5)

    def test_mul(self):
        c = Calculator()
        result = c.mul(5, 7)
        self.assertEqual(result, 35)

    def test_div(self):
        c = Calculator()
        result = c.div(10, 5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculatorWithFixture("test_add"))
    suit.addTest(TestCalculatorWithFixture("test_sub"))
    suit.addTest(TestCalculatorWithFixture("test_mul"))
    suit.addTest(TestCalculatorWithFixture("test_div"))
    # 创建测试运行器
    runner = unittest.TestSuite()
    runner.run(suit)


