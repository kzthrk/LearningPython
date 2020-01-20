#!/usr/bin/env python3.8

value1 = [1, 2, 3]
value2 = [1, 2, 3]

print(value1 == value2)
print(value1 is value2)

value2 = value1
print(value1 == value2)
print(value1 is value2)

print("---")
print( 1 in value1)
print( 4 in value1)