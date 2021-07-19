import unittest

from unittest import mock

from src.demo.calculator import Calculator


# Mock 每次调用返回不同的值
class TestCalculator(unittest.TestCase):
    @mock.patch.object(Calculator,'add')
    def test_add_with_different_return(self,mock_add):
        c = Calculator()
        mock_return = [10,8]
        mock_add.side_effect = mock_return

        result1 = c.add(3,5)
        result2 = c.add(3,5)

        self.assertEqual(result1,mock_return[0])
        self.assertEqual(result2,mock_return[1])

if __name__=='__main__':
    unittest.mian()



