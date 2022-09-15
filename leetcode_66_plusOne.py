from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[len(digits)-1] < 9:
        digits[len(digits) - 1]=digits[len(digits)-1]+1
    else:
        i = len(digits) - 1

        while i >= 0:
            if digits[i] + 1 == 10 and i > 0:
                digits[i]=0
                i=i-1
            elif digits[i] + 1 == 10 and i == 0:
                digits[i] = 0
                list_temp = [1]
                return list_temp + digits
            else:
                digits[i]=digits[i]+1
                break
    return digits

if __name__ == '__main__':
    list_demo=[9,9,9]
    print(plusOne(list_demo))