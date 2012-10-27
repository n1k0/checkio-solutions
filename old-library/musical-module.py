def checkio(values):
    a, b = values
    return a if not b else checkio((b, a % b))

if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First"
    assert checkio((14, 21)) == 7, "Second"
    print 'All ok'

