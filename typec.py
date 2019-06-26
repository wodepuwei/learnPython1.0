#!/usr/bin/python 
#__*__coding:utf8__*__

class Hello(object):
	def hello(self):
		print "hello world"

def fn():
	print "this is fn,hello world"


if __name__=="__main__":
	h = Hello();
	h.hello();
	print type(Hello)
	print type(h)

	Hellotype=type('Hellotype',(object,),dict(hello=fn))		
	print type(Hellotype)
	print type(Hellotype())