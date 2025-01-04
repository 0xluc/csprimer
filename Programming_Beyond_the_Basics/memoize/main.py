import urllib.request

# def fetch(arg):
#    with urllib.request.urlopen(arg) as response:
#        content = response.read().decode("utf-8", errors="replace")
#        return content
#


def memoize(fn):
    cache = {}

    def inner(arg):
        if arg in cache:
            return cache[arg]
        res = fn(arg)
        cache[arg] = res
        return res

    return inner


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(400))
