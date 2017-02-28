# Need to increase recursion limit even when memoization is used if n is too large
# e.g. sys.setrecursionlimit(100000)

def fibonacci_recursive_memo(n, fib_cache={0: 0, 1: 1}):
    """Top-down implementation (recursive) with memoization, O(n^2)"""

    if n < 0:
        return -1

    if n not in fib_cache:
        fib_cache[n] = fibonacci_recursive_memo(n-1) + fibonacci_recursive_memo(n-2)
    return fib_cache[n]


def fibonacci_recursive_tco(n, next_fib=1, summation=0):
    """Top-down implementation (recursive) with tail-call optimization (TCO), O(n)"""
    if n == 0:
        return summation
    else:
        #  summation will be the "next fib" passed in parameter that is the current fib of this call
        #  but the next fib needs to be recalcuated as current_sum + next_fib
        return fibonacci_recursive_tco(n-1, summation+next_fib, next_fib)


def fibonacci_iterative_memo(n, fib_cache={0: 0, 1: 1}):
    """Bottom up implementation (iterative) with memoization, O(n^2)"""

    for i in range(2, n+1):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]

    return fib_cache[n]

if __name__ == '__main__':
    # Iterative with memoization
    print('Iterative with memoization:')
    print(fibonacci_iterative_memo(7))
    print(fibonacci_iterative_memo(800))
    # Tail call optimization
    print('Recursive with TCO:')
    print(fibonacci_recursive_tco(7))
    print(fibonacci_recursive_tco(800))
    # Memoization
    print('Recursive with memoization:')
    print(fibonacci_recursive_memo(7))
    print(fibonacci_recursive_memo(800))

