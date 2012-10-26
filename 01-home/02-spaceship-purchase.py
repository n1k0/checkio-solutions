# Input data: contains four integer numbers:
#
# - the initial Sofia's offer,
# - Sofia's raise to his offer,
# - the initial fare required by the old man's,
# - the old man's reduction of his fare;
#
# Output data: the amount of money that Sofia will pay for the spaceship.

def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    initial_petr, raise_petr, initial_driver, reduction_driver = offers
    return (initial_driver - reduction_driver) / 2

if __name__ == '__main__':
    print checkio([150, 50, 1000, 100])
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'
