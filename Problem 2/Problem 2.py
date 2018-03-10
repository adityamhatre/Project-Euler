from functools import reduce

fibs = [1, 2]
i = 2
while fibs[i - 1] + fibs[i - 2] < 4000000:
    fibs.append(fibs[i - 1] + fibs[i - 2])
    i += 1


def is_even(n):
    return n % 2


def add(a, b):
    return a + b


print(reduce(add, filter(is_even, fibs)))
