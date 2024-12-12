def longest_palindrome(s: str) -> str:
    ans = ''
    for i in range(len(s)):
        l_start = max(i - len(ans) - 1, 0)
        temp = s[l_start:i + 1]
        if temp[:] == temp[::-1]:
            ans = temp
        else:
            temp = temp[1:]
            if temp[:] == temp[::-1]:
                ans = temp
    return ans


if __name__ == '__main__':
    print(longest_palindrome("abaabbdkacaa"))
