# Withdraw without any incident
# 120 - 10 - 0.5 - 1% = 109.4
# 109.4 - 20 - 0.5 - 1% = 88.7
# 88.7 - 30 - 0.5 - 1% = 57.9
#
# Teach Sofia how to use an ATM. The ATM on their home island can give only 5F bills,
# which means that the machine will not give any bill not divisible by 5F.
# In addition to that, the commission for cashing out is 0.5F + 1% from the taken
# out cash plus the robots cannot go beyond the card's balance.
#
# Input: List of decimals. First one denotes Robot's account balance,
# second is a list of money amounts robot want to withdraw.
#
# Output: Account balance after all operations.

import unittest

from decimal import Decimal
from operator import add

def checkio(data):
    balance, withdrawal = data
    withdrawal = filter(lambda x: x < balance and x % 5 == 0, withdrawal)
    if not withdrawal:
        return balance
    withdrawal = map(lambda x: x * Decimal('1.01') + Decimal('.5'), withdrawal)
    total = reduce(add, withdrawal)
    return balance - total if total <= balance else balance

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(Decimal(checkio([Decimal('120'),
            [Decimal('10'), Decimal('20'), Decimal('30')]])), Decimal('57.9'))

    def test_2(self):
        "With one Insufficient Funds, and then withdraw 10 $"
        self.assertEquals(Decimal(checkio([Decimal('120'),
            [Decimal('200'), Decimal('10')]])), Decimal('109.4'))

    def test_3(self):
        "With one incorrect amount"
        self.assertEquals(Decimal(checkio([Decimal('120'),
            [Decimal('3'), Decimal('10')]])), Decimal('109.4'))

    def test_4(self):
        "With another incorrect amount"
        self.assertEquals(checkio([Decimal('120'),
            [Decimal('200'), Decimal('119')]]), Decimal('120'))

if __name__ == '__main__':
    unittest.main(failfast=False)
