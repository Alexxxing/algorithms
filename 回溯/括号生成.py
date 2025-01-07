"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""


def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    tmp = []

    def recur(open):
        if len(tmp) == 2*n:
            ans.append("".join(tmp))
            return
        if open < n:
            tmp.append("(")
            recur(open + 1)
            tmp.pop()
        if (len(tmp) - open) < open:
            tmp.append(")")
            recur(open)
            tmp.pop()
    recur(0)
    return ans


if __name__ == '__main__':
    print(generate_parenthesis(3))
