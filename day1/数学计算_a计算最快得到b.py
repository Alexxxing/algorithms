def int_seq(a, b):
    """
    数学表达式：给定 a <= b , a 经过一系列转换(a + 1 或 a * 2)得到 b, 求最快的方法
    """
    if a == b:
        return str(a)

    if b % 2 == 1:
        return '( ' + int_seq(a, b - 1) + ' + 1 )'
    if b < a * 2:
        return '( ' + int_seq(a, b - 1) + ' + 1 )'

    return int_seq(a, b/2) + ' * 2 '


if __name__ == '__main__':
    math_work = int_seq(5, 101)
    print('113={}'.format(math_work))