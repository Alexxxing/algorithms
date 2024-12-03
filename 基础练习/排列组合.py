import random
from itertools import permutations

if __name__ == '__main__':
    input_words = input("Enter the list(split by 、):")
    result_nums = input("Enter the result nums you need:")
    # 分隔生成列表
    words_list = input_words.split("、")
    # 进行排列组合，生成排列组合结果
    perm = list(permutations(words_list))
    # 随机取出所需个数的排列组合结果
    random_result_list = random.sample(perm, int(result_nums))
    # 每个排列组合结果根据所需个数取出随机个数元素
    for result in random_result_list:
        random_elements_nums = random.randint(1, len(result))
        random_elements_result = random.sample(result, random_elements_nums)
        # 打印结果
        print("、".join(random_elements_result))
