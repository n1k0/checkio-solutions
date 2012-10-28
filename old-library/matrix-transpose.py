import unittest

def checkio(matr):
    return map(list, zip(*matr))

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([[1, 2],
                                   [1, 2]]), [[1, 1],
                                              [2, 2]])

    def test_2(self):
        self.assertEquals(checkio([[1, 0, 3, 4, 0],
                                   [2, 0, 4, 5, 6],
                                   [3, 4, 9, 0, 6]]), [[1, 2, 3],
                                                       [0, 0, 4],
                                                       [3, 4, 9],
                                                       [4, 5, 0],
                                                       [0, 6, 6]])

if __name__ == '__main__':
    unittest.main(failfast=False)
