def insertion_sort(items):
    """
    插入排序
    :param items: 待排序数组
    """

    # for i in range(1, len(items)):
    #     sort_index = i
    #     while sort_index > 0 and items[sort_index - 1] > items[sort_index]:
    #         items[sort_index - 1], items[sort_index] = items[sort_index], items[sort_index - 1]
    #         sort_index -= 1
    n = len(items)
    for i in range(1, n):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1


if __name__ == '__main__':
    # original_list = [1, 91, 2, 4, 5, 33, 11, 6, 56, 19, 3, 29, 7, 1]
    original_list = [5,2,3,1]
    insertion_sort(original_list)
    print(original_list)
