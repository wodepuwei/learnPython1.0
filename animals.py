#!/usr/bin/python 
#__coding:utf-8__ 
class Animal(object):
	def __init__(self,name):
		self.name = name 
	def __str__(self):
		return 'Animal object (name:%s)' %  self.name 

class Mammal(Animal):
	pass 

class Bird(Animal):
	pass

class Flyable(object):
	def fly(self):
		print "flying..."

class Runnable(object):
	def run(self):
		print "running..."	

class Cat(Mammal,Runnable):
	pass

if __name__== '__main__':
	a = Animal();
	print a ;

	b = Bird(a);

	m = Mammal(a)

	c = Cat(m,Runnable());
	c.run();	