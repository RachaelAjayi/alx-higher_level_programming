#!/ussr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_value = 0

    pre_value = 0

    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)

        if value < pre_value:
            int_value -= value
        else:
            int_value += value

        pre_value = value

    return int_value
