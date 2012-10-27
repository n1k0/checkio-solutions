# Calculate sum of the factorials for all digits of the specified positive
# integer number.

import operator

def checkio(data):
    total = 0
    for n in map(int, list(str(data))):
        total += 1 if not n else reduce(operator.mul, xrange(1, n + 1))
    return total

if __name__ == '__main__':
    assert checkio(100) == 3, 'First'
    assert checkio(222) == 6, 'Second'
    assert checkio(1234) == 33, 'Third'
    print 'All ok'
