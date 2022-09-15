from typing import List


def mySqrt(x: int) -> int:
    y=0
    while y <= x:
        if y ** 2 == x:
            return y
        elif y **2 < x and (y+1) **2 > x :
            return y
        else:
            y+=1

if __name__ == '__main__':
    list_demo=1
    print(mySqrt(list_demo))
    #print(2**31)