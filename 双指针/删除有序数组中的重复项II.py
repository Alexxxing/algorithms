from typing import List

"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
"""


def remove_duplicates_II(nums: List[int]) -> int:
    n = len(nums)
    slow, fast = 2, 2
    while fast < n:
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


if __name__ == '__main__':
    data = [1, 1, 1, 2, 2, 3]
    assert remove_duplicates_II(data) == 5
