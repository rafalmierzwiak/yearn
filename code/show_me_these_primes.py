#!/usr/bin/env python3


def count_primes(number):
    return sum((1
                for n in range(2, number+1)
                if is_prime(n)))


def is_prime(number):
    if number < 2:
        return False

    if any((number % divisor == 0
            for divisor in range(2, number))):
        return False

    return True


def next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            return index


print("is n a prime?")
for n in range(-1, 16):
    print("{}: {}".format(n, is_prime(n)))

print("number of prime numbers smaller or equal n:")
for n in range(-1, 16):
    print("{}: {}".format(n, count_primes(n)))

print("next prime:")
for n in range(1, 8):
    print("{}: {}".format(n, next_prime(n)))
