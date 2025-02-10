"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    dic = set(nums)
    ans = 0
    for i in nums:
        if i - 1 in dic:
            continue
        y = i
        while y in nums:
            y += 1
        ans = max(ans, y - i)
    return ans


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive(nums))
