# The robots got to know that the last container NxN (3<=N<=10) that came form
# another island has radiation. There are five different kinds of spare parts.
# It is known that the radiation comes from the biggest union of the parts. Help
# them find the biggest group of spare parts that stay near each other and point
# out their quantity and the number itself.
#
# We have a matrix A NxN (3<=N<=10). Numbers between 1 and 5 are the elements of
# A. Find the biggest group of equal numbers that stay near each other and point
# out their quantity and the number itself.


class GridRunner(object):
    "This is not an efficient approach, but damn. That was fun."

    def __init__(self, matrix, x=0, y=0, dolog=False):
        self.matrix = matrix
        self.x = x
        self.y = y
        self.number = self.number_at(x, y)
        self.to_explore = []
        self.path = []
        self.dolog = dolog
        self.log('started')

    def can_move_to(self, x, y):
        if not self.number_at(x, y):
            self.log("I can't move to (%d, %d), it's a wall" % (x, y))
            return False
        if self.number_at(x, y) != self.number:
            self.log("I can't move to (%d, %d): %d is not %s"
                     % (x, y, int(self.number_at(x, y)), self.number))
            return False
        if (x, y) in self.path:
            self.log("I visited (%d, %d) already" % (x, y))
            return False
        return True

    def dump(self):
        dest_matrix = list(self.matrix)
        for x, y in self.path:
            dest_matrix[y][x] = 'X'
        for row in dest_matrix:
            print ''.join(map(str, row))

    def log(self, message):
        if not self.dolog:
            return
        print "(%d, %d): %s" % (self.x, self.y, message)

    def look_around(self):
        "check for possible moves; returns list of possible coord tuples"
        self.log('looking around')
        up = (self.x, self.y - 1)
        if self.can_move_to(*up):
            self.log('I can go up at (%d, %d)' % up)
            self.to_explore.append(up)
        right = (self.x + 1, self.y)
        if self.can_move_to(*right):
            self.log('I can go right at (%d, %d)' % right)
            self.to_explore.append(right)
        down = (self.x, self.y + 1)
        if self.can_move_to(*down):
            self.log('I can go down at (%d, %d)' % down)
            self.to_explore.append(down)
        left = (self.x - 1, self.y)
        if self.can_move_to(*left):
            self.log('I can go left at (%d, %d)' % left)
            self.to_explore.append(left)

    def number_at(self, x, y):
        try:
            assert x >= 0 and x < len(self.matrix[0])
            assert y >= 0 and y < len(self.matrix)
            return self.matrix[y][x]
        except (AssertionError, IndexError):
            pass

    def move_to(self, x, y):
        if not self.can_move_to(x, y):
            return False
        self.log('moving to (%d, %d)' % (x, y))
        if (x, y) in self.to_explore:
            del self.to_explore[self.to_explore.index((x, y))]
        self.x = x
        self.y = y
        self.path.append((self.x, self.y))
        return True

    def run(self):
        while self.trymove():
            self.trymove()
        return self.path

    def trymove(self):
        self.look_around()
        if self.to_explore:
            x, y = self.to_explore.pop()
            return self.move_to(x, y)
        return False

matrix1 = [
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]
]

matrix2 = [
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]
]

def checkio(matr):
    scores = []
    for x in xrange(len(matr[0])):
        for y in xrange(len(matr)):
            grid = GridRunner(matr, x=x, y=y, dolog=False)
            path = grid.run()
            scores.append([len(path), grid.number])
    best = (0, 0)
    for score in scores:
        if score[0] > best[0]:
            best = score
    return best

if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], 'First'

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], 'Second'

    print 'All ok'
