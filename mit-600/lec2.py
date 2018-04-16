# encoding: utf-8


def square(x):
    return x * x


def is_even(x):
    return (x/2)*2 == x


def least(*args):
    return reduce(b_min, args, args[0])


def b_min(x, y):
    if x > y:
        return y
    else:
        return x


def int_square_root(x):
    ans = 0
    while ans * ans < x:
        ans += 1
    return ans

def divisor(x):
    i = 1
    r = list()
    while i < x:
        if x % i == 0:
            r.append(i)
        i += 1
    return r