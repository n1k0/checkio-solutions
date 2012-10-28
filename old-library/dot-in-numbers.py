# The previous version of robots wasn't able to recognize big numbers.
# Write a module that will place a dot every three digits from the end in the
# numbers longer than 4 digits. There is no reason to insert dots in ordinal
# numbers like 1900th.
#
# Input data: string containing number
# Output data: string with dot-separated number

import unittest

def checkio(txt):
    def splitn(t):
        return ('.'.join(partition(t[::-1], 3)))[::-1] if t.isdigit() else t

    def partition(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    return ' '.join(map(splitn, txt.split(' ')))

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio('123456'), '123.456')

    def test_2(self):
        self.assertEquals(checkio('333'), '333')

    def test_3(self):
        self.assertEquals(checkio('9999999'), '9.999.999')

    def test_4(self):
        self.assertEquals(checkio('123456 567890'), '123.456 567.890')

    def test_5(self):
        self.assertEquals(checkio('price is 5799'), 'price is 5.799')

    def test_6(self):
        self.assertEquals(checkio('he was born in 1966th'),
                          'he was born in 1966th')

if __name__ == '__main__':
    unittest.main(failfast=False)
