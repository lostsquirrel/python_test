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
    memo = { 0:1, 1: 1}
    return mem_fib_x(n, memo)


def mem_fib_x(n, memo):
    global num_calls
    num_calls += 1
    print(num_calls)
    if not memo.has_key(n):
        memo[n] = mem_fib_x(n - 1, memo) + mem_fib_x(n - 2, memo)
    return memo[n]
