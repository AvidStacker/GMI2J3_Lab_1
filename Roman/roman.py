import regex as re


def to_roman(value):
    # Check for boolean type explicitly
    if isinstance(value, bool):
        raise TypeError("Error: value must be of type int, not bool")

    if not isinstance(value, int):
        raise TypeError("Error: value must be of type int")
    
    if value not in range(1, 4000):
        raise IndexError("Index out of range. Value must be in range 1 to 3999")
    
    roman_numeral_map = (('M', 1000),
                        ('CM', 900),
                        ('D', 500),
                        ('CD', 400),
                        ('C', 100),
                        ('XC', 90),
                        ('L', 50),
                        ('XL', 40),
                        ('X', 10),
                        ('IX', 9),
                        ('V', 5),
                        ('IV', 4),
                        ('I', 1)) 

    result = '' 
    for numeral, integer in roman_numeral_map:
        while value >= integer:
            result += numeral
            value -= integer
    return result



def from_roman(string):
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if string == '':
        raise ValueError("Input cannot be blank")
    
    roman_numeral_pattern = re.compile('''
        ^M{0,3}
        (CM|CD|D?C{0,3})
        (XC|XL|L?X{0,3})
        (IX|IV|V?I{0,3})$
    ''', re.VERBOSE)
    
    if not roman_numeral_pattern.search(string):
        raise ValueError('Invalid Roman numeral: {0}'.format(string)) 

    roman_numeral_map = (
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    )

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while string[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
