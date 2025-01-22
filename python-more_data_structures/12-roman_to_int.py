#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    if roman_string is None or not str(roman_string):
        return 0
    for char in reversed(roman_string):
        value = roman_to_int[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
