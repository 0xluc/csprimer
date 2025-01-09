def vec(x, y):
    return (x, y)


def add(*tuples):
    x, y = 0, 0
    for t in tuples:
        x += t[0]
        y += t[1]
    return (x, y)


def mul(t1: tuple, scalar: int):
    return (t1[0] * scalar, t1[1] * scalar)


def sub(t1, t2):
    return add(t1, (-t2[0], -t2[1]))


if __name__ == "__main__":
    v1 = vec(3, 2)
    v2 = vec(1, 1)
    v3 = vec(3, 4)
    assert add(v1, v2, v3) == (7, 7)
    assert mul(v1, 2) == (6, 4)
    assert sub(v1, v2) == (2, 1)
    print("All tests passed")
