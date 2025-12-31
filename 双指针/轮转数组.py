"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]


提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(num: List[int]) -> List[int]:
        m, n = 0, len(num) - 1
        while m < n:
            num[m], num[n] = num[n], num[m]
            m += 1
            n -= 1
        return num

    k = k % len(nums)
    reverse(nums)
    nums[0: k] = reverse(nums[0: k])
    nums[k:] = reverse(nums[k:])


if __name__ == '__main__':
    nums = [1, 2]
    rotate(nums, 7)
    print(nums)
