def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = len(nums)
    count = 0
    i = 0
    while i < l:
        if nums[i] == val:
            nums.pop(i)
            nums.append("_")
            count += 1
        else:
            i += 1
    return count


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    remove_element(nums, 2)
    print(nums)
