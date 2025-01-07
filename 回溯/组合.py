"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    ans = []
    tmp = []

    def recur(i):
        if len(tmp) == k:
            ans.append(tmp[:])
            return
        for j in range(i, n + 1):
            tmp.append(j)
            recur(j + 1)
            tmp.pop()
    recur(1)
    return ans


if __name__ == '__main__':
    print(combine(4, 2))
