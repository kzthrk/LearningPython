#!/usr/bin/env python3.8

import json

json_str = '{"name": "john", "age": 25}'

json_dict = json.loads(json_str)

print(json_str)
print(json_dict)