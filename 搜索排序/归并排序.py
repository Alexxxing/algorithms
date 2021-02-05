def _merge(a, b):
    """
    合并，将最小单元的两个数组进行排序合并
    :param a: 数组a
    :param b: 数组b
    """
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def _merge_sort(nums):
    """
    归并排序
    将待排序数组拆分成多个最小单元
    :param nums: 待排序数组
    """
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    a = _merge_sort(nums[:m])
    b = _merge_sort(nums[m:])
    return _merge(a, b)


def merge_sort(nums, reverse=False):
    nums = _merge_sort(nums)
    if reverse:
        nums = nums[::-1]

    return nums


if __name__ == '__main__':
    original_list = [91, 2, 4, 5, 11, 6, 19, 3, 29, 7, 1]
    result_list = merge_sort(original_list, reverse=True)
    print(result_list)
