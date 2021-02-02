def sub_set(numbers):
    """
    计算所有子集
    :param numbers: 给定的不重复的元素列表，例如[1, 2, 3]
    """
    result = [[]]
    for num in numbers:
        for element in result[:]:
            tmp = element[:]
            tmp.append(num)
            result.append(tmp)

    return result


def subsets_recursive(nums):
    """
    回溯
    :param nums: 待搜索数组
    """
    lst = []
    result = []
    subsets_recursive_helper(result, lst, nums, 0)
    return result


def subsets_recursive_helper(result, lst, num, pos):
    """
    :param result: 返回结果
    :param lst: 中间结果
    :param num: 待搜索数组
    :param pos: 起始位置
    """
    result.append(lst[:])
    for i in range(pos, len(num)):
        lst.append(num[i])
        subsets_recursive_helper(result, lst, num, i+1)
        lst.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(sub_set(nums))
    print(subsets_recursive(nums))