from typing import List


def removeElement(nums: List[int], val: int):
    i=0
    if nums.count(val)==0:
        return len(nums)
    while i < nums.count(val):
        nums.remove(val)
    return (nums,len(nums))

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3]
    print(removeElement(nums,1))