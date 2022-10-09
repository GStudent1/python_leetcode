class Solution:
    def isPowerOfTwo(self, n:int) -> bool:
        if n < 1:
            return False
        if n==1:
            return True
        else :
            return self.isPowerOfTwo(n/2 if n/2)

if __name__ == '__main__':
    result = Solution().isPowerOfTwo(5)
    print(result)

