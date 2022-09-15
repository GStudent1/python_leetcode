def romanToInt(s: str) -> int:
    dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                  "CD": 400, "CM": 900}
    sum = 0
    i = 0
    while i < len(s):
        if s[i:i + 2] in dict_roman:
            sum = sum + dict_roman[s[i:i + 2]]
            i += 2
        else:
            sum = sum + dict_roman[s[i:i + 1]]
            i += 1
    return sum

if __name__ == '__main__':
    str='IX'
    print(romanToInt(str))


