from typing import List


def remove_duplicates(nums: List[int]) -> int:
    n = len(nums)
    c = 0
    for i in range(n):
        if nums[i] != nums[c]:
            c += 1
            nums[c] = nums[i]
    return c


if __name__ == '__main__':
    data = [1, 1, 2]
    assert remove_duplicates(data) == 2
