from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for num in nums:
                if num > target:
                    return nums.index(num)
            else:
                return len(nums)

if __name__ == '__main__':
    str1 = [1,3,5,6]
    target = 7
    sol=Solution()
    list_print=sol.searchInsert(str1,target)
    print(list_print)

