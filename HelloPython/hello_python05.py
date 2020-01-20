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
        try:
            data = line.split(" ")
            print("input: " + str(data))

            x = int(data[0])
            operator = data[1]
            y = int(data[2])

            if operator == "+":
                result = x + y
                print("result: " + str(result))
            elif operator == "-":
                result = x - y 
                print("result: " + str(result))
            elif operator == "*":
                result = x * y
                print("result: " + str(result))
            elif operator == "/":
                result = x / y
                print("result: " + str(result))
            else:
                raise Exception("operator is not valid")
        except ValueError as e:
            print("[Error2]使用可能な値は整数です")
            print(e)
        except ZeroDivisionError as e:
            print("[Error2]ゼロで割ることは出来ません")
            print(e)
        except Exception as e:
            print("[Error2]使用可能な演算子は+-*/のいずれかです")
            print(e)
