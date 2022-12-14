def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fib(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]
    return fib
      