def length_of_longest_substring(s: str) -> int:
    dic, left, ans = {}, -1, 0
    for i in range(len(s)):
        if s[i] in dic:
            left = max(dic[s[i]], left)
        dic[s[i]] = i
        ans = max(ans, i - left)

    return ans


if __name__ == '__main__':
    s = "pwwkew"
    print(length_of_longest_substring(s))
