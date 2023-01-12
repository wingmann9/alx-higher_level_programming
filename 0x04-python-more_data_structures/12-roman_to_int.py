#!/usr/bin/python3

# Function converts roman numerals to integer
def roman_to_int(roman_string):

    # Ensuring it is not an empty string
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    # create a roman numeral dictionary
    roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    num = 0
    # iterate roman_string and return its value in roman_num
    for i in range(len(roman_string)):
        if roman_num.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_num[roman_string[i]] < roman_num[roman_string[i + 1]]):
            num += roman_num[roman_string[i]] * -1
        else:
            num += roman_num[roman_string[i]]
    return (num)
