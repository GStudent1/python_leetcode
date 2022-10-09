"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def isPalindrome(self, s: str) ->bool:
        strtemp=''
        for i in s:
            if i.isalnum():
                strtemp=strtemp+i.lower()
        listrever=list(strtemp)
        listtemprever=listrever[:]
        listtemprever.reverse()
        if listrever==listtemprever:
            return True
        return False

    def isPalindrome_guanfang(self, s: str) ->bool:
        strtemp="".join(st.lower() for st in s if st.isalnum())
        return strtemp==strtemp[::-1]

    def isPalindrome_guanfang_shuangzhizhen(self, s: str) ->bool:
        strtemp="".join(st.lower() for st in s if st.isalnum())
        left=0
        right=len(strtemp)-1
        while left < right:
            if strtemp[left]==strtemp[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        else:
            return True




if __name__ == '__main__':
    s=" "
    sol=Solution()
    print(sol.isPalindrome_guanfang_shuangzhizhen(s))