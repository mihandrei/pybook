def leap_years_util(y):
    """ leap years in the interval [1, y[ """
    # Every 4 years we count one. Every 100 years we should have not counted. Except every 400
    return y / 4 - y / 100 + y / 400


def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0


def str_dow(dow):
    return ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][dow]


def yan1(y):
    # year 1 starts sunday
    # every normal year moves 1 jan by a week day. leaps move it by 2
    ly = leap_years_util(y)
    #  (6 + (y - ly) + ly * 2) % 7
    return (y + ly - 1) % 7


def day_of_year(y, m, d):
    """which day of the year is this"""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        days_in_month[1] = 29
    passed = d
    for i in range(m - 1):
        passed += days_in_month[i]
    return passed


def day_of_week(y, m, d):
    """prints the day of the week that date falls on"""
    return (yan1(y) + day_of_year(y, m, d) - 1) % 7


print str_dow(day_of_week(2014, 2, 10))
