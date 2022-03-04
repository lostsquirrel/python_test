'''
Created on Jan 12, 2015

@author: lisong
'''
class entryExit(object):

    def __init__(self, x, f):
        self.x = x
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__, self.x)

@entryExit
def func1():
    print("inside func1()")

@entryExit
def func2():
    print("inside func2()")

func1()
func2()

