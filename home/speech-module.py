# Input: Integer number. From 0 to 1000
#
# Output: String representation of this number
#
# Example:
#
#     checkio(4)=='four'
#     checkio(143)=='one hundred forty three'
#     checkio(12)=='twelve'
#     checkio(101)=='one hundred one'
#     checkio(212)=='two hundred twelve'

import unittest

def checkio(number):
    def under_100(n):
        comp = first20[n % 10]
        comp = comp if comp != "zero" else ""
        return (tens[n / 10] + ' ' + comp).strip()
    first20 = ("zero one two three four five six seven eight nine ten "
               "eleven twelve thirteen fourteen fifteen sixteen seventeen "
               "eighteen nineteen").split(' ')
    tens = (("none none twenty thirty forty fifty sixty seventy eighty ninety")
        .split(' '))
    if number < len(first20):
        return first20[number]
    elif number < 100:
        return under_100(number)
    return "%s hundred %s" % (first20[number / 100], checkio(number % 100),)

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio(4), 'four')

    def test_2(self):
        self.assertEquals(checkio(12), 'twelve')

    def test_3(self):
        self.assertEquals(checkio(101), 'one hundred one')

    def test_4(self):
        self.assertEquals(checkio(133), 'one hundred thirty three')

    def test_5(self):
        self.assertEquals(checkio(212), 'two hundred twelve')

if __name__ == '__main__':
    unittest.main(failfast=False)
