# had no clue on how to solve the second test of this challenge
def reduce(f, xs, init=None):
    xs = iter(xs)
    # init being None, we need to iterate to the second item from xs
    out = next(xs) if init is None else init
    # out has the first value but xs is now on the second one on the iteration
    for x in xs:
        out = f(out, x)
    return out


def mirror(d, x):
    d[x] = x
    return d


print(reduce(lambda acc, x: acc + x, [1, 2, 3, 4]))
print(reduce(mirror, ["foo", "bar"], {}))


def product(nums):
    return reduce(lambda acc, y: acc * y, nums, 1)


print(product([1, 2, 3, 4]))


def my_map(f, xs):
    return [f(x) for x in xs]


print(my_map(lambda x: x * x, [1, 2, 3, 4]))


def my_filter(f, xs):
    return [x for x in xs if f(x) == True]


print(my_filter(lambda x: x > 0, [0, 1, 1, 2, 0]))


def my_zip(*iters):
    return [[x[y] for x in iters] for y in range(len(iters[0]))]


print(my_zip("abc", "def", (1, 2, 3)))
