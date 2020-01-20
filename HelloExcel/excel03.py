#!/usr/bin/env python3.8

import pandas as pd
import re


FILE_NAME = "sample.xlsx"
SHEET_NAME = "番号順"

df = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME, header=0)
# print(df)
for index, row in df.iterrows():
    # print(row[2])
    b = re.search('[0-9]|[０-９]', row[2])
    if b:
        address = row[2][:b.start()]
        print(address)
    else:
        print("not matched!")
        pass

