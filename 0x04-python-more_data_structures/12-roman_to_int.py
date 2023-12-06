#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "x": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    int_Numb = 0

    for x in range(len(roman_string)):
        if roman_dict.get(roman_string[x], 0) == 0:
            return (0)

        if (x != (len(roman_string) - 1) and
                roman_dict[roman_string[x]] < roman_dict[roman_string[x + 1]]):
                int_Numb += roman_dict[roman_string[x]] * -1

        else:
            int_Numb += roman_dict[roman_string[x]]
    return (int_Numb)
