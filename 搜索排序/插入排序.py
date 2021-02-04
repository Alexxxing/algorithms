def insertion_sort(items):
    """
    插入排序
    :param items: 待排序数组
    """

    for i in range(1, len(items)):
        sort_index = i
        while sort_index > 0 and items[sort_index - 1] > items[sort_index]:
            items[sort_index - 1], items[sort_index] = items[sort_index], items[sort_index - 1]
            sort_index -= 1


if __name__ == '__main__':
    original_list = [1, 91, 2, 4, 5, 33, 11, 6, 56, 19, 3, 29, 7, 1]
    insertion_sort(original_list)
    print(original_list)
