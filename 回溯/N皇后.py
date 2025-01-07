"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

示例 1：

输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
'.Q..'
'...Q'
'Q...'
'..Q.'

'..Q.'
'Q...'
'...Q'
'.Q..'
"""


def total_n_queens(n: int) -> int:
    ans = []
    queue = [0] * n
    col = [False] * n
    tag1 = [False] * 2 * n
    tag2 = [False] * 2 * n

    def recur(r):
        if r == n:
            ans.append(["." * c + "Q" + "." * (n - c - 1) for c in queue])
            return
        for c, ok in enumerate(col):
            if not ok and not tag1[r + c] and not tag2[r - c]:
                queue[r] = c
                col[c] = tag1[r + c] = tag2[r - c] = True
                recur(r + 1)
                col[c] = tag1[r + c] = tag2[r - c] = False
    recur(0)
    return len(ans)


if __name__ == '__main__':
    print(total_n_queens(4))
