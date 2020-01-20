#!/usr/bin/env python3.8

import sys

def add(x, y):
    return x + y

argv = sys.argv

try:
    a = int(argv[1])
    b = int(argv[2])
    c = add(a, b)
    print("result: " + str(c))
except Exception as ex:
    print(ex)