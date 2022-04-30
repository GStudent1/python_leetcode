"""
最长的回文子串
"""


def longestPalindrome(s: str) -> str:
    temp = ''
    for i in range(len(s)):
        index=s.find(i,i+1,len(s))
        if index==-1:
            continue
        elif len(temp) < len(s[i:index + 1]):
            a = s[i:index + 1]
            j = len(a) - 1
            tempone = ''
            while j >= 0:
                tempone = tempone + a[j]
                j = j - 1
            if a == tempone:
                temp = a
        return temp



def rever(s: str):
    temp = ''
    i = len(s) - 1
    while i >= 0:
        temp = temp + s[i]
        i = i - 1
    return temp


if __name__ == '__main__':
    s = "abba"
    #a=s[-4:-3]
    a = longestPalindrome(s)
    print(a)

"""
重复字符的最长子串的长度
"""


def lengthOfLongestSubstring1(s: str) -> int:
    list = {}
    length = 0
    left = -1
    right = 0
    for i in range(len(s)):
        if s[i] not in list:
            list[s[i]] = i
        else:
            left = max(list.get(s[i]), left)
            list[s[i]] = i
        right = i
        if right - left > length:
            length = right - left
    return length


def lengthOfLongestSubstring2(s: str) -> int:
    length = 0
    left = 0
    right = 0
    for i in range(len(s)):
        if s.find(s[i], left, right) == -1:
            pass
        else:
            left = max(s.find(s[i], left, right) + 1, left)
        right = right + 1
        if right - left > length:
            length = right - left
    return length


def lengthOfLongestSubstring3(s: str):
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans
