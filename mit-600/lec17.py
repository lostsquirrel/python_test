# encoding: utf-8
import math, random, pylab


class Location(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, xc, yc):
        return Location(self.x + float(xc), self.y + float(yc))

    def get_coords(self):
        return self.x, self.y

    def get_dist(self, other):
        ox, oy = other.get_coords()
        x_dist = self.x - ox
        y_dist = self.y - oy
        return math.sqrt(x_dist ** 2 + y_dist ** 2)


class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')

    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in CompassPt.__init__')

    def move(self, dist):
        if self.pt == 'N':
            return 0, dist
        elif self.pt == 'S':
            return 0, -dist
        elif self.pt == 'E':
            return dist, 0
        elif self.pt == 'W':
            return -dist, 0
        else:
            raise ValueError('in CompassPt.move')


class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        old_loc = self.loc
        xc, yc = cp.move(dist)
        self.loc = old_loc.move(xc, yc)

    def get_loc(self):
        return self.loc

    def get_drunk(self):
        return self.drunk


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def move(self, field, time=1):
        if field.get_drunk() != self:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)


def perform_trial(time, f):
    start = f.get_loc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.get_drunk().move(f)
        new_loc = f.get_loc()
        distance = new_loc.get_dist(start)
        distances.append(distance)
    return distances


def perform_sim(time, num_trials):
    dist_lists = []
    for trial in range(num_trials):
        d = Drunk('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = perform_trial(time, f)
        dist_lists.append(distances)
    return dist_lists


def ans_quest(max_time, num_trials):
    print(max_time, num_trials)
    means = []
    dist_lists = perform_sim(max_time, num_trials)
    for t in range(max_time + 1):
        tot = 0.0
        for distL in dist_lists:
            tot += distL[t]
        means.append(tot / len(dist_lists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs. Time (' + str(len(dist_lists)) + ' trials)')
    pylab.show()


if __name__ == '__main__':
    ans_quest(500, 500)
