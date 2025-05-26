import unittest
import leapyear

class TestGoodInput(unittest.TestCase):
    '''Your Abc unittests code goes here'''
    def test_valid_leap_years(self):
        leap_years = [2000, 2016, 2020, 2024]

        for year in leap_years:
            with self.subTest(year=year):
                self.assertTrue(leapyear.to_leap_year(year))

    def test_valid_non_leap_years(self):
        non_leap_years = [1900, 2017, 2019, 2023]

        for year in non_leap_years:
            with self.subTest(year=year):
                self.assertFalse(leapyear.to_leap_year(year))

    def test_boundary_values(self):
        self.assertFalse(leapyear.to_leap_year(1))     # Min edge
        self.assertTrue(leapyear.to_leap_year(4))      # First actual leap year
        self.assertTrue(leapyear.to_leap_year(3996))   # Near upper edge
        self.assertFalse(leapyear.to_leap_year(3999))  # Upper edge, not leap

class TestBadInput(unittest.TestCase):
    def test_invalid_leapyears(self):
        invalid_inputs = ["hej", "", "2020", 3.14, None, True, [2020], {"year": 2020}, (2020,), b"2020"]

        for invalid in invalid_inputs:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    leapyear.to_leap_year(invalid)

    def test_out_of_range_values(self):
        with self.assertRaises(IndexError):
            leapyear.to_leap_year(0)
        with self.assertRaises(IndexError):
            leapyear.to_leap_year(4000)
        with self.assertRaises(IndexError):
            leapyear.to_leap_year(-44)
        with self.assertRaises(IndexError):
            leapyear.to_leap_year(9999)

    def test_boolean_input(self):
        # Booleans are technically ints in Python (True == 1, False == 0)
        with self.assertRaises(TypeError):
            leapyear.to_leap_year(True)

        with self.assertRaises(TypeError):
            leapyear.to_leap_year(False)


if __name__ == '__main__':
    unittest.main()
