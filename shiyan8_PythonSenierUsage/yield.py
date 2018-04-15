


def fib(n):
    current = 0
    a, b = 1, 1
    while current < n:
        yield a
        a, b = b, a + b
        current += 1


print(fib(10))


for x in fib(10):
    print(x)
