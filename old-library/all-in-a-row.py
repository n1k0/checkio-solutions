import unittest

def checkio(arr):
    f = []
    [f.extend(checkio(l)) if isinstance(l, list) else f.append(l) for l in arr]
    return f


class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([1, 2, 3]), [1, 2, 3])

    def test_2(self):
        self.assertEquals(checkio([1, [2, 2, 2], 4]), [1, 2, 2, 2, 4])

    def test_3(self):
        self.assertEquals(checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]),
                                  [2, 4, 5, 6, 6, 6, 6, 6, 7])

if __name__ == '__main__':
    unittest.main(failfast=False)
