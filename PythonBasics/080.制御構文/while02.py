#!/usr/bin/env python3.8

n = 0
while n < 5:
    print(n)
    if n == 3:
        break
    n += 1
else:
    print("end of while")

if n == 3:
    print("break the while-loop")
else:
    print("complete the while-loop")