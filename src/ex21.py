"""
Exercise 21 : Validate Date
"""



def is_valid_date(year, month, day):
    from src.ex20 import is_leap_year
    if not (1 <= month <= 12):
        return False
    if is_leap_year(year) and month == 2 and day == 29:
        return True
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False
    if month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False
    if month == 2 and not (1 <= day <= 28):
        return False
    return True
    # FIX: complete this
    pass
