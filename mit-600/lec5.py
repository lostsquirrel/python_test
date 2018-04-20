# encoding: utf-8


def square_root_bi(x, epsilon):

    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon > 0, 'epsilon must be postive, not' + str(epsilon)
    low = 0
    high = max(x, 1)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        # print 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    print x
    assert ctr <= 100, 'Iteration count exceeded '
    print 'Bi method. Num. iterations:', ctr, 'Estimate:', guess
    return guess


def square_root_nr(x, epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon > 0, 'epsilon must be postive, not' + str(epsilon)
    x = float(x)

    guess = x/2.0
    guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
    # print 'Error:', diff, 'guess:', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'NR method. Num. iterations:', ctr, 'Estimate:', guess
    return guess