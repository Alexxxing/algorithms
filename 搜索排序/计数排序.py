def count_sort(items):
    """
    计数排序
    :param items: 待排序数组
    """

    mmax, mmin = items[0], items[0]
    for i in range(len(items)):
        if items[i] < mmin:
            mmin = items[i]
        if items[i] > mmax:
            mmax = items[i]

    nums = mmax - mmin + 1
    count = [0] * nums
    for i in range(len(items)):
        print(items[i] - mmin)
        count[items[i] - mmin] = count[items[i] - mmin] + 1

    print(count)
    pos = 0
    for i in range(nums):
        for j in range(count[i]):
            items[pos] = mmin + i
            pos += 1


if __name__ == '__main__':
    original_list = [1, 57, 2, 4, 5, 33, 11, 6, 56, 19, 3, 29, 7, 1]
    count_sort(original_list)
    print(original_list)
