from functools import reduce

fibs = [1, 2]
i = 2
while fibs[i - 1] + fibs[i - 2] < 4000000:
    fibs.append(fibs[i - 1] + fibs[i - 2])
    i += 1

print(reduce(lambda a, b: a + b, [n for n in fibs if n % 2 == 0]))
