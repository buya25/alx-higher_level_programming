#!/usr/bin/python3
def roman_to_int_converter(ch):
    """
    converts a roman numeral character into the respective integer
    """
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return roman_values.get(ch, -1)


def convert_roman_to_integer(roman_string):
    """
    converts any string of roman numerals to decimal
    """
    if not isinstance(roman_string, str):
        return 0

    integer_value = 0
    previous_value = 0

    for c in roman_string:
        current_value = roman_to_int_converter(c)
        if current_value == -1:
            return 0

        if current_value > previous_value:
            integer_value += current_value - 2 * previous_value
        else:
            integer_value += current_value
        
        previous_value = current_value

    return integer_value
