# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
import unittest


def my_sqrt(x: int) -> int:
    ans = x
    delta = x
    while True:
        if x - (ans * ans) > 1:
            ans = ans // 2
        elif x - (ans * ans) < -1:
            ans

    return ans


class TestMySqrt(unittest.TestCase):

    def test_my_sqrt(self):
        assert my_sqrt(4) == 2


if __name__ == '__main__':

    unittest.main()
