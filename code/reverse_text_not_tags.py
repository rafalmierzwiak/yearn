#!/usr/bin/env python

from __future__ import print_function


def reverse(s):
    return ''.join([s[i-1]
                    for i in range(len(s), 0, -1)])


def reverse_text_not_tags(s, o='<', c='>'):
    i = 0
    tokens = []
    while i < len(s):
        j = s[i:].find(o)
        if j == -1:
            tokens.append(reverse(s[i:]))
            break
        elif j == 0:
            k = s[i+j:].find(c)
            if k == -1:
                tokens.append(s[i+j:])
                break
            else:
                k += 1
                tokens.append(s[i+j:i+j+k])
                i += j + k
        else:
            tokens.append(reverse(s[i:i+j]))
            i += j
    return ''.join(tokens)


for text in ['Reverse me!',
             '<html><head></head><body><h1>Reverse me!</h1></body></html>']:
    print('Text: {}'.format(text))
    print('Text reversed: {}'.format(reverse(text)))
    print('Text reversed not tags: {}'.format(reverse_text_not_tags(text)))
