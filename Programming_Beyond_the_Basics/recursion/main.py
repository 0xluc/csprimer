def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(10))


def palindrome(letters):
    phrase = ""
    for l in letters:
        if ord(l.lower()) in range(97, 123):
            phrase += l.lower()

    def check_palindrome(letters):
        if len(letters) <= 1:
            return True
        return letters[0] == letters[-1] and check_palindrome(letters[1:-1])

    return check_palindrome(phrase)


print(palindrome("A man, a plan, a canal - Panama!"))


def gcd(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    while b - a >= 0:
        if b - a == 0:
            return a
        b = b - a
    return gcd(a, a - b)


print(gcd(1071, 462))
print(gcd(7, 3))
print(gcd(3, 3))


def filter_recursive(f, xs):
    result = []

    def filter(func, elements):
        if len(elements) == 0:
            return result
        if func(elements[0]) == True:
            result.append(elements[0])
        return filter(func, elements[1:])

    return filter(f, xs)


print(filter_recursive(lambda x: x > 10, [1, 11, 20, 4]))


def reduce(f, xs, init=None):
    out = xs[0] if init is None else init

    def reducer(func, elements, out):
        if len(elements) == 0:
            return out
        out = func(out, elements[0])
        return reducer(func, elements[1:], out)

    return reducer(f, xs[1:], out)


print(reduce(lambda acc, x: acc + x, [1, 2, 3, 4]))
