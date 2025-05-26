import unittest
import roman

class TestToRomanGoodInput(unittest.TestCase):
    known_values = [
        (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'),
        (5, 'V'), (6, 'VI'), (9, 'IX'), (10, 'X'),
        (20, 'XX'), (30, 'XXX'), (40, 'XL'), (50, 'L'),
        (60, 'LX'), (90, 'XC'), (100, 'C'), (200, 'CC'),
        (300, 'CCC'), (400, 'CD'), (500, 'D'), (600, 'DC'),
        (900, 'CM'), (1000, 'M'), (2000, 'MM'), (3000, 'MMM'),
        (44, 'XLIV'), (49, 'XLIX'), (99, 'XCIX'), (399, 'CCCXCIX'),
        (444, 'CDXLIV'), (944, 'CMXLIV'), (999, 'CMXCIX'),
        (1492, 'MCDXCII'), (1987, 'MCMLXXXVII'), (2023, 'MMXXIII'),
        (2421, 'MMCDXXI'), (2999, 'MMCMXCIX'), (3888, 'MMMDCCCLXXXVIII'),
        (3999, 'MMMCMXCIX')
    ]

    def test_to_roman(self):
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)

class TestToRomanBadInput(unittest.TestCase):
    def test_invalid_inputs(self):
        '''Should raise TypeError for invalid non-integer inputs and invalid character strings'''

        # Invalid non-integer types
        bad_inputs = [
            [], {}, (), set(), True, False, complex(1, 1), b'X', bytearray(b'X'),
            'a', 'b', 'z', '1', 'x', 'L', 'M', '@#$', 'I V', '123', 'xyz', 'ABC',
            '', 'hello', '12abc', '1000m', 'IXIX'
        ]
        
        for bad_input in bad_inputs:
            with self.assertRaises(TypeError):
                roman.to_roman(bad_input)
                
    def test_out_of_range(self):
        '''Should raise IndexError for inputs out of range'''
        for value in (0, -1, 4000, 10000):
            self.assertRaises(IndexError, roman.to_roman, value)

class TestFromRomanGoodInput(unittest.TestCase):
    known_values = TestToRomanGoodInput.known_values

    def test_from_roman(self):
        for integer, numeral in self.known_values:
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class TestFromRomanBadInput(unittest.TestCase):
    def test_invalid_inputs(self):
        '''Should raise TypeError for non-string inputs'''
        # Non-string invalid inputs
        bad_inputs = [
            10, None, 3.5, True, False, [], {}, set(), complex(1, 1), bytearray(b'X'),
            b'X'  # Byte strings, which aren't valid Roman numerals
        ]
        for bad_input in bad_inputs:
            self.assertRaises(TypeError, roman.from_roman, bad_input)

    def test_invalid_strings(self):
        '''Should raise ValueError for invalid Roman numerals'''
        invalid_strings = [
            'INVALID', '', 'MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII',
            'CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV',
            'IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
            'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'
        ]
        for string in invalid_strings:
            self.assertRaises(ValueError, roman.from_roman, string)

class TestRoundtrip(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n)) == n for all n in valid range'''
        for integer in range(1, 4000):
            numeral = roman.to_roman(integer)
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()
