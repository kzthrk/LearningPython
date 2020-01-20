#!/usr/bin/env python3.8

from person import Member
import const

if __name__ == "__main__":
	member = Member("john", 22)
	print(member)
	print(member.to_dict())

const.TEST = "test"
const.TEST = "test2"

