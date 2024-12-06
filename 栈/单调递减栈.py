def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # 单调递减栈

    for i in range(n):
        # 如果当前元素比栈顶元素大，更新栈顶元素的结果
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)  # 压入当前元素的索引

    return result


if __name__ == '__main__':
    nums = [2, 1, 2, 4, 3]
    print(next_greater_elements(nums))
