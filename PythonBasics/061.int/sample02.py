#!/usr/bin/env python3.8

import sys
import linecache

def exception_info():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)


try:
    a = 1
    x = int(a)
    print(x)
    print("result: " + str(x))
    print("result: " + x)
except Exception as ex:
    print(exception_info())

try:
    a = 2.1
    x = int(a)
    print(x)
    print("result: " + str(x))
    print("result: " + x)
except Exception as ex:
    print(exception_info())

try:
    a = "3"
    x = int(a)
    print(x)
    print("result: " + str(x))
    print("result: " + x)
except Exception as ex:
    print(exception_info())

try:
    a = "4.1"
    x = int(a)
    print(x)
    print("result: " + str(x))
    print("result: " + x)
except Exception as ex:
    print(exception_info())

try:
    a = "a"
    x = int(a)
    print(x)
    print("result: " + str(x))
    print("result: " + x)
except Exception as ex:
    print(exception_info())

