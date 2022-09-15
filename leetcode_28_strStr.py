from typing import List


def strStr(haystack: str, needle: str) -> int:
    i=0
    j=0
    index=-1
    for i in range(len(needle)):
        while j < len(haystack):
            if needle[i]==haystack[j]:
                index = j
                j=j+1
                break
            else:
                j = j + 1
    return index

if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack,needle))