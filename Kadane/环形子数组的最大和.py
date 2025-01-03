from math import inf
from typing import List


def max_sub_array_sum_circular(nums: List[int]) -> int:
    n = len(nums)
    dp = [0 for _ in range(n)]
    max_left_list = [0 for _ in range(n)]
    dp[0] = nums[0]
    max_left_list[0] = nums[0]
    for i in range(1, n):
        dp[i] = dp[i - 1] + nums[i]

    for i in range(1, n):
        max_left_list[i] = max(max_left_list[i - 1] + nums[i], nums[i])
    ans = -inf
    right_sum = 0
    for j in range(n - 1, 0, -1):
        right_sum += nums[j]
        if dp[0:j]:
            max_left = max(dp[0:j])
        else:
            max_left = 0
        ans = max(ans, max_left + right_sum)

    return max(ans, max(max_left_list))


if __name__ == '__main__':
    nums = [1, -2, 3, -2]
    max_sub_array_sum_circular(nums)
