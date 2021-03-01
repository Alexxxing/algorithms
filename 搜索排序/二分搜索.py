def binary_search(alist, item):
    """
    二分搜索, 找出alist中最第一个item的位置
    :param alist: 带搜索且已排好序数组
    :param item: 查询对象
    """

    if len(alist) == 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            right = mid
        if alist[mid] < item:
            left = mid
        if alist[mid] > item:
            right = mid

    if alist[left] == item:
        return left
    if alist[right] == item:
        return right

    return -1


if __name__ == '__main__':
    original_list = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
    result = binary_search(original_list, 2)
    print(result)
