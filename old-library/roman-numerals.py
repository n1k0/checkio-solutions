# Your task is to return roman numeral using the specified integer value from
# range 1...3999.

import unittest

ROMANS = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"),
    (4, "IV"), (1, "I"))

def checkio(number):
    roman = ''
    for value, char in ROMANS:
        rest = number % value
        if number != rest:
            roman += (number / value) * char + checkio(rest)
            break
    return roman


class ChekioTest(unittest.TestCase):
    def test_first(self):
        self.assertEquals(checkio(6), 'VI',)

    def test_second(self):
        self.assertEquals(checkio(76), 'LXXVI',)

    def test_third(self):
        self.assertEquals(checkio(499), 'CDXCIX',)

    def test_fourth(self):
        self.assertEquals(checkio(3888), 'MMMDCCCLXXXVIII',)

if __name__ == '__main__':
    unittest.main(failfast=False)
