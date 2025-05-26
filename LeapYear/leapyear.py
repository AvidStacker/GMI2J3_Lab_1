


def to_leap_year(year):
    '''Python program to check if the input year is a leap year or not'''
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Error: value must be a non-boolean integer")
    if year not in range(1, 4000):
        raise IndexError("Index out of range.")
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # leap year
            else:
                return False  # not a leap year
        else:
            return True  # leap year
    else:
        return False  # not a leap year


if __name__ == '__main__':
    to_leap_year(2021)



