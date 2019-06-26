#!/usr/bin/python
# __coding:utf-8__ 

class d(object):
	def __init__(self,name,sex):
		self.name = name
		self.sex = sex

class D(object):
	def __init__(self,name,sex):
		self.__name = name 
		self.__sex = sex 

	def getName(self):
		return self.__name 

if __name__ == "__main__" :
	dd = d('ddtest','F')
	print dd.name ,dd.sex

	d1 = d('ddname','F')
	print d1.name

	print "+++++++++private values++++++++"
	d2 = D('testprivate','F')
	print d2.getName()


