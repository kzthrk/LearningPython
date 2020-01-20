#!/usr/bin/env python3.8

for val in [1,2,3,0,5]:
    try:
        print(10 / val)
    except Exception as ex:
        print("exception: " + str(ex))
    else:
        print("else of try-except")
    finally:
        print("finally of try-except\n-----")