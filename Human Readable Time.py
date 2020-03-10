#!/usr/bin/env python3
import math


def make_readable(seconds):
    hh = int(math.modf(seconds / 3600)[1])
    mm = int(math.modf((seconds - hh * 3600) / 60)[1])
    ss = int(str((seconds - hh * 3600) - (mm * 60)))
    return "{:02}:{:02}:{:02}".format(hh, mm, ss)
