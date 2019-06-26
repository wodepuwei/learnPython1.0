#!/usr/bin/python  
#__coding:utf-8__ 

class Student(object):
	@property
	def age(self):
		return self.__age 

	@age.setter
	def age(self,value):
		if not isinstance(value,int):
			raise ValueError("age must be an integer");
		if value < 0 or value > 120:
			raise ValueError('age must between 0-120');
		self.__age = value;		


if __name__=='__main__':
	s = Student();
	s.age = 100;
	print s.age;

	s.age = 'ab'		