def generate_parenthesis(n):
    """
    给定括号的个数，求括号的合规组合结果
    :param n: 括号的个数
    """
    # 第一种解
    def generate_list(prefix, left, right, parens=[]):
        tmp = prefix[:]
        if right == 0:
            parens.append(prefix)
        if left > 0:
            tmp.append('(')
            generate_list(tmp, left - 1, right)
            tmp.pop()
        if right > left:
            tmp.append(')')
            generate_list(tmp, left, right - 1)
        return parens

    # 第二种解
    def generate_string(prefix, left, right, parens=[]):
        if right == 0:
            parens.append(prefix)
        if left > 0:
            generate_string(prefix + '(', left - 1, right)
        if right > left:
            generate_string(prefix + ')', left, right - 1)
        return parens

    return generate_list([], n, n)  # 返回列表形式
    # return generate_string('', n, n)  # 返回字符串形式


if __name__ == '__main__':
    print(generate_parenthesis(3))
