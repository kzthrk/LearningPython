#!/usr/bin/env python3.8

import sys
import common
from person import Member

if __name__ == "__main__":
	result = common.plus(1, 2)
	print(result)

	member = Member("john", 22)
	print(member.to_dict())
