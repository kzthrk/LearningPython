#!/usr/bin/env python3.8

import sys

argv = sys.argv

if len(argv) == 1:
    print("no arguments")
elif len(argv) == 2:
    print("argument is one!")
else:
    print("arguments are two or more")

