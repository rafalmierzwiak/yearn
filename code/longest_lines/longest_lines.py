#!/usr/bin/env python3

from sys import argv

lines = {}

with open(argv[1]) as f:
    n = int(f.readline())

    for line in f:
        lines[len(line)] = line
        if len(lines) == n:
            break

    shortest = min(lines)
    longest = max(lines)

    for line in f:
        length = len(line)

        if length < shortest:
            continue

        if length > longest:
            longest = length
            lines[longest] = line
            del lines[shortest]
        else:
            lines[length] = line
            del lines[shortest]
            shortest = min(lines)

for line in reversed(sorted(lines.values(), key=len)):
    print(line.rstrip("\n"))
