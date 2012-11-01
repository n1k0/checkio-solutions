import unittest

from itertools import groupby

N = 4

def submatrix(matr, x, y, size):
    return [row[x:x + size] for row in matr][y:y + size]

def diagonals(matr, N):
    diags = []
    for size in xrange(1, len(matr) + 1):
        for x in xrange(size):
            if x > len(matr) - size:
                continue
            for y in xrange(size):
                if y > len(matr) - size:
                    continue
                submatr = submatrix(matr, x, y, size)
                diags.extend([
                    [row[i] for i, row in enumerate(submatr)],
                    [row[-(i + 1)] for i, row in enumerate(submatr)]
                ])
    return diags

def checkio(matr):
    rotate = lambda lst: zip(*lst[::-1])
    row_ok = lambda r: any([len(list(g)) >= N for _, g in groupby(r)])
    return any([
        any(map(row_ok, matr)),
        any(map(row_ok, rotate(matr))),
        any(map(row_ok, diagonals(matr, N))),
    ])


class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([
            [1, 1, 1, 1],
            [1, 2, 3, 4],
            [5, 4, 3, 1],
            [6, 1, 3, 2]
        ]), True)

    def test_6(self):
        self.assertEquals(checkio([
            [1, 1, 3, 1],
            [1, 2, 3, 4],
            [5, 4, 3, 1],
            [6, 1, 3, 2]
        ]), True)

    def test_2(self):
        self.assertEquals(checkio([
            [7, 6,  5, 7, 9],
            [8, 7,  3, 6, 5],
            [4, 0,  6, 5, 4],
            [9, 8,  4, 0, 5],
            [2, 10, 7, 2, 10]
        ]), False)

    def test_3(self):
        self.assertEquals(checkio([
            [10, 1, 9,  6, 4, 1],
            [2,  5, 4,  2, 2, 7],
            [2,  2, 1,  2, 6, 4],
            [3,  2, 2,  1, 0, 2],
            [7,  9, 6,  2, 5, 7],
            [7,  3, 10, 5, 6, 2]
        ]), True)

    def test_4(self):
        self.assertEquals(checkio([
            [6, 6, 7, 7, 7],
            [1, 7, 3, 6, 5],
            [4, 1, 2, 3, 2],
            [9, 0, 4, 0, 5],
            [2, 0, 7, 5, 10]
        ]), False)

    def test_5(self):
        self.assertEquals(checkio([
            [1,  1, 1,  6, 1, 1, 1],
            [2,  5, 4,  2, 2, 7, 2],
            [2,  6, 1,  2, 6, 4, 3],
            [3,  2, 2,  1, 0, 2, 4],
            [7,  9, 6,  2, 5, 7, 5],
            [7,  3, 10, 5, 6, 2, 5],
            [7,  3, 10, 5, 6, 2, 5]
        ]), False)

    def test_diagonals(self):
        self.assertEquals(diagonals([
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7],
        ], 4), [
            [1],
            [1],
            [1, 3],
            [2, 2],
            [2, 4],
            [3, 3],
            [2, 4],
            [3, 3],
            [3, 5],
            [4, 4],
            [1, 3, 5],
            [3, 3, 3],
            [2, 4, 6],
            [4, 4, 4],
            [2, 4, 6],
            [4, 4, 4],
            [3, 5, 7],
            [5, 5, 5],
            [1, 3, 5, 7],
            [4, 4, 4, 4]])

    def test_submatrix(self):
        matrix = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7],
        ]
        self.assertEquals(submatrix(matrix, 0, 0, 2), [
            [1, 2],
            [2, 3],
        ])
        self.assertEquals(submatrix(matrix, 1, 1, 2), [
            [3, 4],
            [4, 5],
        ])
        self.assertEquals(submatrix(matrix, 1, 0, 2), [
            [2, 3],
            [3, 4],
        ])
        self.assertEquals(submatrix(matrix, 0, 1, 2), [
            [2, 3],
            [3, 4],
        ])
        self.assertEquals(submatrix(matrix, 1, 1, 3), [
            [3, 4, 5],
            [4, 5, 6],
            [5, 6, 7],
        ])

if __name__ == '__main__':
    unittest.main(failfast=False)
