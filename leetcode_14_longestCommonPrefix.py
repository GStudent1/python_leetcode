from typing import List


def longestCommonPrefix_2(strs: List[str]) -> str:
    prefix=""
    str_line =min(strs)
    for j in range(len(str_line)):
        for str in strs:
            if str_line[j]==str[j]:
                continue
            else:
                return prefix
        prefix = prefix + str_line[j]
    return prefix


if __name__ == '__main__':
    str = ["dog","racecar","car"]
    print(longestCommonPrefix_2(str))

