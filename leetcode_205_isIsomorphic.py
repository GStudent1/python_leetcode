"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i=0
        while i < len(s):
            if s.count(s[i],i) == t.count(t[i],i):
                if s.count(s[i],i)==1:
                    i+=1
                    continue
                elif self.loc(i,s,t):
                    i += 1
                    continue
                else:
                    return False
            else:
                return False
        else:
            return True

    def loc(self, i,s: str,t:str):
        list_s=list(s)
        indexs_i=list_s[i]
        list_t = list(t)
        indext_i = list_t[i]
        count=t.count(t[i],i)
        k=0
        while k < count:
            if list_s.index(indexs_i,i)==list_t.index(indext_i,i):
                list_s.remove(list_s[list_s.index(indexs_i,i)])
                list_t.remove(list_t[list_t.index(indext_i,i)])
                k+=1
            else:
                return False
        return True

if __name__ == '__main__':
    s="egg"
    t="add"
    sol=Solution()
    print(sol.isIsomorphic(s,t))