results = set()
keys = set()


def perm_letter(word, rule):
    """
    传入一个Word， 并传入规则Rule，将Word中含有Rule的字符大写并得到所有组合
    例如传入 word : medium-one | rule: 'io'
    得到结果 result : ['medium-one', 'medIum-one', 'medium-One', 'medIum-One']
    :param word: 待处理字符
    :param rule: 规则
    """
    rule = rule.lower()
    for i in rule:
        keys.add(i)
    perm_letter_helper(word, rule, 0, '')


def perm_letter_helper(word, rule, index, prefix):
    length = len(word)

    for i in range(index, length):
        c = word[i]
        if c in keys:
            perm_letter_helper(word, rule, i + 1, prefix + c)
            c = c.upper()
            perm_letter_helper(word, rule, i + 1, prefix + c)
        else:
            prefix += c
    if len(prefix) == len(word):
        results.add(prefix)


if __name__ == '__main__':
    word = 'medium-one'
    rule = 'io'
    perm_letter(word, rule)
    print(results)
