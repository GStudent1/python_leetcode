from typing import List


def removeDuplicates(nums: List[int]) :
    i=0
    for j in range(len(nums)):
        if nums[j] not in nums[0:i]:
            nums[i]=nums[j]
            i=i+1
    return len(nums[0:i])

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3]
    print(removeDuplicates(nums))