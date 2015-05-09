#!/usr/bin/python
import sys
import re

def check(matchobj):
	if matchobj.group(1) : return matchobj.group(1) + 'o' + matchobj.group(1).lower()

def test(str):
	#new_str = re.sub(r'([BCDFGHJKLMPQRSTVWXZ])([bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ])+', r'\1o\1\2o\2', str)
	new_str = re.sub(r'([bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ])', check, str)
	print new_str

if __name__ == "__main__" :
	test(sys.argv[1])
