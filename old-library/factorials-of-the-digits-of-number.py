# Calculate sum of the factorials for all digits of the specified positive
# integer number.

import operator
import unittest

def checkio(data):
    total = 0
    for n in map(int, list(str(data))):
        total += 1 if not n else reduce(operator.mul, xrange(1, n + 1))
    return total

class ChekioTest(unittest.TestCase):
    def test_first(self):
        self.assertEquals(checkio(100), 3)

    def test_second(self):
        self.assertEquals(checkio(222), 6)

    def test_third(self):
        self.assertEquals(checkio(1234), 33)

if __name__ == '__main__':
    unittest.main(failfast=False)
