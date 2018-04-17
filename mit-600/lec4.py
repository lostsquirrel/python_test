# encoding: utf-8
from lec2 import is_even

def solve(numLegs, numHeads):
    pigBackLeg = numLegs - numHeads * 2
    if is_even(pigBackLeg):
        numPig = pigBackLeg / 2
        numChicken = numHeads - numPig
        return (numPig, numChicken)
    return (None, None)