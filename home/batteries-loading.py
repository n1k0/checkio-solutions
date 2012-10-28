# Input data: Input contains list of weights of the details.
# Output data: a number representing the minimal possible weight difference
# between details in his each hands.
#
# Example:
#
#     checkio([10, 10]) == 0
#     checkio([10]) == 10
#     checkio([5, 8, 13, 27, 14]) == 3
#     checkio([5, 5, 6, 5]) == 1
#     checkio([12, 30, 30, 32, 42, 49]) == 9

import itertools
import unittest

def best_balance(stoneset):
    balances = []
    for i in xrange(1, len(stoneset)):
        left = stoneset[0:-(len(stoneset) - i)]
        right = stoneset[i:len(stoneset)]
        balances.append(abs(sum(left) - sum(right)))
    return min(balances)

def checkio(stones):
    """ Minimal possible weight difference between stone piles
    """
    if len(stones) == 1:
        return stones[0]
    return min(set(map(best_balance, list(itertools.permutations(stones)))))

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([10, 10]), 0)

    def test_2(self):
        self.assertEquals(checkio([10]), 10)

    def test_3(self):
        self.assertEquals(checkio([5, 8, 13, 27, 14]), 3)

    def test_4(self):
        self.assertEquals(checkio([5, 5, 6, 5]), 1)

    def test_5(self):
        self.assertEquals(checkio([12, 30, 30, 32, 42, 49]), 9)

if __name__ == '__main__':
    unittest.main(failfast=False)
