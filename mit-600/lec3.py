# encoding: utf-8


def sum_digits(d):
    sum_d = 0
    for c in str(d):
        sum_d += int(c)
    return sum_d

