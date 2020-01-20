#!/usr/bin/env python3.8

import sys

if __name__ == '__main__':
    argv = sys.argv
    # print(argv)
    if len(argv) != 2:
        print('usage : {0} <filename>'.format(argv[0]))
        quit()

    f = open(argv[1], 'r')
    lines = f.readlines()
    f.close()
    # print(lines)

    for line in lines:
        data = line.split(" ")
        print("input: " + str(data))

        x = int(data[0])
        operator = data[1]
        y = int(data[2])

