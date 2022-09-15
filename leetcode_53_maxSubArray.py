from typing import List


def maxSubArray(nums: List[int]) -> int:
    maxlength=0
    curlength=0
    for i in range(len(nums)):
        if maxlength>0:
            curlength=curlength +nums[i]
        else:
            curlength=nums[i]
        if curlength>=0:
            if maxlength< curlength:
                maxlength = curlength
            continue
        else:
            if maxlength< curlength-nums[i]:
                maxlength=curlength-nums[i]
    return maxlength

if __name__ == '__main__':
    s=[-2]
    print(maxSubArray(s))