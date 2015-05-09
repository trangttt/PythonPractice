#!/usr/bin/python
import sys


def intHarmony(arg1, arg2):
	a = int(arg1)
	b = int(arg2)

	print '{:032b}'.format(a)
	print '{:032b}'.format(b)
	print '{:032b}'.format(a ^ b).count('0')

if __name__ == "__main__":
	intHarmony(sys.argv[1], sys.argv[2])
