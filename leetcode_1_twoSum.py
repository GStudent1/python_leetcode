"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def __init__(self):
        self.nums=[]
        self.target=0

    #循环遍历，暴力解法
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    #找出target - nums[i]的差值，返回其下标
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp != nums[i] and nums.count(temp) > 0 or temp == nums[i] and nums.count(temp) >= 2:
                loc = nums.index(temp,i + 1, len(nums))
                return [i, loc]
        return []

    # 找出target - nums[i]的差值，返回其下标
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:len(nums)]:
                loc = nums.index(temp,i + 1, len(nums))
                return [i, loc]
        return []

    # 找出nums存在字典里，在字典里找到该差值，返回其下标
    def twoSum4(self,nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

    def twoSum_re(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = target - i
            if num in nums[i + 1:]:
                j = nums[i + 1:].index(num)
                j=nums.index(num,i+1)
                return [i, i + 1 + j]

if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    sol=Solution()
    #print(sol.twoSum1(nums, target))
    #print(sol.twoSum2(nums, target))
    #print(sol.twoSum3(nums, target))
    #print(sol.twoSum4(nums, target))
    print(sol.twoSum_re(nums,target))

