#!/usr/bin/env python3.8

def divide(val):
    if val == 0:
        raise Exception("No ZERO!")
    print(10 / val)

for val in [1,0,3]:
    try:
        divide(val)
    except Exception as ex:
        print("exception: " + str(ex))
