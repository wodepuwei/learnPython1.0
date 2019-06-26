#!/usr/bin/python 
#__*__utf:8__*__

class FooException(StandardError):
	pass 

def foo(s):
	ss = int(s)
	if ss == 0 :
		raise FooException
	return 10/ss 

foo(0)