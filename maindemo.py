from typing import List




"""
有效的括号
"""
def isValid(s: str) -> bool:
    if s.count("(") != s.count(")") or s.count("{") != s.count("}") or s.count("[") != s.count("]"):
        return False


"""
两数之和
"""
def twoSum(nums: List[int], target: int) -> List[int]:
    c=[]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i] == target:
                c.append(i)
                c.append(j)
    return c

def twoSum2(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

"""
最小差值 I
"""
def smallestRangeI(nums: List[int], k: int) -> int:
    return max(0,max(nums)-min(nums)-2*k)


if __name__ == '__main__':
    str = [1,3,6]
    print(smallestRangeI(str,3))

"""
最后一个单词的长度
"""
def lengthOfLastWord( s: str) -> int:
    slist=s.split()
    laststr=slist[len(slist)-1]
    return len(laststr)

"""
最长公共前缀
"""
def longestCommonPrefix (strs):
    #以第一个字符串作为参照
    for i in range(len(strs[0])):
        #以第一个字符串的第i个字符作为参照
        temp1 = strs[0][i]
        #循环其他字符串的第i个字符，判断是否与第一个字符串的第i个字符相等，不相等则直接返回temp
        for j in range(1,len(strs)):
            if len(strs[j])==i or strs[j][i] != temp1:
                return strs[0][:i]
    return strs[0]

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

"""
无重复字符的最长子串的长度
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



