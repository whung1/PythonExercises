import sys

sys.setrecursionlimit(100000)

fib_cache = {0: 0, 1: 1} # base cases


def fibonacci_recursive(n):
    """Top-down implementation (recursive)"""

    if n < 0:
        return -1

    if n not in fib_cache:
        fib_cache[n] = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    return fib_cache[n]


def fibonacci_iterative(n):
    """Bottom up implementation (iterative)"""

    for i in range(2, n+1):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]

    return fib_cache[n]

if __name__ == '__main__':
    print(fibonacci_recursive(7))
    print(fibonacci_recursive(8181))
    print(fibonacci_iterative(7))
    print(fibonacci_iterative(8181))
