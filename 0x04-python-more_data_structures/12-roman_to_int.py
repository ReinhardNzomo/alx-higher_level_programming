#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    num = len(roman_string) - 1
    val_int = romans[roman_string[num]]

    for x in range(num, 0, -1):
        cur_val = romans[roman_string[x]]
        left_val = romans[roman_string[x - 1]]

        if left_val >= cur_val:
            val_int += left_val
        else:
            val_int -= left_val
    return val_int
