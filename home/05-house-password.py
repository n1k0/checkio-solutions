# Input data: String which is a password.
# Output data: True if the password is safe.
#
# Help Nikola write a password security check module for Sofia.
# Password is considered to be strong enough if its length is more than 10
# symbols and it has at least one digit, one upper and one lower case letters.

def checkio(data):
    # this is just for fun, don't do this at home :)
    ok = lambda fn, r: -len(r) != sum([data.rfind(fn(x)) for x in r])
    return all([ok(str, xrange(10)),
                ok(chr, xrange(65, 91)),
                ok(chr, xrange(97, 123)),
                len(data) >= 10])

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'
    assert checkio('bAse730onE4') == True, 'Second'
    print 'All ok'
