# encoding: utf-8


global num_calls
num_calls = 0


def fib(n):
    global num_calls
    num_calls += 1
    print(num_calls)
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def mem_fib(n):
    memo = {0: 1, 1: 1}
    return mem_fib_x(n, memo)


def mem_fib_x(n, memo):
    global num_calls
    num_calls += 1
    print(num_calls)
    if not memo.has_key(n):
        memo[n] = mem_fib_x(n - 1, memo) + mem_fib_x(n - 2, memo)
    return memo[n]


def max_value(w, v, i, aW):
    """
       knapsack problem
    :param w: weight of item
    :param v: value of item
    :param i: index of item
    :param aW: available weight
    :return:
    """
    # print 'maxVal called with:', i, aW
    global num_calls
    num_calls += 1
    print(num_calls)

    if i == 0:
        if w[i] <= aW:
            return v[i]
        else:
            return 0

    without_i = max_value(w, v, i - 1, aW)
    # check available weight is not enough for the next item
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + max_value(w, v, i - 1, aW - w[i])
    return max(with_i, without_i)

def max_value_mem(w, v, i, aW, m):
    global num_calls
    num_calls += 1
    print(num_calls)
    key = (i, aW)
    if not m.has_key(key):
        if i == 0:
            if w[i] <= aW:
                return v[i]
            else:
                return 0

        without_i = max_value_mem(w, v, i - 1, aW, m)
        # check available weight is not enough for the next item
        if w[i] > aW:
            m[key] = without_i
            return m[key]
        else:
            with_i = v[i] + max_value_mem(w, v, i - 1, aW - w[i], m)
        m[key] = max(with_i, without_i)
    return m[key]


def max_value_x(w, v, i, aW):
    m = dict()
    return max_value_mem(w, v, i, aW, m)