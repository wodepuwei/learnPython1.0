
import logging 
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)

def main(s):
	try:
		bar(s)
	except StandardError,e:
		logging.exception(e) 

main(0)
print 'end'