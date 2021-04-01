def count_func(items):
    """
    :param items: 待计数数组（给你一个字符串，"123123412345"，按出现次数给它们重新打印，
    如果出现次数相同则按原来的顺序打印，结果示例"111222333445"）
    """
    if len(items) == 0:
        return None
    item_dict = {}
    for i in items:
        if i in item_dict:
            item_dict[i] += 1
        else:
            item_dict[i] = 1
    item_dict = sorted(item_dict.items(), key=lambda item: item[1], reverse=False)
    result_data = ''
    for count_info in item_dict:
        for i in range(count_info[1]):
            result_data += str(count_info[0])
    return result_data


if __name__ == '__main__':
    original_list = [99, 1, 2, 3, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]
    result = count_func(original_list)
    print(result)
