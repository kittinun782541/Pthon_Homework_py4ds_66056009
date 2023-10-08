"""
Execise 6
"""


def ordinal_suffix(num):
    # Handle special cases: 11th, 12th, 13th
    if 10 < num % 100 < 14:
        return str(num) + 'th'

    # Handle general cases
    last_digit = num % 10
    if last_digit == 1:
        return str(num) + 'st'
    elif last_digit == 2:
        return str(num) + 'nd'
    elif last_digit == 3:
        return str(num) + 'rd'
    else:
        return str(num) + 'th'

    # FIX : complete this
    pass
