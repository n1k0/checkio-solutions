class GridRunner(object):
    DIRECTIONS = ((0, -1), (0, 1), (1, 0), (-1, 0),)

    def __init__(self, matrix, x=0, y=0):
        self.matrix = matrix
        self.x = x
        self.y = y
        self.number = self.number_at(x, y)
        self.to_explore = []
        self.path = []

    def can_move_to(self, x, y):
        number = self.number_at(x, y)
        return all([number, number == self.number, (x, y) not in self.path])

    def look_around(self):
        for direction in self.DIRECTIONS:
            coords = (self.x + direction[0], self.y + direction[1])
            if self.can_move_to(*coords):
                self.to_explore.append(coords)

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

def checkio(matr):
    scores = []
    for x in xrange(len(matr[0])):
        for y in xrange(len(matr)):
            runner = GridRunner(matr, x=x, y=y)
            scores.append([len(runner.run()), runner.number])
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
