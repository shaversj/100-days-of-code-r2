def count_primes(x, y):
    # Given two integers N and M,
    # count the number of prime numbers between N and M (both inclusive)

    counter = 0

    for num in range(x, y + 1):
        if is_prime(num):
            counter += 1
        else:
            continue

    return counter


def is_prime(num):
    import math

    if num < 2:
        return False

    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False

    return True
