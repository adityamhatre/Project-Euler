def max_prime_factor(x):
    a = x
    b = 2
    c = None
    while b < a / 2:
        if a % b == 0:
            if c is not None and b > c:
                c = b
            a = a / b
            b = 2
        else:
            b += 1
    return a


print(max_prime_factor(600851475143))
