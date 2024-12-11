from collections import defaultdict
from fractions import Fraction


class Operation:

    def __init__(self, op, pri, func):
        self.op = op
        self.pri = pri
        self.func = func

    def cal(self, left, right):
        return self.func(left, right)

    def __ge__(self, other):
        return self.pri >= other.pri

    def __eq__(self, other):
        return self.op == other.op


PLUS = Operation("+", 1, lambda x, y: x + y)
MINS = Operation("-", 1, lambda x, y: x - y)
MULP = Operation("*", 2, lambda x, y: x * y)
DIVD = Operation("/", 2, lambda x, y: Fraction(x, y))
LEFT = Operation("(", 0, lambda x, y: 0)
RIGHT = Operation(")", 0, lambda x, y: 0)
SPAC = Operation(" ", 0, lambda x, y: 0)

OPERATOR_MAP = {
    "+": PLUS,
    "-": MINS,
    "*": MULP,
    "/": DIVD,
    "(": LEFT,
    ")": RIGHT,
    " ": SPAC,
}


class Solution:
    def calculate(self, s):
        ns = []
        op = []
        i = 0
        n = len(s)

        def inc():
            nonlocal i
            i += 1

        def cal():
            r = ns.pop()
            l = ns.pop()
            opr = op.pop()
            ns.append(opr.cal(l, r))

        def nums():
            c = int(s[i])
            inc()
            while i < n and s[i].isdigit():
                c = c * 10 + int(s[i])
                inc()
            ns.append(c)

        def operator():
            c = OPERATOR_MAP[s[i]]
            if op:
                while i < n and op[-1] >= c:
                    cal()
            op.append(c)
            inc()

        def left():
            op.append(OPERATOR_MAP[s[i]])
            inc()

        def right():
            while op[-1] != LEFT:
                cal()
            op.pop()
            inc()

        def space():
            inc()

        mutate = defaultdict(lambda: nums,
            {
                "+": operator,
                "-": operator,
                "*": operator,
                "/": operator,
                "(": left,
                ")": right,
                " ": space,
            }
        )

        while i < n:
            mutate[s[i]]()

        while op:
            cal()

        return ns.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.calculate("(1+(41+5+2)-3)/(6+8)"))
