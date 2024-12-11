def add_binary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    list_a = [int(_) for _ in a]
    list_b = [int(_) for _ in b]

    def insert_list(nums, max_length):
        length = len(nums)
        for i in range(max_length - length):
            nums.insert(0, 0)

    insert_list(list_a, max_len + 1)
    insert_list(list_b, max_len + 1)
    add_one = 0

    while max_len >= 0:
        a_n = list_a[max_len]
        b_n = list_b[max_len]
        if a_n + b_n + add_one < 2:
            list_a[max_len] = a_n + b_n + add_one
            add_one = 0
        else:
            list_a[max_len] = (a_n + b_n + add_one) % 2
            add_one = 1
        max_len -= 1

    if not list_a[0]:
        list_a.pop(0)

    return "".join([str(_) for _ in list_a])


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(add_binary(a, b))
