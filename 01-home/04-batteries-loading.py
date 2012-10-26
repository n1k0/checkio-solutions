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

if __name__ == '__main__':
    assert checkio([10, 10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5, 5, 6, 5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    print 'All is ok'
