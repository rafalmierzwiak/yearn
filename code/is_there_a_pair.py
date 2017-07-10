#!/usr/bin/env python3

from itertools import combinations

def find_pairs(s, a):
    return (p
            for p in combinations(a, 2)
            if sum(p) == s)


def find_number_of_pairs(s, a):
    return sum((1 for p in find_pairs(s, a)))


a = range(1024)
for s in [0, 1, 1022, 1023, 1024, 1023*2-1, 1023*2]:
    print("Array of {} elements (values {}..{}), "
          "Sum to search for: {}".format(len(a), min(a), max(a), s))
    print("Found: {} pairs".format(find_number_of_pairs(s, a)))
