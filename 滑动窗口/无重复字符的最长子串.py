def length_of_longest_substring(s: str) -> int:
#     dic, left, ans = {}, -1, 0
#     for i in range(len(s)):
#         if s[i] in dic:
#             left = max(dic[s[i]], left)
#         dic[s[i]] = i
#         ans = max(ans, i - left)
#
#     return ans
    left = 0
    right = 0
    n = len(s)
    if n == 1:
        return n
    ans = 0
    dict_map = {}
    while right < n:
        if s[right] in dict_map:
            print(ans)
            left = max(left, dict_map[s[right]] + 1)
            dict_map[s[right]] = right
        else:
            dict_map[s[right]] = right
        ans = max(ans, right - left + 1)
        right += 1
    return ans


if __name__ == '__main__':
    s = "nfpdmpi"
    print(length_of_longest_substring(s))
