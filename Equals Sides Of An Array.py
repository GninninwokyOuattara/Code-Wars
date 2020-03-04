#!/usr/bin/env python3

from test import Test


def sum(arr):
    s = 0
    for n in arr:
        s += n
    return s


def find_even_index(arr):
    i = 0
    while i <= len(arr):
        rs, ls = arr[:i], arr[i + 1:]
        sum_rs = sum(rs)
        sum_ls = sum(ls)
        if sum_rs == sum_ls:
            break
        elif i == len(arr):
            return - 1
        i += 1
    return i
