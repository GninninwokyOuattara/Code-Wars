#!/usr/bin/env python3


def solution(n):
    # TODO convert int to roman string
    # I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    ns = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
          90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    lns = list(ns.keys())
    r = ""
    while n != 0:
        for i in reversed(lns):
            if i <= n:
                r += ns[i]
                n -= i
                break
    return r
