def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)


print(factorial_rec(10))


def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


print(factorial(10))


def trampoline(f):
    while callable(f):
        f = f()
    return f


def fac_tramp(n, acc=1):
    if n == 1:
        return acc
    return lambda: fac_tramp(n - 1, acc * n)


print(trampoline(lambda: fac_tramp(10)))


def fib_tramp(n, acc=1, current=1):
    if n == 1:
        return acc
    acc, current = current, acc + current
    return lambda: fib_tramp(n - 1, acc, current)


print(trampoline(fib_tramp(100)))
