"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        temp={}
        left=0
        right=0
        for i in range(len(s)):
            right=i
            while s[right] not in s[i:right]:
                right=right+1
            if length<len(s[i:right]):
                length=len(s[i:right])
        return length


    def lengthOfLongestSubstring2(self, s: str) -> int:
        left=0
        right=0
        length=0
        for i in range(1,len(s)):
            right=i
            if s[i] in s[left:right]:
                left=s.find(s[i],left,right)+1
            if len(s[left:right+1]) > length:
                length=len(s[left:right+1])
        return  length

if __name__ == '__main__':
    s="abcabcbb"
    sol=Solution()
    print(sol.lengthOfLongestSubstring2(s))