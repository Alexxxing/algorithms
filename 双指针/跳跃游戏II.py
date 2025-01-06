"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


"""
from typing import List


def jump(nums: List[int]) -> int:
    ans = 0
    end = 0
    m = 0
    for i in range(len(nums) - 1):
        m = max(m, nums[i] + i)
        if i == end:
            end = m
            ans += 1

    return ans


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
