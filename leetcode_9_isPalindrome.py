class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        listx = list(str(x))
        listreverx = listx[:]
        listreverx.reverse()
        print(listx)
        print(listreverx)
        if listx == listreverx:
            return True
        return False

    def isPalindrome_demo(self, x: int) -> bool:
        list_Palindrome=list(str(x))
        x_copy=list_Palindrome.copy()
        x_copy.reverse()
        if list_Palindrome == x_copy:
            return True
        return False
if __name__ == '__main__':
    s = 123321
    sol = Solution()
    print(sol.isPalindrome_demo(s))
