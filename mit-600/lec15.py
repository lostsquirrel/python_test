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