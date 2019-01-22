#!/usr/bin/env python3

from itertools import product
from math import ceil, sqrt
from sys import argv

with open(argv[1]) as f:
    nmax = int(f.readline())
    numbers = {int(line): 0
               for n, line in enumerate(f)
               if n <= nmax}

xmax = max(numbers)

squares = [x ** 2
           for x in range(int(ceil(sqrt(xmax))) + 1)]

for a, b in product(squares, squares):
    xsum = a + b
    if all([a <= b,
            xsum <= xmax,
            xsum in numbers]):
        numbers[xsum] += 1

for x in numbers.values():
    print(x)
