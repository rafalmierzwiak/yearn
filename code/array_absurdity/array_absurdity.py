#!/usr/bin/env python3

from sys import argv

with open(argv[1]) as f:
    for line in f:
        length, numbers = line.rstrip("\n").split(";")

        duplicates = {}
        for n in numbers.split(","):
            if n in duplicates:
                print(n)
                break
            duplicates[n] = True
