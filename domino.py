import random

class Pips:
    count = None

    def __init__(self, number):
        self.count = number


class Side:
    pips = None

    def __init__(self, pip_value):
        self.pips = pip_value


class Domino:
    top = None
    bottom = None

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return 'top: {}, bottom: {}'.format(self.top.pips.count, self.bottom.pips.count)


class Set:
    domino = []

    def __init__(self, size):
        self.domino = []

        for top in range(0, size + 1):
            for bottom in range(top, size + 1):
                top_side = Side(Pips(top))
                bottom_side = Side(Pips(bottom))
                new_domino = Domino(top_side, bottom_side)
                self.add(new_domino)

    def print_set(self):
        for domino in self.domino:
            print(domino)

    def add(self, domino):
        self.domino.append(domino)

    def scramble(self):
            random.shuffle(self.domino)


set = Set(6)
set.print_set()
