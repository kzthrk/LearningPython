#!/usr/bin/env python3.8

class Person():

	def __init__(self, name = "ken", age = 10):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name + " " + str(self.age)
	
	def to_dict(self):
		return {"name": self.name, "age": self.age}

class Staff(Person):
	is_staff = True

	def to_dict(self):
		return {"name": self.name, "age": self.age, "is_staff": self.is_staff}

class Member(Person):
	is_staff = False

	def to_dict(self):
		return {"name": self.name, "age": self.age, "is_staff": self.is_staff}
