#!/usr/bin/env python3

import sys


def been_processed(processed_words, word):
    for p in processed_words:
        if word in p:
            return True
    return False


output = sys.argv[1]
dictionary = list(reversed(sorted(sys.argv[2].split(), key=len)))
translations = {" ?": "?",
                "  ": " ",
                " anda ": " and a ",
                "'applepie' as": "'apple pie' as"}

processed = []
for word in dictionary:
    if been_processed(processed, word):
        continue
    processed.append(word)
    output = " {} ".format(word).join(output.split(word))

for word, translation in translations.items():
    output = output.replace(word, translation)

print(output.strip())
