#!/usr/bin/env python

from __future__ import print_function


def reverse(text):
    def _(text):
        for i in range(len(text)-1, -1, -1):
            yield text[i]
    return ''.join(_(text))


def reverse_text_not_tags(text, tag_open='<', tag_close='>'):
    def _(text):
        i = 0
        while i < len(text):
            tag_start = text.find(tag_open, i)
            if tag_start == -1:
                yield reverse(text[i:])
                break
            elif tag_start == i:
                tag_end = text.find(tag_close, tag_start)
                if tag_end == -1:
                    yield text[i:tag_start]
                    break
                else:
                    tag_end += 1
                    yield text[i:tag_end]
                    i = tag_end
            else:
                yield reverse(text[i:tag_start])
                i = tag_start
    return ''.join(_(text))


for text in ['Reverse me!',
             '<html><head></head><body><h1>Reverse me!</h1></body></html>']:
    print('Text: {}'.format(text))
    print('Text reversed: {}'.format(reverse(text)))
    print('Text reversed not tags: {}'.format(reverse_text_not_tags(text)))
