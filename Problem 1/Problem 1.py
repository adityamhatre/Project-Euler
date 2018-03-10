from functools import reduce


def add(x, y):
    return x + y


def divisible_by_3_or_5(x):
    return divisible_by_3(x) or divisible_by_5(x)


def divisible_by_3(x):
    return x % 3 == 0


def divisible_by_5(x):
    return x % 5 == 0


print(reduce(add, filter(divisible_by_3_or_5, [a for a in range(1, 10)])))
