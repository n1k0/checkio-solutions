# Write a module for the robots to remember their passwords with the codes
# easily when they come back.
#
# Input: The first four lines contain the Robot's cipher grille. The next four
# lines contain the square with the ciphered password. All the symbols in the
# square are lowercase Latin letters.
# Output: Password

import unittest

def checkio(input_data):
    def fetch(placeholders, grid):
        part = ''
        for x, line in enumerate(placeholders):
            for y, char in enumerate(line):
                if char == 'X':
                    part += grid[x][y]
        return part
    rotate = lambda grid: zip(*grid[::-1])
    placeholders, grid = input_data
    password = fetch(placeholders, grid)
    for _ in xrange(3):
        placeholders = rotate(placeholders)
        password += fetch(placeholders, grid)
    return password

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([[
            'X...',
            '..X.',
            'X..X',
            '....'], [
            'itdf',
            'gdce',
            'aton',
            'qrdi']]), 'icantforgetiddqd')

    def test_2(self):
        self.assertEquals(checkio([[
            '....',
            'X..X',
            '.X..',
            '...X'], [
            'xhwc',
            'rsqx',
            'xqzz',
            'fyzr']]), 'rxqrwsfzxqxzhczy')

if __name__ == '__main__':
    unittest.main(failfast=False)
