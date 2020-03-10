#!/usr/bin/env python3
import string


def pig_it(text):

    return " ".join([w[1:] + w[0] + "ay" if w not in string.punctuation else w
                     for w in text.split()])
