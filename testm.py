#!/usr/bin/env python
#__*__coding:utf8__*__ 

'a test module'

__author__="z3" 

import sys 

def test():
	args=sys.argv
	if len(args) == 1:
		print "hello world"
	elif len(args) == 2:
		print "hello,%s" % args[1]
	else: 
		# print "too many arguments" 


if __name__=="__main__":
	test()
