import random
from typing import List


def quick_sort(data, start, end):
    # 快速排序

    # 判断游标是否重叠, 若重叠则不需要再排序
    if start >= end:
        return
    # 记录初始位置数据
    marked = data[start]

    # 记录起始位置与结束位置
    low = start
    high = end

    # 直到 start 和 end 重合之前一直进行排序操作
    while low < high:
        # 从右至左找出一个比此时 low 游标指定数据小的值, 直至找到为止
        while low < high and data[high] >= marked:
            high -= 1
        data[low] = data[high]
        # 从左至右找出一个比此时 high 游标指定数据大的值, 直至找到为止
        while low < high and data[low] < marked:
            low += 1
        data[high] = data[low]

    # 讲记录的初始位置数据还原到 low 游标对应位置，此时 low 与 high 相遇
    data[low] = marked

    # 重复讲前半段和后半段分别进行排序
    quick_sort(data, start, low - 1)
    quick_sort(data, low + 1, end)


def sortArray(nums: List[int]) -> List[int]:

    def quick_sort(data, start, end):

        if start > end:
            return
        low = start
        high = end
        random_num = random.randint(start, end)
        tag = data[random_num]
        data[low], data[random_num] = data[random_num], data[low]
        while low < high:
            while low < high and data[high] > tag:
                high -= 1
            data[low] = data[high]
            while low < high and data[low] <= tag:
                low += 1
            data[high] = data[low]

        data[low] = tag

        if high == end:
            while high > 0 and nums[high] == nums[high - 1]:
                high -= 1
            quick_sort(data, start, high - 1)
        else:
            quick_sort(data, start, low - 1)
            quick_sort(data, low + 1, end)

    quick_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    # original_list = [91, 2, 4, 5, 11, 6, 19, 3, 29, 7, 1]
    original_list = [4, 2, 1, 5, 3]
    # quick_sort(original_list, 0, len(original_list) - 1)
    sortArray(original_list)
    print(original_list)
