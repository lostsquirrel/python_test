# encoding: utf-8
from lec2 import is_even


def solve(numLegs, numHeads):
    pigBackLeg = numLegs - numHeads * 2
    if is_even(pigBackLeg):
        numPig = pigBackLeg / 2
        numChicken = numHeads - numPig
        return numPig, numChicken
    return None, None


def is_palindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def fib(x):
    """Return fibonacci of x, where x is a non-negative int"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
