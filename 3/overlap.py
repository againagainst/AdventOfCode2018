# #1 @ 509,796: 18x15

import re
import pprint
import itertools


class Claim:
    _REX = re.compile(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)')

    def __init__(self, txt):
        parsed = self._REX.fullmatch(txt).groupdict()
        self.txt = txt
        self._id = int(parsed['id'])
        self.x = int(parsed['x'])
        self.y = int(parsed['y'])
        self.w = int(parsed['w'])
        self.h = int(parsed['h'])
        self.xmin = self.x
        self.ymin = self.y
        self.xmax = self.x+self.w
        self.ymax = self.y+self.h

    def __repr__(self):
        return self.txt

    def __str__(self):
        return '{_id}: {x},{y} ({w}x{h})'.format(_id=self._id, x=self.x, y=self.y, w=self.w, h=self.h)

    def points(self):
        for x in range(self.x, self.xmax):
            for y in range(self.y, self.ymax):
                yield x-1, y-1

def read_data(filename):
    with open(filename, 'r') as fp:
        data = fp.read().split('\n')
        return list(map(Claim, data))

def calc_fabric(claims):
    xmax = max(claims, key=lambda c: c.xmax)
    ymax = max(claims, key=lambda c: c.ymax)
    fabric = [[0]*ymax.ymax for _ in range(xmax.xmax)]
    for c in claims:
        for p in c.points():
            fabric[p[0]][p[1]] = fabric[p[0]][p[1]] + 1
    return fabric

def calc_overlap(claims):
    fabric = calc_fabric(claims)
    #pprint.pprint(fabric)
    return len(list(filter(lambda x: x > 1, itertools.chain(*fabric))))

def find_nonoverlap(claims):
    fabric = calc_fabric(claims)
    for c in claims:
        if all(fabric[p[0]][p[1]]==1 for p in c.points()):
            return c._id

if __name__ == "__main__":
    print(find_nonoverlap(read_data('data.txt')))