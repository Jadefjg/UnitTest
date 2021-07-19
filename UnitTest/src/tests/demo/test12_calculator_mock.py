import unittest

from unittest import mock

from src.demo.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        mock_return = 10
        c.add = mock.Mock(return_value=mock_return)

        result = c.add(3,5)
        self.assertEqual(result,mock_return)

    def test_add_with_side_effect(self):
        c = Calculator()
        mock_return = 10

        # 传递 side_effect 关键字参数，会覆盖 return_value 参数值， 使用真实的 add 方法测试
        c.add = mock.Mock(return_value=mock_return,side_effect=c.add)

        result = c.add(3,5)

        self.assertEqual(result,8)

    @mock.patch.object(Calculator,'add')
    def test_add_with_annotation(self,mock_add):
        c = Calculator()
        mock_return = 10
        mock_add.return_value = mock_return
        result = c.add(3,5)
        self.assertEqual(result,mock_return)

if __name__=='__main__':
    unittest.main()
