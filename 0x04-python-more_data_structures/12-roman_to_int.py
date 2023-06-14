#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    result = 0
    prev_value = 0

    for symbol in roman_string[::-1]:
        if symbol not in roman_values:
            return (0)
        current_value = roman_values[symbol]

        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value

        prev_value = current_value
    return (result)
