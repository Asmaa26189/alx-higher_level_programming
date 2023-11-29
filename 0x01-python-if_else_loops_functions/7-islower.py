#!/usr/bin/python3
def islower(c):
	if c == c.lower() and not c.isnumeric():
		return True
	else:
		return False
