# 暂未调通，不知原因

import nose2
from nose2.tools import params

from src.demo.calculator import Calculator

test_data = [
    {"nums": (3, 5), "total": 8},
    {"nums": (1, 2), "total": 3},
    {"nums": (2, 2), "total": 4}
]


@params(*test_data)
def test_add(data):
    c = Calculator()
    result = c.add(*data["nums"])
    assert result == data["data"]


if __name__ == '__main__':
    nose2.main()
