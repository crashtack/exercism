def is_leap_year(year):
    """Returns True if the inputed year is a leap year"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
