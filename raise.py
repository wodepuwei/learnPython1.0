#!/usr/bin/python 
#__*__utf8__*__ 

def bar(s):
	return 10/int(s)

def foo(s):
	return bar(s)*2 

def main():
	try:
		foo(0)
	except StandardError,e:
		print "error"
		raise 

main()

