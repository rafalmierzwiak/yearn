#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        try:
            a, b = line.strip("\n").split(",")
            if a[-len(b):] == b:
                print("1")
            else:
                print("0")
        except ValueError:
            pass
