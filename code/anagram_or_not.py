#!/usr/bin/env python3


def is_anagram(word1, word2):
    if any((len(word1) != len(word2),
            len(word1) == 0,
            len(word2) == 0)):
        return False

    if any((c not in word2 for c in word1)):
        return False

    return True


for word1, word2 in [("", "abc"),
                     ("abcde", ""),
                     ("abcde", "vwxyz"),
                     ("abcde", "abcde"),
                     ("abcde", "edcba"),
                     ("edcba", "abcde")]:
    print("Is '{}' anagram of '{}'? {} ".format(word1, word2,
                                                "Yes!" if is_anagram(word1, word2) else "No!"))
