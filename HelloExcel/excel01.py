#!/usr/bin/env python3.8

import pandas as pd

FILE_NAME = "sample.xlsx"
SHEET_NAME = "番号順"

df = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME, header=0)
print(df)
