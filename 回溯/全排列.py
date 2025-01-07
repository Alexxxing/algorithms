"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    tmp = []
    used = [False] * n

    def recur():
        if len(tmp) == len(nums):
            ans.append(tmp[:])
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                tmp.append(nums[i])
                recur()
                tmp.pop()
                used[i] = False
    recur()
    return ans


if __name__ == '__main__':
    num = [1, 2, 3]
    print(permute(num))
