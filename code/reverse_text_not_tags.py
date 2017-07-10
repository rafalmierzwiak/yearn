#!/usr/bin/env python

from __future__ import print_function


def reverse(s):
    def _(s):
        for i in range(len(s)-1, -1, -1):
            yield s[i]
    return ''.join(_(s))


def reverse_text_not_tags(s, o='<', c='>'):
    def _(s):
        i = 0
        while i < len(s):
            j = s.find(o, i)
            if j == -1:
                yield reverse(s[i:])
                break
            elif j == i:
                k = s.find(c, j)
                if k == -1:
                    yield s[i:j]
                    break
                else:
                    k += 1
                    yield s[i:k]
                    i = k
            else:
                yield reverse(s[i:j])
                i = j
    return ''.join(_(s))


for text in ['Reverse me!',
             '<html><head></head><body><h1>Reverse me!</h1></body></html>']:
    print('Text: {}'.format(text))
    print('Text reversed: {}'.format(reverse(text)))
    print('Text reversed not tags: {}'.format(reverse_text_not_tags(text)))
