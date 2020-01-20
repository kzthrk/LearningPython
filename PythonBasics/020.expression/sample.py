#!/usr/bin/env python3.8

import sys

x = int(sys.argv[1])
op = sys.argv[2]
y = int(sys.argv[3])

if op == "+":
	z = x + y
	print("result: " + str(z))
elif op == "-":
	z = x - y
	print("result: " + str(z))
else:
	print("その演算子はサポートしていません")