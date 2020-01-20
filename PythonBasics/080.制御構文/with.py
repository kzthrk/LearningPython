#!/usr/bin/env python3.8

# withを用いない書き方
f = open("sample.txt")
print(f.read())
f.close()

# withを用いた書き方
with open("sample.txt") as f:
    print(f.read())

with print("aaa") as p:
    pass