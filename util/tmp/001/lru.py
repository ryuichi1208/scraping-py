from functools import lru_cache

@lru_cache(maxsize=1000)
def fib_memoized(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
