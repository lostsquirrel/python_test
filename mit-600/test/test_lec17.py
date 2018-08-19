# encoding: utf-8

from lec17 import *


def test_simple():
    drunk = Drunk('Homer Simpson')
    for i in range(3):
        f = Field(drunk, Location(0, 0))
        distances = perform_trial(500, f)
        pylab.plot(distances)
    pylab.title('Homer\'s Random Walk')
    pylab.xlabel('Time')
    pylab.ylabel('Distance from Origin')
    pylab.show()


def test_many():
    ans_quest(500, 500)


if '__main__' == __name__:
    # test_simple()
    test_many()
