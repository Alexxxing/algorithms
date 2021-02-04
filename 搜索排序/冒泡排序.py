def bubble_sort(data):
    # 冒泡排序

    n = len(data)
    for i in range(n):
        is_sort = True  # 做标记。当组数已经排好序时，不需要进行后续比较操作，可以直接退出循环
        for j in range(n-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                is_sort = False
        if is_sort:
            break

    return data


if __name__ == '__main__':
    original_list = [91, 2, 4, 5, 11, 6, 19, 3, 29, 7, 1]
    result_list = bubble_sort(original_list)
    print(result_list)
