def selection_sort(items):
    """
    选择排序
    :param items: 待排序数组
    """

    for i in range(len(items)):
        max_index = 0
        for j in range(len(items) - i):
            if items[j] > items[max_index]:
                max_index = j
        items[len(items) - 1 - i], items[max_index] = items[max_index], items[len(items) - 1 - i]


if __name__ == '__main__':
    original_list = [1, 91, 2, 4, 5, 33, 11, 6, 56, 19, 3, 29, 7, 1]
    selection_sort(original_list)
    print(original_list)