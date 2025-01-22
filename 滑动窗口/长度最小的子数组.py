"""
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""
from math import inf
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    ans = inf
    n = len(nums)
    l, r = 0, 0
    s = 0
    while r < n:
        s += nums[r]
        while l <= r and s >= target:
            ans = min(ans, r - l + 1)
            s -= nums[l]
            l += 1
        r += 1
    return ans


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(min_sub_array_len(target, nums))
