class Solution:
    def isPowerOfThree(self, n) -> bool:
        if n==1:
            return True
        elif n < 1 and n==2:
            return False
        else:
            return self.isPowerOfThree(n/3)

if __name__ == '__main__':
    result = Solution().isPowerOfThree(27)
    print(result)

