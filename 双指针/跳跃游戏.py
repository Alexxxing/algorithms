from typing import List


"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
"""


def can_jump(nums: List[int]) -> bool:
    max_jump = 0
    for i in range(len(nums)):
        if i > max_jump:
            return False
        max_jump = max(max_jump, nums[i] + i)
    return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    assert can_jump(nums)
