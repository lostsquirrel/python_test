# coding=utf-8
def generator_function():
    for i in range(10):
        yield i


# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def generator():
    print('before')
    yield  # break 1
    print('middle')
    yield  # break 2
    print('after')


def averager():
    sum_ = 0
    num = 0
    while True:
        # print(sum_, num, sum_ / num if num > 0 else 0)
        sum_ += (yield sum_ / num if num > 0 else 0)
        num += 1


def odds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i


def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def odd_even(n):
    for x in odds(n):
        yield x
    for x in evens(n):
        yield x


def odd_even_x(n):
    yield from odds(n)
    yield from evens(n)
