def simple_custom_pow(a, n):
    """
    快速指数，快速计算a^n结果(for循环)
    :param a: 指数
    :param n: 幂
    """
    p = 1
    for i in range(n):
        p *= a
    return p


def recursion_custom_pow(a, n):
    """
    快速指数，快速计算a^n结果(递归)
    :param a: 指数
    :param n: 幂
    """
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * recursion_custom_pow(a, n - 1)


def fast_custom_pow(a, n):
    """
    快速指数，快速计算a^n结果(递归)
    :param a: 指数
    :param n: 幂
    """
    if n <= 0:
        return 1
    elif n == 1:
        return a
    elif n % 2:
        return fast_custom_pow(a * a, n // 2) * a
    else:
        return fast_custom_pow(a * a, n // 2)


if __name__ == '__main__':
    result = fast_custom_pow(5, 3)
    print(result)
