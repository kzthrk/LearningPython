#!/usr/bin/env python3.8

import sys

def add(x, y):
    return x + y

try:
    print(add(1, 2))
    print(add("1", "2"))

except Exception as ex:
    print(ex)