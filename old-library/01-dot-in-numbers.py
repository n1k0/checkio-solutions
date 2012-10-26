# The previous version of robots wasn't able to recognize big numbers.
# Write a module that will place a dot every three digits from the end in the
# numbers longer than 4 digits. There is no reason to insert dots in ordinal
# numbers like 1900th.
#
# Input data: string containing number
# Output data: string with dot-separated number

def checkio(txt):
    def splitn(t):
        return ('.'.join(partition(t[::-1], 3)))[::-1] if t.isdigit() else t
    def partition(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]
    return ' '.join(map(splitn, txt.split(' ')))

def check(subject, expected):
    value = checkio(subject)
    if value != expected:
        print "FAIL: %s != %s" % (subject, expected)
    else:
        print "PASS: %s" % value

if __name__ == '__main__':
    check('123456', '123.456')
    check('333', '333')
    check('9999999', '9.999.999')
    check('123456 567890', '123.456 567.890')
    check('price is 5799', 'price is 5.799')
    check('he was born in 1966th', 'he was born in 1966th')
