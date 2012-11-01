# Number of keypresses to send an SMS. Keyboard layout:
#
#  1   2   3
# abc def ghi
#  4   5   6
# jkl mno pqr
#  7   8   9
# stu vwx yz
#  0   #
# .,!  _

from itertools import cycle, izip
import unittest

def checkio(line):
    keys = dict(izip("abcdefghijklmnopqrstuvwxyz|.,! ", cycle([1, 2, 3])))
    return sum([keys[c] for c in line])

class ChekioTest(unittest.TestCase):
    def test_first(self):
        self.assertEquals(checkio('diamonds are forever'), 38)

    def test_second(self):
        self.assertEquals(checkio('just do it'), 18)

    def test_third(self):
        self.assertEquals(checkio('tastes great, less filling'), 48)

if __name__ == '__main__':
    unittest.main(failfast=False)
