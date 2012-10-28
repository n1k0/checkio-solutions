import unittest

def checkio(values):
    a, b = values
    return a if not b else checkio((b, a % b))

class ChekioTest(unittest.TestCase):
    def test_first(self):
        self.assertEquals(checkio((12, 8)), 4)

    def test_second(self):
        self.assertEquals(checkio((14, 21)), 7)

if __name__ == '__main__':
    unittest.main(failfast=False)
