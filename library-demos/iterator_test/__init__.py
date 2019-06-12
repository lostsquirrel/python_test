# coding=utf-8
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max_val=0):
        self.max_val = max_val

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max_val:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
