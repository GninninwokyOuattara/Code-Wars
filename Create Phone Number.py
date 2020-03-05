#!/usr/bin/env python3
import re


def create_phone_number(n):
    n = "".join([str(l) for l in n])
    k = re.search(r"(\d\d\d)(\d\d\d)(\d\d\d\d)", n)
    return "({}) {}-{}".format(k.group(1), k.group(2), k.group(3))
