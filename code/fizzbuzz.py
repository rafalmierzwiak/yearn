#!/usr/bin/env python3

import sys

def fizzbuzz(n):
    return ("fizz buzz" if not n % 15 else
            "fizz"      if not n % 3 else
            "buzz"      if not n % 5 else
            n)

for n in range(1, int(sys.argv[1])):
    print(fizzbuzz(n))
