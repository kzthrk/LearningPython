#!/usr/bin/env python3.8

str_dict = {"1": "first","2": "second","3": "third",}

print(str_dict)
str_dict["1"] = "いち"
print(str_dict)

str_dict["4"] = "よん"
print(str_dict)

str_dict2 = {"5": "ご",}
str_dict.update(str_dict2)
print(str_dict)

str_dict3 = {"2": "に",}
str_dict.update(str_dict3)
print(str_dict)
