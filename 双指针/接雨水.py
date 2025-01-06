"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

"""
from typing import List


def trap(height: List[int]) -> int:
    ans = 0
    n = len(height)
    left = [0] * n
    right = [0] * n
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i - 1])
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i + 1])

    for i in range(1, n - 1):
        min_binary = min(left[i], right[i])
        if min_binary > height[i]:
            ans += min_binary - height[i]

    return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))
