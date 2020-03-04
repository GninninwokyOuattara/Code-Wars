#!/usr/bin/env python3


def duplicate_encode(word):
    word = word.lower()
    duplicate = []
    for i in range(len(word)):
        letter = word[i]
        if letter in word[:i]:
            continue
        else:
            indices = [i for i, x in enumerate(word) if x == letter]
            if len(indices) > 1:
                duplicate += indices
    duplicate.sort()
    str = ""
    for i in range(len(word)):
        if i in duplicate:
            str += ")"
        else:
            str += "("
    return str

# indices = [i for i, x in enumerate(my_list) if x in word]
