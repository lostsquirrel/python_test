# encoding: utf-8

import math


# points as lists

def add_points(p1, p2):
    return [p1[0] + p2[0], p1[1] + p2[1]]


# points as classes
class CartesianPoint:
    def __init__(self):
        pass


def same_cartesian_point(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)


def print_cartesian_point(p):
    print('(%s, %s)' % (p.x, p.y))


class cPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x * self.x + self.y * self.y)
        self.angle = math.atan2(self.y, self.x)

    def cartesian(self):
        return (self.x, self.y)

    def polar(self):
        return (self.radius, self.angle)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __cmp__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class pPoint:
    def __init__(self, r, a):
        self.radius = r
        self.angle = a
        self.x = r * math.cos(a)
        self.y = r * math.sin(a)

    def cartesian(self):
        return (self.x, self.y)

    def polar(self):
        return (self.radius, self.angle)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __cmp__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return math.sqrt(((self.start.x - self.end.x) *
                          (self.start.x - self.end.x))
                         + ((self.start.y - self.end.y) *
                            (self.start.y - self.end.y)))


class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def findCenter(box):
    p = cPoint(box.corner.x + box.width / 2.0,
               box.corner.y - box.height / 2.0)
    return p


def growRect(box, dwidth, dheight):
    box.width = box.width + dwidth
    box.height = box.height + dheight


class newPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return newPoint(self.x + other.x, self.y + other.y)

    def __cmp__(self, other):
        return self.x < other.x and self.y < other.y
