#!/usr/bin/env python3.8

import pandas as pd
import re
import requests
from html.parser import HTMLParser

FILE_NAME = "sample.xlsx"
SHEET_NAME = "番号順"


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parent = False
        self.result = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "dl" and "class" in attrs and attrs['class'] == "result mb10 cx":
            self.parent = True

        if self.parent is True and tag == "dt":
            self.result = True

    def handle_data(self, data):
        if self.parent is True and self.result is True:
            m = re.search("^\d{3}-\d{4}$", data)
            # if m and m.start() == 3:
            if m:
                self.data.append(data)
            self.title = False
            self.link = False


df = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME, header=0)
# print(df)
for index, row in df.iterrows():
    # print(row[2])
    b = re.search('[0-9]|[０-９]', row[2])
    if b:
        address = row[2][:b.start()]
        # print(address)
        r = requests.get("https://postcode.goo.ne.jp/search/q/" + address + "/?type=address")
        # print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)
        # print(r.text)

        parser = Parser()
        parser.feed(r.text)
        parser.close()

        for data in parser.data:
            print(data)

        break
    else:
        print("not matched!")
        

