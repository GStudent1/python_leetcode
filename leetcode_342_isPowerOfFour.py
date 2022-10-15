class Solution:
    def isPowerOfFour(self, n) -> bool:
        if n==1:
            return True
        elif n < 1 or n==2 or n==3 :
            return False
        else:
            return self.isPowerOfFour(n/4)

if __name__ == '__main__':
    result = Solution().isPowerOfFour(27)
    print(result)

