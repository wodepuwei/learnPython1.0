#!/usr/bin/python
#__*__coding:utf8__*__ 

__author__= 'z3'

class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list):
	__metaclass__=ListMetaclass

if __name__=='__main__':
	lm = MyList() 
	lm.add(1)
	print lm
