#!/usr/bin/env python3

def rangify(numbers):
    if not numbers:
        return

    numbers = sorted(set(numbers))

    ranges = []
    start = numbers[0]

    try:
        for n in range(len(numbers)):
            if numbers[n+1] - numbers[n] == 1:
                continue
            end = numbers[n]
            ranges.append((start, end))
            start = numbers[n+1]

    except IndexError as e:
        end = numbers[-1]

    ranges.append((start, end))

    return ranges


def textify(ranges):
    texts = []
    for start, end in ranges:
        if start == end:
            texts.append(f"{start}")
        else:
            texts.append(f"{start}-{end}")
    return ','.join(texts)


for numbers in [[],
                [1],
                [1,1],
                [1,2],
                [2,1],
                [1,4,5,8],
                [1,2,4,8],
                [8,4,2,1],
                [1,2,3,3,3,5,8,8,8,13,13,13,14,15,16,17]]:
    if numbers:
        print(textify(rangify(numbers)))
