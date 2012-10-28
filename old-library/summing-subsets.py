# Let G(S) denote the sum of the elements of set S and F(n) be the sum of G(s)
# for all subsets of the set consisting of the first n natural numbers.
# For example, F(3) = (1) + (2) + (3) + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24.
# Given n, calculate F(1) + F(2) + ... + F(n)

import unittest

from itertools import combinations

def checkio(n):
    def compute(n):
        rng = xrange(1, n + 1)
        return sum([sum(map(sum, list(combinations(rng, x)))) for x in rng])
    return sum([compute(x) for x in xrange(1, n + 1)])

class ChekioTest(unittest.TestCase):
    def test_first(self):
        self.assertEquals(checkio(2), 7,)

    def test_second(self):
        self.assertEquals(checkio(3), 31)

    def test_third(self):
        self.assertEquals(checkio(1), 1,)

if __name__ == '__main__':
    unittest.main(failfast=False)
